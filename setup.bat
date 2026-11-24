@echo off
chcp 65001 >nul
echo === 1. Виртуалды орта жасау ===
python -m venv .venv
if errorlevel 1 goto error
call .venv\Scripts\activate.bat
echo === 2. Пакеттерді орнату ===
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
if errorlevel 1 goto error
echo === 3. .env файлын жасау ===
python setup_env.py
echo === 4. Дерекқор миграциялары ===
python manage.py migrate
if errorlevel 1 goto error
echo === 5. Статикалық файлдарды жинау ===
python manage.py collectstatic --noinput
echo.
echo ДАЙЫН! Енді run.bat файлын іске қосыңыз.
pause
exit /b 0
:error
echo ҚАТЕ шықты. Python 3.10+ орнатылғанын тексеріңіз.
pause
exit /b 1
