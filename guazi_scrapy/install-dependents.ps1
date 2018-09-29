
$work = "E:\github\guazi_scrapy"
$dependents = "Twisted-18.7.0-cp36-cp36m-win32.whl","pywin32-224-cp36-cp36m-win32.whl"  
$script =  "env\Scripts"
$pip =  $work+"\"+$script+"\pip.exe"

# 进入项目目录
cd  $work
# 新建虚拟环境
virtualenv env


# 下载依赖(有些依赖库无法通过pip 安装)
New-Item -ItemType Directory -Force -Path whl

foreach ($item in $dependents)
{
  Invoke-WebRequest -Uri https://download.lfd.uci.edu/pythonlibs/h2ufg7oq/$item  -OutFile ./whl/$item
}                       

# 配置whl 依赖
foreach ($item in $dependents)
{
  invoke-expression $pip" install ./whl/"$item 
}      


# 配置环境依赖
invoke-expression $pip" install -r requirements.txt"                 


