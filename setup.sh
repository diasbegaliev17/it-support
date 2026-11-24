#!/usr/bin/env bash
set -o errexit
echo "=== 1. Виртуалды орта жасау ==="
python3 -m venv .venv
source .venv/bin/activate
echo "=== 2. Пакеттерді орнату ==="
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
echo "=== 3. .env файлын жасау ==="
python setup_env.py
echo "=== 4. Дерекқор миграциялары ==="
python manage.py migrate
echo "=== 5. Статикалық файлдарды жинау ==="
python manage.py collectstatic --noinput
echo
echo "ДАЙЫН! Енді ./run.sh іске қосыңыз."
