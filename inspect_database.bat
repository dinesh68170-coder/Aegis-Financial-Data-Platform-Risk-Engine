@echo off
title Inspect Aegis Database
cd /d "%~dp0"

set PYTHON_CMD="C:\Users\Hp\AppData\Local\Programs\Python\Python313\python.exe"
if exist %PYTHON_CMD% (
    %PYTHON_CMD% view_db.py
) else (
    python view_db.py
)

echo.
echo Opening database view in your web browser...
start "" "database_view.html"
echo.
pause
