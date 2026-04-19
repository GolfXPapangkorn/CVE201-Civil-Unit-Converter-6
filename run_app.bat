@echo off
echo Starting Unit Converter...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not added to PATH. 
    echo Please install Python from the Microsoft Store or python.org first.
    pause
    exit /b
)

echo Installing dependencies (if missing)...
python -m pip install -r requirements.txt >nul 2>&1

echo Launching app...
python main.py
