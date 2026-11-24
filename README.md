# IT-қолдау өтінімдерін тіркеу жүйесі

Зертханалық жұмыс-12: Django жобасын Render-ге deploy жасау, конфигурацияны .env арқылы басқару, журнал жүргізу.

## Технологиялар
Python 3.10+, Django 5, python-dotenv, gunicorn, whitenoise, dj-database-url, PostgreSQL (Render), SQLite (жергілікті).

## 1. Басқа компьютерде іске қосу

Қажет: **Python 3.10 немесе жаңарақ** (python.org). Жоба папкасын ашыңыз (ішінде `manage.py` бар).

**Windows:** `setup.bat` файлын екі рет басыңыз (бір рет орындалады), сосын `run.bat`.

**macOS / Linux:**
```bash
chmod +x setup.sh run.sh
./setup.sh
./run.sh
```

Браузерде http://127.0.0.1:8000/ ашыңыз.

`setup` сценарийі автоматты түрде: виртуалды орта жасайды, `requirements.txt` бойынша пакеттерді орнатады, `.env` файлын жаңа `SECRET_KEY` арқылы жасайды, миграцияларды қолданады және статикалық файлдарды жинайды.

### Қолмен орнату (сценарийсіз)
```bash
python -m venv .venv
# Windows:   .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python setup_env.py
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver
```

## 2. Конфигурация (.env)
`.env` файлы репозиторийге **түспейді** (`.gitignore`). Үлгі — `.env.example`:

| Айнымалы | Жергілікті | Render |
| --- | --- | --- |
| SECRET_KEY | `setup_env.py` жасайды | жаңа құпия кілт |
| DEBUG | True | False |
| ALLOWED_HOSTS | localhost,127.0.0.1 | қосымша домені (https:// жоқ) |
| DATABASE_URL | жоқ (SQLite) | Render PostgreSQL Internal Database URL |

Жаңа SECRET_KEY жасау:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## 3. Журнал (logging)
Логгер `tickets` қолданбасында. Терминалға (Render-де **Logs** бөліміне) жазылады:
- **INFO** — `Өтінім сақталды: id=...` (форма дұрыс толтырылғанда)
- **WARNING** — `Өтінім формасы тексеруден өтпеді` (мысалы, тақырып 5 таңбадан қысқа: `abc`)
Құпия мәндер мен толық сипаттама журналға жазылмайды.

## 4. Render-ге жариялау
1. Жобаны GitHub-қа жүктеңіз (`GitHub репозиторий сілтемесі`): `requirements.txt`, `build.sh`, `.env.example`, шаблондар, миграциялар бар; `.env` жоқ.
2. Render → **New → PostgreSQL** құрыңыз, **Internal Database URL** көшіріңіз.
3. Сол аймақта **New → Web Service**, GitHub репозиторийін таңдаңыз:
   - Runtime: `Python 3`
   - Build Command: `bash build.sh`
   - Start Command: `gunicorn config.wsgi:application --bind 0.0.0.0:$PORT`
4. **Environment** бөлімінде: `SECRET_KEY`, `DEBUG=False`, `ALLOWED_HOSTS=<домен>.onrender.com`, `DATABASE_URL`.
5. **Deploy** жасап, Logs-та орнату, collectstatic және migrate аяқталғанын тексеріңіз. Қосымшаны ашып, дұрыс және қате форма жіберіп, Logs-та INFO/WARNING табыңыз.

## 5. Қатені журналдан табу (DisallowedHost)
1. `.env` ішінде `DEBUG=False`, `ALLOWED_HOSTS=localhost` қойып, серверді қайта іске қосыңыз.
2. http://127.0.0.1:8000/ ашыңыз: браузерде **400 Bad Request**, терминалда **DisallowedHost** шығады.
3. **Себебі:** DEBUG=False кезінде Django тек ALLOWED_HOSTS тізіміндегі хосттарға жауап береді, ал `127.0.0.1` тізімде жоқ.
4. **Түзету:** `ALLOWED_HOSTS=localhost,127.0.0.1` деп жазып, серверді қайта іске қосыңыз — бет ашылады (DEBUG=False күйінде).

## Құрылым
```
config/        settings.py, urls.py, wsgi.py
tickets/     models, forms, views, urls, admin, migrations
templates/     base.html және қолданба шаблондары
static/css/    style.css
build.sh       Render build сценарийі
setup.*, run.* жергілікті іске қосу сценарийлері
```
