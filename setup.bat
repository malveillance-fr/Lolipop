@echo off
echo ===========================================
echo       LOLIPOP TOOL - SETUP SCRIPT
echo ===========================================
echo.

echo Checking if Python is installed...
python --version >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo Python is not installed. Please install Python first.
    pause
    exit /b
)

echo Checking if pip is installed...
pip --version >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo pip is not installed. Installing pip...
    python -m ensurepip --upgrade
)

echo Installing required Python libraries...
pip install requests pystyle

echo Checking if project directory exists...
if not exist "Lolipop" (
    echo Creating project directory...
    mkdir Lolipop
)

echo Cloning Lolipop repository...
:: Replace with the actual GitHub repository URL if needed
:: git clone https://github.com/Malveillance/Lolipop.git

echo Verifying installation...
pip show requests >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo Error: requests library not installed properly.
    pause
    exit /b
)

pip show pystyle >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo Error: pystyle library not installed properly.
    pause
    exit /b
)

echo Setting up environment variables...
setx LOLIPOP_DIR "%CD%\Lolipop"
echo LOLIPOP_DIR="%CD%\Lolipop" >> "%USERPROFILE%\AppData\Local\Temp\LolipopEnv.txt"
echo Environment variables set.

echo Checking internet connection...
ping -n 1 google.com >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo No internet connection detected. Some features may not work properly.
    pause
)

echo Creating default configuration files...
if not exist "Lolipop\config.ini" (
    echo [settings] > Lolipop\config.ini
    echo mode=default >> Lolipop\config.ini
    echo timeout=30 >> Lolipop\config.ini
    echo Configuration file created.
)

echo.
echo ===========================================
echo Setup Complete! Lolipop Tool is ready to use.
echo ===========================================
echo.

echo To run Lolipop, use the following command:
echo python Lolipop\lolipop.py
echo.

pause
exit
