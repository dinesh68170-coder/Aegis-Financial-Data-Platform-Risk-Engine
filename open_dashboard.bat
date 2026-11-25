@echo off
title Aegis Web Dashboard Server
cd /d "%~dp0"

echo =====================================================================
echo  STARTING AEGIS LIVE WEB SERVER ON PORT 8080...
echo =====================================================================
echo.

start "" "http://localhost:8080"

set PYTHON_CMD="C:\Users\Hp\AppData\Local\Programs\Python\Python313\python.exe"
if exist %PYTHON_CMD% (
    %PYTHON_CMD% -m aegis.aegis_app --serve
) else (
    python -m aegis.aegis_app --serve
)

pause
