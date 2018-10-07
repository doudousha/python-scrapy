$dic = "./script"
New-Item -ItemType Directory -Force -Path "script"

Invoke-WebRequest -Uri "https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-windows.zip"  -OutFile $("$dic/phantomjs-2.1.1-windows.zip")