@echo off
title Aegis Financial Infrastructure
cd /d "%~dp0"
echo =====================================================================
echo  AEGIS FINANCIAL INFRASTRUCTURE AND AI RISK ENGINE
echo =====================================================================
echo Folder: %CD%
echo.

set PYTHON_CMD="C:\Users\Hp\AppData\Local\Programs\Python\Python313\python.exe"
if exist %PYTHON_CMD% (
    %PYTHON_CMD% run_aegis.py
) else (
    python run_aegis.py
)

echo.
pause
