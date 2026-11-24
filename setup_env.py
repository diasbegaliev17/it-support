"""
.env файлын автоматты түрде жасайды (егер ол жоқ болса).
.env.example үлгісінен көшіріп, жаңа SECRET_KEY жасап қояды.
"""
from pathlib import Path

from django.core.management.utils import get_random_secret_key

base = Path(__file__).resolve().parent
env_file = base / ".env"
example = base / ".env.example"

if env_file.exists():
    print(".env файлы бұрыннан бар - өзгертілмеді.")
else:
    lines = []
    for line in example.read_text(encoding="utf-8").splitlines():
        if line.startswith("SECRET_KEY="):
            line = "SECRET_KEY='" + get_random_secret_key() + "'"
        lines.append(line)
    env_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(".env файлы жасалды.")
