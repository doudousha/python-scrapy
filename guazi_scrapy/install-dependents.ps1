
# 工作目录
$work = "."
# python 环境脚本目录
$script =  "env\Scripts"
# pip.exe 执行目录
$pip = $("$work\$script\pip.exe")
# 当前python 是64位还是32位
$pythonVersion  = 64
# 如果文件存在，是否需要再次强制下载
$forceDownloadWhl = 0

# 进入项目目录
cd  $work
# 新建虚拟环境
if(!(Test-Path $("$work\env") )){
    virtualenv env
}

 # 下载依赖(有些依赖库无法通过pip 安装)
if(Test-Path -Path $("$work\whl-requirements.txt")){
   # 创建whl文件夹存放下载的.whl文件
    New-Item -ItemType Directory -Force -Path "whl"
    $replacePythonVersion = " "
    if( $pythonVersion -ne 64) {$replacePythonVersion="win_amd64"}
    # 将内容转换为字典
    $dependents = Get-Content -raw  $($work+ "/whl-requirements.txt") | %{ $_.replace("==","=")} | %{$_.replace($replacePythonVersion,"win32") } | ConvertFrom-StringData  

    # 下载依赖
    foreach ($item in $dependents.GetEnumerator()) {
        # 文件不存在，或者需要强制下载才从网络下载
        if(!(Test-Path  -Path $("$work/whl/"+$item.Name)  ) -or ($forceDownloadWhl)  ) {
         Invoke-WebRequest -Uri $($item.Value)  -OutFile $("$work/whl/"+$item.Name)
        }
    } 
    # 配置whl 依赖
    foreach ($item in $dependents.GetEnumerator())
    {
      invoke-expression $("$pip install $work/whl/$($item.Name)")
    }
}
              
# 配置环境依赖
invoke-expression $("$pip install -r requirements.txt")            


