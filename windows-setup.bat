@echo off
REM One-click Windows setup for zochat
echo.
echo ================================
echo   ZoChat Windows Setup
echo ================================
echo.

REM Check if Git is installed
where git >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Git is not installed!
    echo Please install Git from: https://git-scm.com/download/win
    pause
    exit /b 1
)

REM Check if Python is installed
where py >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Python is not installed!
    echo Please install Python from: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [1/4] Found Git and Python...
echo.

REM Install Python dependencies
echo [2/4] Installing dependencies...
py -m pip install --quiet wsgidav cheroot requests
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Failed to install Python dependencies
    pause
    exit /b 1
)

echo [3/4] Creating desktop shortcut...
REM Create a shortcut on the desktop
set SCRIPT_DIR=%~dp0
set SHORTCUT=%USERPROFILE%\Desktop\ZoChat.lnk
powershell -Command "$ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut('%SHORTCUT%'); $s.TargetPath = '%SCRIPT_DIR%zochat.bat'; $s.WorkingDirectory = '%SCRIPT_DIR%'; $s.Save()"

echo [4/4] Setup complete!
echo.
echo ================================
echo   You can now run ZoChat by:
echo   1. Double-clicking the desktop shortcut
echo   2. Running: zochat.bat
echo ================================
echo.
pause
