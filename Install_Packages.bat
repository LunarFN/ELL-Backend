@echo off
title ELL Installer
set downloadUrl=https://www.python.org/ftp/python/3.12.1/python-3.12.1-amd64.exe
set installerPath=python_installer.exe
set installDir=C:\temppy
timeout /t 1 /nobreak >nul

echo Downloading Python installer...
curl -o %installerPath% %downloadUrl%
cls
echo Python installer downloaded.
timeout /t 1 /nobreak >nul
cls

echo Installing Python...
echo IMPORTANT! Please accept the UAC prompt and give the Installer access to Administrative Privileges!!!
timeout /t 5 /nobreak >nul
start /wait %installerPath% /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
echo Python installation complete.
timeout /t 5 /nobreak >nul
cls

echo Setting up environment variables...
setx PATH "%PATH%;%installDir%"
echo Environment variables set up.
cls

echo Python version:
python --version
cls

del python_installer.exe
echo Installation script completed.
pip install flask --trusted-host=pypi.org --trusted-host=pypi.python.org --trusted-host=files.pythonhosted.org
pip install flask_cors --trusted-host=pypi.org --trusted-host=pypi.python.org --trusted-host=files.pythonhosted.org
cls
echo You can Close this window now!
pause