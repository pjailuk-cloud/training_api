@echo off
echo Starting Task Manager API...
echo.
echo Virtual environment will be activated automatically
echo Server will run on http://localhost:8000
echo.
echo Press Ctrl+C to stop the server
echo.

venv\Scripts\python.exe -m uvicorn app.main:app --reload
