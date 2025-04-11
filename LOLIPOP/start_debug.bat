@echo off
python Lolipop.py
if %errorlevel% neq 0 (
    echo The tool failed to start due to a "TRACEBACK" error. We recommend reinstalling the tool.
    echo We apologize for this crash.
    echo.
    echo Github: https://github.com/malveillance-fr/Lolipop
)
