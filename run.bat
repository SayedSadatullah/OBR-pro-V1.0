@echo off
title ORB Pro Trading Dashboard
cd /d "%~dp0"
python main.py
if errorlevel 1 (
    echo.
    echo [ERROR] App crashed. Check the output above.
    pause
)
