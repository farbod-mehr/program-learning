# -*- coding: utf-8 -*-
"""داده محتوای فصل‌های ۲ تا ۶ — بخش 🧱 مبانی و اصول پایه"""

CHAPTERS = [

# ================================================================ فصل ۲
dict(
    n=2, icon='🛠️', title='نصب، راه‌اندازی و محیط توسعه', cat=1, mins=90, lvl_label='صفر مطلق',
    hero_desc='قدم‌به‌قدم نصب <span class="term" data-term="python">پایتون</span> و <span class="term" data-term="django">جنگو</span>، ساخت اولین پروژه، آشنایی با <span class="term" data-term="terminal">ترمینال</span>، <span class="term" data-term="venv">محیط مجازی</span> و اجرای اولین سرور — همراه دستورات ویندوز و مک/لینوکس.',
    s1_intro='این فصل اولین برخورد عملی شما با ابزارهاست. تا پایان فصل، محیط توسعه‌تان کامل آماده است و صفحه خوش‌آمدگویی جنگو را در مرورگر می‌بینید — یکی از لذت‌بخش‌ترین لحظات دوره! 🙂',
    objectives=[
        'پایتون را نصب و نسخه‌اش را در <span class="term" data-term="terminal">ترمینال</span> بررسی کنید.',
        '<span class="term" data-term="venv">محیط مجازی</span> بسازید و فعال کنید و بدانید چرا ضروری است.',
        'جنگو را با <span class="term" data-term="pip">pip</span> نصب کنید.',
        'با <code class="inline-code">startproject</code> اولین پروژه را بسازید و نقش هر فایل را بگویید.',
        'سرور توسعه را با <span class="term" data-term="runserver">runserver</span> اجرا و صفحه را در مرورگر ببینید.',
    ],
    s1_position='<strong>جایگاه فصل:</strong> پیش‌نیاز تمام فصل‌های عملی دوره. اگر جایی از نصب گیر کردید، بخش ۹ (خطاهای رایج) را حتماً ببینید — ۹۰٪ مشکلات نصب آنجاست.',
    roadmap=[
        ('نصب پایتون', 'دانلود، نصب و بررسی نسخه در ویندوز/مک/لینوکس.'),
        ('ترمینال و محیط مجازی', 'آشنایی با خط فرمان و ساخت venv.'),
        ('نصب جنگو و ساخت پروژه', 'pip install django و startproject.'),
        ('اجرای سرور', 'runserver و دیدن اولین صفحه؛ مرور فایل‌های پروژه.'),
    ],
    mind_qs=[
        ('چرا نباید بسته‌های پایتون را مستقیم روی پایتونِ اصلی سیستم نصب کرد؟',
         '<p>چون پروژه‌های مختلف به نسخه‌های متفاوت یک بسته نیاز دارند و نصب سراسری باعث <strong>تداخل</strong> می‌شود. <span class="term" data-term="venv">محیط مجازی</span> برای هر پروژه یک «اتاق ایزوله» می‌سازد تا بسته‌ها و نسخه‌هایشان قاطی نشوند.</p>'),
        ('وقتی در مرورگر <code class="inline-code">127.0.0.1:8000</code> را باز می‌کنید، درخواست به کجا می‌رود؟',
         '<p>به <strong>همان کامپیوتر خودتان</strong>! عدد 127.0.0.1 یعنی «خودم» (localhost). سرور توسعه جنگو روی کامپیوتر شما اجرا شده و <span class="term" data-term="request">درخواست</span> مرورگر را locally پاسخ می‌دهد. به اینترنت هم نیازی نیست.</p>'),
        ('فایل <code class="inline-code">manage.py</code> با <code class="inline-code">django-admin</code> چه فرقی دارد؟',
         '<p>هر دو فرمان اجرا می‌کنند؛ اما <span class="term" data-term="manage-py">manage.py</span> به <strong>پروژه شما</strong> و فایل <span class="term" data-term="settings">settings.py</span>اش وصل است (فرمان‌هایی مثل runserver و migrate)، در حالی که django-admin عمومی است و بیشتر برای startproject استفاده می‌شود.</p>'),
    ],
    prereq_intro='قبل از شروع، این موارد را آماده کنید:',
    prereq=[
        'کامل بودن فصل ۱ (مفاهیم وب، <span class="term" data-term="framework">فریم‌ورک</span> و MTV).',
        'یک کامپیوتر با ویندوز ۱۰/۱۱، مک یا لینوکس.',
        'دسترسی به اینترنت فقط برای <strong>دانلود و نصب</strong> (بعد از نصب، دوره آفلاین است).',
        'حدود ۹۰ دقیقه زمان و یک لیوان چای! ☕',
    ],
    prereq_callout=('tip', 'درباره ویرایشگر کد',
        'برای این دوره <strong>VS Code</strong> (رایگان) پیشنهاد می‌شود؛ ولی هر ویرایشگری (حتی PyCharm Community) کار می‌کند. در ویرایشگر، افزونه Python را نصب کنید تا رنگ‌آمیزی و تکمیل خودکار داشته باشید.'),
    concepts=[
        dict(h='۵.۱ نصب پایتون', body=[
            '<p>جنگو با <span class="term" data-term="python">پایتون</span> کار می‌کند، پس اول پایتون لازم است (نسخه ۳.۱۰ به بالا؛ پیشنهاد ما ۳.۱۲). پایتون ۲ سال‌هاست منسوخ شده — حتماً نسخه ۳ را نصب کنید.</p>',
            '<ul><li><strong>ویندوز:</strong> از <code class="inline-code">python.org/downloads</code> نصب‌کننده را بگیرید. در صفحه اول نصب، تیک <strong>«Add python.exe to PATH»</strong> را حتماً بزنید (مهم‌ترین قدم!).</li>'
            '<li><strong>مک:</strong> پایتون معمولاً هست، ولی برای به‌روز بودن با <code class="inline-code">brew install python</code> نصبش کنید.</li>'
            '<li><strong>لینوکس (اوبونتو/دبیان):</strong> <code class="inline-code">sudo apt install python3 python3-venv python3-pip</code></li></ul>',
            '<p>حالا در <span class="term" data-term="terminal">ترمینال</span> (ویندوز: PowerShell یا CMD) بررسی کنید:</p>',
            ('code', 'بررسی نصب پایتون', 'bash', '''python --version
# یا در برخی سیستم‌ها:
python3 --version
# خروجی نمونه: Python 3.12.4'''),
        ]),
        dict(h='۵.۲ ترمینال و محیط مجازی (venv)', body=[
            '<p>ترمینال محیط متنی اجرای دستورات است. برای هر پروژه یک پوشه بسازید و داخلش <span class="term" data-term="venv">محیط مجازی</span> ایجاد کنید:</p>',
            ('code', 'ساخت و فعال‌سازی محیط مجازی', 'bash', '''mkdir django-course && cd django-course

# ساخت محیط مجازی (پوشه .venv ساخته می‌شود)
python -m venv .venv

# فعال‌سازی در ویندوز (PowerShell):
.venv\\Scripts\\Activate.ps1
# فعال‌سازی در ویندوز (CMD):
.venv\\Scripts\\activate.bat
# فعال‌سازی در مک/لینوکس:
source .venv/bin/activate'''),
            '<p>بعد از فعال‌سازی، اول خط فرمان <code class="inline-code">(.venv)</code> ظاهر می‌شود؛ یعنی از این به بعد هر نصبی فقط داخل همین محیط انجام می‌شود. برای خروج: <code class="inline-code">deactivate</code>.</p>',
            ('callout', 'warn', 'قانون طلایی',
             'هر بار که ترمینال جدید باز می‌کنید، <strong>اول venv را فعال کنید</strong> بعد دستور جنگو بزنید. نیمی از خطاهای «django-admin is not recognized» همین است!'),
        ]),
        dict(h='۵.۳ نصب جنگو', body=[
            '<p>با venv فعال، جنگو را با <span class="term" data-term="pip">pip</span> (نصب‌کننده بسته‌های پایتون) نصب کنید:</p>',
            ('code', 'نصب جنگو', 'bash', '''pip install "django>=5.2,<6.0"

# بررسی نصب:
django-admin --version
# خروجی نمونه: 5.2.4

python -m django --version   # روش جایگزین'''),
            '<p>پیشنهاد ما نصب نسخه <strong>5.2 (LTS)</strong> است — نسخهٔ <span class="term" data-term="lts">پشتیبانی بلندمدت</span> که تا ۲۰۲۸ به‌روزرسانی امنیتی می‌گیرد. جزئیات نسخه‌ها در فصل ۲۹.</p>',
        ]),
        dict(h='۵.۴ ساخت اولین پروژه و آناتومی فایل‌ها', body=[
            '<p>با دستور زیر اسکلت <span class="term" data-term="project">پروژه</span> ساخته می‌شود:</p>',
            ('code', 'ساخت پروژه', 'bash', '''django-admin startproject mysite .
# نقطه آخر مهم است: پروژه در همین پوشه ساخته شود، نه زیرپوشه تو در تو'''),
            '<p>ساختار حاصل:</p>',
            ('code', 'ساختار پروژه', 'text', '''django-course/
├── .venv/            ← محیط مجازی (به مخزن کد اضافه نمی‌شود)
├── manage.py         ← رابط فرمان پروژه
└── mysite/
    ├── __init__.py
    ├── settings.py   ← تنظیمات مرکزی پروژه
    ├── urls.py       ← ریشه مسیریابی URLها
    ├── asgi.py       ← ورودی سرور ناهمگام (فصل ۲۶)
    └── wsgi.py       ← ورودی سرور تولید (فصل ۲۶)'''),
            '<p>نگاه سریع به چند تنظیم مهم <span class="term" data-term="settings">settings.py</span>:</p>',
            '<ul>'
            '<li><code class="inline-code">SECRET_KEY</code> — <span class="term" data-term="secret-key">کلید مخفی</span> امضای رمزنگاری؛ هرگز لو نرود.</li>'
            '<li><code class="inline-code">DEBUG = True</code> — <span class="term" data-term="debug">حالت اشکال‌زدایی</span>؛ در تولید باید False شود.</li>'
            '<li><code class="inline-code">ALLOWED_HOSTS = []</code> — دامنه‌های مجاز؛ با DEBUG=True سخت‌گیری نمی‌شود.</li>'
            '<li><code class="inline-code">INSTALLED_APPS</code> — فهرست <span class="term" data-term="app">اپ‌ها</span>؛ فصل ۳ اضافه می‌کنیم.</li>'
            '<li><code class="inline-code">DATABASES</code> — به‌صورت پیش‌فرض <span class="term" data-term="sqlite">SQLite</span> (فایل <code class="inline-code">db.sqlite3</code>).</li></ul>',
        ]),
        dict(h='۵.۵ اجرای سرور توسعه', body=[
            '<p>لحظه دیدن نتیجه! با <span class="term" data-term="runserver">runserver</span> سرور توسعه را اجرا کنید:</p>',
            ('code', 'اجرای سرور', 'bash', '''python manage.py runserver

# خروجی نمونه:
# Starting development server at http://127.0.0.1:8000/
# Quit the server with CTRL-BREAK.'''),
            '<p>مرورگر را باز کنید و به <code class="inline-code">http://127.0.0.1:8000/</code> بروید: 🎉 صفحه خوش‌آمدگویی موشک جنگو! سرور با <code class="inline-code">Ctrl+C</code> متوقف می‌شود و با ذخیره هر فایل، خودش reload می‌کند.</p>',
            ('callout', 'info', 'این سرور چیست؟',
             'runserver یک <span class="term" data-term="server">سرور</span> سبک مخصوص توسعه است. مرورگر شما <span class="term" data-term="client">کلاینت</span> است و یک <span class="term" data-term="request">درخواست</span> می‌فرستد و <span class="term" data-term="response">پاسخ</span> می‌گیرد — دقیقاً همان مفهومی که در فصل ۱ یاد گرفتید، حالا روی کامپیوتر خودتان. برای تولید هرگز از runserver استفاده نمی‌شود (فصل ۲۶).'),
        ]),
    ],
    example_intro='یک دور کامل از صفر تا سرورِ در حال اجرا — همین توالی را عملاً انجام دهید:',
    example=[
        ('code', 'دور کامل راه‌اندازی (مک/لینوکس؛ ویندوز مشابه)', 'bash', '''mkdir blog-project && cd blog-project
python3 -m venv .venv
source .venv/bin/activate
pip install "django>=5.2,<6.0"
django-admin startproject config .
python manage.py runserver'''),
        '<p><strong>تحلیل هر خط:</strong></p>',
        '<ol>'
        '<li>پوشه پروژه ساخته و واردش شدیم.</li>'
        '<li>محیط مجازی <code class="inline-code">.venv</code> ساخته شد.</li>'
        '<li>فعالش کردیم — حالا pip و python این محیط‌اند.</li>'
        '<li>جنگو فقط داخل .venv نصب شد.</li>'
        '<li>پروژه‌ای به نام <code class="inline-code">config</code> در همین پوشه ساخته شد (نام config یک قرارداد حرفه‌ای است).</li>'
        '<li>سرور توسعه بالا آمد → <code class="inline-code">127.0.0.1:8000</code> را ببینید!</li></ol>',
    ],
    workshop_intro='حالا نوبت شماست (حدود ۲۰ دقیقه). اگر جایی خطا گرفتید، اول بخش ۹ را ببینید:',
    workshop_tasks=[
        '<strong>کارگاه ۱:</strong> پوشه‌ای به نام <code class="inline-code">my-first-site</code> بسازید، داخلش venv بسازید و فعال کنید و جنگو نصب کنید. با <code class="inline-code">pip list</code> مطمئن شوید django در فهرست است.',
        '<strong>کارگاه ۲:</strong> پروژه‌ای به نام <code class="inline-code">config</code> در همان پوشه بسازید و سرور را روی پورت <strong>۹۰۰۰</strong> اجرا کنید (راهنما: runserver یک آرگومان پورت هم می‌گیرد).',
        '<strong>کارگاه ۳:</strong> در فایل <span class="term" data-term="settings">settings.py</span> مقدار <code class="inline-code">DEBUG</code> را موقتاً <code class="inline-code">False</code> کنید، صفحه را رفرش کنید و تفاوت را ببینید. بعد برگردانید True. چه نتیجه‌ای گرفتید؟',
    ],
    workshop_answers=[
        ('پاسخ کارگاه ۱ — محیط و نصب',
         '<div class="code-box"><div class="code-head"><span>دستورات کامل</span><span class="lang">Bash</span></div><pre class="code"><code data-lang="bash">mkdir my-first-site && cd my-first-site\npython -m venv .venv\nsource .venv/bin/activate   # ویندوز: .venv\\\\Scripts\\\\activate\npip install "django>=5.2,<6.0"\npip list   # باید: django  5.2.x</code></pre></div>'
         '<p>اگر <code class="inline-code">pip list</code> جنگو را نشان نداد، یعنی venv فعال نبوده؛ فعال کنید و دوباره نصب کنید.</p>'),
        ('پاسخ کارگاه ۲ — پروژه و پورت ۹۰۰۰',
         '<div class="code-box"><div class="code-head"><span>دستورات</span><span class="lang">Bash</span></div><pre class="code"><code data-lang="bash">django-admin startproject config .\npython manage.py runserver 9000</code></pre></div>'
         '<p>حالا در مرورگر: <code class="inline-code">http://127.0.0.1:9000/</code>. پورت فقط عدد درگاه شبکه است؛ ۸۰۰۰ پیش‌فرض است و اجباری نیست.</p>'),
        ('پاسخ کارگاه ۳ — نتیجه DEBUG=False',
         '<p>با <code class="inline-code">DEBUG=False</code> و <code class="inline-code">ALLOWED_HOSTS</code> خالی، جنگو صفحه خطای <strong>«DisallowedHost»</strong> نشان می‌دهد و حتی خطاهای دیگر را هم بدون جزئیات نمایش می‌دهد. درس: DEBUG=False یعنی «هیچ جزئیاتی از خطا به کاربر غریبه نشان نده» — دقیقاً چیزی که در تولید می‌خواهیم (به‌همراه تنظیم صحیح ALLOWED_HOSTS و یک صفحه خطای ۵۰۰ مناسب). DEBUG را برای ادامه دوره True بگذارید.</p>'),
    ],
    errors=[
        ('خطای <code>\'django-admin\' is not recognized</code> یا <code>command not found</code>',
         'سه علت رایج: ① جنگو نصب نیست → <code class="inline-code">pip install django</code>. ② venv فعال نیست → فعالش کنید. ③ در ویندوز، پایتون با تیک PATH نصب نشده → دوباره نصب کنید و «Add to PATH» را بزنید (یا از <code class="inline-code">python -m django</code> استفاده کنید).'),
        ('خطای <code>\'python\' is not recognized</code>',
         'پایتون نصب نیست یا در PATH نیست. در مک/لینوکس ممکن است دستور <code class="inline-code">python3</code> باشد نه <code class="inline-code">python</code>. در ویندوز نصب‌کننده را با گزینه PATH دوباره اجرا کنید.'),
        ('خطای <code>Port 8000 is already in use</code>',
         'سرور قبلی هنوز باز است (شاید در ترمینالی دیگر). آن را با Ctrl+C ببندید یا پورت دیگری بدهید: <code class="inline-code">python manage.py runserver 8080</code>.'),
        ('اجرای Activate.ps1 در PowerShell خطا می‌دهد',
         'سیاست اجرایی PowerShell محدود است. با PowerShell به‌عنوان مدیر: <code class="inline-code">Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser</code> یا از activate.bat در CMD استفاده کنید.'),
    ],
    errors_callout=('danger', 'هرگز این کار را نکنید',
        '<code class="inline-code">pip install django</code> را <strong>بیرون از venv</strong> اجرا نکنید (مگر عمداً). نصب سراسری، ریشه اکثر تداخل‌های عجیب‌وغریب نسخه‌هاست.'),
    exercises=[
        ('تمرین ۱ — فرمان درست را انتخاب کنید',
         '<p><strong>سوال:</strong> برای هر کار کدام فرمان؟ (الف) ساخت محیط مجازی (ب) نصب جنگو (ج) ساخت پروژه (د) اجرای سرور</p>'
         '<p><strong>پاسخ:</strong> الف → <code class="inline-code">python -m venv .venv</code> • ب → <code class="inline-code">pip install django</code> • ج → <code class="inline-code">django-admin startproject NAME .</code> • د → <code class="inline-code">python manage.py runserver</code></p>'),
        ('تمرین ۲ — نقش فایل‌ها',
         '<p><strong>سوال:</strong> نقش هر فایل چیست؟ <code class="inline-code">settings.py</code>، <code class="inline-code">urls.py</code>، <code class="inline-code">manage.py</code>، <code class="inline-code">wsgi.py</code></p>'
         '<p><strong>پاسخ:</strong> settings → تنظیمات مرکزی (پایگاه داده، اپ‌ها، امنیت) • urls → ریشه مسیریابی نشانی‌ها • manage.py → رابط فرمان‌های پروژه • wsgi.py → نقطه اتصال سرورهای تولید مثل Gunicorn (فصل ۲۶).</p>'),
        ('تمرین ۳ — عیب‌یابی',
         '<p><strong>سناریو:</strong> هم‌اتاقی‌تان می‌گوید «دیروز همه‌چیز کار می‌کرد، امروز django-admin کار نمی‌کند!». محتمل‌ترین علت چیست؟</p>'
         '<p><strong>پاسخ:</strong> ترمینال جدید باز کرده و <strong>venv را فعال نکرده</strong>. راه‌حل: <code class="inline-code">cd</code> به پوشه پروژه + فعال‌سازی venv. به او بگویید نشانه فعال بودن، پیشوند <code class="inline-code">(.venv)</code> است.</p>'),
    ],
    quiz=[
        dict(q='چرا برای هر پروژه یک محیط مجازی (venv) می‌سازیم؟',
             opts=['چون جنگو بدون آن نصب نمی‌شود', 'تا بسته‌ها و نسخه‌های پروژه‌های مختلف با هم تداخل نکنند',
                   'چون سرعت اجرا را دو برابر می‌کند', 'چون پایتون فقط یک نسخه می‌تواند داشته باشد'],
             ans='b', explain='محیط مجازی ایزوله‌سازی می‌کند: هر پروژه بسته‌ها و نسخه‌های خودش را دارد و به بقیه سیستم کاری ندارد.'),
        dict(q='کدام گزینه یک پروژه جدید جنگو می‌سازد؟',
             opts=['python manage.py startproject mysite', 'django-admin startproject mysite',
                   'pip install mysite', 'django-admin runserver'],
             ans='b', explain='برای ساخت پروژه از django-admin استفاده می‌شود؛ manage.py بعد از ساخت پروژه وجود دارد (مرغ و تخم‌مرغ!).'),
        dict(q='سرور توسعه جنگو با کدام دستور اجرا می‌شود؟',
             opts=['django-admin startserver', 'python manage.py runserver',
                   'pip run server', 'python server.py'],
             ans='b', explain='runserver فرمان مخصوص manage.py است؛ آدرس پیش‌فرض http://127.0.0.1:8000/.'),
        dict(q='در مرحله تولید (سایت واقعی روی اینترنت) کدام تنظیم درست است؟',
             opts=['DEBUG = True تا خطاها را ببینیم', 'DEBUG = False همراه با ALLOWED_HOSTS تنظیم‌شده',
                   'SECRET_KEY را خالی بگذاریم', 'فرقی نمی‌کند؛ فقط سرعت مهم است'],
             ans='b', explain='DEBUG=True در تولید، جزئیات حساس (کلیدها، مسیرها، کوئری‌ها) را به غریبه‌ها لو می‌دهد؛ پس False + ALLOWED_HOSTS مشخص.'),
        dict(q='نقش فایل settings.py چیست؟',
             opts=['قالب‌های HTML پروژه', 'تنظیمات مرکزی: پایگاه داده، اپ‌ها، قالب‌ها و امنیت',
                   'ذخیره داده‌های کاربران', 'مسیریابی URLها'],
             ans='b', explain='settings.py مرکز پیکربندی پروژه است؛ مسیریابی در urls.py و قالب‌ها در پوشه templatesاند.'),
        dict(q='نشانه فعال بودن محیط مجازی در خط فرمان چیست؟',
             opts=['رنگ ترمینال سبز می‌شود', 'پیشوند (.venv) ابتدای خط فرمان ظاهر می‌شود',
                   'دستور pip غیرفعال می‌شود', 'هیچ نشانه‌ای ندارد'],
             ans='b', explain='بعد از activate، نام محیط (معمولاً .venv) ابتدای prompt اضافه می‌شود؛ دیدن آن یعنی نصب‌ها ایزوله‌اند.'),
    ],
    project_title='محیط توسعه شخصی من',
    project_intro='یک محیط توسعه استاندارد و تکرارپذیر برای خودتان بسازید که در همه فصل‌های بعد از آن استفاده می‌کنید.',
    project_checklist=[
        'پوشه پروژه + venv فعال + جنگو 5.2 نصب‌شده.',
        'پروژه‌ای به نام <code class="inline-code">config</code> ساخته و سرور روی ۱۲۷.۰.۰.۱:۸۰۰۰ اجرا شود.',
        'در settings.py، مقادیر SECRET_KEY، DEBUG، ALLOWED_HOSTS، INSTALLED_APPS و DATABASES را پیدا کنید و نقش هرکدام را در یک خط در بخش یادداشت‌ها بنویسید.',
        'با <code class="inline-code">pip freeze &gt; requirements.txt</code> <span class="term" data-term="requirements">فایل وابستگی</span> پروژه را بسازید.',
        'یک بار ترمینال را ببندید، دوباره باز کنید و کل توالی «cd + فعال‌سازی venv + runserver» را از حفظ انجام دهید. 🙂',
    ],
    project_callout=('tip', 'چرا این پروژه مهم است؟',
        'همین محیط، پایه همه فصل‌های بعد است. عادت «اول venv، بعد دستور» از همین‌جا شکل می‌گیرد.'),
    summary_items=[
        'پایتون ۳ را نصب و در ترمینال بررسی کردیم.',
        'با <span class="term" data-term="venv">venv</span> محیط ایزوله ساختیم؛ قانون طلایی: اول فعال‌سازی، بعد هر دستور.',
        'جنگو را با <span class="term" data-term="pip">pip</span> نصب کردیم (نسخه پیشنهادی: 5.2 LTS).',
        'پروژه را با <code class="inline-code">startproject</code> ساختیم و نقش manage.py، settings.py، urls.py و wsgi.py را شناختیم.',
        'سرور توسعه را با <span class="term" data-term="runserver">runserver</span> اجرا و صفحه خوش‌آمدگویی را دیدیم.',
    ],
    golden='هر پروژه = یک پوشه + یک venv + یک startproject + یک runserver؛ به همین سادگی.',
    faq=[
        ('آیا باید حتماً VS Code داشته باشم؟',
         '<p>خیر. PyCharm Community، Sublime یا هر ویرایشگر دیگری هم کار می‌کند. VS Code به‌خاطر سبکی، رایگان بودن و افزونه عالی Python پیشنهاد اول ماست.</p>'),
        ('پایتون ۳.۱۳ نصب کردم؛ مشکلی ندارد؟',
         '<p>نه! جنگو 5.2 از پایتون 3.10 تا 3.13 پشتیبانی می‌کند. فقط پایتون ۲ یا نسخه‌های خیلی قدیمی (زیر 3.10) مشکل‌سازند.</p>'),
        ('سرور را بگذارم باز بماند اشکالی دارد؟',
         '<p>برای توسعه خیر؛ ولی موقع بستن لپ‌تاپ یا تمام‌شدن کار با Ctrl+C ببندیدش. مصرف منابع runserver ناچیز است.</p>'),
    ],
    next_step='محیط آماده است! در <strong>فصل ۳</strong> اولین <span class="term" data-term="app">اپلیکیشن</span> را می‌سازیم و اولین کد واقعی جنگو (ویو و URL) را می‌نویسیم.',
),

# ================================================================ فصل ۳
dict(
    n=3, icon='🧩', title='اپلیکیشن‌ها (Apps) در جنگو', cat=1, mins=80, lvl_label='مبتدی',
    hero_desc='تفاوت <span class="term" data-term="project">پروژه</span> و <span class="term" data-term="app">اپ</span>، ساخت اولین اپ با startapp، ثبت در INSTALLED_APPS و نوشتن اولین <span class="term" data-term="view">ویو</span> و مسیر <span class="term" data-term="url">URL</span> — اولین کد واقعی شما!',
    s1_intro='تا الان فقط «اسکلت» داشتیم؛ از این فصل کد واقعی می‌نویسیم. اپ‌ها قلب سازمان‌دهی کد در جنگو هستند و هر ویو یک قدم به سمت ساختن سایت واقعی است.',
    objectives=[
        'تفاوت پروژه و <span class="term" data-term="app">اپلیکیشن</span> را توضیح دهید.',
        'با <code class="inline-code">startapp</code> اپ بسازید و فایل‌هایش را بشناسید.',
        'اپ را در <span class="term" data-term="settings">INSTALLED_APPS</span> ثبت کنید.',
        'اولین <span class="term" data-term="view">ویوی تابعی</span> را بنویسید و به یک <span class="term" data-term="url">URL</span> وصل کنید.',
        'صفحه «سلام دنیا»ی خودتان را در مرورگر ببینید!',
    ],
    s1_position='<strong>جایگاه فصل:</strong> روی محیط توسعه فصل ۲ ساخته می‌شود و پایه فصل‌های ۴ (مدل)، ۷ (مسیریابی کامل) و ۸ (ویوها) است.',
    roadmap=[
        ('پروژه در برابر اپ', 'مرز مسئولیت‌ها و ساختار پوشه‌ها.'),
        ('ساخت اپ', 'startapp و آناتومی فایل‌های اپ.'),
        ('ثبت و اتصال', 'INSTALLED_APPS و include در urls.'),
        ('اولین ویو', 'HttpResponse و render — سلام دنیای جنگویی!'),
    ],
    mind_qs=[
        ('اگر سایتی «وبلاگ»، «فروشگاه» و «تماس با ما» دارد، چند اپ باید بسازیم؟',
         '<p>به‌طور کلاسیک سه اپ: <code class="inline-code">blog</code>، <code class="inline-code">shop</code> و <code class="inline-code">pages</code>. قاعده سرانگشتی: <strong>هر مسئولیت مستقل = یک اپ</strong>. مدل‌ها، ویوها و قالب‌های هر بخش داخل اپ خودش می‌ماند.</p>'),
        ('چرا جنگو اصرار دارد ویو یک «درخواست» بگیرد و «پاسخ» برگرداند؟',
         '<p>چون وب همین است! هر <span class="term" data-term="view">ویو</span> در واقع کارخانه تبدیل <span class="term" data-term="request">درخواست</span> به <span class="term" data-term="response">پاسخ</span> است. این قرارداد ساده باعث می‌شود همه چیز (صفحه HTML، فایل، JSON) یک‌شکل مدیریت شود.</p>'),
        ('بدون ثبت اپ در INSTALLED_APPS چه می‌شود؟',
         '<p>جنگو اصلاً نمی‌فهمد اپ شما وجود دارد: مدل‌هایش <span class="term" data-term="migration">مهاجرت</span> نمی‌گیرند، قالب‌هایش پیدا نمی‌شوند و فرمان‌های مدیریتی‌اش کار نمی‌کنند.</p>'),
    ],
    prereq_intro='پیش از شروع مطمئن شوید:',
    prereq=[
        'فصل ۲ کامل شده: پروژه‌ای با <code class="inline-code">config</code> (یا mysite) و venv فعال دارید.',
        'سرور توسعه قابل اجراست و صفحه خوش‌آمدگویی را دیده‌اید.',
        'مفاهیم <span class="term" data-term="request">درخواست</span>/<span class="term" data-term="response">پاسخ</span> و MTV از فصل ۱ یادتان هست.',
        'ویرایشگر کد آماده و پوشه پروژه در آن باز است.',
    ],
    prereq_callout=None,
    concepts=[
        dict(h='۵.۱ پروژه در برابر اپلیکیشن', body=[
            '<p><span class="term" data-term="project">پروژه</span> = <strong>کل وب‌سایت</strong>: تنظیمات مشترک، پایگاه داده و ریشه URLها. <span class="term" data-term="app">اپ</span> = <strong>یک ماژول با مسئولیت مشخص</strong> داخل پروژه: مثل اپ «وبلاگ» یا «نظرسنجی».</p>',
            '<ul>'
            '<li>یک پروژه می‌تواند چند اپ داشته باشد.</li>'
            '<li>یک اپ می‌تواند در چند پروژه <strong>استفاده مجدد</strong> شود (فلسفه اصلی اپ!).</li>'
            '<li>اپ‌ها کنار هم در پوشه <code class="inline-code">apps/</code> یا ریشه پروژه قرار می‌گیرند؛ در دوره ما کنار manage.py.</li></ul>',
        ]),
        dict(h='۵.۲ ساخت اپ و آناتومی آن', body=[
            ('code', 'ساخت اپ وبلاگ', 'bash', '''python manage.py startapp blog'''),
            ('code', 'ساختار اپ', 'text', '''blog/
├── __init__.py
├── admin.py       ← ثبت مدل‌ها در پنل مدیریت (فصل ۶)
├── apps.py        ← کلاس پیکربندی اپ
├── migrations/    ← مهاجرت‌های پایگاه داده (فصل ۵)
├── models.py      ← مدل‌های داده (فصل ۴)
├── tests.py       ← تست‌ها (فصل ۲۰)
└── views.py       ← ویوها (منطق صفحه‌ها)'''),
            '<p>دو فایل دیگر را <strong>خودمان</strong> اضافه می‌کنیم چون جنگو به‌صورت پیش‌فرض نمی‌سازدشان: <code class="inline-code">urls.py</code> (مسیرهای مخصوص اپ) و پوشه <code class="inline-code">templates/blog/</code> (قالب‌ها).</p>',
        ]),
        dict(h='۵.۳ ثبت اپ در INSTALLED_APPS', body=[
            '<p>در <span class="term" data-term="settings">settings.py</span> نام اپ را اضافه کنید:</p>',
            ('code', 'config/settings.py', 'python', '''INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # اپ‌های خودمان:
    "blog",
]'''),
            '<p>آن شش مورد اول، اپ‌های آماده خود جنگو هستند (پنل <span class="term" data-term="admin">ادمین</span>، <span class="term" data-term="authentication">احراز هویت</span>، نشست‌ها و...). حالا اپ blog برای جنگو «وجود دارد».</p>',
        ]),
        dict(h='۵.۴ اولین ویو و اتصال به URL', body=[
            '<p>ویو تابعی ساده‌ترین شکل منطق صفحه است: یک <span class="term" data-term="request">درخواست</span> می‌گیرد، یک <span class="term" data-term="response">پاسخ</span> برمی‌گرداند:</p>',
            ('code', 'blog/views.py', 'python', '''from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>سلام از اولین ویوی من! 🌿</h1>")


def about(request):
    return HttpResponse("اینجا صفحه درباره ماست.")'''),
            '<p>حالا <span class="term" data-term="routing">مسیریابی</span>. اول در اپ، فایل <code class="inline-code">blog/urls.py</code>:</p>',
            ('code', 'blog/urls.py', 'python', '''from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
]'''),
            '<p>و در ریشه پروژه، مسیرهای اپ را با <code class="inline-code">include</code> وصل می‌کنیم:</p>',
            ('code', 'config/urls.py', 'python', '''from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
]'''),
            ('callout', 'info', 'جریان کار',
             'درخواست <code class="inline-code">/about/</code> → از config/urls.py به blog.urls می‌رود (include) → با الگوی <code class="inline-code">about/</code> مطابقت می‌کند → ویوی <code class="inline-code">about</code> اجرا و <span class="term" data-term="response">پاسخ</span> برگردانده می‌شود. جزئیات کامل include و نام‌گذاری در فصل ۷.'),
        ]),
        dict(h='۵.۵ از متن خام به صفحه HTML: render', body=[
            '<p>HttpResponse برای متن ساده خوب است، ولی صفحه واقعی یعنی HTML. فعلاً یک نمونه سریع (فصل ۱۰ کامل توضیح می‌دهد):</p>',
            ('code', 'blog/views.py — استفاده از قالب', 'python', '''from django.shortcuts import render


def home(request):
    context = {"title": "وبلاگ من", "posts_count": 3}
    return render(request, "blog/home.html", context)'''),
            '<p>فایل <code class="inline-code">blog/templates/blog/home.html</code> را بسازید:</p>',
            ('code', 'blog/templates/blog/home.html', 'html', '''<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head><meta charset="utf-8"><title>{{ title }}</title></head>
<body>
  <h1>به {{ title }} خوش آمدید!</h1>
  <p>تعداد نوشته‌ها: {{ posts_count }}</p>
</body>
</html>'''),
            '<p>تابع <span class="term" data-term="render">render</span>، <span class="term" data-term="template">قالب</span> و <span class="term" data-term="context">بافت</span> (دیکشنری داده) را ترکیب و HTML نهایی می‌سازد.</p>',
        ]),
    ],
    example_intro='یک اپ کامل «pages» با دو صفحه — مرحله‌به‌مرحله:',
    example=[
        ('code', '۱) ساخت و ثبت اپ', 'bash', '''python manage.py startapp pages
# سپس "pages" را به INSTALLED_APPS اضافه کنید'''),
        ('code', '۲) ویوها — pages/views.py', 'python', '''from django.shortcuts import render


def home(request):
    return render(request, "pages/home.html", {"name": "دنیای جنگو"})


def about(request):
    return render(request, "pages/about.html")'''),
        ('code', '۳) مسیرها — pages/urls.py و اتصال در config/urls.py', 'python', '''# pages/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
]

# config/urls.py
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pages.urls")),
]'''),
        ('code', '۴) قالب‌ها — pages/templates/pages/home.html', 'html', '''<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head><meta charset="utf-8"><title>خانه</title></head>
<body>
  <h1>سلام {{ name }}! 🌿</h1>
  <a href="/about/">درباره ما</a>
</body>
</html>'''),
        '<p>سرور را اجرا کنید و <code class="inline-code">/</code> و <code class="inline-code">/about/</code> را ببینید. اولین سایت دو صفحه‌ای شما ساخته شد! 🎉</p>',
    ],
    workshop_intro='۲۰ دقیقه وقت بگذارید و خودتان بسازید:',
    workshop_tasks=[
        '<strong>کارگاه ۱:</strong> اپی به نام <code class="inline-code">shop</code> بسازید، ثبتش کنید و ویویی بنویسید که با HttpResponse متن «به فروشگاه خوش آمدید» را در مسیر <code class="inline-code">/shop/</code> نشان دهد.',
        '<strong>کارگاه ۲:</strong> در همان اپ، ویوی <code class="inline-code">product</code> با <span class="term" data-term="render">render</span> و یک قالب بسازید که نام محصول را از <span class="term" data-term="context">بافت</span> بگیرد و نمایش دهد (مسیر: <code class="inline-code">/shop/product/</code>).',
        '<strong>کارگاه ۳:</strong> عمداً نام اپ را از INSTALLED_APPS حذف کنید و ببینید چه خطایی می‌بینید. سپس برگردانید.',
    ],
    workshop_answers=[
        ('پاسخ کارگاه ۱ — اپ shop',
         '<div class="code-box"><div class="code-head"><span>shop/views.py</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">from django.http import HttpResponse\n\n\ndef shop_home(request):\n    return HttpResponse("به فروشگاه خوش آمدید 🛍️")</code></pre></div>'
         '<div class="code-box"><div class="code-head"><span>shop/urls.py</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">from django.urls import path\nfrom . import views\n\nurlpatterns = [\n    path("", views.shop_home, name="shop_home"),\n]</code></pre></div>'
         '<p>و در config/urls.py: <code class="inline-code">path("shop/", include("shop.urls")),</code> + ثبت "shop" در INSTALLED_APPS.</p>'),
        ('پاسخ کارگاه ۲ — ویو با render',
         '<div class="code-box"><div class="code-head"><span>shop/views.py</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">from django.shortcuts import render\n\n\ndef product(request):\n    context = {"product_name": "لپ‌تاپ جنگویی"}\n    return render(request, "shop/product.html", context)</code></pre></div>'
         '<p>قالب در <code class="inline-code">shop/templates/shop/product.html</code> با <code class="inline-code">{{ product_name }}</code>. مسیر: <code class="inline-code">path("product/", views.product)</code> داخل shop/urls.py.</p>'),
        ('پاسخ کارگاه ۳ — نتیجه حذف از INSTALLED_APPS',
         '<p>با حذف نام اپ، قالب‌هایش پیدا نمی‌شوند: خطای <strong>TemplateDoesNotExist</strong> (برای کارگاه ۲) — چون جنگو پوشه templates اپ‌های ثبت‌نشده را جست‌وجو نمی‌کند. ویوهای HttpResponse-only ممکن است هنوز کار کنند (چون import مستقیم‌اند) ولی مدل‌ها و مهاجرت‌ها قطعاً از کار می‌افتند. درس: <strong>ثبت در INSTALLED_APPS یعنی «جنگو، این اپ را بشناس»</strong>.</p>'),
    ],
    errors=[
        ('خطای <code>TemplateDoesNotExist</code>',
         'سه علت: ① اپ در INSTALLED_APPS ثبت نشده. ② مسیر قالب غلط است — ساختار درست: <code class="inline-code">blog/templates/blog/home.html</code> و در ویو: <code class="inline-code">"blog/home.html"</code> (پوشه templates دوبرابر ندارد!). ③ نام فایل اشتباه تایپ شده.'),
        ('صفحه <code>404</code> برای مسیری که نوشته‌ام',
         'معمولاً include درست وصل نشده یا الگوی path اشتباه است. ترتیب مهم است: جنگو urlpatterns را <strong>از بالا به پایین</strong> امتحان می‌کند. همچنین اسلش انتهایی را چک کنید (<code class="inline-code">about/</code> با <code class="inline-code">about</code> فرق دارد).'),
        ('خطای <code>ModuleNotFoundError: No module named \'blog\'</code>',
         'پوشه اپ هم‌سطح manage.py نیست (جایی دیگر ساخته‌اید) یا نام را اشتباه نوشته‌اید. manage.py را پیدا کنید و ببینید پوشه اپ کنارش هست یا نه.'),
        ('فراموشی کاما یا براکت در urlpatterns',
         'SyntaxError با پیام روشن می‌دهد. هر <code class="inline-code">path(...)</code> را با کاما جدا کنید و آخرین <code class="inline-code">]</code> را ببندید.'),
    ],
    errors_callout=None,
    exercises=[
        ('تمرین ۱ — مرز پروژه و اپ',
         '<p><strong>سوال:</strong> برای سایتی با بخش‌های «خبر»، «ویدیو» و «کاربران»، ساختار پروژه/اپ را طراحی کنید.</p>'
         '<p><strong>پاسخ نمونه:</strong> یک پروژه (config) با سه اپ: <code class="inline-code">news</code>، <code class="inline-code">video</code> و <code class="inline-code">accounts</code>. تنظیمات و پایگاه داده مشترک در پروژه؛ هر بخش مدل/ویو/قالب خودش را در اپ خودش دارد.</p>'),
        ('تمرین ۲ — ترتیب اجرا',
         '<p><strong>سوال:</strong> مراحل ساخت یک صفحه جدید را مرتب کنید: نوشتن قالب / ساخت ویو / افزودن path / ثبت اپ.</p>'
         '<p><strong>پاسخ:</strong> ① ثبت اپ در INSTALLED_APPS → ② نوشتن ویو در views.py → ③ افزودن path در urls → ④ ساخت قالب و اتصالش به ویو با render. (ترتیب ۲ و ۴ قابل جابه‌جایی است.)</p>'),
        ('تمرین ۳ — نام‌گذاری',
         '<p><strong>سوال:</strong> چرا پیشنهاد می‌شود قالب‌ها را در <code class="inline-code">templates/blog/</code> بگذاریم نه مستقیم <code class="inline-code">templates/</code>؟</p>'
         '<p><strong>پاسخ:</strong> چون جست‌وجوی قالب جنگو در همه اپ‌ها مشترک است؛ اگر دو اپ هر دو <code class="inline-code">home.html</code> داشته باشند، تداخل پیش می‌آید. پوشه همنام با اپ (namespace) از برخورد جلوگیری می‌کند.</p>'),
    ],
    quiz=[
        dict(q='رابطه پروژه و اپلیکیشن در جنگو کدام است؟',
             opts=['یک پروژه فقط یک اپ می‌تواند داشته باشد', 'پروژه کل سایت است و اپ یک ماژول با مسئولیت مشخص داخل آن',
                   'اپ بزرگ‌تر از پروژه است', 'هر دو یک چیزند'],
             ans='b', explain='پروژه تنظیمات و اسکلت کل سایت را دارد؛ اپ‌ها اجزای مستقل و قابل استفاده مجدد داخل آن‌اند.'),
        dict(q='کدام فایل را جنگو در startapp نمی‌سازد و معمولاً خودمان اضافه می‌کنیم؟',
             opts=['views.py', 'models.py', 'urls.py اپ', 'admin.py'],
             ans='c', explain='urls.py مخصوص اپ (و پوشه templates) را خودمان می‌سازیم؛ بقیه با startapp ایجاد می‌شوند.'),
        dict(q='یک ویوی تابعی در جنگو چه چیزی دریافت و چه چیزی برمی‌گرداند؟',
             opts=['درخواست (request) → پاسخ (response)', 'پاسخ → درخواست',
                   'قالب → مدل', 'URL → پایگاه داده'],
             ans='a', explain='قرارداد ثابت جنگو: ویو = تابعی که HttpRequest می‌گیرد و HttpResponse (یا نتیجه render/redirect) برمی‌گرداند.'),
        dict(q='اگر اپ در INSTALLED_APPS ثبت نشود، کدام مورد از کار می‌افتد؟',
             opts=['فقط پنل ادمین', 'فقط URLها',
                   'مدل‌ها/مهاجرت‌ها، کشف قالب‌ها و فرمان‌های اپ', 'هیچ چیز؛ ثبت اختیاری است'],
             ans='c', explain='جنگو اپ‌های ثبت‌نشده را نمی‌شناسد: مهاجرت مدل‌ها ساخته نمی‌شود و قالب‌هایش در جست‌وجو پیدا نمی‌شوند.'),
        dict(q='تابع render چه ترکیبی را به پاسخ HTML تبدیل می‌کند؟',
             opts=['مدل + ویو', 'قالب + بافت (context)',
                   'URL + ویو', 'فرم + قالب'],
             ans='b', explain='render(request, template, context) قالب را با داده‌های بافت پر و پاسخ HTML می‌سازد.'),
        dict(q='در config/urls.py، تابع include چه کاری می‌کند؟',
             opts=['قالب‌ها را شامل صفحه می‌کند', 'مسیرهای یک اپ را به ریشه مسیریابی پروژه وصل می‌کند',
                   'اپ را نصب می‌کند', 'پایگاه داده را شامل می‌شود'],
             ans='b', explain='include("blog.urls") یعنی «بقیه مسیرها را از فایل urls همان اپ بخوان»؛ یعنی مسیریابی تکه‌تکه و منظم.'),
    ],
    project_title='سایت دو بخشی من',
    project_intro='یک پروژه با دو اپ واقعی بسازید: <code class="inline-code">pages</code> (صفحه‌های عمومی) و <code class="inline-code">blog</code> (مقالات).',
    project_checklist=[
        'اپ pages با صفحه‌های خانه و درباره (با render و قالب).',
        'اپ blog با ویوی فهرست مقالات که فعلاً یک لیست پایتونی ساختگی (hardcode) را به قالب می‌دهد و با حلقه نمایش می‌دهد.',
        'هر دو اپ در INSTALLED_APPS ثبت و با include به ریشه وصل شوند.',
        'در همه قالب‌ها یک لینک مشترک بین صفحه‌ها بگذارید.',
        'ساختار پوشه‌ها را در یادداشت‌ها رسم کنید.',
    ],
    project_callout=('tip', 'نگاه به آینده',
        'فهرست «ساختگی» مقالات در فصل ۴ جای خودش را به <span class="term" data-term="model">مدل</span> و پایگاه داده واقعی می‌دهد — صبور باشید!'),
    summary_items=[
        'پروژه = کل سایت؛ اپ = ماژول مستقل با مسئولیت مشخص.',
        'با <code class="inline-code">startapp</code> اپ ساختیم و نقش models.py، views.py، admin.py و migrations را شناختیم.',
        'اپ را در INSTALLED_APPS ثبت کردیم.',
        'اولین ویوهای تابعی با HttpResponse و <span class="term" data-term="render">render</span> نوشتیم.',
        'با path و include، ویوها را به <span class="term" data-term="url">URL</span>ها وصل کردیم.',
    ],
    golden='اپ = واحد سازمان‌دهی کد؛ ویو = تابعی که درخواست را به پاسخ تبدیل می‌کند؛ urls = نقشهٔ اتصال این دو.',
    faq=[
        ('نام اپ را فارسی یا با حرف بزرگ بگذارم؟',
         '<p>خیر! نام اپ باید شناسه معتبر پایتون باشد: حروف کوچک انگلیسی، بدون فاصله (مثل blog، shop، accounts). عنوان نمایشی فارسی را در قالب و پنل ادمین بگذارید.</p>'),
        ('چند اپ زیاد است؟',
         '<p>قاعده سفت‌وسختی ندارد. یک سایت کوچک با ۲ تا ۵ اپ نرمال است. وقتی دو اپ همیشه با هم تغییر می‌کنند، شاید باید یکی باشند؛ وقتی یک اپ دو مسئولیت مستقل دارد، شاید باید تقسیم شود.</p>'),
        ('می‌توانم همه چیز را در یک اپ بگذارم؟',
         '<p>فنی بله، ولی ساختار به‌هم می‌ریزد و استفاده مجدد از بین می‌رود. در پروژه‌های کوچکِ تمرینی اشکالی ندارد؛ برای پروژه جدی، تفکیک کنید.</p>'),
    ],
    next_step='صفحه‌ها ساخته شدند ولی داده‌هایشان ساختگی است. در <strong>فصل ۴</strong> با <span class="term" data-term="model">مدل‌ها</span> و <span class="term" data-term="orm">ORM</span>، داده‌های واقعی را در پایگاه داده ذخیره و مدیریت می‌کنیم.',
),

# ================================================================ فصل ۴
dict(
    n=4, icon='🗄️', title='مدل‌ها (Models) و پایگاه داده', cat=1, mins=110, lvl_label='مبتدی',
    hero_desc='<span class="term" data-term="database">پایگاه داده</span> و <span class="term" data-term="orm">ORM</span>، انواع فیلد و پارامترهایشان، روابط ForeignKey و ManyToMany، کلاس Meta، ساخت مدل وبلاگ و کار با داده در <span class="term" data-term="django-shell">شل جنگو</span>.',
    s1_intro='تا حالا داده‌ها ساختگی بودند؛ از این فصل سایت شما «حافظه» پیدا می‌کند. مدل‌ها مهم‌ترین بخش اکثر پروژه‌های جنگو هستند — خوب طراحی‌شان کنید، بقیه کارها آسان می‌شود.',
    objectives=[
        'بگویید <span class="term" data-term="orm">ORM</span> چه مشکلی را حل می‌کند.',
        'مدل با فیلدهای مناسب و پارامترهایشان (max_length، default، unique و...) بنویسید.',
        'روابط <span class="term" data-term="foreign-key">یک‌به‌چند</span> و <span class="term" data-term="many-to-many">چندبه‌چند</span> بسازید.',
        'با <span class="term" data-term="django-shell">شل جنگو</span> داده ایجاد، خواندن، ویرایش و حذف کنید (<span class="term" data-term="crud">CRUD</span>).',
        'نقش <code class="inline-code">__str__</code> و کلاس Meta را توضیح دهید.',
    ],
    s1_position='<strong>جایگاه فصل:</strong> پایهٔ فصل ۵ (مهاجرت‌ها)، ۶ (ادمین)، ۱۵ (QuerySet پیشرفته) و عملاً همه پروژه‌های دوره.',
    roadmap=[
        ('ORM و پایگاه داده', 'چرا SQL خام نه؛ جنگو چطور کوئری می‌سازد.'),
        ('مدل و فیلدها', 'انواع فیلد، پارامترها، __str__ و Meta.'),
        ('روابط', 'ForeignKey، OneToOne و ManyToMany.'),
        ('شل و CRUD', 'ساخت/خواندن/ویرایش/حذف داده به‌صورت عملی.'),
    ],
    mind_qs=[
        ('چرا به‌جای نوشتن SQL، از ORM استفاده کنیم؟',
         '<p>سه دلیل: ① <strong>امنیت</strong> — <span class="term" data-term="orm">ORM</span> جلوی <span class="term" data-term="sql-injection">تزریق SQL</span> را می‌گیرد. ② <strong>قابلیت حمل</strong> — کد شما روی SQLite و PostgreSQL یکسان کار می‌کند. ③ <strong>خوانایی</strong> — <code class="inline-code">Post.objects.filter(published=True)</code> از ۱۰ خط SQL تمیزتر است. برای کوئری‌های خیلی خاص، فرار به SQL خام هم ممکن است.</p>'),
        ('رابطه «نویسنده ← پست‌ها» از چه نوعی است؟ یک نویسنده می‌تواند چند پست داشته باشد؟',
         '<p><strong>یک‌به‌چند</strong>: هر پست دقیقاً یک نویسنده دارد، ولی هر نویسنده چند پست. در جنگو: <span class="term" data-term="foreign-key">ForeignKey</span> سمت «چند» (یعنی در مدل Post) تعریف می‌شود.</p>'),
        ('اگر بخواهیم به هر پست چند «برچسب» بدهیم و هر برچسب به چند پست بخورد؟',
         '<p>رابطه <span class="term" data-term="many-to-many">چندبه‌چند</span>: <code class="inline-code">tags = ManyToManyField(Tag)</code>. جنگو خودش جدول واسط را می‌سازد و مدیریت می‌کند.</p>'),
    ],
    prereq_intro='پیش‌نیازها:',
    prereq=[
        'پروژه فصل ۳ با اپ <code class="inline-code">blog</code> آماده باشد.',
        'مفهوم جدول/سطر/ستون پایگاه داده (در ۵.۱ از صفر توضیح می‌دهیم).',
        'آشنایی اولیه با کلاس در پایتون (اگر یادتان نیست، جعبه زیر را بخوانید).',
        '<span class="term" data-term="migration">مهاجرت</span> را فعلاً با دو دستور ساده انجام می‌دهیم؛ منطق کاملش فصل ۵ است.',
    ],
    prereq_callout=('info', 'یادآوری ۳۰ ثانیه‌ای کلاس پایتون',
        'کلاس = قالب ساخت شیء. <code class="inline-code">class Post(models.Model):</code> یعنی «کلاس Post که از Model جنگو ارث می‌برد». هر نمونهٔ آن = یک سطر جدول. اگر با <code class="inline-code">def __str__(self)</code> آشنا نیستید: متدی که می‌گوید «این شیء را چطور به رشته تبدیل کنم».'),
    concepts=[
        dict(h='۵.۱ پایگاه داده و ORM در یک نگاه', body=[
            '<p><span class="term" data-term="database">پایگاه داده</span> = مخزن منظم داده‌ها به شکل <strong>جدول</strong> (سطر و ستون). جنگو به‌صورت پیش‌فرض از <span class="term" data-term="sqlite">SQLite</span> استفاده می‌کند: یک فایل ساده <code class="inline-code">db.sqlite3</code> بدون هیچ نصب اضافی — عالی برای یادگیری و توسعه.</p>',
            '<p><span class="term" data-term="orm">ORM</span> پلی است بین دنیای شیءگرای پایتون و دنیای رابطه‌ای SQL:</p>',
            '<ul>'
            '<li>کلاس مدل ←→ جدول</li>'
            '<li>نمونهٔ مدل ←→ سطر (با یک <span class="term" data-term="primary-key">کلید اصلی</span> یکتا، همان <code class="inline-code">id</code> خودکار)</li>'
            '<li><span class="term" data-term="field">فیلد</span> کلاس ←→ ستون</li></ul>',
            ('code', 'معادل‌های ORM و SQL', 'python', '''# این کد پایتون...
post = Post.objects.get(id=1)
# ...چنین SQL‌ای تولید می‌کند:
# SELECT * FROM blog_post WHERE id = 1;'''),
        ]),
        dict(h='۵.۲ نوشتن اولین مدل', body=[
            ('code', 'blog/models.py', 'python', '''from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    slug = models.SlugField(max_length=200, unique=True)
    body = models.TextField(verbose_name="متن")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title'''),
            '<p>فیلدهای پرکاربرد:</p>',
            '<ul>'
            '<li><code class="inline-code">CharField(max_length=N)</code> — متن کوتاه (max_length <strong>اجباری</strong> است).</li>'
            '<li><code class="inline-code">TextField()</code> — متن بلند بدون محدودیت.</li>'
            '<li><span class="term" data-term="slug">SlugField</span> — شناسه خوانا برای URL (فقط حروف، رقم و خط تیره).</li>'
            '<li><code class="inline-code">IntegerField / DecimalField(max_digits, decimal_places)</code> — عدد / عدد اعشاری دقیق (پول را <strong>هرگز</strong> FloatField نگذارید!).</li>'
            '<li><code class="inline-code">BooleanField, DateTimeField, DateField, EmailField, URLField, ImageField</code></li></ul>',
            '<p>پارامترهای مشترک: <code class="inline-code">null=True</code> (مقدار NULL در دیتابیس مجاز)، <code class="inline-code">blank=True</code> (فیلد در فرم می‌تواند خالی بماند)، <code class="inline-code">unique=True</code>، <code class="inline-code">default=...</code>، <code class="inline-code">choices=...</code>.</p>',
            ('callout', 'tip', 'چرا __str__ مهم است؟',
             'بدون <code class="inline-code">__str__</code>، همه‌جا (مخصوصاً پنل <span class="term" data-term="admin">ادمین</span>) به‌جای «آموزش جنگو» می‌بینید: <code class="inline-code">Post object (1)</code>. همیشه تعریفش کنید.'),
        ]),
        dict(h='۵.۳ روابط بین مدل‌ها', body=[
            ('code', 'blog/models.py — روابط', 'python', '''class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="posts"
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="posts")
    # ... بقیه فیلدهای قبلی


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)'''),
            '<ul>'
            '<li><span class="term" data-term="foreign-key">ForeignKey</span> = یک‌به‌چند. <strong>on_delete اجباری است</strong>: CASCADE (با حذف والد، فرزندها هم حذف شوند)، PROTECT (تا فرزند هست، والد حذف نشود)، SET_NULL (کلید خارجی null شود؛ نیاز به null=True).</li>'
            '<li><span class="term" data-term="many-to-many">ManyToManyField</span> = چندبه‌چند؛ جدول واسط خودکار ساخته می‌شود.</li>'
            '<li><code class="inline-code">related_name</code> = نام دسترسی معکوس: <code class="inline-code">author.posts.all()</code> یا <code class="inline-code">post.comments.all()</code>.</li></ul>',
        ]),
        dict(h='۵.۴ کلاس Meta و اعمال تغییرات (مهاجرت)', body=[
            '<p>کلاس Meta رفتارهای غیرفیلدی مدل را تنظیم می‌کند:</p>',
            ('code', 'کلاس Meta', 'python', '''class Post(models.Model):
    # ...فیلدها...

    class Meta:
        ordering = ["-created_at"]        # ترتیب پیش‌فرض: جدیدترین اول
        verbose_name = "نوشته"
        verbose_name_plural = "نوشته‌ها"'''),
            '<p>برای اینکه مدل‌ها واقعاً در پایگاه داده ساخته شوند، دو فرمان لازم است (منطق کامل در فصل ۵):</p>',
            ('code', 'ساخت و اعمال مهاجرت', 'bash', '''python manage.py makemigrations
python manage.py migrate'''),
        ]),
        dict(h='۵.۵ کار با داده در شل جنگو (CRUD)', body=[
            '<p><span class="term" data-term="django-shell">شل جنگو</span> پایتونِ تعاملی با تنظیمات و مدل‌های بارگذاری‌شده است:</p>',
            ('code', 'python manage.py shell', 'python', '''from blog.models import Author, Post, Tag, Comment

# Create — ایجاد
author = Author.objects.create(name="سارا")
post = Post.objects.create(
    title="سلام جنگو", slug="hello-django",
    body="اولین پست من!", author=author, published=True,
)
tag = Tag.objects.create(name="جنگو")
post.tags.add(tag)                      # اتصال چندبه‌چند

# Read — خواندن
Post.objects.all()                      # همه
Post.objects.get(id=1)                  # دقیقاً یکی (یا خطا)
Post.objects.filter(published=True)     # فیلتر
post.author.name                        # پیمایش رابطه
author.posts.all()                      # دسترسی معکوس

# Update — ویرایش
post.title = "سلام جنگو (ویرایش‌شده)"
post.save()
# یا بدون بارگذاری شیء:
Post.objects.filter(id=1).update(published=False)

# Delete — حذف
comment = Comment.objects.create(post=post, text="عالی!")
comment.delete()                        # حذف یک رکورد
# post.delete()                         # حذف پست (و کامنت‌هایش با CASCADE)'''),
            ('callout', 'info', 'objects چیست؟',
             '<code class="inline-code">objects</code> مدیر (Manager) پیش‌فرض مدل است و دروازه ساخت <span class="term" data-term="queryset">QuerySet</span>ها. فصل ۱۵ تمام قدرتش را باز می‌کنیم.'),
        ]),
    ],
    example_intro='مدل‌های یک «کتابخانه شخصی» را کامل بسازید و داده‌گذاری کنید:',
    example=[
        ('code', 'books/models.py', 'python', '''from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    publisher = models.ForeignKey(
        Publisher, on_delete=models.PROTECT, related_name="books"
    )
    price = models.DecimalField(max_digits=8, decimal_places=0)
    published_year = models.PositiveIntegerField(null=True, blank=True)
    tags = models.ManyToManyField("Tag", blank=True, related_name="books")

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"{self.title} ({self.publisher.name})"


class Tag(models.Model):
    name = models.SlugField(max_length=50, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name'''),
        ('code', 'اعمال و داده‌گذاری در شل', 'bash', '''python manage.py makemigrations books
python manage.py migrate
python manage.py shell'''),
        ('code', 'داخل شل', 'python', '''from books.models import Publisher, Book, Tag

p = Publisher.objects.create(name="نشر جنگو")
t = Tag.objects.create(name="python")
b = Book.objects.create(title="یادگیری جنگو", publisher=p, price=250000)
b.tags.add(t)

Book.objects.filter(publisher__name="نشر جنگو").count()  # 1'''),
        '<p>به <code class="inline-code">publisher__name</code> دقت کنید: دو زیرخط یعنی <strong>پیمایش رابطه</strong> در فیلتر — «کتاب‌هایی که ناشرشان این نام را دارد».</p>',
    ],
    workshop_intro='برای همان اپ blog فصل قبل، لایه داده واقعی بسازید:',
    workshop_tasks=[
        '<strong>کارگاه ۱:</strong> مدل‌های Author، Post (با ForeignKey به Author) و Comment (با ForeignKey به Post) را با فیلدهای مناسب بنویسید و مهاجرت بزنید.',
        '<strong>کارگاه ۲:</strong> در شل: ۲ نویسنده، ۳ پست و ۲ کامنت بسازید؛ سپس همه پست‌های نویسنده اول را با related_name چاپ کنید.',
        '<strong>کارگاه ۳:</strong> ویوی فهرست پست‌های فصل ۳ (که لیست ساختگی داشت) را به داده واقعی وصل کنید: <code class="inline-code">Post.objects.filter(published=True)</code> را به قالب بدهید و با حلقه نمایش دهید.',
    ],
    workshop_answers=[
        ('پاسخ کارگاه ۱ — مدل‌ها',
         '<div class="code-box"><div class="code-head"><span>blog/models.py</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">from django.db import models\n\n\nclass Author(models.Model):\n    name = models.CharField(max_length=100)\n\n    def __str__(self):\n        return self.name\n\n\nclass Post(models.Model):\n    title = models.CharField(max_length=200)\n    slug = models.SlugField(max_length=200, unique=True)\n    body = models.TextField()\n    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="posts")\n    published = models.BooleanField(default=False)\n    created_at = models.DateTimeField(auto_now_add=True)\n\n    class Meta:\n        ordering = ["-created_at"]\n\n    def __str__(self):\n        return self.title\n\n\nclass Comment(models.Model):\n    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")\n    text = models.TextField()\n    created_at = models.DateTimeField(auto_now_add=True)</code></pre></div>'
         '<p>سپس: <code class="inline-code">python manage.py makemigrations blog && python manage.py migrate</code></p>'),
        ('پاسخ کارگاه ۲ — داده‌گذاری و related_name',
         '<div class="code-box"><div class="code-head"><span>شل جنگو</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">a1 = Author.objects.create(name="سارا")\na2 = Author.objects.create(name="رضا")\nPost.objects.create(title="پست ۱", slug="post-1", body="...", author=a1, published=True)\nPost.objects.create(title="پست ۲", slug="post-2", body="...", author=a1, published=True)\nPost.objects.create(title="پست ۳", slug="post-3", body="...", author=a2)\np1 = Post.objects.get(slug="post-1")\nComment.objects.create(post=p1, text="عالی بود")\n\nfor post in a1.posts.all():\n    print(post.title)   # پست ۱ / پست ۲</code></pre></div>'),
        ('پاسخ کارگاه ۳ — اتصال ویو به داده واقعی',
         '<div class="code-box"><div class="code-head"><span>blog/views.py</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">from django.shortcuts import render\nfrom .models import Post\n\n\ndef post_list(request):\n    posts = Post.objects.filter(published=True)\n    return render(request, "blog/post_list.html", {"posts": posts})</code></pre></div>'
         '<div class="code-box"><div class="code-head"><span>blog/templates/blog/post_list.html</span><span class="lang">HTML</span></div><pre class="code"><code data-lang="html">&lt;h1&gt;نوشته‌ها&lt;/h1&gt;\n{% for post in posts %}\n  &lt;article&gt;\n    &lt;h2&gt;{{ post.title }}&lt;/h2&gt;\n    &lt;p&gt;نویسنده: {{ post.author.name }} — {{ post.created_at|date:"Y/m/d" }}&lt;/p&gt;\n  &lt;/article&gt;\n{% empty %}\n  &lt;p&gt;هنوز نوشته‌ای منتشر نشده.&lt;/p&gt;\n{% endfor %}</code></pre></div>'),
    ],
    errors=[
        ('تغییر مدل ولی فراموشی makemigrations/migrate',
         'خطای <code>no such column: blog_post.published</code> یعنی مدل و پایگاه داده هم‌گام نیستند. همیشه بعد از تغییر مدل: makemigrations و بعد migrate.'),
        ('فراموشی <code>on_delete</code> در ForeignKey',
         'خطای <code>TypeError: ForeignKey.__init__() missing 1 required keyword-only argument: \'on_delete\'</code>. فکر کنید با حذف والد چه باید بشود: CASCADE، PROTECT یا SET_NULL.'),
        ('CharField بدون max_length',
         'خطای سیستم‌چک جنگو: <code>CharFields must define a \'max_length\' attribute</code>. برای متن بلند و بی‌محدودیت از TextField استفاده کنید.'),
        ('ذخیره مبلغ با FloatField',
         'خطای مفهومی نه خطای اجرا! Float خطای گردنگردن دارد (۰.۱+۰.۲ ≠ ۰.۳). برای پول: <code class="inline-code">DecimalField(max_digits=10, decimal_places=2)</code>.'),
        ('related_name تکراری',
         'اگر دو ForeignKey از یک مدل به مدل دیگر دارید، جنگو خطای clash می‌دهد؛ برای هر کدام related_name یکتا بگذارید.'),
    ],
    errors_callout=None,
    exercises=[
        ('تمرین ۱ — انتخاب فیلد',
         '<p><strong>سوال:</strong> برای هر داده کدام فیلد؟ (الف) ایمیل کاربر (ب) قیمت محصول (ج) متن ۵۰۰۰ کلمه‌ای مقاله (د) موجود/ناموجود (ه) نشانی تصویر پروفایل</p>'
         '<p><strong>پاسخ:</strong> الف → EmailField • ب → DecimalField • ج → TextField • د → BooleanField • ه → ImageField (یا URLField اگر روی CDN است).</p>'),
        ('تمرین ۲ — ترجمه ORM',
         '<p><strong>سوال:</strong> این کوئری چه می‌کند؟ <code class="inline-code">Comment.objects.filter(post__published=True).order_by("-created_at")[:5]</code></p>'
         '<p><strong>پاسخ:</strong> ۵ کامنت آخرِ پست‌های <strong>منتشرشده</strong> (مرتب از جدیدترین). دو زیرخط = پیمایش رابطه به Post.</p>'),
        ('تمرین ۳ — انتخاب on_delete',
         '<p><strong>سوال:</strong> برای این روابط کدام on_delete؟ (الف) حذف کاربر → پست‌هایش (ب) حذف ناشر → کتاب‌هایش (ج) حذف پست → برچسب‌هایش</p>'
         '<p><strong>پاسخ:</strong> الف → CASCADE (یا بهتر: SET_NULL با null=True تا تاریخچه بماند) • ب → PROTECT (ناشرِ کتابِ موجود نباید حذف شود) • ج → سوال انحرافی است! رابطه پست-برچسب ManyToMany است و on_delete نمی‌گیرد؛ با حذف پست فقط ردیف‌های جدول واسط پاک می‌شوند.</p>'),
    ],
    quiz=[
        dict(q='کدام معادله درباره ORM درست است؟',
             opts=['کلاس مدل = سطر، نمونه = جدول', 'کلاس مدل = جدول، نمونهٔ مدل = سطر، فیلد = ستون',
                   'فیلد = جدول، مدل = ستون', 'ORM همان SQL است با نام دیگر'],
             ans='b', explain='نگاشت: کلاس↔جدول، نمونه↔سطر، فیلد↔ستون. ORM کوئری‌های پایتون را به SQL ترجمه می‌کند.'),
        dict(q='برای ذخیره قیمت محصول کدام فیلد مناسب است؟',
             opts=['FloatField', 'CharField', 'DecimalField', 'IntegerField'],
             ans='c', explain='Decimal دقت اعشار دارد و خطای گردکردن شناور نمی‌دهد؛ Float برای پول خطرناک است.'),
        dict(q='رابطه «هر پست یک نویسنده، هر نویسنده چند پست» با کدام فیلد و در کدام مدل ساخته می‌شود؟',
             opts=['ManyToManyField در Author', 'ForeignKey در Post به Author',
                   'ForeignKey در Author به Post', 'OneToOneField در Post'],
             ans='b', explain='سمت «چند» رابطه (Post) کلید خارجی می‌گیرد. با related_name="posts" از سمت نویسنده هم author.posts.all() در دسترس است.'),
        dict(q='on_delete=models.CASCADE یعنی چه؟',
             opts=['رکورد والد حذف نشود', 'با حذف والد، رکوردهای وابسته هم حذف شوند',
                   'کلید خارجی صفر شود', 'فقط در پنل ادمین حذف ممکن باشد'],
             ans='b', explain='CASCADE = حذف آبشاری: حذف نویسنده، پست‌ها (و با زنجیره، کامنت‌ها) را هم حذف می‌کند.'),
        dict(q='خروجی <code>Post.objects.filter(published=True)</code> چیست؟',
             opts=['یک شیء Post', 'یک QuerySet (تنبل) از پست‌های منتشرشده',
                   'یک لیست پایتون معمولی', 'تعداد پست‌ها'],
             ans='b', explain='filter همیشه QuerySet برمی‌گرداند؛ تنبل است یعنی تا وقتی لازم نشود (حلقه، len، ایندکس) کوئری به دیتابیس نمی‌رود.'),
        dict(q='چرا متد __str__ را در مدل تعریف می‌کنیم؟',
             opts=['اجباری است وگرنه migrate خطا می‌دهد', 'برای نمایش خوانای رکورد در ادمین و شل',
                   'برای مرتب‌سازی رکوردها', 'برای تبدیل به JSON'],
             ans='b', explain='بدون __str__ همه‌جا «Post object (1)» می‌بینید؛ با آن، عنوان یا نام خوانا نمایش داده می‌شود.'),
    ],
    project_title='مدل‌های فروشگاه کتاب',
    project_intro='لایه داده یک فروشگاه کوچک کتاب را طراحی و پیاده‌سازی کنید.',
    project_checklist=[
        'مدل‌ها: Category (با fkey والد برای دسته‌بندی تودرتو — اختیاری)، Book، Author، Customer.',
        'رابطه چندبه‌چند Book↔Author (یک کتاب ممکن است چند نویسنده داشته باشد).',
        'فیلد قیمت با DecimalField و موجودی با PositiveIntegerField.',
        'Meta: ordering مناسب + verbose_name فارسی.',
        'در شل: ۵ کتاب با نویسنده و دسته بسازید و ۳ کوئری معنادار بنویسید (مثلاً کتاب‌های ارزان‌تر از X).',
    ],
    project_callout=('tip', 'طراحی قبل از کد',
        'اول روی کاغذ نمودار ER بکشید: موجودیت‌ها را با دایره و روابط را با خط وصل کنید و نوع رابطه (۱-۱، ۱-ن، ن-ن) را بنویسید. ۱۰ دقیقه طراحی، یک ساعت دیباگ را نجات می‌دهد.'),
    summary_items=[
        '<span class="term" data-term="orm">ORM</span> کلاس پایتون را به جدول پایگاه داده نگاشت می‌کند.',
        'فیلدها را شناختیم؛ پول با Decimal، متن بلند با TextField.',
        'روابط: ForeignKey (یک‌به‌چند با on_delete)، ManyToMany (چندبه‌چند)، related_name برای دسترسی معکوس.',
        'کلاس Meta برای ترتیب و نام نمایشی؛ __str__ برای خوانایی.',
        '<span class="term" data-term="crud">CRUD</span> کامل در <span class="term" data-term="django-shell">شل جنگو</span> + فیلتر با پیمایش رابطه (دو زیرخط).',
    ],
    golden='مدل خوب = طرح پایگاه داده خوب؛ هر رابطه را آگاهانه انتخاب کنید: چندبه‌یک، یک‌به‌یک یا چندبه‌چند.',
    faq=[
        ('برای تولید هم SQLite کافی است؟',
         '<p>برای سایت‌های کم‌ترافیک بله، ولی استاندارد صنعت <span class="term" data-term="postgresql">PostgreSQL</span> است. در فصل ۲۶ تعویضش می‌کنیم — چون ORM داریم، تقریباً فقط settings عوض می‌شود!</p>'),
        ('تعداد فیلدهای مدل چقدر باشد؟',
         '<p>قاعده دقیق ندارد. نشانه هشدار: مدلی با ۳۰+ فیلد یا فیلدهایی که نیمی از رکوردها خالی‌اند — شاید باید به مدل جدا (با OneToOne) تقسیم شود.</p>'),
        ('می‌توانم بدون مدل، مستقیم SQL بزنم؟',
         '<p>بله (متدهای raw و connection.cursor)، ولی تا وقتی مجبور نشده‌اید نکنید: امنیت، قابلیت حمل و خوانایی ORM را از دست می‌دهید.</p>'),
    ],
    next_step='مدل‌ها ساخته شدند، ولی هر تغییرشان چطور بدون از دست رفتن داده روی پایگاه داده اعمال می‌شود؟ <strong>فصل ۵</strong> اختصاصاً درباره <span class="term" data-term="migration">مهاجرت‌ها</span> است.',
),

# ================================================================ فصل ۵
dict(
    n=5, icon='🚂', title='مهاجرت‌ها (Migrations) و مدیریت پایگاه داده', cat=1, mins=85, lvl_label='مبتدی',
    hero_desc='چرخه کامل <span class="term" data-term="migration">مهاجرت</span>: makemigrations، migrate، showmigrations و sqlmigrate؛ آناتومی فایل‌های مهاجرت، بازگشت به عقب و مدیریت تغییرات مدل بدون از دست رفتن داده.',
    s1_intro='در فصل ۴ دو فرمان مهاجرت را مکانیکی زدیم؛ حالا می‌فهمیم زیر کاپوت چه می‌گذرد. مهاجرت‌ها «کنترل نسخهٔ پایگاه داده» هستند — همان نقشی که git برای کد دارد.',
    objectives=[
        'چرخه makemigrations → migrate را دقیق توضیح دهید.',
        'با showmigrations و sqlmigrate وضعیت و SQL واقعی را ببینید.',
        'یک فایل مهاجرت را بخوانید (operations و dependencies).',
        'به مهاجرت قبلی <strong>برگردید</strong> (migrate app 000X).',
        'تغییرات خطرناک (حذف فیلد/جدول) و تغییر نام را امن مدیریت کنید.',
    ],
    s1_position='<strong>جایگاه فصل:</strong> مستقیماً روی فصل ۴ (مدل‌ها) سوار است و تا فصل ۲۶ (استقرار) هر جا مدل عوض شود به آن نیاز دارید.',
    roadmap=[
        ('چرخه مهاجرت', 'makemigrations و migrate و تفاوتشان.'),
        ('دیدن وضعیت', 'showmigrations، sqlmigrate و فایل‌های مهاجرت.'),
        ('بازگشت و اصلاح', 'rollback، squash و تغییرات خطرناک.'),
        ('سناریوهای واقعی', 'تغییر نام، افزودن فیلد به جدول پرداده و...'),
    ],
    mind_qs=[
        ('چرا جنگو مدل را مستقیم روی دیتابیس اعمال نمی‌کند؟',
         '<p>چون تغییر ساختار <strong>تاریخچه</strong> می‌خواهد: تیم چند نفره، محیط توسعه/پروداکشن مختلف و نیاز به بازگشت. <span class="term" data-term="migration">مهاجرت</span> هر تغییر را به یک فایل نسخه‌پذیر تبدیل می‌کند که همه‌جا یکسان اعمال می‌شود.</p>'),
        ('اگر در تیم دو نفر هم‌زمان دو مهاجرت بسازند چه می‌شود؟',
         '<p>شاخه‌های مهاجرت ایجاد می‌شود و موقع migrate خطای «conflicting migrations» می‌گیرید. راه‌حل: <code class="inline-code">python manage.py makemigrations --merge</code> — در بخش خطاهای رایج توضیح می‌دهیم.</p>'),
        ('حذف یک فیلد چه بلایی سر داده‌هایش می‌آید؟',
         '<p>با اعمال مهاجرتِ حذف، ستون و <strong>همه داده‌های آن ستون</strong> پاک می‌شوند. برای همین قبل از حذف فیلد در محیط واقعی، از داده نسخه پشتیبان می‌گیرند یا اول فیلد را «مرده» اعلام می‌کنند (دیگر استفاده نشود) و بعداً حذفش می‌کنند.</p>'),
    ],
    prereq_intro='پیش‌نیازها:',
    prereq=[
        'فصل ۴ کامل شده باشد (مدل‌های Post/Author یا مشابه در اپ blog).',
        'فایل <code class="inline-code">db.sqlite3</code> موجود باشد.',
        'پوشه <code class="inline-code">blog/migrations/</code> را باز کنید تا حین فصل فایل‌هایش را ببینیم.',
        'یک نسخه پشتیبان از db.sqlite3 بگیرید (فقط کپی‌اش کنید!) تا با خیال راحت آزمایش کنیم.',
    ],
    prereq_callout=None,
    concepts=[
        dict(h='۵.۱ چرخه مهاجرت: دو فرمان، دو نقش', body=[
            '<ul>'
            '<li><code class="inline-code">makemigrations</code> — تفاوت <span class="term" data-term="model">مدل</span>‌های فعلی با آخرین مهاجرت را پیدا و <strong>فایل مهاجرت جدید</strong> (در پوشه migrations هر <span class="term" data-term="app">اپ</span>) می‌سازد. هنوز <span class="term" data-term="database">دیتابیس</span> دست نخورده!</li>'
            '<li><code class="inline-code">migrate</code> — فایل‌های ساخته‌شده و اعمال‌نشده را <strong>روی پایگاه داده اجرا</strong> می‌کند و در جدول django_migrations ثبت می‌کند کدام اعمال شده.</li></ul>',
            ('code', 'چرخه استاندارد', 'bash', '''# ۱. مدل را در models.py تغییر بدهید
# ۲. فایل مهاجرت بسازید:
python manage.py makemigrations blog
# → Migrations for 'blog':
#   blog/migrations/0002_post_summary.py

# ۳. اعمالش کنید:
python manage.py migrate'''),
            ('callout', 'warn', 'ترتیب را قاطی نکنید',
             'makemigrations بدون migrate = تغییر فقط روی کاغذ است! و migrate بدون makemigrations = چیزی برای اعمال وجود ندارد. همیشه جفت، به همین ترتیب.'),
        ]),
        dict(h='۵.۲ دیدن وضعیت و SQL پشت صحنه', body=[
            ('code', 'فرمان‌های تشخیصی', 'bash', '''python manage.py showmigrations blog
# blog
#  [X] 0001_initial
#  [X] 0002_post_summary     ← [X] یعنی اعمال شده

python manage.py sqlmigrate blog 0002
# SQL واقعی که اجرا خواهد شد را نشان می‌دهد (بدون اجرا!)'''),
            '<p>یک فایل مهاجرت چه شکلی است؟</p>',
            ('code', 'blog/migrations/0002_post_summary.py', 'python', '''from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),   # ← بعد از کدام مهاجرت اعمال شود
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="summary",
            field=models.TextField(blank=True, default=""),
        ),
    ]'''),
            '<p>فایل مهاجرت <strong>کد <span class="term" data-term="python">پایتون</span> معمولی</strong> است: dependencies زنجیره ترتیب را می‌سازند و operations تغییرات را (AddField، RemoveField، CreateModel، AlterField و...). جنگو از روی همین‌ها SQL مخصوص هر پایگاه داده را تولید می‌کند.</p>',
        ]),
        dict(h='۵.۳ بازگشت به عقب (Rollback)', body=[
            ('code', 'بازگشت به مهاجرت مشخص', 'bash', '''# برگرداندن اپ blog به وضعیت بعد از مهاجرت 0001:
python manage.py migrate blog 0001
# → Unapplying blog.0002_post_summary

# بازگشت کامل (حذف همه مهاجرت‌های اپ):
python manage.py migrate blog zero'''),
            ('callout', 'danger', 'بازگشت هم داده می‌سوزاند!',
             'Unapply کردن AddField یعنی <strong>حذف آن ستون با تمام داده‌هایش</strong>. rollback روی دیتابیس تولید فقط با نسخه پشتیبان معتبر انجام شود.'),
        ]),
        dict(h='۵.۴ سناریوهای واقعی و تغییرات خطرناک', body=[
            '<ul>'
            '<li><strong>تغییر نام فیلد:</strong> جنگو هنگام makemigrations می‌پرسد «آیا این تغییر نام است یا حذف+افزودن؟» — اگر Yes را بزنید، RenameField ساخته و <strong>داده حفظ می‌شود</strong>. اگر اشتباه حذف+افزودن بسازد، داده آن ستون می‌سوزد؛ فایل مهاجرت را قبل از migrate بخوانید!</li>'
            '<li><strong>افزودن فیلد بدون default به جدولِ پرداده:</strong> جنگو می‌پرسد چه مقداری برای سطرهای موجود؟ یا فیلد را <code class="inline-code">null=True</code> یا دارای <code class="inline-code">default</code> تعریف کنید.</li>'
            '<li><strong>unique کردن فیلدی که داده تکراری دارد:</strong> موقع migrate خطای یکپارچگی می‌گیرید؛ اول داده تکراری را پاک کنید.</li>'
            '<li><strong>مهاجرت داده (Data Migration):</strong> گاهی باید خودِ داده‌ها را تغییر دهید (نه ساختار) — با <code class="inline-code">makemigrations --empty</code> و تابع RunPython. نمونه کامل در فصل ۱۶ (سیگنال) و پروژه‌ها.</li></ul>',
        ]),
        dict(h='۵.۵ چند نکته حرفه‌ای', body=[
            '<ul>'
            '<li>فایل‌های migrations را <strong>در git کامیت کنید</strong>؛ آن‌ها بخشی از تاریخچه پروژه‌اند.</li>'
            '<li>در محیط توسعه، اگر مهاجرت خراب شد و هنوز داده مهمی ندارید: حذف فایل مهاجرت + حذف <span class="term" data-term="sqlite">db.sqlite3</span> + makemigrations + migrate = شروع تمیز.</li>'
            '<li>برای پروژه‌های بزرگ با صدها مهاجرت: <code class="inline-code">squashmigrations</code> چند مهاجرت را در یکی خلاصه می‌کند.</li>'
            '<li>هرگز فایل مهاجرتِ <strong>اعمال‌شده در تولید</strong> را دستی ویرایش نکنید؛ مهاجرت جدید بسازید.</li></ul>',
        ]),
    ],
    example_intro='یک چرخه کامل و واقعی: افزودن فیلد، دیدن SQL، اعمال، و بازگشت:',
    example=[
        ('code', '۱) تغییر مدل', 'python', '''# blog/models.py — افزودن به Post:
    summary = models.TextField(blank=True, default="")'''),
        ('code', '۲) ساخت و بررسی مهاجرت', 'bash', '''python manage.py makemigrations blog
python manage.py sqlmigrate blog 0002
# خروجی نمونه (SQLite):
# ALTER TABLE "blog_post" ADD COLUMN "summary" text NOT NULL DEFAULT '';'''),
        ('code', '۳) اعمال و آزمایش', 'bash', '''python manage.py migrate
python manage.py shell
# >>> from blog.models import Post
# >>> p = Post.objects.first(); p.summary = "خلاصه"; p.save()'''),
        ('code', '۴) پشیمانی! بازگشت', 'bash', '''python manage.py migrate blog 0001
# Unapplying blog.0002 — ستون summary و داده‌هایش حذف شد'''),
    ],
    workshop_intro='این سناریوها را روی پروژه خودتان تمرین کنید:',
    workshop_tasks=[
        '<strong>کارگاه ۱:</strong> فیلد <code class="inline-code">views_count = PositiveIntegerField(default=0)</code> را به Post اضافه کنید، مهاجرت بسازید، SQL را با sqlmigrate ببینید و اعمال کنید.',
        '<strong>کارگاه ۲:</strong> نام فیلد <code class="inline-code">body</code> را به <code class="inline-code">content</code> تغییر دهید. دقت کنید جنگو چه سوالی می‌پرسد و خروجی makemigrations چه عملیاتی دارد. داده‌های موجود حفظ شدند؟',
        '<strong>کارگاه ۳:</strong> یک مدل جدید <code class="inline-code">Draft</code> بسازید، مهاجرت بزنید، سپس با <code class="inline-code">migrate blog zero</code> و حذف فایل‌های مهاجرت و db.sqlite3، پروژه را به ابتدا برگردانید و دوباره بسازید (تمرین «شروع تمیز»).',
    ],
    workshop_answers=[
        ('پاسخ کارگاه ۱',
         '<div class="code-box"><div class="code-head"><span>دستورات</span><span class="lang">Bash</span></div><pre class="code"><code data-lang="bash">python manage.py makemigrations blog\npython manage.py sqlmigrate blog 0003\npython manage.py migrate\npython manage.py showmigrations blog</code></pre></div>'
         '<p>چون default=0 دارد، سطرهای موجود بدون سوال مقدار ۰ می‌گیرند و مهاجرت بی‌خطر است.</p>'),
        ('پاسخ کارگاه ۲',
         '<p>موقع makemigrations جنگو می‌پرسد: <code class="inline-code">Did you rename post.body to post.content (a TextField)? [y/N]</code> — با <strong>y</strong> پاسخ دهید تا <code class="inline-code">RenameField</code> بسازد و داده حفظ شود. اگر N بزنید، RemoveField + AddField ساخته و همه متن‌ها از بین می‌روند. همیشه بعد از makemigrations، فایل ساخته‌شده را باز و operations را چک کنید.</p>'),
        ('پاسخ کارگاه ۳',
         '<p>توالی شروع تمیز: ① <code class="inline-code">python manage.py migrate blog zero</code> (اختیاری اگر db را حذف می‌کنید) ② حذف همه فایل‌های migrations به‌جز <code class="inline-code">__init__.py</code> ③ حذف db.sqlite3 ④ makemigrations و migrate. این کار <strong>همه داده‌ها را پاک می‌کند</strong> — فقط در توسعه و وقتی داده آزمایشی است انجامش دهید.</p>'),
    ],
    errors=[
        ('خطای <code>Conflicting migrations detected</code>',
         'دو شاخه مهاجرت هم‌زمان ساخته شده (کار تیمی). راه‌حل: <code class="inline-code">python manage.py makemigrations --merge</code> یک مهاجرت ادغام می‌سازد؛ بعد migrate بزنید.'),
        ('خطای <code>no such table</code> یا <code>column ... does not exist</code>',
         'مهاجرت‌ها اعمال نشده‌اند: <code class="inline-code">python manage.py migrate</code> بزنید. اگر باز هم خطا داد، showmigrations را چک کنید که همه [X] باشند.'),
        ('خطای <code>NOT NULL constraint failed</code> هنگام افزودن فیلد',
         'فیلدی بدون default و بدون null=True به جدولِ دارای سطر اضافه کرده‌اید؛ سطرهای قدیمی مقدار ندارند. فیلد را default‌دار کنید یا مهاجرت را برگردانید و اصلاح کنید.'),
        ('مهاجرت را دستی ویرایش کردم و حالا migrate خطا می‌دهد',
         'اگر مهاجرت <strong>اعمال نشده</strong> را خراب کرده‌اید: حذفش کنید و دوباره makemigrations بزنید. اگر اعمال شده را ویرایش کرده‌اید، وضعیت جدول django_migrations با واقعیت فرق دارد — در توسعه، شروع تمیز راحت‌ترین راه است.'),
    ],
    errors_callout=('tip', 'عادت حرفه‌ای',
        'بعد از هر makemigrations، یک نگاه به فایل تولیدشده بیندازید. ۳۰ ثانیه بازبینی، از فاجعهٔ «حذف ناخواستهٔ ستون» در تولید جلوگیری می‌کند.'),
    exercises=[
        ('تمرین ۱ — فرمان درست',
         '<p><strong>سوال:</strong> کدام فرمان برای هر کار؟ (الف) دیدن اینکه چه مهاجرت‌هایی اعمال شده (ب) دیدن SQL یک مهاجرت بدون اجرا (ج) ساخت فایل مهاجرت (د) برگرداندن اپ به وضعیت اولیه</p>'
         '<p><strong>پاسخ:</strong> الف → showmigrations • ب → sqlmigrate app 000X • ج → makemigrations • د → migrate app zero</p>'),
        ('تمرین ۲ — تحلیل فایل مهاجرت',
         '<p><strong>سوال:</strong> در فایل مهاجرت، dependencies و operations چه می‌کنند؟</p>'
         '<p><strong>پاسخ:</strong> dependencies = «اول کدام مهاجرت‌ها باید اعمال شوند» (زنجیره ترتیب و هماهنگی بین اپ‌ها) • operations = فهرست تغییرات (ساخت مدل/فیلد، حذف، تغییر نام و...) که به SQL ترجمه می‌شوند.</p>'),
        ('تمرین ۳ — سناریوی تیمی',
         '<p><strong>سناریو:</strong> هم‌تیمی‌تان مهاجرت 0005 را ساخته و push کرده؛ شما هم روی همان اپ 0005 خودتان را ساخته‌اید. بعد از pull چه می‌بینید و چه می‌کنید؟</p>'
         '<p><strong>پاسخ:</strong> دو فایل با شماره یکسان/شاخه متفاوت → خطای conflict موقع migrate. راه‌حل: <code class="inline-code">makemigrations --merge</code> (فایل 0006_merge ساخته می‌شود) و بعد migrate. در تیم‌های حرفه‌ای این کار روزمره است.</p>'),
    ],
    quiz=[
        dict(q='تفاوت makemigrations و migrate چیست؟',
             opts=['فرقی ندارند', 'makemigrations فایل مهاجرت را می‌سازد؛ migrate آن را روی پایگاه داده اعمال می‌کند',
                   'migrate فایل را می‌سازد؛ makemigrations اعمال می‌کند', 'هر دو فقط وضعیت را نشان می‌دهند'],
             ans='b', explain='اول ساخت فایل (makemigrations)، بعد اجرا روی دیتابیس (migrate). دو مرحله کاملاً جدا.'),
        dict(q='کدام فرمان SQL واقعی یک مهاجرت را بدون اجرا نشان می‌دهد؟',
             opts=['showmigrations', 'sqlmigrate', 'migrate --sql', 'dbshell'],
             ans='b', explain='sqlmigrate app 000X دقیقاً همان SELECT/ALTERهایی را چاپ می‌کند که migrate اجرا خواهد کرد.'),
        dict(q='بازگرداندن (unapply) مهاجرتی که یک فیلد اضافه کرده بود، چه اثری دارد؟',
             opts=['فقط تعریف فیلد حذف می‌شود، داده می‌ماند', 'ستون و همه داده‌های آن فیلد حذف می‌شوند',
                   'هیچ اثری روی داده ندارد', 'دیتابیس قفل می‌شود'],
             ans='b', explain='RemoveField یعنی DROP COLUMN — داده آن ستون برای همیشه می‌رود. برای همین در تولید با نسخه پشتیبان کار می‌کنند.'),
        dict(q='هنگام تغییر نام فیلد، makemigrations چه می‌پرسد و چرا مهم است؟',
             opts=['نام جدید را می‌پرسد؛ مهم نیست', 'می‌پرسد «تغییر نام است یا حذف+افزودن؟»؛ انتخاب غلط داده را می‌سوزاند',
                   'هیچ چیز نمی‌پرسد', 'رمز عبور می‌پرسد'],
             ans='b', explain='اگر «تغییر نام» را انتخاب کنید RenameField داده را حفظ می‌کند؛ انتخاب اشتباه، RemoveField+AddField می‌سازد و داده ستون حذف می‌شود.'),
        dict(q='فایل‌های پوشه migrations در گیت چه وضعیتی دارند؟',
             opts=['در gitignore گذاشته می‌شوند', 'کامیت می‌شوند؛ بخشی از تاریخچهٔ طرح پایگاه داده‌اند',
                   'فقط 0001_initial کامیت می‌شود', 'خود جنگو در سرور تولید می‌سازدشان'],
             ans='b', explain='مهاجرت‌ها کد پروژه‌اند؛ همه محیط‌ها (توسعه، تست، تولید) باید دقیقاً همان تاریخچه را اعمال کنند.'),
        dict(q='خطای «conflicting migrations» چه وقتی رخ می‌دهد و راه‌حلش چیست؟',
             opts=['وقتی دیتابیس خراب است؛ حذف db.sqlite3', 'وقتی دو شاخه مهاجرت هم‌زمان ساخته شود؛ makemigrations --merge',
                   'وقتی DEBUG=False است؛ True کردن', 'وقتی venv فعال نیست؛ فعال کردن'],
             ans='b', explain='در کار تیمی طبیعی است: دو نفر هر کدام مهاجرتی بر پایه یک والد می‌سازند. --merge یک مهاجرت ادغام بی‌خطر تولید می‌کند.'),
    ],
    project_title='تاریخچهٔ مدل وبلاگ',
    project_intro='مدل‌های وبلاگ را طی چند مرحله تکامل دهید و تاریخچه مهاجرت‌ها را مستند کنید.',
    project_checklist=[
        'مرحله ۱: افزودن summary و views_count به Post (هر کدام یک مهاجرت).',
        'مرحله ۲: تغییر نام body → content (با RenameField و حفظ داده).',
        'مرحله ۳: افزودن مدل Category و اتصال Post به آن (مهاجرت دو اپ یا یک اپ؟).',
        'با showmigrations وضعیت نهایی را چاپ و در یادداشت‌ها ذخیره کنید.',
        'یک بار rollback تا مرحله ۲ انجام دهید و دوباره forward بزنید.',
    ],
    project_callout=None,
    summary_items=[
        'چرخه طلایی: تغییر مدل → makemigrations → (بازبینی فایل) → migrate.',
        'showmigrations وضعیت و sqlmigrate پشت‌صحنه SQL را نشان می‌دهد.',
        'فایل مهاجرت = dependencies (ترتیب) + operations (تغییرات).',
        'rollback ممکن است ولی داده‌سوز؛ تغییر نام با RenameField امن است.',
        'مهاجرت‌ها در git کامیت می‌شوند؛ تعارض تیمی با --merge حل می‌شود.',
    ],
    golden='مهاجرت = گیتِ پایگاه داده: هر تغییر ساختار، یک کامیتِ قابل اعمال و قابل بازگشت.',
    faq=[
        ('در تولید چطور مهاجرت اعمال می‌شود؟',
         '<p>معمولاً در فرایند <span class="term" data-term="deployment">دیپلوی</span>: بعد از pull کردن کد جدید، <code class="inline-code">python manage.py migrate</code> اجرا می‌شود (فصل ۲۶ در اسکریپت استقرار می‌بینید). migrate هوشمند است: فقط مهاجرت‌های اعمال‌نشده را اجرا می‌کند.</p>'),
        ('makemigrations می‌گوید «No changes detected» ولی مدل را عوض کرده‌ام!',
         '<p>یا تغییر را ذخیره نکرده‌اید، یا در اپ اشتباهی نوشته‌اید، یا اپ در INSTALLED_APPS نیست. نام اپ را هم صریح بدهید: <code class="inline-code">makemigrations blog</code> تا پیام دقیق‌تر بگیرید.</p>'),
        ('__init__.py در پوشه migrations را حذف کردم؛ چه شود؟',
         '<p>بدون آن، پوشه یک پکیج پایتون نیست و جنگو مهاجرت‌ها را نمی‌بیند. یک فایل خالی __init__.py برگردانید (یا از git برگردانید).</p>'),
    ],
    next_step='لایه داده کامل شد. حالا در <strong>فصل ۶</strong> بدون نوشتن حتی یک خط HTML، یک پنل مدیریت حرفه‌ای برای همین مدل‌ها می‌سازیم: <span class="term" data-term="admin">Admin Panel</span>.',
),

# ================================================================ فصل ۶
dict(
    n=6, icon='🎛️', title='پنل مدیریت (Admin Panel)', cat=1, mins=80, lvl_label='مبتدی',
    hero_desc='ساخت <span class="term" data-term="superuser">ابرکاربر</span>، ثبت مدل‌ها در پنل، شخصی‌سازی با list_display، list_filter، search_fields و fieldsets — و آماده‌سازی پنل برای پروژه واقعی.',
    s1_intro='پنل ادمین یکی از «باتری‌های همراه» جنگو است: بدون نوشتن فرم و صفحه، رابط کامل CRUD برای مدل‌هایتان می‌سازد. تیم‌های محتوا ساعت‌ها با آن کار می‌کنند، پس حرفه‌ای ساختنش ارزش دارد.',
    objectives=[
        'با <code class="inline-code">createsuperuser</code> حساب مدیر بسازید و وارد <code class="inline-code">/admin/</code> شوید.',
        'مدل را با دکوریتور <span class="term" data-term="decorator">@register</span> یا تابع register ثبت کنید.',
        'فهرست را با list_display، list_filter، search_fields و list_editable شخصی‌سازی کنید.',
        'فرم ویرایش را با fieldsets و readonly_fields مرتب کنید.',
        'رابطه‌ها را با raw_id_fields، autocomplete و prepopulated_fields مدیریت کنید.',
    ],
    s1_position='<strong>جایگاه فصل:</strong> بعد از مدل‌ها (فصل ۴) و مهاجرت (فصل ۵). مجوزهای ریزتر پنل در فصل ۱۳ و فرم‌های پیشرفته در فصل ۱۱ می‌آید.',
    roadmap=[
        ('ورود به پنل', 'createsuperuser و اولین لاگین.'),
        ('ثبت مدل‌ها', 'register و ModelAdmin.'),
        ('شخصی‌سازی فهرست', 'list_display تا list_editable.'),
        ('شخصی‌سازی فرم', 'fieldsets، readonly و روابط هوشمند.'),
    ],
    mind_qs=[
        ('پنل ادمین از کجا می‌فهمد چه فیلدهایی نشان دهد؟',
         '<p>از خود <span class="term" data-term="model">مدل</span>! به‌صورت پیش‌فرض همه فیلدها را در فرم می‌آورد. هنر ما <strong>شخصی‌سازی</strong> است: کدام ستون‌ها در فهرست، کدام فیلترها، کدام فیلدها فقط‌خواندنی.</p>'),
        ('اگر هزاران پست داشته باشیم، جست‌وجوی پنل کند نمی‌شود؟',
         '<p>search_fields روی متن <strong>LIKE</strong> می‌زند که روی داده حجیم کند است. برای حجم بالا: <span class="term" data-term="db-index">ایندکس</span> روی فیلدهای جست‌وجوشونده (فصل ۲۷) یا اتصال جست‌وجوی تخصصی. برای شروع همین کافی است.</p>'),
        ('همه کاربران سایت باید به پنل دسترسی داشته باشند؟',
         '<p>نه! <span class="term" data-term="admin">پنل ادمین</span> مخصوص <strong>کاربران اداری</strong> است (is_staff=True). کاربر عادی سایت هیچ‌وقت وارد /admin/ نمی‌شود. سطح دسترسی‌ها فصل ۱۳ است.</p>'),
    ],
    prereq_intro='پیش‌نیازها:',
    prereq=[
        'مدل‌های فصل ۴ (Author, Post, Comment, Tag) با مهاجرت‌های اعمال‌شده.',
        'اپ‌های <code class="inline-code">django.contrib.admin</code> و <code class="inline-code">auth</code> در INSTALLED_APPS باشند (پیش‌فرض هستند).',
        'سرور توسعه در حال اجرا.',
        'چند رکورد نمونه در دیتابیس (از شل فصل ۴).',
    ],
    prereq_callout=None,
    concepts=[
        dict(h='۵.۱ ساخت ابرکاربر و ورود', body=[
            ('code', 'ساخت حساب مدیر', 'bash', '''python manage.py createsuperuser
# Username: admin
# Email: admin@example.com
# Password: ********'''),
            '<p>حالا <code class="inline-code">http://127.0.0.1:8000/admin/</code> را باز کنید و وارد شوید. فعلاً فقط Groupها و Userها هستند — چون مدل‌های خودمان را هنوز <strong>ثبت</strong> نکرده‌ایم.</p>',
            ('callout', 'info', 'ابرکاربر کیست؟',
             '<span class="term" data-term="superuser">ابرکاربر</span> کاربری با is_superuser=True است؛ یعنی همه <span class="term" data-term="permission">مجوزها</span> را دارد و همه مدل‌های ثبت‌شده را در پنل می‌بیند.'),
        ]),
        dict(h='۵.۲ ثبت مدل‌ها', body=[
            ('code', 'blog/admin.py', 'python', '''from django.contrib import admin

from .models import Author, Comment, Post, Tag


# روش ۱: دکوریتور (رایج‌ترین)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


# روش ۲: تابع register
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment)'''),
            '<p>رفرش کنید — بخش BLOG با چهار مدل ظاهر شد! کلاس خالی <code class="inline-code">PostAdmin(admin.ModelAdmin): pass</code> هم همین رفتار پیش‌فرض را دارد؛ ولی جایی است که از اینجا به بعد شخصی‌سازی می‌کنیم.</p>',
        ]),
        dict(h='۵.۳ شخصی‌سازی صفحه فهرست', body=[
            ('code', 'PostAdmin کامل', 'python', '''@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published", "created_at")
    list_filter = ("published", "created_at", "author")
    search_fields = ("title", "body")
    list_editable = ("published",)          # ویرایش سریع در همان فهرست
    list_per_page = 25
    date_hierarchy = "created_at"           # نوار پیمایش زمانی بالای فهرست
    ordering = ("-created_at",)'''),
            '<ul>'
            '<li><code class="inline-code">list_display</code> — ستون‌های جدول فهرست (می‌تواند متد هم باشد: <code class="inline-code">def preview(self, obj): return obj.body[:50]</code>).</li>'
            '<li><code class="inline-code">list_filter</code> — فیلترهای کناری؛ روی فیلدهای کم‌تنوع عالی است (بولی، تاریخ، FK).</li>'
            '<li><code class="inline-code">search_fields</code> — جعبه جست‌وجو (پسوند <code class="inline-code">__icontains</code> ضمنی).</li>'
            '<li><code class="inline-code">list_select_related = ("author",)</code> — جلوی کوئری <span class="term" data-term="n-plus-one">N+1</span> فهرست را می‌گیرد (فصل ۱۵).</li></ul>',
        ]),
        dict(h='۵.۴ شخصی‌سازی فرم ویرایش', body=[
            ('code', 'fieldsets و readonly', 'python', '''@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        ("محتوا", {"fields": ("title", "slug", "body", "summary")}),
        ("انتشار", {"fields": ("author", "published", "created_at")}),
        ("برچسب‌ها", {"fields": ("tags",), "classes": ("collapse",)}),
    )
    readonly_fields = ("created_at", "updated_at")
    prepopulated_fields = {"slug": ("title",)}   # ساخت خودکار slug از عنوان
    filter_horizontal = ("tags",)                # ویجت دوپنجره‌ای برای M2M'''),
            '<p>نتیجه: فرم ویرایش به بخش‌های تمیز تقسیم می‌شود، فیلدهای زمانی دستی تغییر نمی‌کنند و اسلاگ خودکار از عنوان ساخته می‌شود (فارسی‌اش هم با allow_unicode در SlugField کار می‌کند).</p>',
        ]),
        dict(h='۵.۵ روابط، Inline و اکشن‌ها', body=[
            ('code', 'Inline و اکشن سفارشی', 'python', '''class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0                 # چند فرم خالی اضافه نشان نده


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = (CommentInline,)
    actions = ("publish_posts",)

    @admin.action(description="انتخاب‌شده‌ها را منتشر کن")
    def publish_posts(self, request, queryset):
        updated = queryset.update(published=True)
        self.message_user(request, f"{updated} پست منتشر شد.")'''),
            '<p>با <strong>Inline</strong>، کامنت‌های هر پست داخل صفحه ویرایش همان پست مدیریت می‌شوند. با <strong>اکشن</strong>، عملیات گروهی (انتشار دسته‌جمعی) اضافه می‌کنیم.</p>',
        ]),
    ],
    example_intro='پنل کامل یک فروشگاه کتاب — جمع همه تکنیک‌ها:',
    example=[
        ('code', 'books/admin.py', 'python', '''from django.contrib import admin

from .models import Book, Publisher, Tag


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ("name", "books_count")
    search_fields = ("name",)

    @admin.display(description="تعداد کتاب‌ها", ordering="cnt")
    def books_count(self, obj):
        return obj.books.count()


class BookTagInline(admin.TabularInline):
    model = Book.tags.through
    extra = 0


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "publisher", "price", "published_year")
    list_filter = ("publisher", "published_year")
    search_fields = ("title",)
    list_select_related = ("publisher",)
    autocomplete_fields = ("publisher",)    # نیاز به search_fields در PublisherAdmin
    inlines = (BookTagInline,)

    fieldsets = (
        (None, {"fields": ("title", "publisher")}),
        ("قیمت‌گذاری", {"fields": ("price", "published_year")}),
    )


admin.site.unregister(Tag)   # مدیریت برچسب‌ها فقط از inline کتاب‌ها'''),
        '<p>به <code class="inline-code">list_select_related</code> و <code class="inline-code">autocomplete_fields</code> دقت کنید — این‌ها تفاوت پنل «کارراه‌انداز» و پنل «حرفه‌ای» هستند.</p>',
    ],
    workshop_intro='پنل وبلاگ خودتان را بسازید:',
    workshop_tasks=[
        '<strong>کارگاه ۱:</strong> مدل‌های blog را ثبت کنید؛ برای Post: list_display (عنوان، نویسنده، published، تاریخ)، list_filter و search_fields بگذارید.',
        '<strong>کارگاه ۲:</strong> کامنت‌ها را به‌صورت Inline در صفحه ویرایش پست نشان دهید و یک اکشن «تأیید کامنت‌های انتخاب‌شده» بنویسید (فیلد approved را اول به Comment اضافه کنید).',
        '<strong>کارگاه ۳:</strong> Author را طوری ثبت کنید که در فرم Post، به‌جای dropdown معمولی، autocomplete با جست‌وجوی نام نشان داده شود.',
    ],
    workshop_answers=[
        ('پاسخ کارگاه ۱',
         '<div class="code-box"><div class="code-head"><span>blog/admin.py</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">@admin.register(Post)\nclass PostAdmin(admin.ModelAdmin):\n    list_display = ("title", "author", "published", "created_at")\n    list_filter = ("published", "created_at")\n    search_fields = ("title", "body")\n    list_select_related = ("author",)\n    prepopulated_fields = {"slug": ("title",)}</code></pre></div>'),
        ('پاسخ کارگاه ۲',
         '<div class="code-box"><div class="code-head"><span>Inline + اکشن</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">class CommentInline(admin.TabularInline):\n    model = Comment\n    extra = 0\n\n\n@admin.action(description="تأیید کامنت‌های انتخاب‌شده")\ndef approve_comments(modeladmin, request, queryset):\n    n = queryset.update(approved=True)\n    modeladmin.message_user(request, f"{n} کامنت تأیید شد.")\n\n\n@admin.register(Comment)\nclass CommentAdmin(admin.ModelAdmin):\n    list_display = ("post", "approved", "created_at")\n    actions = (approve_comments,)</code></pre></div>'
         '<p>یادتان نرود فیلد <code class="inline-code">approved = BooleanField(default=False)</code> را به مدل اضافه و مهاجرت بزنید.</p>'),
        ('پاسخ کارگاه ۳',
         '<div class="code-box"><div class="code-head"><span>autocomplete برای author</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">@admin.register(Author)\nclass AuthorAdmin(admin.ModelAdmin):\n    search_fields = ("name",)      # ← شرط لازم autocomplete\n\n\n@admin.register(Post)\nclass PostAdmin(admin.ModelAdmin):\n    autocomplete_fields = ("author",)\n    # ...</code></pre></div>'
         '<p>autocomplete_fields فقط روی FK/M2O و M2M کار می‌کند و مدل مقصد <strong>باید</strong> search_fields داشته باشد، وگرنه خطای سیستم‌چک می‌گیرید.</p>'),
    ],
    errors=[
        ('در پنل به‌جای عنوان، <code>Post object (1)</code> می‌بینم',
         'مدل <code class="inline-code">__str__</code> ندارد (یا رشته برنمی‌گرداند). متد __str__ را اضافه کنید — تغییرش نیاز به مهاجرت ندارد.'),
        ('خطای <code>\'PostAdmin.list_display[1]\', \'author\' is not a callable</code>',
         'در list_display نامی نوشته‌اید که نه فیلد مدل است نه متد/خاصیت ادمین. تایپو را چک کنید؛ برای فیلدِ رابطه هم <code class="inline-code">"author__name"</code> مجاز نیست — متد کوچک بنویسید.'),
        ('خطای E035 برای autocomplete_fields',
         'مدل مقصد search_fields ندارد. اول در ModelAdminِ مدل مقصد search_fields بگذارید.'),
        ('ورود به /admin/ با حساب کاربری عادی رد می‌شود',
         'پنل فقط کاربران is_staff را راه می‌دهد. با createsuperuser حساب بسازید یا در پنل (از راه کاربر دیگر) تیک staff status را بزنید.'),
        ('رمز ابرکاربر را فراموش کردم',
         'راه سریع: <code class="inline-code">python manage.py changepassword admin</code> یا ساخت ابرکاربر جدید با createsuperuser.'),
    ],
    errors_callout=None,
    exercises=[
        ('تمرین ۱ — انتخاب ابزار',
         '<p><strong>سوال:</strong> برای هر نیاز کدام ویژگی؟ (الف) ستون وضعیت در فهرست (ب) فیلتر بر اساس تاریخ (ج) جست‌وجو در عنوان (د) گروه‌بندی فیلدهای فرم (ه) ویرایش سریع published بدون ورود به فرم</p>'
         '<p><strong>پاسخ:</strong> الف → list_display • ب → list_filter یا date_hierarchy • ج → search_fields • د → fieldsets • ه → list_editable</p>'),
        ('تمرین ۲ — متد در list_display',
         '<p><strong>سوال:</strong> ستونی «کوتاهه متن» (۵۰ حرف اول body) در فهرست پست‌ها بسازید.</p>'
         '<p><strong>پاسخ:</strong> در PostAdmin: <code class="inline-code">@admin.display(description="خلاصه") def excerpt(self, obj): return obj.body[:50]</code> و اضافه کردن "excerpt" به list_display.</p>'),
        ('تمرین ۳ — امنیت',
         '<p><strong>سوال:</strong> چرا readonly_fields برای created_at مهم است؟</p>'
         '<p><strong>پاسخ:</strong> چون auto_now_add فقط موقع <strong>ایجاد</strong> مقدار می‌دهد؛ در ویرایش، فیلد قابل ویرایش بودنش اجازه دست‌کاری تاریخ ایجاد را به کاربر ادمین می‌دهد. readonly یعنی داده سیستمی دست‌نخوردنی بماند.</p>'),
    ],
    quiz=[
        dict(q='کدام فرمان حساب ابرکاربر می‌سازد؟',
             opts=['python manage.py createadmin', 'python manage.py createsuperuser',
                   'django-admin superuser', 'python manage.py adduser'],
             ans='b', explain='createsuperuser کاربری با is_staff و is_superuser می‌سازد که کلید ورود به /admin/ است.'),
        dict(q='برای نمایش ستون‌های دلخواه در فهرست پنل از چه استفاده می‌شود؟',
             opts=['list_filter', 'list_display', 'fieldsets', 'search_fields'],
             ans='b', explain='list_display ستون‌های جدول فهرست را تعیین می‌کند؛ فیلد، متد یا خاصیت قابل قبول است.'),
        dict(q='شرط استفاده از autocomplete_fields روی یک ForeignKey چیست؟',
             opts=['مدل مقصد list_display داشته باشد', 'مدل مقصد search_fields داشته باشد',
                   'فیلد unique باشد', 'مدل مقصد Inline داشته باشد'],
             ans='b', explain='ویجت autocomplete با همان search_fields مدل مقصد جست‌وجو می‌کند؛ بدون آن خطای سیستم‌چک E035 می‌گیرید.'),
        dict(q='کدام گزینه کامنت‌های یک پست را داخل صفحه ویرایش خودِ پست مدیریت می‌کند؟',
             opts=['list_editable', 'TabularInline', 'fieldsets', 'actions'],
             ans='b', explain='Inline (Tabular یا Stacked) فرم‌های مدل وابسته را درون صفحه مدل والد جاسازی می‌کند.'),
        dict(q='prepopulated_fields = {"slug": ("title",)} چه می‌کند؟',
             opts=['slug را از title در دیتابیس کپی می‌کند', 'در فرم، slug را به‌طور زنده از روی title می‌سازد',
                   'عنوان را از slug می‌سازد', 'فیلد slug را فقط‌خواندنی می‌کند'],
             ans='b', explain='جاوااسکریپت سمت فرم، هم‌زمان با تایپ عنوان، اسلاگ پیشنهادی (slugify‌شده) تولید می‌کند؛ کاربر می‌تواند اصلاحش کند.'),
        dict(q='کاربران عادی سایت (بدون is_staff) چه دسترسی به /admin/ دارند؟',
             opts=['فقط خواندن', 'فقط مدل‌های خودشان', 'هیچ — صفحه ورود ردشان می‌کند', 'دسترسی کامل مثل ابرکاربر'],
             ans='c', explain='پنل ادمین مخصوص کاربران staff است. کاربر عادی حتی با رمز درست، پیام «permission denied» می‌گیرد.'),
    ],
    project_title='پنل مدیریت وبلاگ حرفه‌ای',
    project_intro='پنلی بسازید که یک ویراستار غیرفنی بتواند بدون آموزش کل سایت را مدیریت کند.',
    project_checklist=[
        'ثبت همه مدل‌ها با ModelAdmin اختصاصی.',
        'Post: فهرست ۵ ستونی، فیلتر انتشار، جست‌وجو، date_hierarchy، fieldsets دوبخشی و slug خودکار.',
        'Comment: Inline در پست + اکشن تأیید/رد دسته‌جمعی.',
        'Author: autocomplete و نمایش تعداد پست‌ها در فهرست.',
        'یک کاربر «ویراستار» (غیر ابرکاربر) بسازید و با آن وارد شوید؛ چه مدل‌هایی را می‌بیند؟ (اشاره به فصل ۱۳)',
    ],
    project_callout=('tip', 'معیار موفقیت',
        'اگر توانستید بدون رفتن به شل، یک پست کامل با کامنت و برچسب بسازید و منتشر کنید — پروژه موفق است.'),
    summary_items=[
        'با createsuperuser وارد پنل آمادهٔ <code class="inline-code">/admin/</code> شدیم.',
        'مدل‌ها را با @admin.register ثبت کردیم.',
        'فهرست را با list_display/list_filter/search_fields/list_editable شخصی‌سازی کردیم.',
        'فرم را با fieldsets/readonly_fields/prepopulated_fields مرتب کردیم.',
        'Inline و اکشن‌های گروهی ساختیم و نکات کارایی (list_select_related، autocomplete) را دیدیم.',
    ],
    golden='پنل ادمین خوب = رابطی که تیم محتوا بدون برنامه‌نویس بتواند با آن کار کند.',
    faq=[
        ('می‌توانم ظاهر پنل را عوض کنم؟',
         '<p>بله: تغییر عنوان/هدر با <code class="inline-code">admin.site.site_header</code>، و برای تغییرات اساسی پکیج‌هایی مثل Jazzmin یا Grappelli قالب پنل را عوض می‌کنند. در شروع کار لازم نیست.</p>'),
        ('پنل ادمین برای سایت‌های بزرگ مناسب است؟',
         '<p>برای مدیریت محتوا بله؛ هزاران سایت تولیدی از آن استفاده می‌کنند. فقط برای داده حجیم، search/filter را هوشمندانه تنظیم کنید و در صورت نیاز داشبوردهای اختصاصی (با CBVها) بسازید.</p>'),
        ('چطور به بعضی کاربران فقط دسترسی یک مدل بدهم؟',
         '<p>با Group و <span class="term" data-term="permission">مجوزها</span> — دقیقاً موضوع فصل ۱۳. ادمین به‌طور خودکار فقط مدل‌هایی را نشان می‌دهد که کاربر مجوزشان را دارد.</p>'),
    ],
    next_step='داده‌ها ساخت و مدیریت شدند؛ حالا در <strong>فصل ۷</strong> یاد می‌گیریم URLهای زیبا و پویا (مثل <code class="inline-code">/blog/hello-django/</code>) بسازیم تا این داده‌ها به صفحه‌های عمومی برسند.',
),
]
