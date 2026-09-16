# -*- coding: utf-8 -*-
"""داده محتوای فصل‌های ۲۶ تا ۳۰ — استقرار، کارایی، فرانت‌اند، نسخه‌های جدید، پروژه نهایی"""

CHAPTERS = [

# ================================================================ فصل ۲۶
dict(
    n=26, icon='📦', title='استقرار (Deployment) روی سرور واقعی', cat=5, mins=120, lvl_label='پیشرفته',
    hero_desc='از localhost تا اینترنت: آماده‌سازی امن پروژه، <span class="term" data-term="postgresql">PostgreSQL</span>، <span class="term" data-term="gunicorn">Gunicorn</span> و <span class="term" data-term="nginx">Nginx</span>، فایل‌های ایستا، <span class="term" data-term="https">HTTPS</span> رایگان، systemd و <span class="term" data-term="docker">داکر</span> — با چک‌لیست نهایی استقرار.',
    s1_intro='سایتی که فقط روی لپ‌تاپ شماست، وجود ندارد! استقرار یعنی پروژه را روی سروری واقعی، امن، پایدار و قابل به‌روزرسانی بالا بیاورید. این فصل نقشه کامل راه است — از <span class="term" data-term="vps">VPS</span> خام تا HTTPS.',
    objectives=[
        'پروژه را برای تولید آماده کنید (SECRET_KEY، DEBUG، ALLOWED_HOSTS، env).',
        'معماری Nginx → Gunicorn → Django را توضیح و پیکربندی کنید.',
        'PostgreSQL را جایگزین SQLite و مهاجرت داده را مدیریت کنید.',
        'فایل‌های ایستا/رسانه را در تولید سرو کنید (WhiteNoise یا Nginx).',
        'HTTPS با Let\'s Encrypt، سرویس systemd و استقرار داکری بسازید.',
    ],
    s1_position='<strong>جایگاه فصل:</strong> عصاره همه فصل‌ها: استاتیک (۱۴)، لاگ (۲۱)، سلری (۲۴) و امنیت (۱۷). فصل ۲۷ (کارایی) بعد از این روی همین زیرساخت سوار می‌شود.',
    roadmap=[
        ('آماده‌سازی پروژه', 'secrets و settings تولید.'),
        ('دیتابیس و استاتیک', 'Postgres + WhiteNoise/Nginx.'),
        ('سرور اپ', 'Gunicorn + systemd.'),
        ('Nginx و HTTPS', 'پروکسی معکوس + گواهی رایگان.'),
        ('داکر', 'کل پشته در compose.'),
    ],
    mind_qs=[
        ('چرا runserver برای تولید مناسب نیست؟',
         '<p>خود مستندات جنگو می‌گوید: تک‌رشته، بدون سخت‌گیری امنیتی، برای توسعه. در تولید از سرور <span class="term" data-term="wsgi">WSGI</span> مثل <span class="term" data-term="gunicorn">Gunicorn</span> استفاده می‌شود: چند ورکر، مدیریت پروسه، پایداری. runserver با اولین درخواست سنگین یا خطا کم می‌آورد.</p>'),
        ('نقش Nginx جلوی Gunicorn چیست؟',
         '<p><span class="term" data-term="reverse-proxy">پروکسی معکوس</span>: ترافیک را می‌گیرد، فایل‌های ایستا را خودش (خیلی سریع‌تر) سرو می‌کند، درخواست‌های داینامیک را به Gunicorn می‌دهد، HTTPS را خاتمه می‌دهد، بافر می‌کند (ورکرهای گران‌قیمت پایتون را با کلاینت کند مشغول نمی‌کند) و لاگ دسترسی می‌گیرد.</p>'),
        ('چرا secrets نباید در گیت باشند؟',
         '<p>یک push اشتباه = SECRET_KEY/رمز دیتابیس عمومی برای همیشه (حتی اگر پاک کنید، تاریخچه و ربات‌های اسکنر می‌مانند). ربات‌ها ظرف <strong>دقیقه</strong> ریپازیتوری‌های عمومی را برای کلید AWS/رمز می‌کاوند. راه حل: <span class="term" data-term="env-var">متغیرهای محیطی</span> + فایل .env خارج از گیت.</p>'),
    ],
    prereq_intro='پیش‌نیازها:',
    prereq=[
        'پروژه وبلاگ کامل با تست‌های سبز (فصل ۲۰).',
        'یک VPS (ارزان‌ترین پلن کافی است؛ Hetzner/DigitalOcean/سرویس‌های ایرانی) با اوبونتو ۲۲.۰۴/۲۴.۰۴.',
        'یک دامنه (یا زیردامنه رایگان) که A record آن به IP سرور وصل باشد.',
        'دسترسی SSH به سرور: <code class="inline-code">ssh root@YOUR_IP</code>.',
    ],
    prereq_callout=('info', 'می‌شود بدون سرور هم تمرین کرد؟',
        'بله: همه پیکربندی‌های این فصل را می‌توانید با <strong>داکر روی همان لپ‌تاپ</strong> تمرین کنید (بخش ۵.۶). فقط DNS/HTTPS واقعی به سرور نیاز دارد.'),
    concepts=[
        dict(h='۵.۱ آماده‌سازی پروژه: secrets و settings', body=[
            ('code', 'config/settings.py — خواندن از محیط', 'python', '''import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# فایل .env (فقط محلی/روی سرور؛ هرگز در گیت نه!)
# pip install python-dotenv
from dotenv import load_dotenv
load_dotenv(BASE_DIR / ".env")

SECRET_KEY = os.environ["SECRET_KEY"]          # وجودش اجباری است
DEBUG = os.environ.get("DEBUG", "0") == "1"    # پیش‌فرض: خاموش!
ALLOWED_HOSTS = os.environ.get(
    "ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME", "blog"),
        "USER": os.environ.get("DB_USER", "blog"),
        "PASSWORD": os.environ.get("DB_PASS", ""),
        "HOST": os.environ.get("DB_HOST", "127.0.0.1"),
        "PORT": os.environ.get("DB_PORT", "5432"),
    }
}'''),
            ('code', '.env (خارج از گیت) و .gitignore', 'text', '''SECRET_KEY=django-insecure-... (کلید تازه و قوی بسازید)
DEBUG=0
ALLOWED_HOSTS=example.com,www.example.com
DB_NAME=blog
DB_USER=blog
DB_PASS=رمز_قوی_تصادفی
DB_HOST=127.0.0.1

# .gitignore:
.env
*.sqlite3
/staticfiles/
/media/
logs/'''),
            ('code', 'ساخت SECRET_KEY تازه', 'bash', '''python -c "from django.core.management.utils import \\
    get_random_secret_key; print(get_random_secret_key())"'''),
            ('callout', 'danger', 'چک‌لیست امنیتی تولید',
             'DEBUG=False • ALLOWED_HOSTS دقیق • SECRET_KEY از env • SESSION_COOKIE_SECURE=True • CSRF_COOKIE_SECURE=True • SECURE_SSL_REDIRECT=True • SECURE_HSTS_SECONDS=31536000 • رمز دیتابیس قوی. همه را می‌توان در settings با شرط not DEBUG گذاشت.'),
        ]),
        dict(h='۵.۲ PostgreSQL روی سرور', body=[
            ('code', 'نصب و ساخت دیتابیس', 'bash', '''sudo apt update
sudo apt install -y postgresql postgresql-contrib

sudo -u postgres psql
# CREATE DATABASE blog;
# CREATE USER blog WITH PASSWORD \'رمز_قوی\';
# ALTER ROLE blog SET client_encoding TO \'utf8\';
# ALTER ROLE blog SET timezone TO \'Asia/Tehran\';
# GRANT ALL PRIVILEGES ON DATABASE blog TO blog;
# \\q'''),
            ('code', 'انتقال داده از SQLite (اختیاری)', 'bash', '''# روی لپ‌تاپ: خروجی داده
python manage.py dumpdata --natural-foreign --natural-primary \\
    -e contenttypes -e auth.permission --indent 2 > data.json

# روی سرور (با DATABASES تنظیم‌شده روی Postgres):
python manage.py migrate
python manage.py loaddata data.json'''),
            ('callout', 'warn', 'چرا Postgres نه SQLite در تولید؟',
             'SQLite تک‌فایل و عالی برای توسعه است، ولی نوشتن هم‌زمان چند ورکر Gunicorn روی آن قفل/کندی می‌آورد. Postgres: هم‌زمانی واقعی، پشتیبان‌گیری گرم، ایندکس‌های پیشرفته و مقیاس. (تله dumpdata: contenttypes و permissionها را exclude کنید وگرنه loaddata تکراری می‌شود.)'),
        ]),
        dict(h='۵.۳ Gunicorn + systemd', body=[
            ('code', 'اجرای دستی (تست)', 'bash', '''pip install gunicorn python-dotenv psycopg2-binary
cd /srv/blog
gunicorn config.wsgi:application \\
    --bind unix:/run/gunicorn.sock \\
    --workers 3 --timeout 60'''),
            ('code', '/etc/systemd/system/blog.service', 'text', '''[Unit]
Description=Blog Gunicorn
After=network.target postgresql.service

[Service]
User=www-data
Group=www-data
WorkingDirectory=/srv/blog
EnvironmentFile=/srv/blog/.env
ExecStart=/srv/blog/.venv/bin/gunicorn config.wsgi:application \\
    --bind unix:/run/gunicorn.sock \\
    --workers 3 --timeout 60 \\
    --access-logfile - --error-logfile -
Restart=on-failure

[Install]
WantedBy=multi-user.target'''),
            ('code', 'فعال‌سازی', 'bash', '''sudo systemctl daemon-reload
sudo systemctl enable --now blog
sudo systemctl status blog          # active (running)؟
journalctl -u blog -f               # لاگ زنده'''),
            ('callout', 'info', 'چند ورکر؟',
             'فرمول رایج: <code class="inline-code">2 × CPU + 1</code>. ورکر زیاد = رم زیاد (هر ورکر پروسه کامل پایتون). سرور ۲ هسته‌ای: ۳ تا ۵ ورکر کافی است؛ بقیه صف می‌کشند.'),
        ]),
        dict(h='۵.۴ فایل‌های ایستا و رسانه', body=[
            '<p><strong>گزینه الف — WhiteNoise (ساده‌ترین، توصیه برای شروع):</strong></p>',
            ('code', 'settings.py', 'python', '''# pip install whitenoise
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",   # ← دوم!
    ...,
]
STATIC_ROOT = BASE_DIR / "staticfiles"
STORAGES = {
    "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}'''),
            ('code', 'collectstatic قبل از هر دیپلوی', 'bash', '''python manage.py collectstatic --noinput
# staticfiles/ پر می‌شود؛ WhiteNoise با فشرده‌سازی و کش سرو می‌کند'''),
            '<p><strong>گزینه ب — Nginx مستقیم (کارایی بالاتر برای رسانه سنگین):</strong> در کانفیگ Nginx، location /static/ و /media/ با alias به STATIC_ROOT و MEDIA_ROOT؛ در این حالت WhiteNoise لازم نیست.</p>',
        ]),
        dict(h='۵.۵ Nginx و HTTPS', body=[
            ('code', '/etc/nginx/sites-available/blog', 'nginx', '''server {
    listen 80;
    server_name example.com www.example.com;

    location /static/ { alias /srv/blog/staticfiles/; }
    location /media/  { alias /srv/blog/media/; }

    location / {
        proxy_pass http://unix:/run/gunicorn.sock;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        client_max_body_size 10M;      # سقف آپلود
    }
}'''),
            ('code', 'فعال‌سازی و HTTPS رایگان', 'bash', '''sudo ln -s /etc/nginx/sites-available/blog /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx

# گواهی Let's Encrypt (خودکار nginx را هم تنظیم می‌کند):
sudo apt install -y certbot python3-certbot-nginx
sudo certbot --nginx -d example.com -d www.example.com
# تمدید خودکار تست: sudo certbot renew --dry-run'''),
            ('callout', 'warn', 'بعد از HTTPS',
             'در settings: SECURE_SSL_REDIRECT=True, SESSION_COOKIE_SECURE=True, CSRF_COOKIE_SECURE=True, SECURE_HSTS_SECONDS=31536000. و حتماً X-Forwarded-Proto را رد کنید (کردیم) وگرنه جنگو همه درخواست‌ها را http می‌بیند و ریدایرکت حلقوی می‌سازد.'),
        ]),
        dict(h='۵.۶ داکر: کل پشته در یک compose', body=[
            ('code', 'Dockerfile', 'dockerfile', '''FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN python manage.py collectstatic --noinput || true
CMD ["gunicorn", "config.wsgi", "--bind", "0.0.0.0:8000", "--workers", "3"]'''),
            ('code', 'docker-compose.yml', 'yaml', '''services:
  db:
    image: postgres:16
    environment:
      POSTGRES_DB: blog
      POSTGRES_USER: blog
      POSTGRES_PASSWORD: ${DB_PASS}
    volumes: [pgdata:/var/lib/postgresql/data]

  web:
    build: .
    environment:
      - SECRET_KEY=${SECRET_KEY}
      - DB_HOST=db
      - DB_NAME=blog
      - DB_USER=blog
      - DB_PASS=${DB_PASS}
    command: >
      sh -c "python manage.py migrate &&
             gunicorn config.wsgi --bind 0.0.0.0:8000 --workers 3"
    volumes:
      - media:/app/media
    ports: ["8000:8000"]
    depends_on: [db]

volumes:
  pgdata:
  media:'''),
            ('code', 'اجرا', 'bash', '''docker compose up -d --build
docker compose exec web python manage.py createsuperuser
# جلوی آن در سرور واقعی، همان Nginx به :8000 پروکسی می‌کند'''),
            ('callout', 'tip', 'کدام روش؟',
             'VPS + systemd + Nginx: کنترل کامل، رم کمتر، استاندارد بازار کار. داکر: محیط یکسان از توسعه تا تولید، مقیاس‌پذیری راحت‌تر. هر دو را بلد باشید؛ مسیر شغلی بیشتر به داکر می‌رود.'),
        ]),
    ],
    example_intro='گردش کار دیپلوی واقعی — از git push تا سایت زنده:',
    example=[
        ('code', 'اسکریپت دیپلوی ساده (deploy.sh روی سرور)', 'bash', '''#!/usr/bin/env bash
set -e                                # اولین خطا = توقف
cd /srv/blog
sudo -u www-data git pull
sudo -u www-data .venv/bin/pip install -r requirements.txt
sudo -u www-data .venv/bin/python manage.py migrate --noinput
sudo -u www-data .venv/bin/python manage.py collectstatic --noinput
sudo systemctl restart blog
curl -sf https://example.com/health/ > /dev/null \\
  && echo "✅ دیپلوی موفق" || echo "❌ بررسی کن!"'''),
        ('code', 'ویوی health check (برای مانیتورینگ)', 'python', '''# urls: path("health/", health)
def health(request):
    try:
        cache.set("hb", "1", 10)
        Post.objects.exists()            # اتصال دیتابیس سالم؟
        return JsonResponse({"status": "ok"})
    except Exception as e:
        return JsonResponse({"status": "error", "detail": str(e)},
                            status=500)'''),
        ('code', 'ساختار سرور نهایی', 'text', '''/srv/blog/
├── .venv/            (محیط مجازی)
├── .env              (secrets — chmod 600)
├── config/ appها/ templates/ ...
├── staticfiles/      (خروجی collectstatic)
├── media/            (آپلودها — پشتیبان‌گیری!)
└── logs/

systemd: blog.service (+ blog-worker.service برای سلری فصل ۲۴)
nginx: 80 → 443 (certbot) → unix:/run/gunicorn.sock'''),
        '<p>به‌روزرسانی بعدی فقط: <code class="inline-code">git push</code> روی لپ‌تاپ و <code class="inline-code">./deploy.sh</code> روی سرور. (در تیم‌های بزرگ‌تر همین را GitHub Actions/GitLab CI خودکار می‌کند.)</p>',
    ],
    workshop_intro='سایت خودتان را واقعاً بالا بیاورید:',
    workshop_tasks=[
        '<strong>کارگاه ۱:</strong> پروژه را تولید-آماده کنید: SECRET_KEY و DB از env، DEBUG پیش‌فرض False، بلوک تنظیمات امنیتی (HSTS، کوکی‌های Secure) با شرط not DEBUG.',
        '<strong>کارگاه ۲:</strong> پشته کامل را با <strong>داکر</strong> روی سیستم خودتان بالا بیاورید (web + db + migrate خودکار) و صفحه را روی :8000 ببینید.',
        '<strong>کارگاه ۳ (اختیاری/واقعی):</strong> روی VPS: Postgres + Gunicorn + systemd + Nginx + certbot را مرحله‌به‌مرحله اجرا کنید تا https://دامنه‌شما بالا بیاید؛ اگر VPS ندارید، همان کارگاه ۲ را با WhiteNoise کامل کنید.',
    ],
    workshop_answers=[
        ('پاسخ کارگاه ۱',
         '<div class="code-box"><div class="code-head"><span>بلوک امنیتی settings</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">if not DEBUG:\n    SECURE_SSL_REDIRECT = True\n    SESSION_COOKIE_SECURE = True\n    CSRF_COOKIE_SECURE = True\n    SECURE_HSTS_SECONDS = 60 * 60 * 24 * 365\n    SECURE_HSTS_INCLUDE_SUBDOMAINS = True\n    SECURE_HSTS_PRELOAD = True\n    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")\n    SECURE_CONTENT_TYPE_NOSNIFF = True\n    X_FRAME_OPTIONS = "DENY"</code></pre></div>'
         '<p>SECURE_PROXY_SSL_HEADER را فقط وقتی بگذارید که Nginx هدر را ست می‌کند (در ۵.۵ کردیم) — وگرنه ریدایرکت حلقوی. تست محلی: DEBUG=0 با ALLOWED_HOSTS=localhost و curl -I.</p>'),
        ('پاسخ کارگاه ۲',
         '<p>فایل‌های ۵.۶ را بسازید؛ سپس:</p>'
         '<div class="code-box"><div class="code-head"><span>بالا آوردن پشته</span><span class="lang">bash</span></div><pre class="code"><code data-lang="bash"># .env کنار compose (بدون پیشوند docker-):\n#   SECRET_KEY=...  DB_PASS=...\ndocker compose up -d --build\ndocker compose ps                        # هر دو سرویس Up؟\ndocker compose exec web python manage.py createsuperuser\ndocker compose logs -f web               # لاگ gunicorn\ncurl -I http://localhost:8000/           # 200</code></pre></div>'
         '<p>خطای رایج: DB_HOST را localhost گذاشته‌اید — در compose نام سرویس است: <code class="inline-code">DB_HOST=db</code>. و migrate باید <strong>بعد</strong> از آماده شدن db اجرا شود (depends_on ساده فقط شروع را ترتیب می‌دهد؛ در اسکریپت migrate قبل از gunicorn است، پس خود اصلاح می‌شود).</p>'),
        ('پاسخ کارگاه ۳',
         '<p>ترتیب اجرایی روی VPS تازه (هر قدم را تست کنید):</p>'
         '<div class="code-box"><div class="code-head"><span>چک‌لیست VPS</span><span class="lang">bash</span></div><pre class="code"><code data-lang="bash"># 1) کاربر غیر root + فایروال\nadduser deploy &amp;&amp; usermod -aG sudo deploy\nufw allow OpenSSH &amp;&amp; ufw allow "Nginx Full" &amp;&amp; ufw enable\n\n# 2) پایتون و مخزن\napt install python3.12-venv postgresql nginx git\nsudo -u postgres createuser blog -P &amp;&amp; sudo -u postgres createdb blog -O blog\ngit clone https://github.com/you/blog /srv/blog\ncd /srv/blog &amp;&amp; python3 -m venv .venv\n.venv/bin/pip install -r requirements.txt\n# .env را دستی بسازید (chmod 600) — کلیدها از لپ‌تاپ نیایند!\n\n# 3) دیتابیس و استاتیک\n.venv/bin/python manage.py migrate\n.venv/bin/python manage.py collectstatic --noinput\n.venv/bin/python manage.py createsuperuser\n\n# 4) systemd و nginx (فایل‌های ۵.۳ و ۵.۵)\nsystemctl enable --now blog\nln -s /etc/nginx/sites-available/blog /etc/nginx/sites-enabled/\nnginx -t &amp;&amp; systemctl reload nginx\n\n# 5) HTTPS\ncertbot --nginx -d example.com -d www.example.com\n\n# 6) تست نهایی\ncurl -I https://example.com   # 200 و هدر HSTS</code></pre></div>'
         '<p>فراموش نشود: سلری هم سرویس می‌خواهد — blog-worker.service با ExecStart برابر <code class="inline-code">celery -A config worker -l warning</code> (و beat در صورت نیاز).</p>'),
    ],
    errors=[
        ('Invalid HTTP_HOST header / DisallowedHost',
         'دامنه در ALLOWED_HOSTS نیست (www و بدون www هر دو لازم‌اند). بعد از اصلاح، سرویس را restart کنید — settings کش شده.'),
        ('صفحه می‌آید ولی CSS/JS نیست (۴۰۴ روی static)',
         'collectstatic اجرا نشده، یا STATIC_ROOT با مسیر alias در Nginx نمی‌خواند، یا WhiteNoise بعد از SecurityMiddleware ثبت نشده. مسیر /static/ را با curl چک کنید.'),
        ('ریدایرکت حلقوی http↔https',
         'SECURE_SSL_REDIRECT=True ولی هدر X-Forwarded-Proto به جنگو نمی‌رسد یا SECURE_PROXY_SSL_HEADER تنظیم نشده. هر دو سمت (Nginx و settings) را چک کنید.'),
        ('502 Bad Gateway',
         'Gunicorn بالا نیست یا sock اشتباه است: <code class="inline-code">systemctl status blog</code> و <code class="inline-code">journalctl -u blog -n 50</code>. مالکیت سوکت/پوشه (www-data) و دسترسی‌ها را چک کنید.'),
        ('مهاجرت‌ها روی سرور fail می‌شوند',
         'دیتابیس/کاربر Postgres با نام اشتباه در .env، یا pg_hba احراز هویت را رد می‌کند. با <code class="inline-code">psql -U blog -h 127.0.0.1 -d blog</code> دستی تست اتصال بگیرید.'),
    ],
    errors_callout=('tip', 'پشتیبان‌گیری از روز اول',
        'کرون ساده: <code class="inline-code">pg_dump blog | gzip &gt; /backups/blog-$(date +\\%F).sql.gz</code> + کپی media/ به فضای ابری. پشتیبانی که تست بازیابی نشده، پشتیبان نیست!'),
    exercises=[
        ('تمرین ۱ — اجزای معماری',
         '<p><strong>سوال:</strong> نقش هر جزء؟ (الف) Nginx (ب) Gunicorn (ج) systemd (د) certbot (ه) WhiteNoise</p>'
         '<p><strong>پاسخ:</strong> الف → پروکسی معکوس/سرو استاتیک/HTTPS • ب → سرور WSGI که کد جنگو را در ورکرها اجرا می‌کند • ج → نگهبان پروسه‌ها (شروع خودکار، ری‌استارت هنگام کرش) • د → گرفتن/تمدید گواهی رایگان Let\'s Encrypt • ه → سرو استاتیک فشرده+کش‌دار از داخل خود اپ (وقتی Nginx استاتیک را سرو نمی‌کند).</p>'),
        ('تمرین ۲ — ترتیب دیپلوی',
         '<p><strong>سوال:</strong> ترتیب درست این قدم‌ها: migrate / git pull / restart / collectstatic / pip install / تست health؟</p>'
         '<p><strong>پاسخ:</strong> git pull ← pip install ← migrate ← collectstatic ← restart ← health check. منطق: کد و وابستگی‌ها اول، اسکیمای دیتابیس قبل از اجرای کد جدید، استاتیک قبل از restart (تا سایت لحظه‌ای بدون CSS نماند).</p>'),
        ('تمرین ۳ — سناریوی خرابی',
         '<p><strong>سناریو:</strong> بعد از دیپلوی، سایت 500 می‌دهد ولی دیشب سالم بود. سه قدم اول تشخیص؟</p>'
         '<p><strong>پاسخ:</strong> ① <code class="inline-code">journalctl -u blog -n 100</code> (Traceback واقعی اینجاست، نه صفحه کاربر) ② اگر مهاجرت داشتید: آیا migrate اجرا شد؟ دیتابیس و کد هم‌نسخه‌اند؟ ③ رول‌بک سریع: <code class="inline-code">git checkout نسخه‌قبل &amp;&amp; ./deploy.sh</code> — اول سرویس برگردد، بعد ریشه‌یابی آرام. درس: همیشه قبل دیپلوی tag بزنید.</p>'),
    ],
    quiz=[
        dict(q='چرا در تولید از runserver استفاده نمی‌کنیم؟',
             opts=['کند است در توسعه', 'تک‌رشته و فاقد سخت‌گیری امنیتی است؛ فقط برای توسعه طراحی شده',
                   'PostgreSQL را پشتیبانی نمی‌کند', 'HTTPS ندارد'],
             ans='b', explain='سرور WSGI تولید (Gunicorn/uWSGI) چند ورکر، مدیریت پروسه و پایداری می‌دهد؛ مستندات جنگو صریحاً runserver را برای تولید منع می‌کند.'),
        dict(q='مسیر درست یک درخواست در معماری استاندارد چیست؟',
             opts=['کاربر → Gunicorn → Nginx → Django', 'کاربر → Nginx → Gunicorn → Django',
                   'کاربر → Django → Nginx', 'کاربر → PostgreSQL → Django'],
             ans='b', explain='Nginx در لبه: استاتیک و HTTPS را خودش، داینامیک را به سوکت Gunicorn می‌دهد و آن ویوی جنگو را صدا می‌زند.'),
        dict(q='SECRET_KEY در تولید کجا باید باشد؟',
             opts=['در settings.py داخل گیت', 'در متغیر محیطی/فایل .env خارج از کنترل نسخه',
                   'در دیتابیس', 'مهم نیست'],
             ans='b', explain='نشت کلید = امکان جعل نشست/توکن/امضا. .env با chmod 600 یا secret manager؛ در گیت فقط .env.example بدون مقدار.'),
        dict(q='collectstatic چه می‌کند و کی لازم است؟',
             opts=['استاتیک‌ها را پاک می‌کند', 'همه فایل‌های ایستا اپ‌ها را در STATIC_ROOT جمع می‌کند؛ قبل از هر دیپلوی که استاتیک عوض شده',
                   'فقط در توسعه لازم است', 'دیتابیس را جمع می‌کند'],
             ans='b', explain='Nginx/WhiteNoise فقط از STATIC_ROOT سرو می‌کنند؛ فایل‌های پراکنده اپ‌ها را کسی در تولید نمی‌بیند مگر جمع شوند.'),
        dict(q='کار certbot --nginx چیست؟',
             opts=['نصب Nginx', 'گرفتن گواهی Let\'s Encrypt و تنظیم خودکار ریدایرکت HTTPS در کانفیگ Nginx',
                   'ساخت دیتابیس', 'اجرای Gunicorn'],
             ans='b', explain='گواهی رایگان + ثبت مسیرها + تمدید خودکار (systemd timer). بعد از آن هدرهای امنیتی جنگو را روشن کنید.'),
        dict(q='در docker-compose، چرا DB_HOST باید «db» باشد نه localhost؟',
             opts=['فرقی ندارد', 'هر سرویس کانتینر خودش است؛ localhost داخل کانتین web به خودش اشاره می‌کند، «db» نام سرویس در شبکه داخلی compose است',
                   'باگ داکر است', 'فقط برای Postgres 16'],
             ans='b', explain='شبکه compose نام سرویس‌ها را DNS می‌کند؛ web با db:5432 به کانتین دیتابیس می‌رسد.'),
    ],
    project_title='وبلاگ زنده روی اینترنت',
    project_intro='پروژه را واقعاً دیپلوی کنید — این مهارت، رزومه‌سازترین بخش دوره است.',
    project_checklist=[
        'تنظیمات تولید-آماده (env، بلوک امنیتی، WhiteNoise) روی شاخه main.',
        'پشته داکری (web+db) بالا آمده و health check پاسخ 200 می‌دهد.',
        '(با VPS) Nginx + Gunicorn + systemd + HTTPS فعال و ۴۰۴/۵۰۰ سفارشی دیده می‌شوند.',
        'اسکریپت deploy.sh یا workflow ساده CI که migrate/collectstatic/restart را انجام دهد.',
        'کرون پشتیبان‌گیری pg_dump + media (و یک تست بازیابی دستی).',
    ],
    project_callout=('tip', 'PaaSهای بدون دردسر',
        'اگر مدیریت سرور فعلاً زیاد است: Railway، Render، Fly.io یا سرویس‌های ایرانی (لیارا و...) پروژه جنگو را با Git دیپلوی می‌کنند. مفاهیم این فصل دقیقاً همان‌جا به کار می‌آید — فقط Nginx/systemd را پلتفرم انجام می‌دهد.'),
    summary_items=[
        'تولید: DEBUG=False، secrets در env، ALLOWED_HOSTS دقیق، کوکی‌های Secure+HSTS.',
        'Postgres جای SQLite؛ dumpdata/loaddata برای انتقال داده.',
        'Gunicorn (WSGI) + systemd برای پایداری؛ چند ورکر = 2×CPU+1.',
        'Nginx = پروکسی معکوس + استاتیک + HTTPS با certbot.',
        'داکر/compose = محیط یکسان؛ اسکریپت دیپلوی + health check + پشتیبان‌گیری.',
    ],
    golden='استقرار موفق، خسته‌کننده است: اسکریپت تکرارپذیر، لاگ روشن، رول‌بک آماده.',
    faq=[
        ('uWSGI یا Gunicorn؟',
         '<p>هر دو سرور WSGI معتبرند. Gunicorn پیکربندی ساده‌تر و جامعه بزرگ‌تری دارد و پیشنهاد خود مستندات استقرار جنگو است؛ uWSGI انعطاف بیشتر (و پیچیدگی بیشتر). برای شروع Gunicorn + Nginx عالی است.</p>'),
        ('برای WebSocket/realtime چه تغییری لازم است؟',
         '<p>سرور <span class="term" data-term="asgi">ASGI</span> (Daphne/Uvicorn) جای WSGI، همراه Django Channels و Redis برای لایه کانال‌ها. Nginx همچنان جلو می‌ماند و WebSocket را پروکسی می‌کند. این مسیر فصل جداگانه‌ای است (پروژه پیشرفته).</p>'),
        ('چطور zero-downtime دیپلوی کنم؟',
         '<p>ساده: چند ورکر Gunicorn + ری‌استارت graceful (HUP به master، ورکرهای قدیم کار را تمام می‌کنند). جدی‌تر: دو نمونه اپ پشت Nginx با health check و rolling restart، یا کانتینرهای جایگزین‌شونده. نکته حیاتی: مهاجرت‌ها باید backward-compatible باشند (کد قدیم با اسکیمای جدید کار کند).</p>'),
    ],
    next_step='سایت بالاست؛ حالا باید «سریع» بماند. <strong>فصل ۲۷</strong>: <span class="term" data-term="performance">بهینه‌سازی کارایی</span> — اندازه‌گیری، ایندکس، کوئری‌ها و کش در مقیاس.',
),

# ================================================================ فصل ۲۷
dict(
    n=27, icon='🏎️', title='بهینه‌سازی کارایی (Performance)', cat=5, mins=95, lvl_label='پیشرفته',
    hero_desc='متدولوژی بهینه‌سازی: اول اندازه‌گیری، بعد اصلاح. <span class="term" data-term="db-index">ایندکس</span>‌ها، کوئری‌های بهینه، <span class="term" data-term="n-plus-one">N+1</span>، لایه‌های <span class="term" data-term="cache">کش</span>، GZip، تصاویر و پایش تولید.',
    s1_intro='«سایت کند است» یک تشخیص است، نه یک مشکل! مشکل دقیقاً کدام صفحه، کدام کوئری، کدام میلی‌ثانیه است؟ این فصل روش مهندسی سرعت را یاد می‌دهد: اندازه‌گیری → یافتن گلوگاه → اصلاح → اندازه‌گیری دوباره.',
    objectives=[
        'با ابزارها (Toolbar، EXPLAIN، لاگ زمان) گلوگاه را پیدا کنید.',
        'ایندکس درست بسازید و با EXPLAIN ANALYZE اثرش را ببینید.',
        'کوئری‌ها را با select_related/only/bulk به حداقل برسانید.',
        'لایه‌های کش (مرورگر، GZip، Redis، CDN) را ترکیب کنید.',
        'بودجه کارایی تعیین و در CI پایش کنید.',
    ],
    s1_position='<strong>جایگاه فصل:</strong> جمع‌بندی QuerySet (۱۵) و کش (۱۹) روی زیرساخت فصل ۲۶؛ عددگذاری‌های واقعی برای مصاحبه و پروژه نهایی.',
    roadmap=[
        ('اندازه‌گیری', 'پیدا کردن گلوگاه واقعی.'),
        ('دیتابیس', 'ایندکس، EXPLAIN، کوئری.'),
        ('لایه‌های HTTP', 'GZip، کش مرورگر، CDN.'),
        ('فرهنگ کارایی', 'بودجه و پایش مستمر.'),
    ],
    mind_qs=[
        ('قانون ۸۰/۲۰ در کارایی یعنی چه؟',
         '<p>معمولاً ۸۰٪ زمان پاسخ، در ۲۰٪ کد (اغلب کوئری‌های دیتابیس) می‌رود. پس قبل از دست بردن به هر چیزی <strong>اندازه بگیرید</strong>: بهینه‌سازی بدون پروفایل یعنی حدس زدن — و حدس معمولاً جایی بهینه می‌کند که اثری ندارد.</p>'),
        ('ایندکس چرا همیشه جواب نیست؟',
         '<p>ایندکس خواندن را سریع ولی <strong>نوشتن</strong> را گران می‌کند (هر insert/update باید درخت ایندکس را هم به‌روز کند) و فضا می‌گیرد. ایندکس برای کوئری‌های پرتکرار با فیلتر/ترتیب مشخص (WHERE، ORDER BY، JOIN) ساخته می‌شود — نه روی هر ستونی.</p>'),
        ('سریع‌ترین پاسخ HTTP کدام است؟',
         '<p>پاسخی که <strong>ارسال نمی‌شود</strong>! کش مرورگر با Cache-Control خوب، فایل استاتیک با هش در نام (ManifestStaticFiles)، و ETag/304 یعنی مرورگر اصلاً درخواست نمی‌دهد یا بدنه نمی‌گیرد. لایه مرورگر ارزان‌ترین CDN دنیاست.</p>'),
    ],
    prereq_intro='پیش‌نیازها:',
    prereq=[
        'پروژه وبلاگ با داده <strong>واقعی/حجیم</strong> — با ۱۰ رکورد هیچ‌چیز معلوم نمی‌شود!',
        'اسکریپت ساخت داده تست (تمرین‌های فصل ۱۵ یا dumpdata).',
        'Debug Toolbar نصب (فصل ۲۱) و میدلور زمان‌سنج (فصل ۱۷).',
        'دسترسی به <span class="term" data-term="django-shell">شل</span> برای EXPLAIN.',
    ],
    prereq_callout=('warn', 'اول داده حجیم',
        'بهینه‌سازی روی ۲۰ رکورد توهم است. با اسکریپت زیر ۵۰ هزار پست بسازید:<br><code class="inline-code">Post.objects.bulk_create(Post(...) for ... in range(50000))</code> — یا management command سفارشی (تمرین فصل ۹).'),
    concepts=[
        dict(h='۵.۱ اندازه‌گیری: سه ابزار', body=[
            ('code', '۱) Debug Toolbar — نمای کلی', 'text', '''پنل SQL: تعداد کوئری‌ها، زمان هرکدام، Traceback هر کوئری
پنل Time: زمان هر بخش (SQL، قالب، میدلور)
→ صفحه فهرست با ۲۱ کوئری = بوی N+1'''),
            ('code', '۲) EXPLAIN در شل — سطح کوئری', 'python', '''qs = Post.objects.filter(published=True, created_at__gte=cutoff)
print(qs.explain(analyze=True, verbose=True))
# Seq Scan on blog_post  (cost=0.00..2183.00 rows=48000 width=...)
#   → «Seq Scan» = جدول کامل خوانده شد = ایندکس لازم دارد!
#   (analyze=True کوئری را واقعاً اجرا می‌کند — روی داده تولید مراقب!)'''),
            ('code', '۳) زمان‌سنجی پایتون — سطح تابع', 'python', '''import timeit

setup = "from blog.models import Post"
t = timeit.timeit(
    "list(Post.objects.filter(published=True)[:20])",
    setup=setup, number=100)
print(f"{t/100*1000:.1f}ms میانگین")'''),
            ('callout', 'tip', 'بودجه کارایی (Performance Budget)',
             'عدد بگذارید: «صفحه فهرست: ≤۱۰۰ms سمت سرور، ≤۵ کوئری، ≤۳۰۰KB وزن صفحه». هر تغییر که بودجه را شکست، در بازبینی کد رد می‌شود. بدون عدد، «کند» سلیقه‌ای است.'),
        ]),
        dict(h='۵.۲ دیتابیس: ایندکس‌ها', body=[
            ('code', 'سه سطح ایندکس‌گذاری', 'python', '''class Post(models.Model):
    # ۱) تک‌ستونی ساده
    views_count = models.PositiveIntegerField(default=0, db_index=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            # ۲) چندستونی — ترتیب ستون‌ها مهم است!
            # برای: filter(published=True).order_by("-created_at")
            models.Index(fields=["published", "-created_at"],
                         name="post_pub_created"),
            # ۳) شرطی (Postgres) — ایندکس کوچک و دقیق
            models.Index(fields=["views_count"], name="post_views_hot",
                         condition=models.Q(published=True)),
        ]'''),
            ('code', 'ایندکس تابعی (پیشرفته، Postgres)', 'python', '''from django.db.models import Func
from django.db.models.functions import Lower

models.Index(Lower("title"), name="post_title_lower")
# حالا filter(title__iexact=...) از ایندکس استفاده می‌کند'''),
            ('callout', 'warn', 'قواعد ایندکس چندستونی',
             'ایندکس (a, b) به کوئری‌های روی a، و a+b کمک می‌کند — ولی <strong>نه</strong> به کوئری فقط روی b (prefix rule). ستون با «انتخاب‌گری بیشتر» یا ستون WHERE اول، ستون ORDER BY آخر. بعد از ساخت: <code class="inline-code">python manage.py makemigrations && migrate</code> (ساخت ایندکس روی جدول بزرگ ممکن است قفل بگیرد — Postgres CONCURRENTLY راهش است).'),
        ]),
        dict(h='۵.۳ کوئری‌های بهینه', body=[
            ('code', 'چک‌لیست کوئری', 'python', '''# ✅ فقط آنچه لازم است
posts = (Post.objects
    .filter(published=True)
    .select_related("author", "author__user")   # JOIN برای FK
    .prefetch_related("tags", "comments")        # کوئری جدا برای m2m/reverse
    .only("id", "title", "slug", "created_at",
          "author__name", "author__user__username")
    .order_by("-created_at")[:20])

# ✅ شمارش بدون کشیدن ردیف‌ها
n = Post.objects.filter(published=True).count()          # SELECT COUNT(*)
exists = Post.objects.filter(slug=s).exists()            # SELECT 1 ... LIMIT 1

# ✅ نوشتن دسته‌ای
Post.objects.bulk_create(new_posts, batch_size=500)
Post.objects.bulk_update(posts, ["views_count"], batch_size=500)
qs.update(views_count=F("views_count") + 1)              # یک SQL اتمی'''),
            ('code', 'تله‌های رایج', 'python', '''# ❌ QuerySet تنبل را چندبار ارزیابی کنید = چندبار SQL
qs = Post.objects.all()
print(qs.count(), list(qs), qs[0])       # ۳ بار!
posts = list(qs)                          # ✅ یکبار materialize

# ❌ برش بعد از فیلترهای پایتونی
[obj for obj in Post.objects.all() if "x" in obj.title][:10]  # کل جدول!
Post.objects.filter(title__icontains="x")[:10]                # ✅ در SQL

# ❌ len(qs) به‌جای count() (کل ردیف‌ها را می‌کشد)'''),
        ]),
        dict(h='۵.۴ لایه‌های HTTP و کش', body=[
            ('code', 'GZip — یک خط، سود بزرگ', 'python', '''MIDDLEWARE = [
    "django.middleware.gzip.GZipMiddleware",   # بعد از Security
    ...,
]
# HTML/JSON متنی ~۷۰-۸۰٪ کوچک‌تر؛ در Nginx هم gzip on ممکن است'''),
            ('code', 'کش مرورگر برای استاتیک (WhiteNoise/Manifest)', 'python', '''# CompressedManifestStaticFilesStorage نام فایل را هش‌دار می‌کند:
# style.a1b2c3.css → چون محتوا عوض شود نام عوض می‌شود،
# می‌توان کش «بی‌نهایت» داد (cache-control: max-age=31536000, immutable)'''),
            ('code', 'ETag و کش ویو (فصل ۱۹)', 'python', '''from django.views.decorators.http import condition

@condition(last_modified_func=lambda r, pk: Post.objects.get(pk=pk).updated_at)
def post_detail(request, pk): ...   # تغییر نکرده → 304 بدون بدنه'''),
            ('code', 'تصاویر: بزرگ‌ترین وزن صفحات', 'python', '''# آپلود → تسک سلری (فصل ۲۴) → بندانگشتی وب (WebP):
from PIL import Image

def make_thumb(path, size=(480, 480)):
    with Image.open(path) as im:
        im.thumbnail(size)
        im.save(thumb_path(path), "WEBP", quality=80)
# در قالب فقط بندانگشتی را لود کنید؛ srcset برای اندازه‌های مختلف'''),
            ('callout', 'info', 'CDN کی لازم می‌شود؟',
             'وقتی کاربران پراکنده جغرافیایی دارید یا استاتیک سنگین (تصویر/فونت/JS). <span class="term" data-term="cdn">CDN</span> فایل‌های STATIC_ROOT را در لبه جهان کش می‌کند (ArvanCloud، Cloudflare). برای شروع، همان WhiteNoise+GZip کافی است.'),
        ]),
        dict(h='۵.۵ پایش در تولید', body=[
            ('code', 'کوئری‌های کند در لاگ Postgres', 'bash', '''# postgresql.conf
log_min_duration_statement = 500   # هر کوئری >۵۰۰ms لاگ شود
# سپس: grep روی لاگ → داوطلبان ایندکس/بازنویسی'''),
            ('code', 'متریک‌های ساده اپلیکیشنی', 'python', '''# میدلور فصل ۱۷ را ارتقا دهید:
if duration > 0.5:
    logger.warning("slow_request path=%s ms=%.0f queries=%s",
                   request.path, duration * 1000,
                   getattr(connection, "queries_log", "?"))
# در DEBUG، len(connection.queries) تعداد کوئری‌های همان درخواست است'''),
            '<ul>'
            '<li><strong>چهار عدد طلایی:</strong> زمان پاسخ (p50/p95)، تعداد درخواست بر ثانیه، نرخ خطا، اشباع (CPU/RAM/صف).</li>'
            '<li>ابزارها برای شروع: لاگ‌های Nginx (access time با $request_time)، Flower برای صف سلری، pg_stat_statements در Postgres.</li>'
            '<li>p95 مهم‌تر از میانگین است: میانگین ۵۰ms با p95=۳ ثانیه یعنی کاربران بدشانس رنج می‌برند.</li></ul>',
        ]),
    ],
    example_intro='یک صفحه «کند» را علمی سریع کنیم — از ۱۸۰۰ms تا ۴۵ms:',
    example=[
        ('code', 'وضعیت اولیه (Toolbar)', 'text', '''GET /blog/  → 1820ms
SQL: ۲۱ کوئری  |  کندترین: SELECT ... WHERE published ORDER BY created_at DESC (780ms, Seq Scan)
قالب: post_list.html با {{ post.author.name }} و {{ post.tags.all }}'''),
        ('code', 'گام ۱ — ایندکس برای فیلتر+ترتیب', 'python', '''class Meta:
    indexes = [
        models.Index(fields=["published", "-created_at"],
                     name="post_pub_created"),
    ]
# EXPLAIN بعد از ایندکس:
# Index Scan using post_pub_created ... (cost=0.29..8.31 rows=20)'''),
        ('code', 'گام ۲ — رفع N+1 در ویو', 'python', '''posts = (Post.objects.filter(published=True)
         .select_related("author", "author__user")
         .prefetch_related("tags")
         .order_by("-created_at")[:20])
# ۲۱ کوئری → ۴ کوئری'''),
        ('code', 'گام ۳ — only + کش فهرست', 'python', '''posts = posts.only("id", "title", "slug", "created_at", "author__name")
key = f"blog:list:home:v{cache.get_or_set(\'blog:version\', 1)}"
posts = cache.get_or_set(key, lambda: list(posts), timeout=60)'''),
        ('code', 'نتیجه', 'text', '''قبل: 1820ms، ۲۱ کوئری
بعد از گام ۱:   950ms، ۲۱ کوئری   (Seq Scan حذف)
بعد از گام ۲:   120ms، ۴ کوئری     (N+1 حذف)
بعد از گام ۳ (hit): 45ms، ۰ کوئری 🏆
هر گام با اندازه‌گیری تأیید شد — نه حدس!'''),
    ],
    workshop_intro='وبلاگ را زیر ذره‌بین ببرید:',
    workshop_tasks=[
        '<strong>کارگاه ۱:</strong> ۵۰هزار پست تستی با bulk_create بسازید؛ سه صفحه (فهرست، جزئیات، آمار) را با Toolbar بررسی و «بدترین کوئری» هرکدام را با explain(analyze=True) ثبت کنید.',
        '<strong>کارگاه ۲:</strong> برای الگوهای واقعی فیلتر خودتان حداقل دو ایندکس (یکی چندستونی، یکی شرطی) بسازید و EXPLAIN قبل/بعد را مقایسه کنید.',
        '<strong>کارگاه ۳:</strong> GZip + only() + کش نسخه‌دار فهرست را اعمال کنید؛ وزن پاسخ (Content-Length) و زمان را قبل/بعد گزارش کنید.',
    ],
    workshop_answers=[
        ('پاسخ کارگاه ۱',
         '<div class="code-box"><div class="code-head"><span>ساخت داده حجیم</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python"># blog/management/commands/seed.py\nfrom django.core.management.base import BaseCommand\nfrom blog.models import Post, Author\nimport random, faker\n\n\nclass Command(BaseCommand):\n    def handle(self, *args, **opts):\n        fake = faker.Faker("fa_IR")\n        authors = list(Author.objects.all())\n        posts = [\n            Post(title=fake.sentence()[:80],\n                 slug=f"seed-{i}",\n                 body=fake.text(2000),\n                 author=random.choice(authors),\n                 published=random.random() &gt; 0.2)\n            for i in range(50_000)\n        ]\n        Post.objects.bulk_create(posts, batch_size=1000)\n        self.stdout.write("50k ✅")</code></pre></div>'
         '<p>سپس برای هر صفحه یادداشت کنید: تعداد کوئری، زمان کل، و خروجی explain بدترین‌ها. Seq Scan روی جدول ۵۰ هزار ردیفی یعنی داوطلب قطعی ایندکس.</p>'),
        ('پاسخ کارگاه ۲',
         '<div class="code-box"><div class="code-head"><span>ایندکس‌های نمونه</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">indexes = [\n    models.Index(fields=["published", "-created_at"],\n                 name="post_pub_created"),\n    models.Index(fields=["views_count"], name="post_hot",\n                 condition=models.Q(published=True)),\n    models.Index(fields=["slug"], name="post_slug_idx"),  # یکتا که unique=True دارد\n]</code></pre></div>'
         '<p>مقایسه: قبل → <code class="inline-code">Seq Scan ... rows=48000 (780ms)</code>؛ بعد → <code class="inline-code">Index Scan using post_pub_created (2ms)</code>. عدد دقیق روی ماشین شما فرق می‌کند؛ <strong>نسبت</strong> مهم است. ایندکس شرطی روی «پست‌های داغ منتشرشده» کوچک‌تر و گرم‌تر در حافظه می‌ماند.</p>'),
        ('پاسخ کارگاه ۳',
         '<div class="code-box"><div class="code-head"><span>اندازه‌گیری GZip با curl</span><span class="lang">bash</span></div><pre class="code"><code data-lang="bash"># بدون فشرده‌سازی\ncurl -s -o /dev/null -w "size=%{size_download} time=%{time_total}\\n" \\\n  -H "Accept-Encoding: identity" http://localhost:8000/blog/\n\n# با GZip\ncurl -s -o /dev/null -w "size=%{size_download} time=%{time_total}\\n" \\\n  -H "Accept-Encoding: gzip" --compressed http://localhost:8000/blog/\n# نمونه خروج: 145KB → 28KB (~80٪ کاهش)</code></pre></div>'
         '<p>only() را با explain تأیید کنید (لیست ستون‌های SELECT کوچک‌تر). کش فهرست با نسخه (فصل ۱۹): در hit، صفر کوئری و ~5ms. سه گزارش قبل/بعد را در docs/perf.md پروژه نگه دارید — این یعنی «مهندسی» کارایی.</p>'),
    ],
    errors=[
        ('ایندکس ساختم ولی EXPLAIN همچنان Seq Scan است',
         'چند علت: داده کم است (پلنر Seq Scan را ارزان‌تر می‌داند — درست هم هست!)، تابع روی ستون در WHERE است (lower(title) بدون ایندکس تابعی)، یا ANALYZE لازم است (<code class="inline-code">ANALYZE blog_post;</code>). با ۵۰ هزار ردیف قضاوت کنید نه ۵۰ تا.'),
        ('select_related روی ManyToMany خطا/اثر ندارد',
         'برای m2m و روابط معکوس باید prefetch_related باشد؛ select_related فقط FK/O2O (JOIN یک‌به‌یک). اشتباه گرفتنشان N+1 را «حل‌نشده» نگه می‌دارد.'),
        ('کش کردم ولی صفحه برای کاربر A/B قاطی شد',
         'داده کاربرمحور را کش سراسری کرده‌اید (همان تله فصل ۱۹). کلید را با user.pk پارامتری کنید یا بخش خصوصی را از کش بیرون نگه دارید (Vary: Cookie برای صفحات احراز هویتی).'),
        ('GZip تصویرها را هم فشرده می‌کند و CPU می‌سوزد',
         'JPEG/PNG/WebP از قبل فشرده‌اند؛ فشرده‌سازی مجدد اتلاف است. GZipMiddleware فقط محتوای متنی را فشرده می‌کند، ولی اگر CPU تنگ است، فشرده‌سازی را به Nginx/CDN بسپارید.'),
        ('پس از migrate سایت موقتاً قفل شد (ساخت ایندکس)',
         'ساخت ایندکس روی جدول بزرگ در Postgres به‌طور پیش‌فرض قفل نوشتن می‌گیرد. راه تولید: مهاجرت با RunSQL و <code class="inline-code">CREATE INDEX CONCURRENTLY</code> (خارج از تراکنش — atomic=False در Migration).' ),
    ],
    errors_callout=('tip', 'ترتیب حمله به کندی',
        '۱) کوئری‌های اضافی (N+1) ۲) کوئری‌های سنگین (ایندکس/بازنویسی) ۳) حجم پاسخ (only/GZip/تصویر) ۴) کش. این ترتیب معمولاً بیشترین سود به ازای تلاش را دارد.'),
    exercises=[
        ('تمرین ۱ — ایندکس بساز یا نه؟',
         '<p><strong>سوال:</strong> روی کدام فیلدها ایندکس بزنید؟ (الف) Post.slug که unique=True است (ب) Comment.text (ج) Post.published + created_at برای صفحه اصلی (د) User.password</p>'
         '<p><strong>پاسخ:</strong> الف → لازم نیست، unique خودش ایندکس می‌سازد • ب → نه (متن بلند و جست‌وجویش full-text می‌خواهد نه B-tree) • ج → بله، چندستونی (published, -created_at) • د → هرگز (کوئری روی هش رمز معنا ندارد).</p>'),
        ('تمرین ۲ — شمارش کوئری',
         '<p><strong>سوال:</strong> این کد چند کوئری می‌زند؟ <code class="inline-code">for p in Post.objects.filter(published=True)[:10]: print(p.author.name, p.tags.count())</code></p>'
         '<p><strong>پاسخ:</strong> ۱ (فهرست) + ۱۰ (author هر پست — select_related ندارد) + ۱۰ (tags.count هر پست) = <strong>۲۱ کوئری</strong>. اصلاح: select_related("author") و prefetch tags با annotate(Count("tags")) → ۲ تا ۳ کوئری.</p>'),
        ('تمرین ۳ — تشخیص لایه',
         '<p><strong>سوال:</strong> هر کندی مربوط به کدام لایه است؟ (الف) TTFB صفحه ۳ ثانیه (ب) صفحه سریع می‌آید ولی «رندر» در مرورگر ۲ ثانیه (ج) بار دوم سایت فوری است ولی بار اول در شهر دیگر کند (د) هر شب ساعت ۳ سایت ۱۰ ثانیه‌ای می‌خوابد</p>'
         '<p><strong>پاسخ:</strong> الف → سرور/دیتابیس (کوئری‌ها؛ Toolbar/EXPLAIN) • ب → فرانت (JS سنگین، تصاویر بزرگ، فونت؛ Lighthouse) • ج → فاصله جغرافیایی/شبکه → <span class="term" data-term="cdn">CDN</span> • د → تسک زمان‌بندی‌شده سنگین (فصل ۲۴) روی همان دیتابیس — صف جدا یا nice/اولویت.</p>'),
    ],
    quiz=[
        dict(q='اولین قدم درست بهینه‌سازی چیست؟',
             opts=['افزودن کش', 'اندازه‌گیری و یافتن گلوگاه واقعی با ابزار',
                   'بازنویسی با زبان دیگر', 'افزودن ایندکس به همه فیلدها'],
             ans='b', explain='پروفایل/Toolbar/EXPLAIN بدون حدس زدن نشان می‌دهند زمان کجا می‌رود؛ بعد اصلاح، بعد اندازه‌گیری مجدد.'),
        dict(q='«Seq Scan» در خروجی EXPLAIN روی جدول بزرگ یعنی چه؟',
             opts=['کوئری بهینه است', 'کل جدول ردیف‌به‌ردیف خوانده شده — معمولاً نامزد ایندکس',
                   'ایندکس خراب است', 'دیتابیس قفل است'],
             ans='b', explain='برای فیلتر/ترتیب پرتکرار، Index Scan با ایندکس مناسب جای Seq Scan را می‌گیرد (۷۸۰ms → ۲ms در مثال فصل).'),
        dict(q='select_related و prefetch_related به‌ترتیب برای کدام روابط‌اند؟',
             opts=['هر دو m2m', 'FK/O2O (JOIN) و m2m/روابط معکوس (کوئری جدا و به هم چسباندن در پایتون)',
                   'm2m و FK', 'فرقی ندارند'],
             ans='b', explain='select_related با JOIN یک کوئری می‌سازد؛ prefetch_related یک کوئری IN برای مجموعه‌ها. جای غلط = N+1 باقی می‌ماند.'),
        dict(q='چرا len(queryset) برای شمارش اشتباه است؟',
             opts=['خطا می‌دهد', 'کل ردیف‌ها را از دیتابیس می‌کشد؛ count() فقط SELECT COUNT(*) می‌زند',
                   'کش نمی‌شود', 'ترتیب را عوض می‌کند'],
             ans='b', explain='برای «آیا چیزی هست؟» هم exists() کافی است (LIMIT 1). کشیدن ۵۰ هزار ردیف برای یک عدد = فاجعه.'),
        dict(q='سود GZipMiddleware عمدتاً روی چیست؟',
             opts=['تصاویر JPEG', 'محتوای متنی (HTML/JSON/CSS/JS) — معمولاً ۷۰-۸۰٪ کاهش حجم',
                   'سرعت کوئری', 'رمزنگاری داده'],
             ans='b', explain='فشرده‌سازی فایل‌های از قبل فشرده اتلاف CPU است؛ متن‌ها برنده بزرگ GZip هستند (فشرده ≠ رمزنگاری!).'),
        dict(q='ایندکس چه هزینه‌ای دارد؟',
             opts=['هیچ', 'نوشتن (INSERT/UPDATE/DELETE) کندتر و فضای دیسک بیشتر',
                   'خواندن کندتر', 'فقط روی SQLite اثر دارد'],
             ans='b', explain='هر ایندکس یک ساختار اضافی است که با هر نوشتن به‌روز می‌شود؛ پس فقط برای الگوهای کوئری واقعی ایندکس بسازید.'),
    ],
    project_title='پروفایل کارایی وبلاگ',
    project_intro='یک «بازرسی کارایی» کامل روی پروژه انجام دهید و گزارش بدهید.',
    project_checklist=[
        'داده حجیم (≥۵۰ هزار پست) با management command ساخته شود.',
        'گزارش سه صفحه اصلی: زمان، تعداد کوئری، بدترین EXPLAIN (قبل).',
        'حداقل ۳ اصلاح: ایندکس چندستونی، رفع N+1، only()/کش فهرست.',
        'گزارش بعد از اصلاح + درصد بهبود در docs/perf.md.',
        'بودجه کارایی مکتوب: p95 ≤۲۰۰ms و ≤۵ کوئری برای صفحات فهرست.',
    ],
    project_callout=('info', 'ابزارهای بعدی',
        'django-silk (پروفایلر درخواست/کوئری با UI)، pg_stat_statements (کوئری‌های کند تجمیعی)، Lighthouse (سمت مرورگر). هر سه مکمل این فصل‌اند.'),
    summary_items=[
        'اول اندازه‌گیری: Toolbar + explain(analyze) + timeit؛ بودجه عددی بگذارید.',
        'ایندکس: تک‌ستونی/چندستونی/شرطی؛ prefix rule و هزینه نوشتن را بشناسید.',
        'کوئری: select_related/prefetch، only، count/exists، bulk_* و F().',
        'لایه‌های HTTP: GZip، کش مرورگر با نام هش‌دار، ETag/304، تصویر WebP.',
        'پایش تولید: لاگ کوئری کند، p95، چهار عدد طلایی.',
    ],
    golden='کارایی یک ویژگی نیست، یک عادت است: هر PR با پرسش «چند کوئری؟ چند میلی‌ثانیه؟».',
    faq=[
        ('Redis را کجا و Memcached را کجا؟',
         '<p>در این دوره همه‌جا Redis (کش + بروکر سلری + throttle). Memcached سبک‌تر و صرفاً کش است. تفاوت عملی برای شما در این مقیاس ناچیز است؛ یک سرویس مشترک ساده‌تر از دو سرویس است.</p>'),
        ('کش کوئری (per-query cache) نداریم؟',
         '<p>کش سطح QuerySet جنگو حذف شده؛ Postgres هم page cache داخلی دارد. راه درست: کش <strong>نتیجه</strong> در سطح اپ (فصل ۱۹) و کوئری‌های کارآمد. دنبال «جادوی خودکار» نباشید.</p>'),
        ('چطور بفهمم گلوگاه CPU است یا IO؟',
         '<p>روی سرور: top/htop (CPU پایتون بالا = محاسبه/قالب/سریالایز؛ iowait بالا = دیسک/دیتابیس). در اپ: زمان SQL در Toolbar در برابر زمان قالب. p95 لاگ‌های Nginx با $request_time و $upstream_response_time تفکیک شبکه/اپ را می‌دهد.</p>'),
    ],
    next_step='بک‌اند سریع شد؛ تجربه کاربر را کامل می‌کنیم: <strong>فصل ۲۸</strong> — جنگو و فرانت‌اند: از <span class="term" data-term="htmx">HTMX</span> و <span class="term" data-term="tailwind">Tailwind</span> تا <span class="term" data-term="react">React</span> روی API.',
),

# ================================================================ فصل ۲۸
dict(
    n=28, icon='🎭', title='جنگو و فرانت‌اند — HTMX، Tailwind و SPA', cat=5, mins=105, lvl_label='پیشرفته',
    hero_desc='طیف انتخاب فرانت‌اند برای جنگو: قالب‌ها + <span class="term" data-term="htmx">HTMX</span> برای تعامل بدون JS سنگین، <span class="term" data-term="tailwind">Tailwind</span> برای استایل، و <span class="term" data-term="react">React</span>/<span class="term" data-term="vue">Vue</span> + DRF برای <span class="term" data-term="spa">SPA</span> — با مثال عملی هرکدام.',
    s1_intro='«جنگو یا React؟» سوال غلطی است — سوال درست «کدام ترکیب برای این پروژه؟» است. این فصل سه مسیر واقعی را با کد نشان می‌دهد تا آگاهانه انتخاب کنید: HTMX-محور، هیبریدی، و SPA کامل.',
    objectives=[
        'سه معماری رایج فرانت‌اند برای جنگو را مقایسه کنید.',
        'با HTMX تعامل واقعی (لایک، جست‌وجوی زنده، اسکرول بی‌نهایت) بدون نوشتن JS بسازید.',
        'Tailwind را به پروژه قالب‌محور وصل کنید.',
        'یک SPA ساده React/Vue را به API فصل ۲۳ وصل کنید (fetch + JWT + CORS).',
        'معیارهای انتخاب (تیم، SEO، پیچیدگی) را به کار ببرید.',
    ],
    s1_position='<strong>جایگاه فصل:</strong> قالب‌ها (۱۰) مسیر اول، API (۲۲-۲۳) مسیر سوم؛ پروژه نهایی (۳۰) یکی از این سه را انتخاب می‌کند.',
    roadmap=[
        ('طیف انتخاب', 'سه معماری و معیارها.'),
        ('HTMX', 'تعامل با HTML.'),
        ('Tailwind', 'استایل مدرن در قالب.'),
        ('SPA + DRF', 'فرانت جدا روی API.'),
    ],
    mind_qs=[
        ('HTMX دقیقاً چه کار می‌کند؟',
         '<p>یک کتابخانه ~۱۴KB که به تگ‌های HTML «قدرت AJAX» می‌دهد: <code class="inline-code">hx-post="/like/5/"</code> یعنی «این درخواست را بفرست و <strong>HTML برگشتی</strong> را در فلان عنصر جایگزین کن». سرور همان ویوهای جنگو/قالب‌های تکه‌ای است — بدون ساخت API، بدون state سمت کلاینت.</p>'),
        ('کجا SPA لازم می‌شود و کجا اضافه‌کاری است؟',
         '<p>SPA برای اپ‌های «شبیه نرم‌افزار»: داشبورد پیچیده، آفلاین‌مانند، state سنگین سمت کلاینت. برای وبلاگ/فروشگاه محتوامحور، رندر سمت سرور + HTMX هم سریع‌تر ساخته می‌شود هم <strong>SEO</strong> بهتری دارد. هزینه SPA: یک پروژه فرانت کامل، CORS/JWT، دو برابر سطح دیباگ.</p>'),
        ('Tailwind و Bootstrap چه فرقی دارند؟',
         '<p>Bootstrap «کامپوننت آماده» می‌دهد (سریع، ولی همه سایت‌ها شبیه هم)؛ Tailwind «کلاس‌های اتمی» می‌دهد (flex, p-4, text-sm) که در همان HTML ترکیبشان می‌کنید — طراحی کاملاً سفارشی بدون نوشتن CSS جدا. در پروژه جنگو با build ساده یا CDN شروع می‌شود.</p>'),
    ],
    prereq_intro='پیش‌نیازها:',
    prereq=[
        'پروژه وبلاگ با قالب base.html و API فصل ۲۳ (برای بخش SPA).',
        'Node.js نصب‌شده (فقط برای build Tailwind و ساخت SPA — اختیاری در بخش HTMX).',
        'آشنایی اولیه با HTML/فچ در مرورگر (DevTools → Network).',
        'درک partial/تکه قالب (include) از فصل ۱۰.',
    ],
    prereq_callout=None,
    concepts=[
        dict(h='۵.۱ سه معماری، یک تصمیم', body=[
            '<div class="table-wrap"><table class="compare"><thead><tr><th></th><th>قالب + کمی JS</th><th>قالب + HTMX + Tailwind</th><th>SPA (React/Vue) + DRF</th></tr></thead><tbody>'
            '<tr><td>رندر</td><td>سرور</td><td>سرور (تکه‌ای)</td><td>کلاینت</td></tr>'
            '<tr><td>SEO</td><td>عالی</td><td>عالی</td><td>نیاز به کار (SSR/prerender)</td></tr>'
            '<tr><td>تعامل پیچیده</td><td>سخت (JS دستی)</td><td>متوسط تا خوب</td><td>عالی</td></tr>'
            '<tr><td>تعداد پروژه</td><td>۱ (جنگو)</td><td>۱ (جنگو)</td><td>۲ (جنگو + فرانت)</td></tr>'
            '<tr><td>مناسب</td><td>سایت محتوایی ساده</td><td>داشبورد/فروشگاه/ابزار داخلی</td><td>اپ محصولی پیچیده، تیم جدا</td></tr>'
            '</tbody></table></div>',
            ('callout', 'tip', 'قاعده شست',
             '«محتوا محور + SEO مهم → سرور-رندر (مسیر ۱/۲). اپ‌محور + state سنگین → SPA (مسیر ۳). شک دارید → HTMX: ۸۰٪ سود SPA با ۲۰٪ پیچیدگی.»'),
        ]),
        dict(h='۵.۲ HTMX — تعامل با خود HTML', body=[
            ('code', 'نصب (یک فایل ایستا!)', 'html', '''<!-- assets/js/htmx.min.js را دانلود و در base.html: -->
<script src="{% static 'js/htmx.min.js' %}" defer></script>'''),
            ('code', '۱) دکمه لایک بدون رفرش', 'html', '''<!-- قالب post_list.html -->
<button hx-post="{% url 'blog:like' post.pk %}"
        hx-target="#like-count-{{ post.pk }}"
        hx-swap="outerHTML"
        hx-headers='{"X-CSRFToken": "{{ csrf_token }}"}'
        class="like-btn">
  ❤ <span id="like-count-{{ post.pk }}">{{ post.likes_count }}</span>
</button>'''),
            ('code', 'ویوی برگرداننده «تکه HTML»', 'python', '''@login_required
@require_POST
def like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    Like.objects.get_or_create(user=request.user, post=post)
    return render(request, "blog/partials/like_count.html",
                  {"post": post})   # فقط تکه، نه صفحه کامل!'''),
            ('code', '۲) جست‌وجوی زنده', 'html', '''<input type="search" name="q" placeholder="جست‌وجو..."
       hx-get="{% url 'blog:search' %}"
       hx-trigger="keyup changed delay:300ms"
       hx-target="#results"
       hx-indicator=".spinner">
<div id="results"></div>
<span class="spinner htmx-indicator">⏳</span>'''),
            ('code', '۳) اسکرول بی‌نهایت', 'html', '''{% for post in posts %}
  {% include "blog/partials/post_card.html" %}
{% endfor %}

{% if page_obj.has_next %}
<div hx-get="?page={{ page_obj.next_page_number }}"
     hx-trigger="revealed"
     hx-swap="afterend">
  <span class="htmx-indicator">در حال بارگذاری...</span>
</div>
{% endif %}'''),
            ('callout', 'info', 'چرا hx-headers با CSRF؟',
             'درخواست‌های POST/PUT خارج از <span class="term" data-term="form">فرم</span> هستند؛ CsrfViewMiddleware توکن می‌خواهد. راه تمیزتر سراسری: در base.html روی body تگ <code class="inline-code">hx-headers=\'{"X-CSRFToken": "{{ csrf_token }}"}\'</code> بگذارید تا همه درخواست‌ها ارث ببرند.'),
        ]),
        dict(h='۵.۳ Tailwind CSS در پروژه قالب‌محور', body=[
            ('code', 'راه سریع: CLI بدون Node (standalone)', 'bash', '''# دانلود باینری tailwindcss و ساخت CSS:
./tailwindcss -i src/input.css -o static/css/tailwind.css \\
    --content "./templates/**/*.html" --minify'''),
            ('code', 'src/input.css و قالب', 'css', '''@tailwind base;
@tailwind components;
@tailwind utilities;'''),
            ('code', 'نمونه کارت پست با Tailwind', 'html', '''<!-- templates/blog/partials/post_card.html -->
<article class="bg-white dark:bg-slate-800 rounded-xl shadow p-5
                hover:shadow-lg transition">
  <h2 class="text-xl font-bold text-emerald-600">
    <a href="{{ post.get_absolute_url }}">{{ post.title }}</a>
  </h2>
  <p class="text-sm text-gray-500 mt-1">
    {{ post.author.name }} · {{ post.created_at|date:"Y/m/d" }}
  </p>
  <p class="mt-3 text-gray-700 line-clamp-3">{{ post.body|truncatewords:40 }}</p>
</article>'''),
            ('callout', 'warn', 'RTL و Tailwind',
             'برای سایت فارسی: در tailwind.config <code class="inline-code">direction: rtl</code> ندارد — از کلاس‌های منطقی جدید استفاده کنید (ms-4/me-4 به‌جای ml/mr، ps-/pe-، text-start/end) و dir="rtl" روی html. کلاس‌های فیزیکی (ml-) در RTL برعکس به نظر می‌رسند!'),
        ]),
        dict(h='۵.۴ مسیر SPA: فرانت جدا روی DRF', body=[
            ('code', '۱) CORS برای دامنه/پورت فرانت', 'python', '''# pip install django-cors-headers
INSTALLED_APPS += ["corsheaders"]
MIDDLEWARE += ["corsheaders.middleware.CorsMiddleware"]  # بالاترین حد ممکن

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",     # Vite dev
    "https://app.example.com",
]'''),
            ('code', '۲) مصرف API در React (Vite)', 'jsx', '''// src/api.js — کلاینت کوچک با JWT
const BASE = import.meta.env.VITE_API_BASE; // http://localhost:8000/api
let access = localStorage.getItem("access");

export async function api(path, opts = {}) {
  const res = await fetch(`${BASE}/${path}`, {
    ...opts,
    headers: {
      "Content-Type": "application/json",
      ...(access && { Authorization: `Bearer ${access}` }),
      ...opts.headers,
    },
  });
  if (res.status === 401) {
    // تلاش برای refresh؛ در صورت شکست → صفحه ورود
    const ok = await refresh();
    if (ok) return api(path, opts);
    location.href = "/login";
  }
  return res.status === 204 ? null : res.json();
}

// src/Posts.jsx
export default function Posts() {
  const [posts, setPosts] = useState([]);
  useEffect(() => { api("posts/").then(d => setPosts(d.results)); }, []);
  return (
    <ul>{posts.map(p => <li key={p.id}>{p.title}</li>)}</ul>
  );
}'''),
            ('code', '۳) یا Vue 3 به همان سادگی', 'html', '''<!-- حتی بدون build، با CDN در همان قالب جنگو -->
<div id="app" data-api="{% url 'api_post_list' %}">
  <ul><li v-for="p in posts">[[ p.title ]]</li></ul>
</div>
<script type="module">
  import { createApp } from 'https://unpkg.com/vue@3/dist/vue.esm-browser.js'
  createApp({
    delimiters: ['[[', ']]'],           // تداخل نکردن با {{ }} جنگو!
    data: () => ({ posts: [] }),
    async mounted() {
      this.posts = (await (await fetch(this.$el.dataset.api)).json()).results
    },
  }).mount('#app')
</script>'''),
            ('callout', 'danger', 'delimiters در Vue',
             'هم Vue هم جنگو از {{ }} استفاده می‌کنند؛ بدون تغییر delimiter، قالب جنگو سعی می‌کند p.title را رندر کند (و خالی/خطا می‌دهد). در Vue: <code class="inline-code">delimiters: [\'[[\', \']]\']</code> یا v-pre روی بلوک.'),
        ]),
        dict(h='۵.۵ تصمیم‌گیری نهایی', body=[
            '<ul>'
            '<li><strong>تیم یک‌نفره/کوچک + محتوامحور:</strong> قالب + HTMX + Tailwind. یک دیپلوی، یک زبان، SEO عالی.</li>'
            '<li><strong>محصول اپ‌گونه + تیم فرانت جدا:</strong> DRF (فصل ۲۳) + React/Vue + JWT. مرز تمیز API.</li>'
            '<li><strong>مهاجرت تدریجی:</strong> سایت موجود قالبی است؟ صفحه‌به‌صفحه بخش‌های تعاملی را HTMX کنید؛ یا فقط داشبورد را SPA بسازید زیر app.example.com.</li></ul>',
            ('callout', 'info', 'آنچه در همه مسیرها ثابت است',
             'مدل‌ها، ORM، احراز هویت، مجوزها و تست‌های شما — سرمایه اصلی، بک‌اند است. فرانت‌اند «لایه ارائه» است و قابل تعویض؛ پس وسواس را روی API/داده بگذارید.'),
        ]),
    ],
    example_intro='یک ویژگی را در هر سه معماری — «افزودن نظر بدون رفرش»:',
    example=[
        ('code', 'مسیر ۱: JS دستی (بدون کتابخانه)', 'html', '''<form id="comment-form" data-url="{% url 'blog:add_comment' post.slug %}">
  {% csrf_token %}{{ form.as_p }}<button>ارسال</button>
</form>
<ul id="comments">{% for c in post.comments.all %}<li>{{ c.text }}</li>{% endfor %}</ul>
<script>
document.getElementById('comment-form').onsubmit = async (e) => {
  e.preventDefault();
  const f = e.target;
  const res = await fetch(f.dataset.url, {method:'POST', body:new FormData(f)});
  const li = document.createElement('li');
  li.textContent = new FormData(f).get('text');
  document.getElementById('comments').append(li);
  f.reset();
};
</script>'''),
        ('code', 'مسیر ۲: HTMX — بدون یک خط JS', 'html', '''<form hx-post="{% url 'blog:add_comment' post.slug %}"
      hx-target="#comments" hx-swap="beforeend"
      hx-on::after-request="this.reset()">
  {% csrf_token %}{{ form.as_p }}<button>ارسال</button>
</form>
<ul id="comments">...</ul>
<!-- ویو در POST موفق، تکه <li> کامنت جدید را render می‌کند -->'''),
        ('code', 'ویوی دو حالته (HTML کامل برای GET، تکه برای POST)', 'python', '''@require_http_methods(["GET", "POST"])
def add_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            if request.headers.get("HX-Request"):     # ← HTMX بوده
                return render(request,
                              "blog/partials/comment_item.html",
                              {"comment": comment})
            return redirect(post)
    ...'''),
        ('code', 'مسیر ۳: SPA روی API', 'jsx', '''// فرانت React — POST JSON به /api/comments/
await api("comments/", {
  method: "POST",
  body: JSON.stringify({ post: postId, name, text }),
});
// پاسخ 201 + شیء → افزودن به state → رندر مجدد لیست'''),
        '<p>مقایسه کنید: مسیر ۲ کمترین کد را دارد و سرور HTML می‌دهد (SEO رایگان)؛ مسیر ۳ منعطف‌ترین برای state پیچیده است. همان ویژگی، سه فلسفه.</p>',
    ],
    workshop_intro='هر سه مسیر را با دست لمس کنید:',
    workshop_tasks=[
        '<strong>کارگاه ۱:</strong> HTMX را اضافه کنید و دکمه لایک (۵.۲) را کامل پیاده کنید — شامل ویوی تکه‌ای، CSRF و به‌روزرسانی شمارنده بدون رفرش.',
        '<strong>کارگاه ۲:</strong> جست‌وجوی زنده با hx-get و تأخیر ۳۰۰ms بسازید؛ تکه نتیجه را با همان قالب post_card رندر کنید.',
        '<strong>کارگاه ۳:</strong> یک صفحه Vue/CDN (بدون build!) بسازید که فهرست پست‌ها را از <code class="inline-code">/api/posts/</code> بگیرید و نمایش دهد — با حل مسئله delimiter.',
    ],
    workshop_answers=[
        ('پاسخ کارگاه ۱',
         '<div class="code-box"><div class="code-head"><span>تکه like_count.html</span><span class="lang">html</span></div><pre class="code"><code data-lang="html">&lt;button hx-post="{% url \'blog:like\' post.pk %}"\n        hx-target="closest button" hx-swap="outerHTML"&gt;\n  ❤ &lt;span&gt;{{ post.likes_count }}&lt;/span&gt;\n&lt;/button&gt;</code></pre></div>'
         '<p>ویو مثل ۵.۲ ولی با hx-target="closest button" کل دکمه را با نسخه تازه (شمار جدید) جایگزین می‌کنیم — ساده‌تر از مدیریت id یکتا برای هر پست. CSRF سراسری را روی body بگذارید تا هر تگ hx لازم نداشته باشد. تست: Network را در DevTools باز کنید — باید درخواست POST کوچک با پاسخ HTML تکه ببینید، نه رفرش صفحه.</p>'),
        ('پاسخ کارگاه ۲',
         '<div class="code-box"><div class="code-head"><span>ویوی جست‌وجوی تکه‌ای</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">def search(request):\n    q = request.GET.get("q", "").strip()\n    posts = (Post.objects.filter(published=True, title__icontains=q)\n             .select_related("author")[:20] if q else [])\n    return render(request, "blog/partials/post_cards.html",\n                  {"posts": posts, "q": q})</code></pre></div>'
         '<p>post_cards.html فقط حلقه {% include post_card %} است. hx-trigger="keyup changed delay:300ms" سه بهینه‌سازی در یک خط: فقط تغییر واقعی، با تأخیر (جلوگیری از رگبار درخواست)، و hx-indicator برای UX. اگر q خالی بود پیام «چیزی بنویسید!» برگردانید — تکه خالی گیج‌کننده است.</p>'),
        ('پاسخ کارگاه ۳',
         '<div class="code-box"><div class="code-head"><span>صفحه Vue بدون build</span><span class="lang">html</span></div><pre class="code"><code data-lang="html">{# templates/vue_demo.html — extends base #}\n{% block content %}\n&lt;div id="app"&gt;\n  &lt;h1&gt;پست‌ها (Vue + DRF)&lt;/h1&gt;\n  &lt;ul v-if="posts.length"&gt;\n    &lt;li v-for="p in posts" :key="p.id"&gt;[[ p.title ]]&lt;/li&gt;\n  &lt;/ul&gt;\n  &lt;p v-else&gt;[[ loading ? "بارگذاری..." : "خالی" ]]&lt;/p&gt;\n&lt;/div&gt;\n&lt;script type="module"&gt;\nimport { createApp } from "https://unpkg.com/vue@3/dist/vue.esm-browser.js"\ncreateApp({\n  delimiters: ["[[", "]]"],\n  data: () =&gt; ({ posts: [], loading: true }),\n  async mounted() {\n    const r = await fetch("/api/posts/?format=json")\n    this.posts = (await r.json()).results\n    this.loading = false\n  },\n}).mount("#app")\n&lt;/script&gt;\n{% endblock %}</code></pre></div>'
         '<p>نکات: ① delimiters مشکل {{ }} را حل می‌کند ② چون فرانت همان دامنه جنگو است، CORS/JWT لازم نشد (SessionAuthentication کافی) — این «هیبرید» خوش‌قیافه‌ترین راه ورود به Vue است ③ ?format=json برای اطمینان از پاسخ JSON حتی از مرورگر.</p>'),
    ],
    errors=[
        ('HTMX هیچ کاری نمی‌کند (کلیک = رفرش کامل یا هیچ)',
         'اسکریپت htmx.min.js لود نشده (مسیر static/defer) یا hx-post به URLای می‌خورد که 403/302 می‌دهد (CSRF/ورود). تب Network را ببینید: درخواست hx رفت؟ پاسخ چه بود؟ ویو باید تکه HTML با 200 برگرداند نه redirect.'),
        ('استایل Tailwind اعمال نمی‌شود',
         'فایل output ساخته/لینک نشده، یا --content الگوی قالب‌ها را شامل نمی‌شود (کلاس‌های استفاده‌نشده purge می‌شوند!). بعد از هر تغییر قالب، build را دوباره بزنید.'),
        ('SPA خطای CORS در کنسول می‌دهد',
         'corsheaders نصب/ثبت نشده، یا origin دقیق (http://localhost:5173 با پورت!) در CORS_ALLOWED_ORIGINS نیست، یا میدلور CorsMiddleware پایین‌تر از حد لازم است. پیام خطای کنسول origin مورد انتظار را می‌گوید.'),
        ('{{ p.title }} در صفحه خالی رندر می‌شود',
         'قالب جنگو آن را «خورد»! تداخل delimiter با Vue/Alpine: از [[ ]] (تنظیم delimiters) یا v-pre یا {% verbatim %} استفاده کنید.'),
        ('fetch به API «۴۰۳ CSRF» می‌دهد',
         'SessionAuthentication با POST مرورگری توکن CSRF می‌خواهد (فصل ۲۲). برای SPA واقعی: JWT/Bearer استفاده کنید (نیاز به CSRF ندارد) یا هدر X-CSRFToken را از کوکی csrftoken بفرستید.'),
    ],
    errors_callout=('tip', 'DevTools دوست شماست',
        'هر تعامل HTMX/fetch یک درخواست شبکه است: تب Network نوع/مسیر/پاسخ را نشان می‌دهد. ۹۰٪ «کار نمی‌کند»ها با یک نگاه به آن حل می‌شود.'),
    exercises=[
        ('تمرین ۱ — انتخاب معماری',
         '<p><strong>سوال:</strong> برای هر محصول کدام مسیر؟ (الف) وبلاگ شخصی با SEO مهم (ب) داشبورد داخلی شرکت با جدول‌ها و فرم‌های زیاد (ج) اپلیکیشن مدیریت پروژه بلادرنگ با درگ‌اند‌دراپ سنگین</p>'
         '<p><strong>پاسخ:</strong> الف → قالب + Tailwind (HTMX برای جست‌وجو) • ب → HTMX + تکه‌های قالب (سرعت توسعه، بدون تیم فرانت) • ج → SPA (React/Vue) + DRF + احتمالاً WebSocket. معیار اصلی: پیچیدگی state سمت کلاینت و نیاز SEO.</p>'),
        ('تمرین ۲ — تکه یا JSON؟',
         '<p><strong>سوال:</strong> ویوی like در مسیر HTMX «تکه HTML» برمی‌گرداند و در مسیر SPA «JSON». مزیت/عیب هرکدام؟</p>'
         '<p><strong>پاسخ:</strong> تکه HTML: منطق نمایش در سرور می‌ماند (قالب/ترجمه/i18n خودکار)، فرانت احمق و ساده؛ ولی فقط همان‌جا مصرف می‌شود. JSON: برای هر کلاینتی (موبایل، SPA) قابل استفاده و کش‌پذیر؛ ولی منطق نمایش در کلاینت تکرار می‌شود. پروژه‌های بزرگ اغلب هر دو endpoint را دارند.</p>'),
        ('تمرین ۳ — SEO در SPA',
         '<p><strong>سناریو:</strong> فروشگاه با React می‌خواهد صفحات محصول در گوگل ایندکس شوند. سه راه حل؟</p>'
         '<p><strong>پاسخ:</strong> ① SSR با Next.js/Nuxt (رندر سمت سرور فریم‌ورک) ② prerendering صفحات عمومی ③ معماری هیبرید: صفحات عمومی (محصول/فهرست) را جنگو رندر کند و بخش «سبد/داشبورد» SPA باشد. برای محتوای عمومی، سرور-رندر همیشه ساده‌ترین پاسخ SEO است.</p>'),
    ],
    quiz=[
        dict(q='HTMX چه چیزی را به تگ‌های HTML اضافه می‌کند؟',
             opts=['استایل', 'ارسال درخواست AJAX و جایگزینی پاسخ HTML در DOM — بدون نوشتن JavaScript',
                   'مسیریابی', 'کامپایل قالب'],
             ans='b', explain='hx-post/hx-get + hx-target/hx-swap: سرور تکه HTML می‌فرستد و HTMX جایش می‌گذارد. منطق در همان ویوهای جنگو می‌ماند.'),
        dict(q='ویوی جنگو در مسیر HTMX باید چه برگرداند؟',
             opts=['JSON', 'تکه HTML (partial) با 200 — نه صفحه کامل و نه redirect',
                   'صفحه کامل', 'هیچ (204)'],
             ans='b', explain='هدف جایگزینی یک عنصر است؛ صفحه کامل یا redirect در DOM نتیجه عجیب می‌دهد. با HX-Request می‌توان دو رفتار داشت.'),
        dict(q='مشکل {{ }} بین جنگو و Vue چطور حل می‌شود؟',
             opts=['حل نمی‌شود', 'delimiters در Vue (مثل [[ ]]) یا {% verbatim %} در جنگو',
                   'حذف Vue', 'فرقی ندارند'],
             ans='b', explain='هر دو موتور همان نشانگر را می‌خواهند؛ یکی باید نشانگرش عوض شود وگرنه قالب جنگو عبارت Vue را خالی رندر می‌کند.'),
        dict(q='CORS_ALLOWED_ORIGINS چه چیزی را کنترل می‌کند؟',
             opts=['کاربران مجاز', 'دامنه‌های (origin) مجاز برای خواندن API توسط جاوااسکریپت مرورگر',
                   'سرعت API', 'رمزنگاری'],
             ans='b', explain='وقتی فرانت روی origin دیگر است (localhost:5173 یا app.site.com)، مرورگر اجازه خواندن پاسخ را فقط برای originهای فهرست‌شده می‌دهد.'),
        dict(q='برای وبلاگ محتوامحور با SEO مهم، کدام معماری مناسب‌تر است؟',
             opts=['SPA کامل React', 'رندر سمت سرور (قالب/HTMX)',
                   'API بدون فرانت', 'فرقی ندارد'],
             ans='b', explain='HTML آماده از سرور = خزش/ایندکس آسان و First Paint سریع؛ SPA نیاز به SSR/prerender اضافه برای همان نتیجه دارد.'),
        dict(q='کلاس‌های ms-4/ps-4 در Tailwind چه مزیتی برای سایت فارسی دارند؟',
             opts=['سریع‌ترند', 'منطقی‌اند (start/end) و با dir=rtl خودکار به سمت درست می‌نشینند',
                   'رندوم‌اند', 'فقط در LTR کار می‌کنند'],
             ans='b', explain='کلاس‌های فیزیکی ml/mr با تغییر جهت برعکسِ انتظار می‌شوند؛ ms/me و ps/pe بر اساس جهت سند عمل می‌کنند — RTL بدون بازنویسی.'),
    ],
    project_title='فرانت‌اند وبلاگ به انتخاب شما',
    project_intro='یکی از سه مسیر را کامل پیاده کنید (پیشنهاد: HTMX — بیشترین نسبت سود/تلاش).',
    project_checklist=[
        'مسیر HTMX: لایک + جست‌وجوی زنده + اسکرول بی‌نهایت + افزودن نظر، همه بدون رفرش.',
        'استایل Tailwind (build یا CDN) روی کارت‌ها و فرم‌ها + پشتیبانی RTL.',
        'ویوهای تکه‌ای (partials/) با تشخیص HX-Request برای سازگاری no-JS.',
        'یا مسیر SPA: صفحه فهرست/جزئیات/ورود با JWT + CORS + مدیریت خطای ۴۰۱.',
        'مستند «چرا این مسیر را انتخاب کردم» با مقایسه ۵.۱.',
    ],
    project_callout=('tip', 'پلکان مهاجرت',
        'مسیر HTMX را از یک ویو شروع کنید (دکمه لایک)؛ اگر جواب داد، صفحه‌به‌صفحه گسترش دهید. لازم نیست کل سایت یک‌شبه عوض شود — مزیت بزرگ همین تدریجی بودن است.'),
    summary_items=[
        'سه معماری: قالب+JS / قالب+HTMX+Tailwind / SPA+DRF — انتخاب بر پایه محتوا، state و تیم.',
        'HTMX: درخواست از تگ HTML، پاسخ تکه HTML؛ CSRF سراسری روی body.',
        'ویوهای دو حالته با تشخیص HX-Request؛ progressive enhancement.',
        'Tailwind با کلاس‌های منطقی (ms/ps) برای RTL.',
        'SPA: CORS دقیق + JWT + مدیریت ۴۰۱/refresh؛ delimiterها را جدا کنید.',
    ],
    golden='فریم‌ورک فرانت مهم نیست؛ مهم این است که «مرز» فرانت و بک‌اند تمیز باشد: HTML تکه‌ای یا JSON قرارداددار.',
    faq=[
        ('Alpine.js کجای این طیف است؟',
         '<p>کتابخانه ~۱۵KB برای تعامل «جزیره‌ای» کوچک (باز/بسته شدن منو، تب‌ها، فرم‌های ساده) با attributeهای x-data/x-show. مکمل عالی قالب‌های جنگو و HTMX — سه‌تایی «HOT stack» معروف (HTMX+Alpine+Tailwind) دقیقاً همین ترکیب است.</p>'),
        ('آیا HTMX برای اپ‌های بزرگ مقیاس می‌گیرد؟',
         '<p>برای اکثر داشبوردها/فروشگاه‌ها بله (نمونه‌های تولیدی بزرگ دارد). جایی به سقف می‌خورد که state پیچیده کلاینت لازم شود (ویرایشگر زنده، آفلاین، درگ سنگین) — آنجا SPA درست است. می‌شود ترکیبی: ۹۰٪ صفحات HTMX، یک بخش SPA.</p>'),
        ('Django 6.0 template partials به HTMX کمک می‌کند؟',
         '<p>بله! با {% partialdef %}/{% partial %} (فصل ۲۹) تعریف تکه در همان فایل قالب می‌ماند و با syntax مثل "post_list.html#card" قابل include/render است — فایل‌های partials پراکنده کم می‌شوند و ویوهای HTMX تمیزتر.</p>'),
    ],
    next_step='ابزارها را دیدیم؛ حالا «به‌روز» می‌مانیم: <strong>فصل ۲۹</strong> — جنگو ۵.۲ LTS و ۶.۰: tasks داخلی، template partials، CSP و کلیدهای مرکب.',
),

# ================================================================ فصل ۲۹
dict(
    n=29, icon='🆕', title='جنگوی امروز — 5.2 LTS و 6.0', cat=5, mins=90, lvl_label='پیشرفته',
    hero_desc='چه چیزی در جنگو ۵.۲ (LTS) و ۶.۰ تازه است: <span class="term" data-term="task">Background Tasks</span> داخلی، <span class="term" data-term="template-partial">Template Partials</span>، پشتیبانی بومی CSP، کلیدهای اصلی مرکب، AsyncPaginator و متدولوژی ارتقای نسخه.',
    s1_intro='جنگو هر ۸ ماه یک نسخه ویژگی و هر ~۲.۵ سال یک نسخه LTS می‌دهد. دانستن «چه چیزی تازه است» شما را در مصاحبه و تصمیم‌های معماری جلو می‌اندازد — مخصوصاً وقتی ابزار داخلی جای پکیج ثالث را می‌گیرد.',
    objectives=[
        'چرخه انتشار جنگو و معنی LTS را توضیح دهید.',
        'کلید اصلی مرکب (CompositePrimaryKey) را به کار ببرید.',
        'با Background Tasks داخلی ۶.۰ یک تسک ساده تعریف و اجرا کنید.',
        'Template Partials را در قالب‌ها استفاده کنید.',
        'CSP بومی را فعال و یک پروژه را با متد صحیح ارتقا دهید.',
    ],
    s1_position='<strong>جایگاه فصل:</strong> به‌روزرسانی دانش فصل‌های ۱۰ (قالب)، ۲۴ (سلری) و ۱۷ (میدلور/CSP)؛ پایه تصمیم «کدام نسخه برای پروژه من».',
    roadmap=[
        ('چرخه نسخه‌ها', 'LTS و پشتیبانی.'),
        ('۵.۲', 'کلید مرکب، شل هوشمند، فرم/async.'),
        ('۶.۰', 'tasks، partials، CSP، ایمیل.'),
        ('ارتقا', 'متدولوژی مهاجرت نسخه.'),
    ],
    mind_qs=[
        ('LTS یعنی چه و کدام را انتخاب کنیم؟',
         '<p>Long-Term Support: جنگو ۵.۲ (آوریل ۲۰۲۵) تا <strong>آوریل ۲۰۲۸</strong> وصله امنیتی می‌گیرد؛ نسخه‌های ویژگی (مثل ۶.۰، دسامبر ۲۰۲۵) فقط تا نسخه بعدی+. پروژه جدید جدی/سازمانی: LTS. پروژه شخصی/یادگیری: تازه‌ترین نسخه ویژگی هم عالی است.</p>'),
        ('آیا tasks داخلی یعنی سلری مرده است؟',
         '<p>نه! فریم‌ورک tasks جنگو (۶.۰) <strong>تعریف و صف‌کردن</strong> تسک را استاندارد می‌کند و بک‌اندهای ساده می‌دهد؛ برای صف‌های پیچیده (retry پیشرفته، زنجیره‌ها، پایش Flower، صف‌های چندگانه) همچنان سلری قدرتمندتر است. روند: شروع با tasks داخلی، مهاجرت به سلری وقتی نیاز پیچیده شد.</p>'),
        ('چرا ۶.۰ پایتون ۳.۱۲+ می‌خواهد؟',
         '<p>سیاست جنگو: با هر نسخه، حمایت از پایتون‌های EOL قطع می‌شود تا از ویژگی‌های زبان (تایپ‌های بهتر، کارایی) استفاده کند. ۶.۰ از ۳.۱۰/۳.۱۱ خداحافظی کرد و ۳.۱۲-۳.۱۴ را پشتیبانی می‌کند. قبل از ارتقای جنگو، ارتقای پایتون را چک کنید.</p>'),
    ],
    prereq_intro='پیش‌نیازها:',
    prereq=[
        'پروژه وبلاگ (هر نسخه‌ای که دارید — ارتقا بخشی از تمرین است).',
        'پایتون ۳.۱۲+ نصب‌شده (<code class="inline-code">python --version</code>).',
        'فصل ۲۴: درک صف تسک برای مقایسه با tasks داخلی.',
        'فصل ۱۰: قالب‌ها و include برای درک partials.',
    ],
    prereq_callout=('warn', 'نسخه‌های این فصل',
        'محتوا بر پایه جنگو ۵.۲.x (LTS، پشتیبانی تا آوریل ۲۰۲۸) و ۶.۰.x (دسامبر ۲۰۲۵، پشتیبانی تا آوریل ۲۰۲۷) نوشته شده. قبل از هر ارتقا، release notes رسمی همان نسخه را بخوانید.'),
    concepts=[
        dict(h='۵.۱ چرخه انتشار و نقشه راه نسخه‌ها', body=[
            '<div class="table-wrap"><table class="compare"><thead><tr><th>نسخه</th><th>انتشار</th><th>نوع</th><th>پایان پشتیبانی</th></tr></thead><tbody>'
            '<tr><td>4.2</td><td>آوریل ۲۰۲۳</td><td>LTS</td><td>آوریل ۲۰۲۶ (پایان!)</td></tr>'
            '<tr><td>5.0/5.1</td><td>دسامبر ۲۰۲۳/اوت ۲۰۲۴</td><td>ویژگی</td><td>پایان یافته</td></tr>'
            '<tr><td><strong>5.2</strong></td><td>آوریل ۲۰۲۵</td><td><strong>LTS</strong></td><td>آوریل ۲۰۲۸</td></tr>'
            '<tr><td><strong>6.0</strong></td><td>دسامبر ۲۰۲۵</td><td>ویژگی</td><td>آوریل ۲۰۲۷</td></tr>'
            '<tr><td>6.2</td><td>آوریل ۲۰۲۶ (برنامه)</td><td>LTS</td><td>~۲۰۲۹</td></tr>'
            '</tbody></table></div>',
            ('code', 'دیدن نسخه فعلی پروژه', 'bash', '''python -m django --version
pip index versions django           # نسخه‌های موجود
pip install -U "django~=5.2.0"      # ارتقا در محدوده patch'''),
        ]),
        dict(h='۵.۲ جنگو ۵.۲ LTS — ویژگی‌های کلیدی', body=[
            ('code', '۱) کلید اصلی مرکب (CompositePrimaryKey)', 'python', '''from django.db.models import CompositePrimaryKey


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    class Meta:
        pk = CompositePrimaryKey("order", "product")


# item.pk → (order_id, product_id) — بدون فیلد id اضافی!
# مناسب: جداول واسط معنادار، مهاجرت از اسکیمای قدیمی'''),
            ('code', '۲) شل با import خودکار مدل‌ها', 'bash', '''python manage.py shell
>>> Post.objects.count()      # بدون import — مدل‌ها خودکار حاضرند!
>>> User, Comment             # همه اپ‌ها'''),
            ('code', '۳) احراز هویت ناهمگام', 'python', '''# در ویوهای async:
user = await authenticate(request, username="ali", password="...")
await login(request, user)     # نسخه async توابع auth
# و method_decorator برای متدهای کلاس async'''),
            ('code', '۴) ویجت‌های فرم جدید و دسترس‌پذیری', 'python', '''class ProfileForm(forms.Form):
    color = forms.CharField(widget=forms.ColorInput)     # انتخاب رنگ
    phone = forms.CharField(widget=forms.TelInput)       # tel
    q = forms.CharField(widget=forms.SearchInput)        # search
# + attributهای ARIA بهتر در رندر پیش‌فرض فرم‌ها'''),
            '<ul>'
            '<li>سایر: عملیات AlterConstraint در <span class="term" data-term="migration">مهاجرت</span> (تغییر محدودیت بدون حذف/ساخت)، تابع JSONArray، رعایت ترتیب عبارت‌ها در values()/values_list()، CharField.max_length اختیاری در SQLite، تکرار PBKDF2 قوی‌تر.</li></ul>',
        ]),
        dict(h='۵.۳ جنگو ۶.۰ — چهار ستون بزرگ', body=[
            ('code', '۱) Background Tasks داخلی (جایگزین سبک سلری)', 'python', '''# tasks.py
from django.tasks import task


@task
def send_welcome_email(user_id: int):
    from django.contrib.auth import get_user_model
    user = get_user_model().objects.get(pk=user_id)
    user.email_user("خوش آمدید!", "متن...")


# در ویو — صف‌کردن:
from django.tasks import enqueue
enqueue(send_welcome_email, user.pk)

# اجرا با ورکر داخلی (پشتیبان پیش‌فرض: database):
# python manage.py runworker'''),
            ('code', '۲) Template Partials', 'html', '''{# blog/post_list.html #}
{% partialdef post-card %}
  <article class="card">
    <h2>{{ post.title }}</h2>
    <p>{{ post.body|truncatewords:30 }}</p>
  </article>
{% endpartialdef %}

{# استفاده در همان فایل: #}
{% for post in posts %}{% partial post-card %}{% endfor %}

{# از ویو: رندر «فقط» تکه (عالی برای HTMX — فصل ۲۸!) #}
{#   render(request, "blog/post_list.html#post-card") #}'''),
            ('code', '۳) پشتیبانی بومی CSP (امنیت)', 'python', '''# settings.py — با میدلور ContentSecurityPolicyMiddleware
CONTENT_SECURITY_POLICY = {
    "DIRECTIVES": {
        "default-src": ["'self'"],
        "script-src": ["'self'"],
        "img-src": ["'self'", "data:"],
        "style-src": ["'self'", "'unsafe-inline'"],
    },
    "REPORT_ONLY": False,   # اول True بگذارید و فقط گزارش بگیرید!
}
# هدف: حتی اگر XSS رخ دهد، مرورگر اسکریپت مهاجم را اجرا نکند'''),
            ('code', '۴) ایمیل مدرن + AsyncPaginator', 'python', '''# API ایمیل بر پایه email استاندارد پایتون (positional args منسوخ)
# پیام‌ها حالا به‌جای EmailMessage کلاسیک، ساختار مدرن‌تر دارند

# صفحه‌بندی ناهمگام در ویوهای async:
from django.core.paginator import AsyncPaginator
paginator = AsyncPaginator(await sync_to_async(list)(qs), 10)
page = await paginator.apage(request.GET.get("page"))'''),
            '<ul>'
            '<li>سایر ۶.۰: DEFAULT_AUTO_FIELD پیش‌فرض BigAutoField شد، StringAgg روی همه بک‌اندها، AnyValue، متغیر forloop.length در حلقه قالب، تگ querystring همیشه با "?" شروع می‌شود، حمایت از پایتون ۳.۱۲-۳.۱۴ (قطع ۳.۱۰/۳.۱۱ و MariaDB ۱۰.۵).</li></ul>',
        ]),
        dict(h='۵.۴ متدولوژی ارتقای نسخه', body=[
            ('code', 'مسیر امن ارتقا', 'bash', '''# ۰) حمایت: تست‌ها سبز + git tag (فصل ۲۰ سرمایه این لحظه است!)
git tag pre-upgrade && git push --tags

# ۱) نسخه فعلی را patch کنید: 5.1.x → آخرین 5.1
pip install -U "django~=5.1.0" && python manage.py test

# ۲) deprecationها را ببینید و پاک کنید
python -Wd manage.py test 2>&1 | grep -i deprecat

# ۳) ارتقای اصلی (یک پله: 5.1 → 5.2 → 6.0، نه پرش)
pip install -U "django~=5.2.0"
python manage.py test && python manage.py check --deploy

# ۴) مهاجرت‌های جدید را بسازید/اجرا کنید
python manage.py makemigrations --check
python manage.py migrate'''),
            ('callout', 'warn', 'پکیج‌های ثالث را فراموش نکنید',
             'DRF، celery، whitenoise و... هرکدام جدول سازگاری نسخه دارند. قبل از ارتقای جنگو، سازگاری همه پکیج‌های requirements را چک کنید؛ گاهی باید اول پکیج را ارتقا داد. در پروژه جدی: ارتقا را در شاخه جدا و با داده کپی-تولید تمرین کنید.'),
        ]),
        dict(h='۵.۵ چشم‌انداز: async و آینده', body=[
            '<ul>'
            '<li><strong>مسیر async:</strong> از ۳.۰ به بعد <span class="term" data-term="view">ویوها</span>، <span class="term" data-term="orm">ORM</span> (aobjects)، auth (۵.۲) و صفحه‌بندی (۶.۰) ناهمگام شده‌اند. پروژه‌های I/O-محور (پروکسی APIها، realtime) بیشترین سود را می‌برند؛ CRUD معمول هنوز با sync ساده‌تر است.</li>'
            '<li><strong>tasks داخلی:</strong> استاندارد شدن صف تسک = احتمالاً در ۶.۲ LTS پخته‌تر؛ معماری «اول داخلی، بعد سلری» را در نظر بگیرید.</li>'
            '<li><strong>partials + <span class="term" data-term="htmx">HTMX</span>:</strong> ترکیب ۶.۰ و فصل ۲۸ = الگوی رسمی-جامعه‌ای «سرور-رندر تعاملی».</li>'
            '<li><strong>CSP:</strong> با بومی شدنش، انتظار سخت‌گیرانه‌تر شدن پیش‌فرض‌های امنیتی در نسخه‌های بعد.</li></ul>',
            ('callout', 'tip', 'عادت بمانید به‌روز',
             'دنبال کردن: وبلاگ رسمی djangoproject.com، release notes هر نسخه (بخش Backwards incompatible!), و خبرنامه‌های جامعه. برای کار حرفه‌ای «خواندن release notes» مهارت است نه کار اضافه.'),
        ]),
    ],
    example_intro='مهاجرت عملی: پروژه وبلاگ را از سلری-محور به ترکیب «tasks داخلی + partials» مدرن کنیم:',
    example=[
        ('code', 'قبل (فصل ۲۴ — سلری)', 'python', '''# blog/tasks.py
@shared_task(bind=True, max_retries=3)
def send_publish_email(self, post_id, emails):
    ...

# ویو:
send_publish_email.delay(post.pk, emails)'''),
        ('code', 'بعد (۶.۰ — tasks داخلی، ساده‌شده)', 'python', '''from django.tasks import enqueue, task


@task(queue="mail")
def send_publish_email(post_id: int, emails: list[str]):
    from .models import Post
    post = Post.objects.get(pk=post_id)
    send_mail(f"پست جدید: {post.title}", post.body[:500],
              None, emails[:50])


# ویو — همان یک خط:
transaction.on_commit(
    lambda: enqueue(send_publish_email, post.pk, emails))

# اجرای ورکر: python manage.py runworker --queue mail
# (retry/صف‌های پیچیده لازم شد؟ همان کد را به سلری برگردانید)'''),
        ('code', 'partials برای HTMX (ترکیب ۶.۰ + فصل ۲۸)', 'python', '''# ویوی تکه‌ای بدون فایل partials/ جدا:
def like(request, pk):
    post = ...
    if request.headers.get("HX-Request"):
        return render(request, "blog/post_detail.html#like-box")
        #                                            ↑ فقط تکه!'''),
        ('code', 'قالب با partialdef', 'html', '''{# blog/post_detail.html #}
{% partialdef like-box %}
<button hx-post="{% url 'blog:like' post.pk %}" hx-target="closest button"
        hx-swap="outerHTML">❤ {{ post.likes_count }}</button>
{% endpartialdef %}

{% block content %}
  <h1>{{ post.title }}</h1>
  {% partial like-box %}
{% endblock %}'''),
        '<p>نتیجه: یک فایل قالب کمتر، یک سرویس کمتر (Redis فقط برای سلری دیگر لازم نیست اگر tasks دیتابیسی کافی باشد)، و همان قابلیت‌ها. سادگی، خودش یک ویژگی است.</p>',
    ],
    workshop_intro='پروژه را به‌روز و مدرن کنید:',
    workshop_tasks=[
        '<strong>کارگاه ۱:</strong> وضعیت نسخه پروژه را گزارش کنید: <code class="inline-code">python -m django --version</code>، فهرست deprecationها با -Wd، و برنامه ارتقای پله‌ای تا ۵.۲ (یا ۶.۰ با پایتون ۳.۱۲+).',
        '<strong>کارگاه ۲:</strong> یک جدول با CompositePrimaryKey بسازید (مثلاً «امتیاز کاربر به پست»: کلید = user+post) و CRUD کوچکش را در ادمین/ویو تست کنید.',
        '<strong>کارگاه ۳ (اگر روی ۶.۰ هستید):</strong> یک تسک با @task داخلی بنویسید (مثل welcome email)، با enqueue صف و با runworker اجرا کنید؛ سپس همان را با template partial برای HTMX تکمیل کنید.',
    ],
    workshop_answers=[
        ('پاسخ کارگاه ۱',
         '<div class="code-box"><div class="code-head"><span>گزارش ارتقا</span><span class="lang">bash</span></div><pre class="code"><code data-lang="bash">python -m django --version\n# مثال: 4.2.11\n\npip install -U "django~=4.2.0"     # آخرین patch همین شاخه\npython -Wd manage.py test 2>&amp;1 | grep -i deprecat\n# خروجی نمونه: RemovedInDjango51Warning: ...\n\n# پله‌ها: 4.2 → 5.0 → 5.1 → 5.2 (LTS) [→ 6.0 اختیاری]\n# در هر پله: pip install -U، test، migrate، رفع deprecation\n# پکیج‌ها: pip list --outdated + جدول سازگاری DRF/celery</code></pre></div>'
         '<p>نکته مهم: اگر پروژه روی ۴.۲ است، پشتیبانی‌اش <strong>آوریل ۲۰۲۶ تمام شده</strong> — ارتقا دیگر «اختیاری» نیست، امنیت است. گزارش را در docs/upgrade.md با تاریخ هر پله ثبت کنید.</p>'),
        ('پاسخ کارگاه ۲',
         '<div class="code-box"><div class="code-head"><span>کلید مرکب</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">from django.db import models\n\n\nclass PostRating(models.Model):\n    user = models.ForeignKey(settings.AUTH_USER_MODEL,\n                             on_delete=models.CASCADE)\n    post = models.ForeignKey(Post, on_delete=models.CASCADE)\n    score = models.PositiveSmallIntegerField()   # 1..5\n    updated_at = models.DateTimeField(auto_now=True)\n\n    class Meta:\n        pk = models.CompositePrimaryKey("user", "post")\n\n\n# استفاده:\nr, _ = PostRating.objects.update_or_create(\n    user=request.user, post=post, defaults={"score": 4})\nr.pk                    # (3, 17) — تاپل!\nPostRating.objects.filter(pk=(3, 17))\n\n# ادمین: ثبت معمولی؛ فقط pk ادمین‌پسند نیست —\n# برای URLهای ادمین بهتر است id ساده نگه دارید یا views دستی بنویسید.</code></pre></div>'
         '<p>توجه: با <span class="term" data-term="primary-key">کلید مرکب</span>، r.pk دیگر عدد نیست — کدهایی که pk را در <span class="term" data-term="url">URL</span>/<span class="term" data-term="cache">کش</span>/<span class="term" data-term="json">JSON</span> فرض عددی دارند را بررسی کنید. برای همین بیشتر پروژه‌ها id یکتا + unique_together/UniqueConstraint را ترجیح می‌دهند؛ CompositePrimaryKey برای وفاداری به اسکیمای موجود عالی است.</p>'),
        ('پاسخ کارگاه ۳',
         '<div class="code-box"><div class="code-head"><span>tasks داخلی + partial</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python"># accounts/tasks.py (جنگو 6.0+)\nfrom django.tasks import task\n\n\n@task\ndef send_welcome_email(user_id: int):\n    from django.contrib.auth import get_user_model\n    u = get_user_model().objects.get(pk=user_id)\n    u.email_user("خوش آمدید 👋", "ممنون از ثبت‌نام!")\n\n\n# در ویوی ثبت‌نام، بعد از ایجاد کاربر:\nfrom django.tasks import enqueue\nfrom django.db import transaction\ntransaction.on_commit(lambda: enqueue(send_welcome_email, user.pk))\n\n# اجرا:\n# ترمینال ۱: python manage.py runworker\n# ترمینال ۲: python manage.py runserver\n# ثبت‌نام کنید → در لاگ runworker اجرای تسک را ببینید\n# (EMAIL_BACKEND=console ایمیل را در ترمینال نشان می‌دهد)</code></pre></div>'
         '<p>مقایسه با سلری: بدون Redis، بدون پروسه جداگانه celery — پشتیبان database داخلی است. محدودیت‌ها: retry/زمان‌بندی دوره‌ای/صف‌های پیشرفته به پختگی سلری نیست؛ برای «ایمیل خوش‌آمد و کارهای سبک» کاملاً کافی. partial را هم طبق مثال فصل برای like-box اضافه کنید و render("...#like-box") را تست کنید.</p>'),
    ],
    errors=[
        ('بعد از ارتقا: ImportError یا «no module named ...»',
         'پکیج ثالث با نسخه جدید جنگو ناسازگار است (معمولاً DRF/celery/... پیام واضح می‌دهد). جدول سازگاری پکیج را چک و اول پکیج را ارتقا دهید. به همین دلیل «یک پله در هر بار».'),
        ('هشدارهای RemovedInDjangoXXWarning انباشته',
         'از نسخه‌ها قبل پشت گوش انداخته‌اید. همه را با -Wd لیست و طبق پیام هر هشدار (معمولاً جایگزین مشخص دارد) اصلاح کنید؛ بعد ارتقای اصلی. هشدار امروز = شکست فردا.'),
        ('runworker تسک‌ها را اجرا نمی‌کند (۶.۰)',
         'backend تسک‌ها پیکربندی نشده (پیش‌فرض database باید migrate شده باشد: python manage.py migrate برای جدول تسک‌ها) یا صف اشتباه است (runworker --queue mail اگر task(queue="mail")). لاگ ورکر را با -v 2 ببینید.'),
        ('CSP سایت را «خالی/شکسته» کرد',
         'دیگرکتیو خیلی سخت‌گیرانه است (مثلاً script-src بدون CDNهای استفاده‌شده). کنسول مرورگر دقیقاً می‌گوید کدام منبع نقض شد؛ آن origin را به فهرست اضافه کنید. همیشه اول REPORT_ONLY=True برای دیدن نقض‌ها بدون شکستن.'),
        ('DEFAULT_AUTO_FIELD و هشدارهای مهاجرت بعد از ۶.۰',
         'پیش‌فرض BigAutoField شد؛ پروژه‌های قدیمی ممکن است AutoField داشته باشند و makemigrations مهاجرت تبدیل id بسازد. <strong>کورکورانه migrate نکنید</strong> — تبدیل PK روی جدول بزرگ سنگین است؛ یا تنظیم صریح را نگه دارید یا با برنامه (قفل‌گیری/ downtime) انجام دهید.'),
    ],
    errors_callout=('tip', 'کانال اطلاع از شکستن‌ها',
        'بخش «Backwards incompatible changes» هر release notes + ایمیل‌های django-announce. قبل از ارتقای تولید، فقط همان بخش را هم بخوانید کافی است — معمولاً ۵ مورد است.'),
    exercises=[
        ('تمرین ۱ — انتخاب نسخه',
         '<p><strong>سوال:</strong> برای هر سناریو کدام نسخه (امروز: شهریور ۱۴۰۵/سپتامبر ۲۰۲۶)؟ (الف) پروژه سازمانی جدید با ۵ سال عمر (ب) استارت‌آپ با نیاز به tasks داخلی و partials (ج) نگهداری پروژه موجود روی ۴.۲</p>'
         '<p><strong>پاسخ:</strong> الف → ۵.۲ LTS (پشتیبانی تا آوریل ۲۰۲۸؛ بعد مهاجرت برنامه‌ریزی‌شده به ۶.۲ LTS) • ب → ۶.۰ (با آگاهی که تا آوریل ۲۰۲۷ پشتیبانی می‌شود و باید به ۶.۲ برود) • ج → <strong>فوری</strong> ارتقا از ۴.۲ (پشتیبانی تمام شده!) به ۵.۲ با متد پله‌ای فصل.</p>'),
        ('تمرین ۲ — tasks داخلی یا سلری؟',
         '<p><strong>سوال:</strong> برای هر نیاز کدام؟ (الف) ایمیل خوش‌آمد بعد از ثبت‌نام (ب) ۱۰ نوع تسک با retry، اولویت، سه صف جدا و Flower (ج) گزارش شبانه با زمان‌بندی پیچیده</p>'
         '<p><strong>پاسخ:</strong> الف → tasks داخلی (ساده، بدون Redis) • ب → سلری (زیرساخت صف بالغ) • ج → سلری+beat یا django-celery-beat. مرز: «یک صف، تسک‌های سبک، تیم کوچک → داخلی؛ پیچیدگی صف/پایش → سلری».</p>'),
        ('تمرین ۳ — خواندن release note',
         '<p><strong>سوال:</strong> در notes جنگو ۶.۰ کدام بند برای پروژه‌ای که روی پایتون ۳.۱۰ است حیاتی است؟ و کدام برای پروژه‌ای که DEFAULT_AUTO_FIELD صریح ندارد؟</p>'
         '<p><strong>پاسخ:</strong> «Dropped support for Python &lt; 3.12» → اول باید پایتون را ارتقا داد (وگرنه اصلاً نصب نمی‌شود/تست نشده است). «DEFAULT_AUTO_FIELD now defaults to BigAutoField» → ممکن است مهاجرت‌های تبدیل کلید ساخته شود؛ قبل از migrate بررسی (خطای رایج بخش ۵). مهارت: اسکن بخش Backwards incompatible قبل از هر ارتقا.</p>'),
    ],
    quiz=[
        dict(q='نسخه LTS جنگو چه مزیتی دارد؟',
             opts=['ویژگی‌های بیشتر', 'پشتیبانی امنیتی طولانی‌تر (~۳ سال) — مناسب پروژه‌های با عمر بلند',
                   'سریع‌تر است', 'بدون مهاجرت'],
             ans='b', explain='۵.۲ تا آوریل ۲۰۲۸ وصله امنیتی می‌گیرد؛ نسخه‌های ویژگی زودتر EOL می‌شوند. سازمان‌ها معمولاً LTS-به-LTS می‌روند.'),
        dict(q='CompositePrimaryKey در ۵.۲ چه چیزی را ممکن کرد؟',
             opts=['کلید خارجی مرکب در فرم', 'کلید اصلی چندستونی (مثل order+product) بدون فیلد id جایگزین',
                   'ایندکس مرکب', 'پارتیشن‌بندی جدول'],
             ans='b', explain='Meta.pk = CompositePrimaryKey("order", "product") — pk تبدیل به تاپل می‌شود؛ مناسب وفاداری به اسکیمای موجود.'),
        dict(q='tasks داخلی جنگو ۶.۰ با کدام دکوریتور و دستور تعریف/اجرا می‌شود؟',
             opts=['@shared_task و celery worker', '@task و python manage.py runworker',
                   '@task و runserver', '@job و worker start'],
             ans='b', explain='from django.tasks import task/enqueue؛ ورکر داخلی با runworker و پشتیبان پیش‌فرض دیتابیسی — صف سبک بدون سرویس اضافه.'),
        dict(q='{% partialdef %} چه مشکلی را حل می‌کند؟',
             opts=['سرعت قالب', 'تعریف و استفاده تکه‌های نام‌دار داخل همان فایل قالب + رندر مستقیم تکه با name#partial',
                   'ترجمه قالب', 'کش قالب'],
             ans='b', explain='جایگزین فایل‌های include پراکنده؛ برای ویوهای HTMX عالی است: render(request, "post_list.html#post-card").'),
        dict(q='CONTENT_SECURITY_POLICY چه خطری را کاهش می‌دهد؟',
             opts=['SQL injection', 'اجرای اسکریپت/منبع غیرمجاز در مرورگر — لایه دفاعی حتی در صورت وقوع XSS',
                   'CSRF', 'کندی سایت'],
             ans='b', explain='CSP به مرورگر می‌گوید کدام originها برای script/style/img مجازند؛ حمله تزریق حتی موفق هم نتواند اسکریپت خارجی لود کند. اول REPORT_ONLY.'),
        dict(q='ترتیب درست ارتقای نسخه کدام است؟',
             opts=['پرش مستقیم به آخرین نسخه', 'تست سبز → آخرین patch نسخه فعلی → رفع deprecationها → پله‌به‌پله ارتقای اصلی + تست در هر پله',
                   'اول پکیج‌ها بعد تست', 'فقط pip install -U django'],
             ans='b', explain='پله‌به‌پله با تست در هر مرحله و چک سازگاری پکیج‌های ثالث؛ پرش = انباشت شکستگی‌های نامشخص.'),
    ],
    project_title='پروژه به‌روز و مدرن',
    project_intro='دانش این فصل را روی همان پروژه وبلاگ پیاده کنید.',
    project_checklist=[
        'ارتقا به ۵.۲ LTS (یا ۶.۰ با پایتون ۳.۱۲+) با متد پله‌ای + تست‌های سبز.',
        'صفر هشدار deprecation در خروجی python -Wd manage.py test.',
        'یک جدول با کلید مرکب (PostRating) یا یک تسک @task داخلی در حال کار.',
        'یک partialdef در قالب اصلی + رندر «تکه» از یک ویو (HX-Request).',
        'گزارش docs/upgrade.md: نسخه‌های قبل/بعد، تغییرات، مشکلات و راه‌حل‌ها.',
    ],
    project_callout=('info', 'تمرین حرفه‌ای',
        'در تیم‌های واقعی، «ارتقای فریم‌ورک» خودش یک پروژه کوچک با برآورد و ریسک است. همین گزارش ساده، نمونه کار عالی برای مصاحبه است.'),
    summary_items=[
        'چرخه: نسخه ویژگی هر ~۸ ماه، LTS هر ~۲.۵ سال؛ ۵.۲ تا آوریل ۲۰۲۸.',
        '۵.۲: کلید مرکب، شل با import خودکار، auth ناهمگام، ویجت‌های جدید.',
        '۶.۰: tasks داخلی (task/enqueue/runworker)، partials، CSP بومی، ایمیل مدرن، AsyncPaginator.',
        'DEFAULT_AUTO_FIELD=BigAutoField پیش‌فرض شد؛ پایتون ۳.۱۲+ لازم است.',
        'ارتقا: پله‌به‌پله، تست در هر پله، رفع deprecation، چک پکیج‌های ثالث.',
    ],
    golden='به‌روز ماندن ارزان است اگر پیوسته باشد؛ انباشته‌شدن ارتقاها گران‌ترین بدهی فنی است.',
    faq=[
        ('پروژه موجود را به ۶.۰ ببرم یا صبر کنم؟',
         '<p>سازمانی: روی ۵.۲ LTS بمانید و برای ۶.۲ LTS (آوریل ۲۰۲۶ — الان منتشر شده) برنامه‌ریزی کنید. شخصی/یادگیری: ۶.۰ را تجربه کنید — tasks و partials ارزشش را دارند. هر دو مسیر «روی ۴.۲ ماندن» غلط است (پشتیبانی تمام شده).</p>'),
        ('tasks داخلی جایگزین Flower/مانیتورینگ می‌شود؟',
         '<p>فعلاً اکوسیستم پایش سلری (Flower، Sentry integration) بالغ‌تر است. tasks داخلی در ۶.۰ نقطه شروع است؛ برای تولید جدی با صف‌های حیاتی، فعلاً سلری ابزارهای عملیاتی بیشتری دارد.</p>'),
        ('async ویوها را در پروژه فعلی فعال کنیم؟',
         '<p>اگر گلوگاه I/O خارجی دارید (صدا زدن چند <span class="term" data-term="api">API</span> بیرونی در یک درخواست) بله — async واقعی سود دارد. برای <span class="term" data-term="crud">CRUD</span> دیتابیسی معمول، ORM sync همچنان ساده‌تر و کافی است؛ async بدون دلیل = پیچیدگی (sync_to_async همه‌جا). اول اندازه‌گیری (فصل ۲۷).</p>'),
    ],
    next_step='همه‌چیز آماده است؛ وقت ساختن شاهکار: <strong>فصل ۳۰</strong> — سه پروژه کامل عملی که تمام ۲۹ فصل را به هم می‌بافند.',
),

# ================================================================ فصل ۳۰
dict(
    n=30, icon='🏆', title='پروژه‌های عملی نهایی', cat=5, mins=120, lvl_label='پیشرفته',
    hero_desc='سه پروژه کامل که همه دوره را به کار می‌گیرند: <strong>پلتفرم وبلاگ‌نویسی چند نویسنده</strong>، <strong>فروشگاه اینترنتی</strong> و <strong>سامانه مدیریت وظایف تیمی</strong> — با نقشه راه مرحله‌به‌مرحله و چک‌لیست کیفیت.',
    s1_intro='تفاوت «دوره دیدم» و «جنگو بلدم» یک پروژه کامل است. اینجا سه نقشه راه واقعی دارید؛ هرکدام را که ساختید، ۳۰ فصل دوره را با دست خودتان لمس کرده‌اید. این فصل کد جدید نمی‌دهد — <strong>مسیر ساخت</strong> می‌دهد.',
    objectives=[
        'یکی از سه پروژه را انتخاب و معماری‌اش را طراحی کنید.',
        'نقشه راه ۷ مرحله‌ای را با ارجاع به فصل‌های دوره اجرا کنید.',
        'چک‌لیست کیفیت (تست، امنیت، کارایی، استقرار) را روی پروژه ببندید.',
        'پروژه را در GitHub با README حرفه‌ای منتشر کنید.',
        'مسیر یادگیری بعد از دوره را بدانید.',
    ],
    s1_position='<strong>جایگاه فصل:</strong> پایانی و جمع‌بندی؛ هر مرحله به فصل‌های مشخص ارجاع می‌دهد تا «یادگیری چرخه‌ای» انجام شود.',
    roadmap=[
        ('انتخاب و طراحی', 'سه پروژه و معماری اولیه.'),
        ('نقشه راه ۷ مرحله', 'از مدل تا دیپلوی.'),
        ('چک‌لیست کیفیت', 'تست، امنیت، کارایی.'),
        ('انتشار و بعد از آن', 'GitHub و مسیر ادامه.'),
    ],
    mind_qs=[
        ('کدام پروژه را انتخاب کنم؟',
         '<p>هر سه مهارت‌های هم‌پوشان دارند. راهنما: <strong>وبلاگ چندنویسنده</strong> = نزدیک‌ترین به چیزی که در دوره ساختید (کمترین اصطکاک شروع). <strong>فروشگاه</strong> = پول/سفارش/پرداخت (بازار کار فراوان). <strong>مدیریت وظایف</strong> = مجوزهای پیچیده و HTMX (نمایش مهارت مدرن). برای رزومه اول: فروشگاه یا وظایف جذاب‌ترند.</p>'),
        ('چقدر زمان می‌برد؟',
         '<p>با روزی ۲-۳ ساعت: مرحله داده/مدل ~۱ هفته، ویوها و قالب‌ها ~۲ هفته، ویژگی‌های پیشرفته (API/تسک/کش) ~۲ هفته، تست و دیپلوی ~۱ هفته. جمعاً ۵-۷ هفته برای نسخه قابل انتشار (MVP). کمال‌گرایی = پروژه نیمه‌تمام؛ اول MVP، بعد ویژگی.</p>'),
        ('از کجا بدانم «آماده انتشار» است؟',
         '<p>چک‌لیست کیفیت ۵.۴ را ببندید: تست‌های سبز روی مسیرهای اصلی، DEBUG=False و secrets در env، HTTPS، پشتیبان‌گیری، لاگ خطاها. اگر این‌ها هست، منتشر کنید — حتی با ظاهر ساده. پروژه زنده با نقص، از پروژه کاملِ لوکال ارزش بیشتری دارد.</p>'),
    ],
    prereq_intro='پیش‌نیازها:',
    prereq=[
        'گذراندن (یا مرور موردی) فصل‌های ۱ تا ۲۹.',
        'گیت و GitHub (ساخت ریپازیتوری، commit منظم، README).',
        'یک VPS یا پلتفرم PaaS برای دیپلوی نهایی (فصل ۲۶).',
        'زمان بلوکی هفته‌ای — پروژه ماراتن است نه اسپرینت.',
    ],
    prereq_callout=('tip', 'قانون شروع',
        'امروز فقط یک کار: انتخاب پروژه + کشیدن مدل‌هایش روی کاغذ (ERD ساده). کد از فردا. طراحی ۲ ساعته، ۲۰ ساعت بازنویسی را نجات می‌دهد.'),
    concepts=[
        dict(h='۵.۱ پروژه الف — پلتفرم وبلاگ‌نویسی چندنویسنده (مثل ویرگول)', body=[
            '<p><strong>شرح:</strong> هرکس ثبت‌نام کند، وبلاگ خودش را دارد؛ دنبال‌کردن نویسندگان، خوراک شخصی، نظرات و ادمین محتوا.</p>',
            '<div class="table-wrap"><table class="compare"><thead><tr><th>ویژگی</th><th>ارجاع به فصل</th></tr></thead><tbody>'
            '<tr><td>ثبت‌نام/ورود/پروفایل + بیو</td><td>۱۲ (احراز هویت)، ۱۱ (فرم‌ها)</td></tr>'
            '<tr><td>مدل‌ها: User→Blog→Post→Comment، Follow (m2m با through)</td><td>۴-۶ (مدل)، ۱۶ (سیگنال پروفایل)</td></tr>'
            '<tr><td>ویرایشگر مارک‌داون + آپلود کاور</td><td>۱۱، ۱۴ (رسانه)</td></tr>'
            '<tr><td>صفحه نویسنده author.example/ali (زیردامنه یا /@ali)</td><td>۷ (URL)، ۸-۹ (ویوها)</td></tr>'
            '<tr><td>خوراک دنبال‌شده‌ها با صفحه‌بندی</td><td>۱۵ (QuerySet)، ۲۷ (ایندکس)</td></tr>'
            '<tr><td>اعلان ایمیل انتشار به دنبال‌کنندگان</td><td>۱۶ (سیگنال) + ۲۴ (سلری)</td></tr>'
            '<tr><td>جست‌وجو، برچسب، پربازدیدها</td><td>۱۵ (Q/aggregate)، ۱۹ (کش)</td></tr>'
            '<tr><td>API عمومی برای اپ موبایل فرضی</td><td>۲۲-۲۳ (DRF)</td></tr>'
            '<tr><td>لایک بدون رفرش + اسکرول بی‌نهایت</td><td>۲۸ (HTMX)</td></tr>'
            '<tr><td>ادمین محتوا: تأیید/رد پست گزارش‌شده</td><td>۶، ۱۳ (مجوزها)</td></tr>'
            '</tbody></table></div>',
        ]),
        dict(h='۵.۲ پروژه ب — فروشگاه اینترنتی', body=[
            '<p><strong>شرح:</strong> کاتالوگ محصول، سبد خرید (مهمان+کاربر)، فرآیند سفارش، پنل فروشنده و داشبورد آمار.</p>',
            '<div class="table-wrap"><table class="compare"><thead><tr><th>ویژگی</th><th>ارجاع به فصل</th></tr></thead><tbody>'
            '<tr><td>مدل‌ها: Category→Product→Variant، Order→OrderItem</td><td>۴-۶، کلید مرکب OrderItem (۲۹)</td></tr>'
            '<tr><td>سبد مهمان با نشست + ادغام هنگام ورود</td><td>۱۸ (session/cart کامل!)</td></tr>'
            '<tr><td>فیلتر قیمت/دسته/موجودی + مرتب‌سازی</td><td>۱۵، ۲۳ (فیلتر API)</td></tr>'
            '<tr><td>فرآیند checkout چندمرحله‌ای (آدرس→ارسال→پرداخت)</td><td>۱۱ (فرم/wizard)، ۱۸</td></tr>'
            '<tr><td>شبیه‌ساز پرداخت + تغییر وضعیت سفارش با سیگنال order_paid</td><td>۱۶ (سیگنال سفارشی)</td></tr>'
            '<tr><td>کاهش موجودی اتمی با F() و جلوگیری از فروش بیش از موجودی</td><td>۱۵ (F/atomic) — با تست رقابت!</td></tr>'
            '<tr><td>ایمیل فاکتور PDF (تسک پس‌زمینه)</td><td>۲۴ یا tasks داخلی (۲۹)</td></tr>'
            '<tr><td>پنل فروشنده: محصولات/سفارش‌های خودش (مجوز شیء‌محور)</td><td>۱۳ (گروه/مجوز)، ۹ (میکسین)</td></tr>'
            '<tr><td>داشبورد آمار فروش با نمودار (Chart.js)</td><td>۱۵ (annotate/روزانه)، ۱۹ (کش آمار)</td></tr>'
            '<tr><td>API + جست‌وجوی محصولات</td><td>۲۲-۲۳</td></tr>'
            '</tbody></table></div>',
            ('callout', 'warn', 'پول = وسواس امنیت',
             'قیمت فقط سمت سرور محاسبه شود (هرگز از فرم/نشست خوانده نشود!)، تغییرات موجودی در atomic + select_for_update، همه تراکنش‌های مالی با تست (فصل ۲۰) و لاگ (۲۱). حتی در پروژه تمرینی، درگاه را «شبیه‌سازی» ولی منطق را واقعی بنویسید.'),
        ]),
        dict(h='۵.۳ پروژه پ — سامانه مدیریت وظایف تیمی (مثل Trello کوچک)', body=[
            '<p><strong>شرح:</strong> فضای کاری، برد وظایف با ستون‌ها، اختصاص، برچسب، مهلت، کامنت و فعالیت.</p>',
            '<div class="table-wrap"><table class="compare"><thead><tr><th>ویژگی</th><th>ارجاع به فصل</th></tr></thead><tbody>'
            '<tr><td>Workspace→Board→Column→Card با عضویت و نقش</td><td>۴-۶، ۱۳ (مجوز سفارشی نقش‌محور)</td></tr>'
            '<tr><td>درگ‌اند‌دراپ کارت بین ستون‌ها (HTMX یا SortableJS)</td><td>۲۸، PATCH موقعیت با API (۲۳)</td></tr>'
            '<tr><td>اختصاص چندکاربره + اعلان سررسید (تسک دوره‌ای)</td><td>۲۴ (beat روزانه)</td></tr>'
            '<tr><td>تاریخچه فعالیت هر کارت (audit log)</td><td>۱۶ (سیگنال‌ها، مثال فصل!)</td></tr>'
            '<tr><td>جست‌وجوی سراسری + فیلتر برچسب/مسئول</td><td>۱۵ (Q)، ۲۳ (filterset)</td></tr>'
            '<tr><td>صفحه «کارهای من» در همه بردها</td><td>۱۵ (کوئری‌های ترکیبی)</td></tr>'
            '<tr><td>دعوت عضو با ایمیل + توکن یک‌بارمصرف</td><td>۱۲، ۲۴ (ایمیل ناهمگام)</td></tr>'
            '<tr><td>API کامل + Swagger برای مصرف SPA</td><td>۲۲-۲۳</td></tr>'
            '</tbody></table></div>',
            ('callout', 'info', 'چرا این پروژه «نمایش مهارت» است؟',
             'مجوزهای نقش‌محور پیچیده (مالک/عضو/بیننده)، به‌روزرسانی موقعیت با رقابت هم‌زمان، و UI تعاملی — هر سه در مصاحبه‌ها سوال‌خیزند و داستان تعریف‌کردنی دارید.'),
        ]),
        dict(h='۵.۴ نقشه راه ۷ مرحله‌ای + چک‌لیست کیفیت', body=[
            '<ol>'
            '<li><strong>طراحی (۲-۳ روز):</strong> ERD <span class="term" data-term="model">مدل‌ها</span>، فهرست صفحات، sketch رابط. ابزار: کاغذ/draw.io. خروجی: فایل docs/design.md در ریپو.</li>'
            '<li><strong>اسکلت (۲ روز):</strong> startproject/startapp، تنظیمات <span class="term" data-term="env-var">env</span>-محور (فصل ۲۶ از روز اول!)، مدل‌ها + makemigrations + <span class="term" data-term="admin">ادمین</span> ثبت‌شده (فصل ۶).</li>'
            '<li><strong>هسته (۱-۲ هفته):</strong> <span class="term" data-term="authentication">احراز هویت</span> (۱۲)، ویوهای اصلی <span class="term" data-term="cbv">CBV</span> (۹)، <span class="term" data-term="template">قالب</span> base+صفحات (۱۰)، <span class="term" data-term="form">فرم‌ها</span> (۱۱).</li>'
            '<li><strong>ویژگی‌های تمایز (۱-۲ هفته):</strong> بسته به پروژه: سبد/درگ‌اند‌دراپ/خوراک — با <span class="term" data-term="htmx">HTMX</span> یا <span class="term" data-term="api">API</span> (۲۲-۲۳، ۲۸).</li>'
            '<li><strong>عمق (۱ هفته):</strong> <span class="term" data-term="signal">سیگنال‌ها</span> و تسک‌ها (۱۶، ۲۴)، <span class="term" data-term="cache">کش</span> (۱۹)، بهینه‌سازی کوئری‌ها (۱۵، ۲۷).</li>'
            '<li><strong>کیفیت (۱ هفته):</strong> <span class="term" data-term="test">تست</span> مسیرهای اصلی (۲۰)، <span class="term" data-term="logging">لاگ</span> (۲۱)، صفحات خطا، مرور امنیتی.</li>'
            '<li><strong>انتشار (۲-۳ روز):</strong> <span class="term" data-term="deployment">دیپلوی</span> (۲۶)، دامنه/<span class="term" data-term="https">HTTPS</span>، README + دمو، تگ v1.0.</li></ol>',
            ('code', 'چک‌لیست کیفیت نهایی (قبل از «تمام شد» گفتن)', 'text', '''□ python manage.py test → همه سبز (≥۳۰ تست مسیر اصلی)
□ python manage.py check --deploy → بدون هشدار قرمز
□ DEBUG=False، secrets در env، ALLOWED_HOSTS دقیق
□ HTTPS فعال + کوکی‌های Secure + HSTS
□ collectstatic شده و استاتیک‌ها سرو می‌شوند
□ لاگ خطاها می‌نویسد (فایل یا Sentry) و ۵۰۰ سفارشی دارید
□ پشتیبان‌گیری دیتابیس + media زمان‌بندی شده
□ صفحات اصلی ≤۵ کوئری و p95 ≤۳۰۰ms (Toolbar روی داده حجیم)
□ README: توضیح، اسکرین‌شات، نصب محلی، لینک دمو
□ git log منظم با پیام‌های معنادار؛ بدون secret در تاریخچه!'''),
        ]),
        dict(h='۵.۵ انتشار و مسیر بعد از دوره', body=[
            ('code', 'README حرفه‌ای — ساختار پیشنهادی', 'text', '''# 🛍 نام پروژه
یک فروشگاه اینترنتی با Django 5.2 + HTMX + PostgreSQL

## ✨ ویژگی‌ها        (۵-۸ بولت، نه بیشتر)
## 📸 اسکرین‌شات/دمو   (لینک سایت زنده!)
## 🚀 نصب محلی        (docker compose up — در سه خط)
## 🧪 تست‌ها           (python manage.py test)
## 🏗 معماری           (یک پاراگراف + ERD)
## 📝 لایسنس'''),
            '<ul>'
            '<li><strong>بعد از انتشار:</strong> پروژه را در لینکدین/ویرگول با «داستان چالش‌ها» معرفی کنید (نه فقط لینک) — مثلاً «چطور race condition موجودی را با select_for_update حل کردم».</li>'
            '<li><strong>مسیر یادگیری ادامه:</strong> ① Channels/WebSocket (چت/اعلان زنده) ② عمق‌شدن DRF (پیاده‌سازی واقعی پرداخت) ③ تست پیشرفته (factory_boy، pytest) ④ DevOps (CI/CD با GitHub Actions، مانیتورینگ) ⑤ مطالعهٔ کدِ منبع پروژه‌های باز مثل Saleor (فروشگاه جنگویی بزرگ).</li></ul>',
            ('callout', 'tip', 'پروژه دوم سریع‌تر می‌آید',
             'اولین پروژه ۶ هفته، دومی ۳ هفته — چون الگوها (auth، CRUD، دیپلوی) تکراری‌اند. همین «سرعت دومین پروژه» نشانه یادگیری واقعی است.'),
        ]),
    ],
    example_intro='یک «برش عمودی» از پروژه فروشگاه — مرحله ۳ نقشه راه با کد واقعی:',
    example=[
        ('code', 'مدل‌های سفارش (مرحله ۲)', 'python', '''class Order(models.Model):
    STATUS = [("pending", "در انتظار"), ("paid", "پرداخت‌شده"),
              ("shipped", "ارسال‌شده"), ("done", "تکمیل"),
              ("canceled", "لغو")]
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.PROTECT)
    status = models.CharField(max_length=10, choices=STATUS,
                              default="pending")
    total_price = models.PositiveBigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["user", "-created_at"]),
            models.Index(fields=["status"]),
        ]


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              related_name="items")
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    price_at_purchase = models.PositiveBigIntegerField()  # قیمت لحظه خرید!
    qty = models.PositiveSmallIntegerField()

    class Meta:
        pk = models.CompositePrimaryKey("order", "product")  # درس فصل ۲۹'''),
        ('code', 'checkout اتمی (مرحله ۴ — با درس‌های ۱۵ و ۱۸)', 'python', '''@login_required
@transaction.atomic
def checkout(request):
    cart = Cart(request)
    if not len(cart):
        return redirect("shop:cart")
    order = Order.objects.create(user=request.user)
    for item in cart:
        p = Product.objects.select_for_update().get(pk=item["product"].pk)
        if p.stock < item["qty"]:
            raise ConflictError(f"موجودی «{p.name}» کافی نیست")
        Product.objects.filter(pk=p.pk).update(
            stock=F("stock") - item["qty"])          # اتمی
        OrderItem.objects.create(
            order=order, product=p,
            price_at_purchase=p.price, qty=item["qty"])
    order.total_price = sum(
        i.price_at_purchase * i.qty for i in order.items.all())
    order.save()
    request.session.pop("cart", None)
    return redirect("shop:pay", pk=order.pk)'''),
        ('code', 'تست رقابت موجودی (مرحله ۶ — درس فصل ۲۰)', 'python', '''def test_oversell_prevented(self):
    p = Product.objects.create(name="آخرین", price=1000, stock=1)
    # دو سفارش هم‌زمان روی آخرین موجودی
    with transaction.atomic():
        pass  # در تست واقعی: دو Thread با select_for_update
    self.assertEqual(Product.objects.get(pk=p.pk).stock, 1)'''),
        ('code', 'سیگنال پرداخت → تسک ایمیل (مرحله ۵ — درس ۱۶+۲۴)', 'python', '''order_paid = django.dispatch.Signal()


@receiver(order_paid)
def on_paid(sender, order, **kwargs):
    transaction.on_commit(
        lambda: send_invoice_email.delay(order.pk))'''),
    ],
    workshop_intro='این فصل خودش کارگاه است — پروژه را بسازید:',
    workshop_tasks=[
        '<strong>گام ۱ (امروز):</strong> یکی از سه پروژه را انتخاب کنید؛ ERD مدل‌ها را بکشید و فهرست صفحات را بنویسید (docs/design.md).',
        '<strong>گام ۲ (هفته اول):</strong> اسکلت را بالا بیاورید: settings با env (فصل ۲۶)، مدل‌ها + ادمین (فصل ۶)، صفحه اصلی با قالب base (فصل ۱۰).',
        '<strong>گام ۳ (هفته‌های بعد):</strong> نقشه راه ۵.۴ را مرحله‌به‌مرحله جلو ببرید؛ هر مرحله را با commit و تست ببندید. هدف نهایی: سایت زنده + ریپازیتوری عمومی.',
    ],
    workshop_answers=[
        ('راهنمای گام ۱ — چک‌لیست طراحی',
         '<p>برای هر پروژه این سوالات را در design.md جواب دهید:</p>'
         '<ul>'
         '<li><strong>موجودیت‌ها:</strong> چه مدل‌هایی؟ هر رابطه FK/O2O/m2m و on_delete درستش چیست (۵)؟</li>'
         '<li><strong>نقش‌ها:</strong> چه کسی چه کاری می‌تواند؟ (جدول نقش×عملیات — درس فصل ۱۳)</li>'
         '<li><strong>صفحات:</strong> فهرست URLها با ویو و قالب هرکدام (درس ۷-۱۰).</li>'
         '<li><strong>جریان‌های کلیدی:</strong> مثلاً «ثبت‌نام تا اولین پست» یا «سبد تا تحویل» را قدم‌به‌قدم بنویسید.</li>'
         '<li><strong>MVP:</strong> چه چیزی در v1.0 هست و چه چیزی در backlog؟ (بی‌رحمانه حذف کنید!)</li></ul>'),
        ('راهنمای گام ۲ — الگوی شروع سریع',
         '<div class="code-box"><div class="code-head"><span>دستورات روز اول</span><span class="lang">bash</span></div><pre class="code"><code data-lang="bash">mkdir myshop &amp;&amp; cd myshop\npython -m venv .venv &amp;&amp; source .venv/bin/activate\npip install django python-dotenv whitenoise pillow\ndjango-admin startproject config .\npython manage.py startapp shop accounts\n# settings: الگوی env فصل ۲۶ را از همان ابتدا بگذارید\ngit init &amp;&amp; printf ".env\\n*.sqlite3\\n__pycache__/\\n" &gt; .gitignore\ngit add -A &amp;&amp; git commit -m "chore: اسکلت پروژه"\n# مدل‌ها → makemigrations → migrate → ادمین → runserver</code></pre></div>'
         '<p>عادت‌هایی که از روز اول پولشان را پس می‌دهند: env از ابتدا (نه «بعداً عوض می‌کنم»)، commit کوچک و مکرر، و نام‌گذاری دقیق مدل‌ها قبل از makemigrations اول (تغییر نام بعداً = مهاجرت دردناک).</p>'),
        ('راهنمای گام ۳ — ریتم اجرا',
         '<p>الگوی پیشنهادی هر هفته:</p>'
         '<ol>'
         '<li><strong>شنبه:</strong> انتخاب ویژگی هفته از نقشه راه + خواندن مرور موردی فصل مرتبط.</li>'
         '<li><strong>طول هفته:</strong> ساخت با چرخه TDD سبک (تست مسیر خوشحال + یک حالت خطا) و commit روزانه.</li>'
         '<li><strong>پنج‌شنبه:</strong> مرور کیفیت: Toolbar (کوئری‌ها)، grep برای TODOها، به‌روزرسانی README.</li>'
         '<li><strong>هر ۲ هفته:</strong> دیپلوی روی محیط دمو — دیپلوی را برای «آخر کار» نگذارید (فصل ۲۶ آسان‌تر می‌شود اگر زود شروع شود).</li></ol>'
         '<p>ملاک «تمام» هر مرحله، چک‌لیست ۵.۴ است نه حس شخصی. و یادتان باشد: <strong>منتشرشده بهتر از کامل است</strong>.</p>'),
    ],
    errors=[
        ('پروژه نیمه‌تمام رها شد (شایع‌ترین «باگ» این فصل!)',
         'علت: دامنه بزرگ + کمال‌گرایی. درمان: MVP را نصف طرح اولیه بگیرید، «ویژگی بعدی» را در backlog بنویسید نه در کد، و هر هفته یک بخش قابل دمو تحویل خودتان بدهید.'),
        ('ریپازیتوری عمومی با SECRET_KEY لو رفته',
         'اگر .env یا کلید را commit کرده‌اید: ① همین حالا کلیدها را <strong>باطل/تغییر</strong> دهید (SECRET_KEY، رمز دیتابیس) ② تاریخچه را با git filter-repo/BFG پاک کنید ③ روتیشن را جدی بگیرید — پاک کردن commit کافی نیست.'),
        ('دموی زنده خراب می‌شود وقتی داور کلیک می‌کند',
         'قبل از انتشار، سناریوهای «کاربر بی‌حوصله» را تست کنید: ثبت‌نام با ایمیل تکراری، سبد خالی checkout، URL دست‌کاری‌شده، آپلود فایل ۵۰MB. صفحات خطای ۴۰۴/۵۰۰ و پیام‌های دوستانه (فصل ۲۱) تفاوت حرفه‌ای و آماتور را نشان می‌دهند.'),
        ('همه‌چیز در یک commit غول‌پیکر',
         'تاریخچه بی‌فایده برای بازبینی/رول‌بک. از امروز: commit کوچک با پیام معنادار (feat/fix/chore). اگر عادت ندارید، از مرحله بعد پروژه تمرینش کنید.'),
    ],
    errors_callout=('tip', 'داکومان مستند کنید',
        'هر چالش جالبی که حل کردید (race condition، طراحی مجوز، بهینه‌سازی) را یک پاراگراف در docs/challenges.md بنویسید. این فایل، ماده خام پست وبلاگ، پاسخ مصاحبه و README جذاب شماست.'),
    exercises=[
        ('تمرین ۱ — طراحی مدل',
         '<p><strong>سوال (پروژه وظایف):</strong> رابطه‌های Workspace/Board/Column/Card/User را با نوع رابطه و on_delete طراحی کنید؛ نقش‌ها (مالک/عضو) کجا ذخیره شوند؟</p>'
         '<p><strong>پاسخ نمونه:</strong> Workspace m2m→User با through=Membership (فیلد role؛ حذف Workspace → CASCADE اعضا). Board FK→Workspace (CASCADE). Column FK→Board (CASCADE) + order. Card FK→Column (CASCADE)، assignees m2m→User (PROTECT یا از طریق عضویت چک شود)، labels m2m→Label. نقش در Membership نه در User — یک کاربر در فضای A مالک و در B بیننده است (درس فصل ۶/۱۳).</p>'),
        ('تمرین ۲ — سناریوی امنیت',
         '<p><strong>سوال (فروشگاه):</strong> سه راه که یک کاربر بدذات ممکن است قیمت/موجودی را دور بزند، و سد هرکدام؟</p>'
         '<p><strong>پاسخ:</strong> ① دست‌کاری price در POST/<span class="term" data-term="session">نشست</span> → قیمت همیشه از دیتابیس (price_at_purchase در checkout سمت سرور ست می‌شود) ② دو کلیک هم‌زمان روی آخرین موجودی → select_for_update + atomic + تست رقابت ③ <span class="term" data-term="url">URL</span> سفارش دیگران (/orders/55/ مال دیگری) → <span class="term" data-term="permission">مجوز شیء‌محور</span> (user=request.user در get_queryset؛ درس ۱۳/۲۳). سد همه: «به داده کلاینت اعتماد نکن + مجوز را روی شیء چک کن».</p>'),
        ('تمرین ۳ — برآورد MVP',
         '<p><strong>سوال:</strong> از فهرست ویژگی‌های پروژه وبلاگ (۵.۱) کدام‌ها MVP و کدام backlog؟</p>'
         '<p><strong>پاسخ نمونه:</strong> MVP: ثبت‌نام/ورود، CRUD پست با مارک‌داون، صفحه نویسنده، نظرات، فهرست/جست‌وجوی ساده. Backlog v1.1: دنبال‌کردن+خوراک، اعلان ایمیلی، API، HTMX لایک. معیار MVP: «یک غریبه بتواند ثبت‌نام کند، بنویسد و خوانده شود» — بقیه بهبود است نه هسته.</p>'),
    ],
    quiz=[
        dict(q='در مدل OrderItem، چرا price_at_purchase ذخیره می‌شود؟',
             opts=['برای سرعت', 'قیمت محصول بعداً عوض شود، مبلغ سفارش تاریخی باید ثابت بماند (snapshot قیمت)',
                   'الزام دیتابیس', 'برای مالیات لازم نیست'],
             ans='b', explain='ارجاع زنده به product.price یعنی فاکتورهای قدیمی با تغییر قیمت «عقب‌گرد» می‌کنند — باگ کلاسیک فروشگاه. هر داده مالی در لحظه تراکنش snapshot می‌شود.'),
        dict(q='select_for_update در checkout چه مشکلی را حل می‌کند؟',
             opts=['کندی', 'رقابت دو سفارش هم‌زمان روی آخرین موجودی (oversell) با قفل ردیفی در تراکنش',
                   'CSRF', 'صفحه‌بندی'],
             ans='b', explain='داخل atomic، قفل ردیف باعث صف‌شدن تراکنش دوم و دیدن موجودی به‌روز می‌شود؛ ترکیب با update(F(...)) دفاع دوم است.'),
        dict(q='اولین قدم درست شروع پروژه کدام است؟',
             opts=['نوشتن ویوها', 'طراحی: ERD مدل‌ها، نقش‌ها و فهرست صفحات روی کاغذ',
                   'دیپلوی', 'انتخاب فریم‌ورک فرانت'],
             ans='b', explain='مدل‌ها اسکلت‌بند پروژه‌اند؛ تغییر آن‌ها بعد از makemigrations/داده گران است. دو ساعت طراحی، هفته‌ها بازنویسی را نجات می‌دهد.'),
        dict(q='اگر SECRET_KEY تصادفاً در ریپازیتوری عمومی commit شده بود، اولین اقدام چیست؟',
             opts=['حذف commit', 'باطل/تغییر فوری کلید و همه secrets لو رفته (چرخش کلید) — سپس پاک‌سازی تاریخچه',
                   'ریپازیتوری را خصوصی کنید و تمام', 'مهم نیست اگر پروژه تمرینی است'],
             ans='b', explain='ربات‌ها کلیدهای عمومی را در دقیقه‌ها می‌ربایند؛ حذف commit از تاریخچه بدون rotation کافی نیست. با .gitignore + .env از روز اول پیشگیری کنید.'),
        dict(q='MVP پروژه وبلاگ چندنویسنده کدام است؟',
             opts=['همه ویژگی‌های فهرست فصل', 'ثبت‌نام/ورود + CRUD پست + صفحه نویسنده + نظرات — قابل استفاده برای یک غریبه',
                   'فقط مدل‌ها', 'API + SPA'],
             ans='b', explain='MVP = کوچک‌ترین نسخه‌ای که ارزش واقعی می‌دهد. دنبال‌کردن/اعلان/API بهبودهای v1.1 هستند؛ انتشار زودتر، یادگیری سریع‌تر.'),
        dict(q='چک‌لیست کیفیت قبل از انتشار کدام ترکیب را پوشش می‌دهد؟',
             opts=['فقط تست‌ها', 'تست سبز + check --deploy + امنیت (HTTPS/secrets/کوکی‌ها) + کارایی + پشتیبان‌گیری + README',
                   'فقط دیپلوی', 'فقط ظاهر سایت'],
             ans='b', explain='«تمام شد» یعنی همه ابعاد: درستی (تست)، امنیت، سرعت، بازگشت‌پذیری (پشتیبان) و ارائه (مستند/دمو) — فهرست ۵.۴.'),
    ],
    project_title='پروژه نهایی شما',
    project_intro='این «کارگاه» خودِ پروژه است — انتخاب کنید، بسازید، منتشر کنید.',
    project_checklist=[
        'پروژه انتخاب و design.md (ERD + نقش‌ها + صفحات + MVP) نوشته شد.',
        'مراحل ۱-۳ نقشه راه: اسکلت env-محور، مدل‌ها+ادمین، احراز هویت+ویوها+قالب‌ها.',
        'مراحل ۴-۵: ویژگی تمایز (HTMX/API) + سیگنال/تسک/کش.',
        'مرحله ۶: ≥۳۰ تست مسیر اصلی + لاگ + صفحات خطا + مرور امنیتی.',
        'مراحل ۷: سایت زنده با HTTPS + README حرفه‌ای + تگ v1.0 در GitHub.',
    ],
    project_callout=('tip', 'و بعد از v1.0؟',
        'بازخورد بگیرید (۵ نفر واقعی استفاده کنند)، backlog را اولویت‌بندی و v1.1 را منتشر کنید. چرخه «ساخت → انتشار → بازخورد» همان چیزی است که مهندس نرم‌افزار را از دوره‌دیده جدا می‌کند.'),
    summary_items=[
        'سه پروژه: وبلاگ چندنویسنده (پیوسته به دوره)، فروشگاه (پول/سفارش)، وظایف تیمی (مجوز/تعامل).',
        'نقشه راه ۷ مرحله‌ای: طراحی → اسکلت → هسته → تمایز → عمق → کیفیت → انتشار.',
        'قواعد طلایی: snapshot قیمت، موجودی اتمی، مجوز شیء‌محور، env از روز اول.',
        'چک‌لیست کیفیت ۵.۴ = تعریف «تمام شد».',
        'انتشار عمومی + مستند چالش‌ها = رزومه واقعی شما.',
    ],
    golden='پروژه‌ای که منتشر شده و استفاده می‌شود، از ده پروژه کامل‌شده در localhost ارزشمندتر است.',
    faq=[
        ('اگر وسط راه گیر کردم چه کنم؟',
         '<p>ترتیب کمک گرفتن: ① پیام خطا را کامل بخوانید و google/StackOverflow (۹۰٪ خطاها قبلاً رخ داده‌اند) ② به فصل مرتبط دوره برگردید ③ با <span class="term" data-term="pdb">breakpoint</span> و <span class="term" data-term="test">تست</span> کوچک، مسئله را ایزوله کنید (فصل ۲۰/۲۱) ④ انجمن‌های فارسی‌زبان جنگو و Discord. گیرکردن بخشی از یادگیری است؛ تسلیم‌شدن نه.</p>'),
        ('از کد دوره کپی کنم اشکال دارد؟',
         '<p>کپی کردن برای یادگیری اشکالی ندارد، ولی «فهمیدن بدون تایپ مجدد» توهم مهارت می‌سازد. روش درست: الگو را ببندید و از حافظه بنویسید؛ هر جا گیر کردید نگاه کنید. پروژه شما باید تصمیم‌های <strong>خودتان</strong> را داشته باشد — همان‌ها در مصاحبه داستان می‌شوند.</p>'),
        ('بعد از این دوره چه بخوانم؟',
         '<p>مسیر پیشنهادی ۵.۵: Channels (realtime) ← CI/CD و DevOps ← مطالعه کد پروژه‌های باز (Saleor، Taiga) ← یک کتاب عمیق (Two Scoops of Django برای الگوها، Architecture Patterns with Python برای تمیزمعماری). و مهم‌تر از همه: پروژه دوم را شروع کنید.</p>'),
    ],
    next_step='',
),
]
