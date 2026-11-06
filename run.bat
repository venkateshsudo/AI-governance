@echo off
setlocal
cd /d "%~dp0"

where python >nul 2>nul
if errorlevel 1 (
  echo.
  echo   Python 3 is required to run the local preview server.
  echo   Install it from https://www.python.org/downloads/ and try again.
  echo.
  pause
  exit /b 1
)

python serve.py %*
if errorlevel 1 pause
