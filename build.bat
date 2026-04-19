@echo off
echo Building the Unit Converter App...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not added to PATH. 
    echo Please install Python from the Microsoft Store or python.org first.
    pause
    exit /b
)

echo Installing dependencies...
python -m pip install pyinstaller customtkinter

echo Compiling to executable...
python -m PyInstaller --noconsole --onefile --windowed --name "UnitConverter" main.py

echo.
echo ==========================================
echo Build complete! Your application is located in the "dist" folder.
echo ==========================================
pause
