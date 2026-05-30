@echo off
echo ===================================================
echo   TaskFlow Project Launcher
echo ===================================================
echo.
echo Starting Django Backend Server on http://127.0.0.1:8000 ...
start "TaskFlow Backend" cmd /k "cd Backend && python manage.py runserver"

echo.
echo Starting React Vite Frontend Server on http://localhost:5173 ...
start "TaskFlow Frontend" cmd /k "cd Frontend && npm run dev"

echo.
echo Both servers have been launched in separate windows!
echo Please keep those windows open while using TaskFlow.
echo ===================================================
pause
