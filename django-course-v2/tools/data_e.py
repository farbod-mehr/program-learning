# -*- coding: utf-8 -*-
"""داده محتوای فصل‌های ۲۱ تا ۲۵ — دیباگ، DRF مقدماتی و پیشرفته، سلری، بومی‌سازی"""

CHAPTERS = [

# ================================================================ فصل ۲۱
dict(
    n=21, icon='🐞', title='اشکال‌زدایی (Debug) و لاگ‌گیری', cat=4, mins=80, lvl_label='متوسط',
    hero_desc='روش‌های حرفه‌ای یافتن ریشه خطا: خواندن <span class="term" data-term="traceback">Traceback</span>، نقشه راه <span class="term" data-term="debug">DEBUG</span>، ابزار <span class="term" data-term="pdb">pdb</span>، <span class="term" data-term="debug-toolbar">Debug Toolbar</span>، پیکربندی <span class="term" data-term="logging">لاگ</span> و صفحه‌های خطای سفارشی.',
    s1_intro='باگ از بین نمی‌رود؛ فقط پنهان می‌شود تا بدترین لحظه ظاهر شود! در این فصل «متدولوژی شکار باگ» یاد می‌گیرید: از خواندن علمی خطاها تا ابزارهای تعاملی و لاگ‌گیری استاندارد.',
    objectives=[
        'یک Traceback را از پایین به بالا بخوانید و خط مقصر را بیابید.',
        'با DEBUG و صفحات خطای جنگو کار کنید و بدانید چرا در تولید باید خاموش باشد.',
        'با pdb/breakpoint() اجرای برنامه را گام‌به‌گام بازرسی کنید.',
        'django-debug-toolbar نصب کنید و کوئری‌ها را زنده ببینید.',
        'پیکربندی استاندارد LOGGING بسازید و صفحه‌های 404/500 سفارشی بگذارید.',
    ],
    s1_position='<strong>جایگاه فصل:</strong> ابزار پشتیبان همه فصل‌های قبل و بعد؛ لاگ‌ها در استقرار (فصل ۲۶) حیاتی می‌شوند.',
    roadmap=[
        ('خواندن خطا', 'Traceback و انواع استثناها.'),
        ('ابزارهای تعاملی', 'DEBUG، pdb و Toolbar.'),
        ('لاگ‌گیری', 'پیکربندی LOGGING استاندارد.'),
        ('خطا در تولید', 'صفحات سفارشی و گزارش‌گیری.'),
    ],
    mind_qs=[
        ('چرا DEBUG=True در تولید فاجعه است؟',
         '<p>صفحه خطای DEBUG همه‌چیز را لو می‌دهد: مسیر فایل‌ها، متغیرها، <strong>تنظیمات (گاهی SECRET_KEY!)</strong> و تکه‌های کد. مهاجم با یک خطای ساده نقشه کامل پروژه را می‌گیرد. جنگو هم با DEBUG=False و بدون ALLOWED_HOSTS درست، اساساً سرویس نمی‌دهد.</p>'),
        ('Traceback را از کجا بخوانیم؟',
         '<p>از <strong>پایین</strong> به بالا! آخرین فریم، محل واقعی انفجار است؛ فریم‌های بالایی مسیر رسیدن به آن. بعد پیام استثنا (خط آخر) را بخوانید: Usually همان پاسخ است.</p>'),
        ('print یا logging؟',
         '<p>print برای دیباگ لحظه‌ای خوب است ولی در تولید: سطح ندارد، فیلتر ندارد، مقصد ندارد (فایل/سرویس) و تاریخچه ندارد. logging استاندارد پایتون همه را می‌دهد — با DEBUG/INFO/WARNING/ERROR و هندلرهای متفاوت.</p>'),
    ],
    prereq_intro='پیش‌نیازها:',
    prereq=[
        'پروژه وبلاگ در حال اجرا (هر باگی که خودتان دارید، طلای این فصل است!).',
        'فصل ۱۷: میدلور زمان‌سنج برای ابزار اندازه‌گیری.',
        'فصل ۲۰: تست‌ها به‌عنوان ابزار بازتولید باگ.',
        'آشنایی با ترمینال و خواندن انگلیسی خطاها.',
    ],
    prereq_callout=None,
    concepts=[
        dict(h='۵.۱ آناتومی یک خطای جنگو', body=[
            ('code', 'یک Traceback واقعی (با DEBUG=True)', 'text', '''Internal Server Error: /blog/post/99/
Traceback (most recent call last):
  File ".../django/core/handlers/exception.py", line 55, in inner
    response = get_response(request)
  File ".../blog/views.py", line 42, in post_detail
    post = Post.objects.get(slug=slug)
  File ".../django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
django.core.exceptions.ObjectDoesNotExist → DoesNotExist:
Post matching query does not exist.
   ↑ فریم مقصر            ↑ نوع استثنا و پیام'''),
            '<p>ترتیب خواندن: ① خط آخر (نوع و پیام استثنا) ② پایین‌ترین فریم از <strong>کد خودتان</strong> (blog/views.py:42) ③ بازسازی ذهنی: get به‌جای get_object_or_404 → برای اسلاگ ناموجود DoesNotExist → ۵۰۰!</p>',
            '<ul>'
            '<li><strong>استثناهای رایج:</strong> DoesNotExist (یافت نشد)، IntegrityError (نقض محدودیت دیتابیس مثل یکتایی)، ValidationError (فرم/مدل)، TemplateSyntaxError (خطای قالب — با شماره خط قالب)، ModuleNotFoundError (نصب/مسیر).</li></ul>',
            ('callout', 'tip', 'قانون ۵۰۰ها',
             'هر 500 یعنی استثنای مدیریت‌نشده در کد شما. 4xxها معمولاً خطای «کاربر» هستند (یافت نشد، دسترسی ممنوع) و 5xxها خطای «برنامه».'),
        ]),
        dict(h='۵.۲ ابزار تعاملی: pdb و breakpoint()', body=[
            ('code', 'توقف وسط اجرا و بازرسی زنده', 'python', '''def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    breakpoint()          # ← اجرای برنامه همین‌جا می‌ایستد (Python 3.7+)
    comments = post.comments.all()
    return render(request, "blog/post_detail.html", {...})

# در ترمینال:
# (Pdb) post                 → نمایش شیء
# (Pdb) post.title           → بررسی صفت
# (Pdb) comments.count()     → اجرای کوئری زنده
# (Pdb) request.user         → چه کسی درخواست داده
# (Pdb) n  → خط بعد  |  s → ورود به تابع  |  c → ادامه  |  q → خروج'''),
            ('code', 'در قالب و شل هم می‌شود', 'python', '''# داخل django shell:
python manage.py shell
>>> from blog.models import Post
>>> breakpoint()      # یا از debug() هم استفاده کنید

# در تست (فصل ۲۰) برای دیدن وضعیت لحظه شکست:
def test_x(self):
    breakpoint()'''),
        ]),
        dict(h='۵.۳ django-debug-toolbar', body=[
            ('code', 'نصب (فقط توسعه!)', 'python', '''# pip install django-debug-toolbar
INSTALLED_APPS += ["debug_toolbar"]
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
INTERNAL_IPS = ["127.0.0.1"]

# urls.py — فقط در توسعه:
if settings.DEBUG:
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]'''),
            '<p>نوار کنار مرورگر این‌ها را زنده نشان می‌دهد: <strong>SQL</strong> (تعداد و متن کوئری‌ها + زمان)، زمان هر بخش، قالب‌های رندرشده، سیگنال‌ها، تنظیمات، نشست. بهترین ابزار یافتن N+1 در عمل!</p>',
            ('callout', 'danger', 'هرگز در تولید نصب نماند',
             'Toolbar کل SQL و تنظیمات را به مرورگر می‌دهد. در requirements تولید جدا کنید (فصل ۲۶: requirements-dev.txt) و مطمئن شوید DEBUG=False آن را بی‌اثر می‌کند.'),
        ]),
        dict(h='۵.۴ پیکربندی LOGGING استاندارد', body=[
            ('code', 'settings.py', 'python', '''LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {"format": "{levelname} {asctime} {name} {message}",
                   "style": "{"},
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler",
                    "formatter": "simple"},
        "file": {"class": "logging.handlers.RotatingFileHandler",
                 "filename": BASE_DIR / "logs" / "app.log",
                 "maxBytes": 1024 * 1024 * 5,   # ۵MB
                 "backupCount": 3,
                 "formatter": "simple"},
    },
    "loggers": {
        "django": {"handlers": ["console"], "level": "WARNING"},
        "django.request": {"handlers": ["file"], "level": "ERROR"},
        "blog": {"handlers": ["console", "file"], "level": "DEBUG"},
    },
}'''),
            ('code', 'استفاده در کد', 'python', '''import logging

logger = logging.getLogger(__name__)   # → logger "blog.views"


def publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    logger.info("انتشار پست %s توسط %s", post.pk, request.user)
    try:
        send_notification(post)
    except Exception:
        logger.exception("خطا در ارسال اعلان پست %s", post.pk)  # + Traceback
        # نمی‌گذاریم اعلان ناموفق، انتشار را بشکند'''),
            '<ul>'
            '<li><strong>logger.exception</strong> = error + ثبت خودکار Traceback — در except بهترین انتخاب.</li>'
            '<li>سطح‌ها: DEBUG (جزئیات دیباگ) < INFO (رویداد عادی) < WARNING (قابل توجه) < ERROR (شکست عملیات) < CRITICAL.</li>'
            '<li>هرگز داده حساس (رمز، توکن) لاگ نکنید!</li></ul>',
        ]),
        dict(h='۵.۵ خطاها در تولید: صفحات سفارشی و گزارش‌گیری', body=[
            ('code', 'قالب‌های خطا (ریشه templates/)', 'html', '''{# templates/404.html #}
{% extends "base.html" %}
{% block content %}
<h1>۴۰۴ — صفحه پیدا نشد 🤷</h1>
<p>شاید نشانی عوض شده. از <a href="{% url \'blog:list\' %}">فهرست</a> شروع کنید.</p>
{% endblock %}

{# templates/500.html — قالب‌گیر سنگین استفاده نکنید #}'''),
            ('code', 'DEBUG=False در تولید', 'python', '''DEBUG = False                        # صفحات خطای سفارشی فعال شوند
ALLOWED_HOSTS = ["example.com", "www.example.com"]

ADMINS = [("Admin", "admin@example.com")]   # ایمیل خطای 500
# EMAIL_BACKEND واقعی تنظیم شود (فصل ۲۴ با سلری)'''),
            ('callout', 'info', 'Sentry و دوستان',
             'در پروژه جدی، سرویس‌هایی مثل <strong>Sentry</strong> هر استثنا را با Traceback کامل، بافت درخواست و کاربر گزارش می‌کنند و گروه‌بندی/هشدار می‌دهند. نصب: pip install sentry-sdk + sentry_sdk.init(dsn=...) در settings.'),
        ]),
    ],
    example_intro='شکار یک باگ واقعی از گزارش کاربر تا اصلاح — گام‌به‌گام:',
    example=[
        ('code', 'گزارش کاربر', 'text', '''«وقتی روی پست کلیک می‌کنم گاهی صفحه سفید خطا می‌دهد.
 دوباره رفتم درست شد!»

→ ۵۰۰ مقطعی = احتمال Race Condition یا داده ناسازگار. اول لاگ!'''),
        ('code', 'گام ۱: لاگ را ببینید (logs/app.log)', 'text', '''ERROR 2026-01-12 blog.views ...
Traceback:
  File ".../blog/views.py", line 58, in post_detail
    author_profile = post.author.user.profile
AttributeError: \'User\' object has no attribute \'profile\''''),
        ('code', 'گام ۲: بازتولید با تست (فصل ۲۰)', 'python', '''def test_detail_without_profile(self):
    u = User.objects.create_user("noprofile", password="p")
    a = Author.objects.create(name="A", user=u)   # پروفایل نساختیم
    post = Post.objects.create(..., author=a, published=True)
    r = self.client.get(post.get_absolute_url())
    self.assertEqual(r.status_code, 200)          # ← فعلاً FAIL (قرمز!)'''),
        ('code', 'گام ۳: اصلاح ریشه‌ای', 'python', '''# ویو: به‌جای دسترسی مستقیم، با احتیاط:
author_profile = getattr(post.author.user, "profile", None)

# بهتر: سیگنال post_save روی User (فصل ۱۶) که پروفایل را
# «همیشه» می‌سازد → ریشه مشکل (داده ناسازگار) حذف می‌شود.

# مهاجرت داده برای کاربران موجود بدون پروفایل (فصل ۷/۱۵):
def create_missing_profiles(apps, schema_editor):
    User = apps.get_model("auth", "User")
    Profile = apps.get_model("accounts", "Profile")
    for u in User.objects.all():
        Profile.objects.get_or_create(user=u)'''),
        ('code', 'گام ۴: تست سبز + لاگ تأیید', 'text', '''python manage.py test blog.tests.test_profile → OK
دیپلوی. در لاگ دیگر AttributeError ثبت نمی‌شود. ✅

درس: گزارش مبهم ← لاگ دقیق ← تست بازتولید ← اصلاح ریشه ← تست سبز'''),
    ],
    workshop_intro='جعبه‌ابزار دیباگ خودتان را کامل کنید:',
    workshop_tasks=[
        '<strong>کارگاه ۱:</strong> Debug Toolbar را نصب کنید و در صفحه فهرست پست‌ها تعداد کوئری‌ها را ببینید. یک N+1 پیدا و با select_related رفعش کنید (قبل/بعد را اسکرین‌شات بگیرید).',
        '<strong>کارگاه ۲:</strong> LOGGING مفهوم ۵.۴ را پیاده کنید؛ سه لاگ (info در ورود، warning در فرم نامعتبر، exception در یک try) بگذارید و خروجی console و فایل را ببینید.',
        '<strong>کارگاه ۳:</strong> یک باگ عمدی بسازید (AttributeError در ویو)، با DEBUG=True صفحه خطا را تحلیل کنید، سپس DEBUG=False بگذارید و صفحه 404/500 سفارشی خودتان را تست کنید.',
    ],
    workshop_answers=[
        ('پاسخ کارگاه ۱',
         '<p>مثال واقعی: صفحه فهرست با ۱۰ پست، پنل SQL عدد <strong>۱۱ یا ۲۱</strong> کوئری را نشان می‌دهد (۱ برای فهرست + ۱/۲ برای هر author). در ویو:</p>'
         '<div class="code-box"><div class="code-head"><span>رفع N+1</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python"># قبل\nposts = Post.objects.filter(published=True)\n\n# بعد — همان ۲ کوئری برای هر تعداد پست\nposts = (Post.objects.filter(published=True)\n         .select_related("author", "author__user")\n         .prefetch_related("tags"))</code></pre></div>'
         '<p>در Toolbar → SQL زمان کل هم می‌افتد (مثلاً ۴۵ms → ۸ms). این همان مهارت فصل ۱۵ است که با ابزار فصل ۲۱ <strong>دیده</strong> می‌شود.</p>'),
        ('پاسخ کارگاه ۲',
         '<p>تنظیمات را عیناً از ۵.۴ کپی کنید؛ پوشه logs را بسازید و .gitignore کنید. نمونه خروجی فایل:</p>'
         '<div class="code-box"><div class="code-head"><span>logs/app.log</span><span class="lang">text</span></div><pre class="code"><code data-lang="text">INFO 2026-01-12 blog.views ورود کاربر ali\nWARNING 2026-01-12 blog.views فرم کامنت نامعتبر: {"text": ["..."]}\nERROR 2026-01-12 blog.tasks خطا در ارسال ایمیل\nTraceback (most recent call last): ...</code></pre></div>'
         '<p>نکته: logger درخواست‌های جنگو (django.request) هر 500 را خودش ERROR لاگ می‌کند — حتی بدون کد شما.</p>'),
        ('پاسخ کارگاه ۳',
         '<div class="code-box"><div class="code-head"><span>باگ عمدی و بررسی</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python"># views.py — عمداً:\nrequest.user.nonexistent_thing   # AttributeError!\n\n# با DEBUG=True: صفحه زرد جنگو با Traceback کامل\n# با DEBUG=False: قالب 500.html شما\n\n# تست صفحه خطای سفارشی:\nfrom django.test import TestCase, override_settings\n\n\n@override_settings(DEBUG=False, ALLOWED_HOSTS=["testserver"])\nclass ErrorPageTest(TestCase):\n    def test_404_page(self):\n        r = self.client.get("/no-such-page/")\n        self.assertEqual(r.status_code, 404)\n        self.assertTemplateUsed(r, "404.html")</code></pre></div>'
         '<p>دقت کنید: در تست باید DEBUG=False شود چون پیش‌فرض تست True است و صفحه سفارشی را دور می‌زند.</p>'),
    ],
    errors=[
        ('خطای ۵۰۰ بدون هیچ توضیحی در تولید',
         'DEBUG=False و لاگ تنظیم نشده! هیچ چیز را حدس نزنید: LOGGING را با هندلر django.request → فایل فعال کنید؛ صفحه خطا برای کاربر، Traceback برای شما.'),
        ('DisallowedHost / Invalid HTTP_HOST header',
         'دامنه‌ای که با آن باز شده در ALLOWED_HOSTS نیست. در توسعه ["localhost", "127.0.0.1"] و در تولید دامنه‌های واقعی. هرگز ["*"] در تولید.'),
        ('breakpoint() در تولید فریز می‌کند',
         'pdb منتظر ورودی ترمینال می‌ایستد و ورکر قفل می‌شود! هیچ‌وقت breakpoint در کد دیپلوی‌شده نگذارید؛ قبل از دیپلوی grep کنید: <code class="inline-code">grep -rn "breakpoint\\|pdb" --include="*.py" .</code>.'),
        ('خطاهای ایمیل نمی‌شوند (ADMINS)',
         'EMAIL_BACKEND پیش‌فرض کنسول است! برای ایمیل واقعی smtp را تنظیم کنید (فصل ۲۴) و SERVER_EMAIL را معتبر بگذارید.'),
        ('Toolbar نمایش داده نمی‌شود',
         'INTERNAL_IPS شامل IP شما نیست (در داکر IP متفاوت است — از request.META["REMOTE_ADDR"] لاگ بگیرید)، یا {% debug_toolbar %}/میدلور جا افتاده.'),
    ],
    errors_callout=None,
    exercises=[
        ('تمرین ۱ — تشخیص از پیام',
         '<p><strong>سوال:</strong> علت احتمالی هر پیام؟ (الف) <code class="inline-code">UNIQUE constraint failed: blog_post.slug</code> (ب) <code class="inline-code">Reverse for \'detail\' with arguments \'()\' not found</code> (ج) <code class="inline-code">TemplateDoesNotExist: blog/post_lst.html</code> (د) <code class="inline-code">MultiValueDictKeyError: \'title\'</code></p>'
         '<p><strong>پاسخ:</strong> الف → slug تکراری ذخیره شده (IntegrityError — فصل ۶) • ب → args خالی به url برگردانده‌اید (اسلاگ/آی‌دی جا افتاده) • ج → غلط تایپی نام قالب • د → کلید در request.POST نیست (فرم فیلد title را نفرستاده یا GET بوده).</p>'),
        ('تمرین ۲ — انتخاب ابزار',
         '<p><strong>سوال:</strong> برای هر وضعیت کدام ابزار؟ (الف) «کوئری‌های این صفحه چندتاست؟» (ب) «مقدار این متغیر وسط تابع چیست؟» (ج) «در تولید چه خطاهایی رخ داده؟» (د) «این باگ را چطور همیشه نگهبانی کنم؟»</p>'
         '<p><strong>پاسخ:</strong> الف → Debug Toolbar • ب → breakpoint()/pdb • ج → LOGGING فایل + Sentry • د → تست بازتولید (فصل ۲۰، تمرین ۳).</p>'),
        ('تمرین ۳ — سطح لاگ',
         '<p><strong>سناریو:</strong> برای هر رویداد کدام سطح؟ (الف) کاربر با رمز غلط تلاش کرد (ب) اتصال به سرویس ایمیل ناموفق بود ولی عملیات اصلی انجام شد (ج) پرداخت ناموفق و سفارش نصفه ماند (د) مقدار یک متغیر در حلقه برای دیباگ</p>'
         '<p><strong>پاسخ:</strong> الف → WARNING (امنیتی/قابل توجه) • ب → ERROR یا WARNING با exception (بستگی به اهمیت اعلان) • ج → CRITICAL/ERROR فوری + هشدار • د → DEBUG (فقط توسعه).</p>'),
    ],
    quiz=[
        dict(q='Traceback را از کجا شروع به خواندن می‌کنیم؟',
             opts=['از بالای فایل', 'از خط آخر (پیام استثنا) و پایین‌ترین فریم کد خودمان',
                   'از وسط', 'فرقی نمی‌کند'],
             ans='b', explain='پیام استثنا «چه شد» و آخرین فریم کد شما «کجا شد» را می‌گوید؛ فریم‌های فریم‌ورک معمولاً نویز مسیرند.'),
        dict(q='چرا DEBUG=True در تولید خطرناک است؟',
             opts=['کند است', 'اطلاعات حساس (تنظیمات، مسیرها، متغیرها) را در صفحه خطا لو می‌دهد',
                   'لاگ نمی‌گیرد', 'CSRF را غیرفعال می‌کند'],
             ans='b', explain='صفحه خطای DEBUG عملاً نقشه کامل پروژه را به هرکس نشان می‌دهد — گاهی شامل SECRET_KEY. در تولید همیشه False.'),
        dict(q='breakpoint() چه می‌کند؟',
             opts=['خطا می‌دهد', 'اجرا را متوقف و پوسته تعاملی pdb را باز می‌کند',
                   'لاگ می‌نویسد', 'تست را اجرا می‌کند'],
             ans='b', explain='معادل import pdb; pdb.set_trace() از پایتون ۳.۷ به بعد — برای بازرسی زنده متغیرها و گام‌زدن عالی است.'),
        dict(q='logger.exception چه فرقی با logger.error دارد؟',
             opts=['هیچ', 'Traceback فعلی را هم خودکار ثبت می‌کند',
                   'فقط در except کار نمی‌کند', 'سطحش بالاتر است'],
             ans='b', explain='exception = error + stack trace خودکار؛ داخل بلوک except همیشه انتخاب بهتری است.'),
        dict(q='پنل SQL در Debug Toolbar بیشتر برای چیست؟',
             opts=['دیدن قالب‌ها', 'شمارش و بازرسی کوئری‌های اجراشده — یافتن N+1',
                   'تست فرم‌ها', 'مدیریت نشست'],
             ans='b', explain='تعداد کوئری غیرمنطقی نسبت به داده = بوی N+1؛ با select_related/prefetch_related رفع می‌شود (فصل ۱۵).'),
        dict(q='قالب صفحه خطای سفارشی ۵۰۰ کجا قرار می‌گیرد؟',
             opts=['هر جای templates', 'ریشه templates با نام دقیق 500.html',
                   'در static', 'باید در urls ثبت شود'],
             ans='b', explain='جنگو با DEBUG=False به‌ترتیب دنبال templates/500.html (و 404.html و...) می‌گردد؛ ثبت URL لازم نیست.'),
    ],
    project_title='سامانه پایداری وبلاگ',
    project_intro='پروژه را «قابل دیباگ و قابل اتکا» کنید.',
    project_checklist=[
        'پیکربندی LOGGING کامل (console در توسعه + فایل چرخشی در همه‌جا).',
        'نصب Debug Toolbar فقط در توسعه (requirements جدا یا شرط DEBUG).',
        'صفحات 404.html و 500.html سفارشی + تست با override_settings.',
        'سه نقطه لاگ معنادار در ویوها (ورود، انتشار، فرم نامعتبر).',
        'مستند «راهنمای باگ‌یابی» یک‌صفحه‌ای در docs پروژه خودتان.',
    ],
    project_callout=('tip', 'عادت حرفه‌ای',
        'هر باگی که حل می‌کنید: ① تست بازتولید ② لاگ مناسب در مسیر ③ یادداشت یک‌خطی در مستند باگ‌یابی. سه ماه بعد خودتان تشکر می‌کنید.'),
    summary_items=[
        'Traceback از پایین/پیام خوانده می‌شود؛ 5xx = باگ کد شما.',
        'DEBUG در تولید همیشه False + ALLOWED_HOSTS دقیق.',
        'breakpoint() برای بازرسی زنده؛ فقط در توسعه!',
        'Debug Toolbar = رادار کوئری‌ها و زمان‌ها.',
        'LOGGING با سطوح و هندلرها؛ logger.exception در except.',
    ],
    golden='باگ بازتولیدشدنی، باگ نیمه‌حل‌شده است: اول بازتولید (تست/لاگ)، بعد اصلاح.',
    faq=[
        ('Sentry رایگان است؟',
         '<p>پلن رایگان برای پروژه شخصی/کوچک کافی است و self-hosted هم دارد. جایگزین‌ها: Rollbar، Bugsnag. حتی بدون سرویس، لاگ فایل + ایمیل ADMINS شروع خوبی است.</p>'),
        ('چطور خطاهای جاوااسکریپت سمت کاربر را بفهمم؟',
         '<p>لاگ سمت سرور آن‌ها را نمی‌بیند! window.onerror را به یک endpoint گزارش‌گر بفرستید یا از Sentry Browser SDK استفاده کنید. برای شروع، کنسول DevTools کاربر را راهنمایی کنید.</p>'),
        ('لاگ‌ها در داکر/چند ورکر چطور مدیریت شوند؟',
         '<p>استاندارد: لاگ به stdout/stderr بنویسید (هندلر console) و جمع‌آوری فایل را به زیرساخت (docker logs، journalctl، Loki/ELK) بسپارید. RotatingFileHandler برای VPS تک‌سرور خوب است.</p>'),
    ],
    next_step='باگ‌ها را شکار کردیم؛ حالا در را برای دنیا باز می‌کنیم: <strong>فصل ۲۲</strong> — <span class="term" data-term="api">API</span> و <span class="term" data-term="drf">Django REST Framework</span>: سریالایزرها، APIView و اولین endpoint.',
),

# ================================================================ فصل ۲۲
dict(
    n=22, icon='🔌', title='REST API با DRF — مقدماتی', cat=4, mins=100, lvl_label='متوسط',
    hero_desc='ساخت اولین <span class="term" data-term="api">API</span> با <span class="term" data-term="drf">Django REST Framework</span>: مفاهیم REST و <span class="term" data-term="endpoint">endpoint</span>، <span class="term" data-term="serializer">سریالایزر</span>ها، APIView، جنریک‌ها و کاوشگر API (Browsable API).',
    s1_intro='تا اینجا جنگو HTML تحویل می‌داد؛ حالا یاد می‌گیریم همان داده‌ها را به‌صورت JSON به هر کلاینتی (اپ موبایل، فرانت‌اند جدا، سرویس دیگر) بدهیم. DRF استانداردی‌ترین راه ساخت API در جنگو است.',
    objectives=[
        'مفاهیم REST (منابع، متدها، کدهای وضعیت) را توضیح دهید.',
        'DRF را نصب و در INSTALLED_APPS ثبت کنید.',
        'با ModelSerializer مدل را به JSON و برگردانید.',
        'با APIView یک endpoint کامل CRUD بنویسید.',
        'از GenericAPIView/ListCreate برای کد کمتر استفاده کنید.',
    ],
    s1_position='<strong>جایگاه فصل:</strong> مدل‌ها (۴-۶)، ویوها (۸-۹) و احراز هویت (۱۲) پایه‌های مستقیم این فصل‌اند؛ ادامه در فصل ۲۳.',
    roadmap=[
        ('REST و JSON', 'قراردادها و کدها.'),
        ('سریالایزر', 'مدل ⇄ JSON.'),
        ('APIView', 'ویوی دستی API.'),
        ('جنریک‌ها', 'CRUD با کد کمتر.'),
    ],
    mind_qs=[
        ('فرق APIView با ویوی معمولی جنگو چیست؟',
         '<p>ورودی/خروجی با فرمت‌های مختلف (<span class="term" data-term="json">JSON</span>, فرم، HTML کاوشگر)، مدیریت محتوای درخواست (request.data به‌جای POST)، <span class="term" data-term="authentication">احراز هویت</span>/<span class="term" data-term="authorization">مجوز</span> یکپارچه و پاسخ‌های استاندارد. در باطن همان View جنگو است که «چندزبانه» شده.</p>'),
        ('request.data و request.POST چه فرقی دارند؟',
         '<p>POST فقط داده فرم‌کدگذاری‌شده را می‌خواند؛ request.data هر فرمتی (JSON شامل!) را یک‌جا می‌دهد. کلاینت‌های API معمولاً JSON می‌فرستند — پس همیشه request.data.</p>'),
        ('چرا PUT کامل و PATCH جزئی است؟',
         '<p>قرارداد <span class="term" data-term="rest">REST</span>: PUT یعنی «این منبع را با این تصویر <strong>کامل</strong> جایگزین کن» (فیلدهای غایب پاک/پیش‌فرض)؛ PATCH یعنی «فقط این تکه‌ها را تغییر بده». DRF در ویوهای به‌روزرسانی، partial=True را برای PATCH ست می‌کند.</p>'),
    ],
    prereq_intro='پیش‌نیازها:',
    prereq=[
        'پروژه وبلاگ با مدل‌های Post/Comment (فصل ۶).',
        'درک JSON و متدهای HTTP (GET/POST/PUT/PATCH/DELETE).',
        'کدهای وضعیت (فصل ۸): 200/201/204/400/401/403/404.',
        'نصب DRF: <code class="inline-code">pip install djangorestframework</code>.',
    ],
    prereq_callout=('warn', 'نسخه‌ها',
        'این فصل بر پایه djangorestframework نسخه ۳.۱۵+ و جنگو ۵.x نوشته شده. اگر خطای import دیدید، نسخه را با <code class="inline-code">pip show djangorestframework</code> چک کنید.'),
    concepts=[
        dict(h='۵.۱ REST در یک نگاه', body=[
            '<p><span class="term" data-term="rest">REST</span> سبک معماری است: هر چیز یک <strong>منبع</strong> با نشانی یکتا (URL) است و با متدهای HTTP روی آن عمل می‌کنیم:</p>',
            '<div class="table-wrap"><table class="compare"><thead><tr><th>عملیات</th><th>متد + مسیر</th><th>پاسخ</th></tr></thead><tbody>'
            '<tr><td>فهرست پست‌ها</td><td>GET /api/posts/</td><td>200 + آرایه JSON</td></tr>'
            '<tr><td>ایجاد پست</td><td>POST /api/posts/</td><td>201 + شیء ساخته‌شده</td></tr>'
            '<tr><td>جزئیات پست ۵</td><td>GET /api/posts/5/</td><td>200 + شیء</td></tr>'
            '<tr><td>ویرایش کامل/جزئی</td><td>PUT / PATCH /api/posts/5/</td><td>200 + شیء به‌روز</td></tr>'
            '<tr><td>حذف پست ۵</td><td>DELETE /api/posts/5/</td><td>204 بدون بدنه</td></tr>'
            '</tbody></table></div>',
            ('code', 'settings.py', 'python', '''INSTALLED_APPS = [
    ...
    "rest_framework",   # ← کاوشگر API و ابزارها
]

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS":
        "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
}'''),
        ]),
        dict(h='۵.۲ سریالایزر: پل مدل و JSON', body=[
            ('code', 'blog/serializers.py', 'python', '''from rest_framework import serializers

from .models import Comment, Post


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "name", "text", "created_at"]
        read_only_fields = ["id", "created_at"]


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)  # تودرتو
    author_name = serializers.CharField(source="author.name",
                                        read_only=True)

    class Meta:
        model = Post
        fields = ["id", "title", "slug", "body", "published",
                  "author_name", "comments", "created_at"]
        read_only_fields = ["id", "slug", "created_at"]'''),
            ('code', 'دو جهت سریالایزر', 'python', '''# مدل → JSON (خواندن)
s = PostSerializer(post)
s.data            # OrderedDict آماده JsonResponse

# JSON → مدل (نوشتن، با اعتبارسنجی!)
s = PostSerializer(data=request.data)
s.is_valid(raise_exception=True)   # 400 خودکار با جزئیات خطاها
post = s.save()'''),
            ('callout', 'info', 'fields = "__all__"؟',
             'راحت ولی خطرناک: با تغییر مدل، ناخواسته فیلدی حساس (مثل is_staff یا فیلد داخلی) در API نشت می‌کند. فهرست صریح فیلدها عادت حرفه‌ای است.'),
        ]),
        dict(h='۵.۳ APIView — کنترل کامل دستی', body=[
            ('code', 'blog/views_api.py', 'python', '''from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post
from .serializers import PostSerializer


class PostListAPI(APIView):
    def get(self, request):
        posts = Post.objects.filter(published=True)
        page = self.paginate_queryset(posts)
        if page is not None:
            return self.get_paginated_response(
                PostSerializer(page, many=True).data)
        return Response(PostSerializer(posts, many=True).data)

    def post(self, request):
        s = PostSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        s.save(author=request.user.author)
        return Response(s.data, status=status.HTTP_201_CREATED)


class PostDetailAPI(APIView):
    def get_object(self, pk):
        return get_object_or_404(Post, pk=pk, published=True)

    def get(self, request, pk):
        return Response(PostSerializer(self.get_object(pk)).data)

    def patch(self, request, pk):
        post = self.get_object(pk)
        s = PostSerializer(post, data=request.data, partial=True)
        s.is_valid(raise_exception=True)
        s.save()
        return Response(s.data)

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)'''),
            ('code', 'blog/urls_api.py', 'python', '''urlpatterns = [
    path("posts/", PostListAPI.as_view(), name="api_post_list"),
    path("posts/<int:pk>/", PostDetailAPI.as_view(), name="api_post_detail"),
]
# در urls اصلی پروژه:
# path("api/", include("blog.urls_api")),'''),
        ]),
        dict(h='۵.۴ جنریک‌ها: همان CRUD با کد کمتر', body=[
            ('code', 'معادل بخش ۵.۳ در چند خط', 'python', '''from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PostListAPI(generics.ListCreateAPIView):
    queryset = Post.objects.filter(published=True)
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.author)


class PostDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.filter(published=True)
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]'''),
            '<div class="table-wrap"><table class="compare"><thead><tr><th>جنریک</th><th>متدها</th></tr></thead><tbody>'
            '<tr><td>ListAPIView / CreateAPIView</td><td>GET فهرست / POST</td></tr>'
            '<tr><td>RetrieveAPIView</td><td>GET جزئیات</td></tr>'
            '<tr><td>UpdateAPIView / DestroyAPIView</td><td>PUT+PATCH / DELETE</td></tr>'
            '<tr><td>ListCreateAPIView</td><td>GET + POST</td></tr>'
            '<tr><td>RetrieveUpdateDestroyAPIView</td><td>GET + PUT + PATCH + DELETE</td></tr>'
            '</tbody></table></div>',
            ('callout', 'tip', 'perform_create/perform_update',
             'hookهای جنریک برای تزریق داده (author از request، ip از متا) قبل از save — دقیقاً مثل form_valid در CBVها (فصل ۹).'),
        ]),
        dict(h='۵.۵ کاوشگر API و تست سریع', body=[
            '<p>چون rest_framework در INSTALLED_APPS است، اگر API را <strong>در مرورگر</strong> باز کنید، صفحه HTML تعاملی (Browsable API) می‌بینید: داده‌ها، فرم POST، حتی DELETE — بدون نوشتن هیچ فرانت‌اندی!</p>',
            ('code', 'تست با curl / کلاینت تست', 'bash', '''# خواندن
curl http://localhost:8000/api/posts/

# نوشتن (JSON)
curl -X POST http://localhost:8000/api/posts/ \\
  -H "Content-Type: application/json" \\
  -d '{"title": "پست جدید", "body": "متن..."}\''''),
            ('code', 'تست خودکار با APIClient (فصل ۲۰)', 'python', '''from rest_framework.test import APITestCase


class PostAPITest(APITestCase):
    def test_list_ok(self):
        r = self.client.get("/api/posts/", format="json")
        self.assertEqual(r.status_code, 200)

    def test_create_requires_auth(self):
        r = self.client.post("/api/posts/", {"title": "t", "body": "b"})
        self.assertIn(r.status_code, (401, 403))'''),
        ]),
    ],
    example_intro='API کامل «نظرات» به‌صورت تودرتو زیر پست — الگوی واقعی پروژه‌ها:',
    example=[
        ('code', 'serializers — تودرتو و نوشتنی', 'python', '''class CommentSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.filter(published=True))

    class Meta:
        model = Comment
        fields = ["id", "post", "name", "text", "created_at"]
        read_only_fields = ["id", "created_at"]

    def validate_text(self, value):
        if "تبلیغ" in value:
            raise serializers.ValidationError("متن تبلیغاتی مجاز نیست.")
        return value'''),
        ('code', 'views — فهرست با فیلتر و ایجاد', 'python', '''class CommentListAPI(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        qs = Comment.objects.select_related("post")
        post_id = self.request.query_params.get("post")
        if post_id:
            qs = qs.filter(post_id=post_id)
        return qs'''),
        ('code', 'urls', 'python', '''path("comments/", CommentListAPI.as_view()),
path("comments/<int:pk>/", generics.RetrieveDestroyAPIView.as_view(
    queryset=Comment.objects.all(),
    serializer_class=CommentSerializer)),'''),
        ('code', 'نمونه پاسخ GET /api/comments/?post=5', 'json', '''{
  "count": 2,
  "results": [
    {
      "id": 12,
      "post": 5,
      "name": "رضا",
      "text": "عالی بود!",
      "created_at": "2026-01-10T14:22:03Z"
    }
  ]
}'''),
        '<p>همین <span class="term" data-term="api">API</span> را یک اپ موبایل یا فرانت‌اند React (فصل ۲۸) مصرف می‌کند — بدون تغییر در بک‌اند.</p>',
    ],
    workshop_intro='وبلاگ را API-محور کنید:',
    workshop_tasks=[
        '<strong>کارگاه ۱:</strong> دو endpoint با جنریک‌ها بسازید: <code class="inline-code">/api/posts/</code> (فهرست+ایجاد) و <code class="inline-code">/api/posts/&lt;pk&gt;/</code> (جزئیات+ویرایش+حذف). در کاوشگر مرورگر تست کنید.',
        '<strong>کارگاه ۲:</strong> سریالایزر Post را طوری گسترش دهید که <code class="inline-code">tags</code> (فهرست نام‌ها، فقط خواندنی) و <code class="inline-code">comment_count</code> را برگرداند.',
        '<strong>کارگاه ۳:</strong> با APIClient دو تست بنویسید: ایجاد پست بدون ورود → 401/403؛ با force_authenticate → 201 و بررسی داده ذخیره‌شده.',
    ],
    workshop_answers=[
        ('پاسخ کارگاه ۱',
         '<p>کد مفهوم ۵.۴ عیناً جواب است؛ نکات تکمیلی:</p>'
         '<div class="code-box"><div class="code-head"><span>urls_api.py کامل</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">from django.urls import path\nfrom rest_framework import generics\n\nfrom .models import Post\nfrom .serializers import PostSerializer\n\n\nclass PostListAPI(generics.ListCreateAPIView):\n    queryset = Post.objects.filter(published=True).select_related("author")\n    serializer_class = PostSerializer\n\n    def perform_create(self, serializer):\n        serializer.save(author=self.request.user.author)\n\n\nclass PostDetailAPI(generics.RetrieveUpdateDestroyAPIView):\n    queryset = Post.objects.filter(published=True)\n    serializer_class = PostSerializer\n\n\nurlpatterns = [\n    path("posts/", PostListAPI.as_view()),\n    path("posts/&lt;int:pk&gt;/", PostDetailAPI.as_view()),\n]</code></pre></div>'
         '<p>در <code class="inline-code">http://localhost:8000/api/posts/</code> کاوشگر را ببینید؛ فرم RAW data را امتحان کنید.</p>'),
        ('پاسخ کارگاه ۲',
         '<div class="code-box"><div class="code-head"><span>فیلدهای محاسباتی</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">class PostSerializer(serializers.ModelSerializer):\n    tags = serializers.SerializerMethodField()\n    comment_count = serializers.IntegerField(\n        source="comments.count", read_only=True)\n\n    class Meta:\n        model = Post\n        fields = ["id", "title", "slug", "body", "published",\n                  "tags", "comment_count", "created_at"]\n\n    def get_tags(self, obj):\n        return list(obj.tags.values_list("name", flat=True))</code></pre></div>'
         '<p><strong>هشدار <span class="term" data-term="n-plus-one">N+1</span>:</strong> comments.count برای هر پست یک کوئری است! در get_queryset ویو فهرست: <code class="inline-code">.annotate(comment_count=Count("comments")).prefetch_related("tags")</code> و فیلد سریالایزر را به IntegerField ساده تبدیل کنید (فصل ۱۵ در API هم صادق است).</p>'),
        ('پاسخ کارگاه ۳',
         '<div class="code-box"><div class="code-head"><span>tests_api.py</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">from rest_framework.test import APITestCase\n\n\nclass PostCreateAPITest(APITestCase):\n    def test_anonymous_cannot_create(self):\n        r = self.client.post("/api/posts/",\n                             {"title": "t", "body": "bb"}, format="json")\n        self.assertIn(r.status_code, (401, 403))\n\n    def test_author_can_create(self):\n        u = User.objects.create_user("a", password="p")\n        author = Author.objects.create(name="A", user=u)\n        self.client.force_authenticate(user=u)\n        r = self.client.post("/api/posts/",\n                             {"title": "t", "body": "bb"}, format="json")\n        self.assertEqual(r.status_code, 201)\n        self.assertTrue(Post.objects.filter(title="t", author=author).exists())</code></pre></div>'
         '<p>force_authenticate مسیر ورود واقعی را دور می‌زند — برای تست منطق ویو عالی است. برای تست خودِ احراز هویت، client.credentials(HTTP_AUTHORIZATION=...) یا login را استفاده کنید.</p>'),
    ],
    errors=[
        ('خطای 405 Method Not Allowed',
         'متد درخواست با متدهای تعریف‌شده ویو نمی‌خواند (مثلاً POST به RetrieveAPIView). جنریک درست یا متد get/post/... در APIView را چک کنید.'),
        ('«You called this URL via POST, but the data... CSRF» (خطای 403 CSRF در API)',
         'SessionAuthentication فعال است و مرورگر/کلاینت توکن CSRF ندارد. برای API معمولاً Token/JWT استفاده می‌شود (فصل ۲۳)؛ در تست با APIClient مشکلی نیست.'),
        ('AttributeError: got AttributeError when trying to get field value...',
         'نام فیلد در Meta.fields با چیزی که سریالایزر می‌تواند بخواند نمی‌خواند (مثلاً source اشتباه یا property بدون خروجی). نام فیلد/property مدل را چک کنید.'),
        ('400 با پیام «This field is required» برای فیلدی که نفرستاده‌اید',
         'فیلد در سریالایزر خواندنی نیست؛ read_only_fields را اضافه کنید یا در ویو مقدارش را تزریق کنید (perform_create).'),
        ('کاوشگر API نمایش داده نمی‌شود',
         'rest_framework در INSTALLED_APPS نیست، یا با curl/هدر Accept: application/json درخواست داده‌اید (کاوشگر فقط برای درخواست‌های HTML مرورگر است).'),
    ],
    errors_callout=None,
    exercises=[
        ('تمرین ۱ — متد و کد وضعیت',
         '<p><strong>سوال:</strong> برای هر سناریو متد HTTP و کد وضعیت موفق؟ (الف) ساخت نظر جدید (ب) گرفتن فهرست پست‌ها (ج) حذف پست (د) تغییر فقط عنوان پست (ه) درخواست جزئیات پستی که وجود ندارد</p>'
         '<p><strong>پاسخ:</strong> الف → POST / 201 • ب → GET / 200 • ج → DELETE / 204 • د → PATCH / 200 • ه → GET / 404.</p>'),
        ('تمرین ۲ — طراحی سریالایزر',
         '<p><strong>سوال:</strong> در سریالایزر ثبت‌نام، کدام فیلدها read_only و کدام write_only؟ (id، password، email، created_at، is_staff)</p>'
         '<p><strong>پاسخ:</strong> read_only: id, created_at (و is_staff که هرگز از کلاینت گرفته نشود — کلاً نگذارید!) • write_only: password (در خروجی JSON برنگردد) • معمولی: email.</p>'),
        ('تمرین ۳ — APIView یا جنریک؟',
         '<p><strong>سوال:</strong> برای هر مورد کدام مناسب‌تر؟ (الف) CRUD استاندارد روی یک مدل (ب) endpoint گزارش‌گیری که سه کوئری تجمیعی را ترکیب می‌کند (ج) endpoint که دو مدل را در یک پاسخ برمی‌گرداند</p>'
         '<p><strong>پاسخ:</strong> الف → جنریک/ViewSet (کد کمتر، رفتار استاندارد) • ب و ج → APIView (منطق سفارشی؛ جنریک‌ها برای «یک مدل، CRUD» طراحی شده‌اند).</p>'),
    ],
    quiz=[
        dict(q='request.data در DRF چه مزیتی بر request.POST دارد؟',
             opts=['سریع‌تر است', 'بدنه JSON و سایر فرمت‌ها را هم یک‌جا می‌خواند',
                   'فقط خواندنی است', 'نیاز به CSRF ندارد'],
             ans='b', explain='کلاینت‌های API معمولاً JSON می‌فرستند؛ request.POST آن را نمی‌بیند ولی request.data همه فرمت‌ها را پشتیبانی می‌کند.'),
        dict(q='کد وضعیت پاسخ موفق DELETE طبق قرارداد REST چیست؟',
             opts=['200 با شیء حذف‌شده', '204 بدون بدنه', '302', '404'],
             ans='b', explain='204 No Content: عملیات موفق و چیزی برای برگرداندن نیست. (بعضی APIها 200 با پیام می‌دهند؛ 204 استانداردتر است.)'),
        dict(q='is_valid(raise_exception=True) چه می‌کند؟',
             opts=['فقط True/False', 'در نامعتبر بودن، خودکار پاسخ 400 با جزئیات خطاهای فیلدها برمی‌گرداند',
                   'داده را پاک می‌کند', 'استثنا را مخفی می‌کند'],
             ans='b', explain='DRF ValidationError را گرفته و به Response با status=400 و دیکشنری خطاها تبدیل می‌کند — بدون کد اضافه.'),
        dict(q='کدام جنریک هم GET جزئیات و هم PUT/PATCH و DELETE را پوشش می‌دهد؟',
             opts=['ListCreateAPIView', 'RetrieveUpdateDestroyAPIView',
                   'CreateAPIView', 'UpdateAPIView'],
             ans='b', explain='نام‌ها ترکیبی‌اند: Retrieve=GET جزئیات، Update=PUT/PATCH، Destroy=DELETE.'),
        dict(q='چرا fields = "__all__" توصیه نمی‌شود؟',
             opts=['کند است', 'با تغییر مدل ممکن است فیلد حساس ناخواسته در API نشت کند',
                   'کار نمی‌کند', 'فقط خواندنی می‌شود'],
             ans='b', explain='فهرست صریح فیلدها «قرارداد API» را آگاهانه نگه می‌دارد؛ نشت تصادفی داده از رایج‌ترین باگ‌های امنیتی API است.'),
        dict(q='hook مناسب برای ست‌کردن author از کاربر لاگین‌شده در ListCreateAPIView چیست؟',
             opts=['get_queryset', 'perform_create', 'serializer.data', 'dispatch'],
             ans='b', explain='perform_create قبل از save صدا زده می‌شود: serializer.save(author=self.request.user.author).'),
    ],
    project_title='API عمومی وبلاگ',
    project_intro='نسخه API وبلاگ را بسازید که یک اپ موبایل فرضی بتواند مصرف کند.',
    project_checklist=[
        'نصب DRF و تنظیم REST_FRAMEWORK (صفحه‌بندی ۱۰ تایی).',
        'سریالایزرهای Post و Comment (فیلد صریح + validate سفارشی).',
        'endpointها: posts (List/Create)، posts/pk (RUD)، comments با فیلتر ?post=.',
        'تست با کاوشگر مرورگر + curl برای هر متد.',
        'حداقل ۴ تست APIClient (فهرست، ایجاد با/بدون احراز هویت، ۴۰۴).',
    ],
    project_callout=('info', 'مستندسازی',
        'از همین ابتدا مسیرها و پاسخ‌ها را در docs/api.md یادداشت کنید؛ در فصل ۲۳ مستندسازی خودکار OpenAPI را هم اضافه می‌کنیم.'),
    summary_items=[
        'REST = منابع با URL + متدهای HTTP + کدهای وضعیت قرارداددار.',
        'ModelSerializer دو جهت: data خواندن، data=... نوشتن با اعتبارسنجی.',
        'APIView کنترل دستی؛ جنریک‌ها CRUD آماده با hookها.',
        'request.data همیشه؛ perform_create برای تزریق author.',
        'کاوشگر API + curl + APIClient: سه ابزار تست سریع.',
    ],
    golden='API خوب، قرارداد صریح است: فیلدهای اعلامی، کدهای وضعیت درست و پیام خطای خوانا.',
    faq=[
        ('DRF تنها گزینه است؟',
         '<p>نه: Django Ninja (سریع‌تر، type-hint محور، OpenAPI خودکار) گزینه مدرن‌تری است و JsonResponse خالص هم ممکن. ولی DRF بالغ‌ترین اکوسیستم (مجوزها، صفحه‌بندی، مستندسازی) را دارد و بازار کار ایران/جهان اکثراً DRF است.</p>'),
        ('ورژن‌گذاری API چطور است؟',
         '<p>رایج‌ترین: پیشوند مسیر <code class="inline-code">/api/v1/...</code>. وقتی قرارداد را شکستید، v2 بسازید و v1 را مدت‌دار نگه دارید. تغییرات سازگار (افزودن فیلد) نیاز به نسخه جدید ندارند.</p>'),
        ('چطور فقط JSON بدهم و کاوشگر HTML حذف شود؟',
         '<p>در REST_FRAMEWORK: <code class="inline-code">"DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"]</code> — کاوشگر فقط یک renderer است.</p>'),
    ],
    next_step='پایه API ساخته شد؛ حالا حرفه‌ای‌اش می‌کنیم: <strong>فصل ۲۳</strong> — <span class="term" data-term="viewset">ViewSet</span> و <span class="term" data-term="router">Router</span>، مجوزها، <span class="term" data-term="throttling">محدودسازی نرخ</span>، <span class="term" data-term="jwt">JWT</span> و مستندسازی خودکار.',
),

# ================================================================ فصل ۲۳
dict(
    n=23, icon='🚀', title='DRF پیشرفته — ViewSet، مجوزها و JWT', cat=4, mins=105, lvl_label='پیشرفته',
    hero_desc='<span class="term" data-term="viewset">ViewSet</span> و <span class="term" data-term="router">Router</span> برای CRUD فشرده، کلاس‌های مجوز، <span class="term" data-term="pagination">صفحه‌بندی</span> و فیلترینگ، <span class="term" data-term="throttling">Throttling</span>، احراز هویت <span class="term" data-term="token">Token</span>/<span class="term" data-term="jwt">JWT</span> و مستندسازی <span class="term" data-term="openapi">OpenAPI</span>.',
    s1_intro='فصل قبل endpoint ساختیم؛ حالا همان را با یک‌سوم کد، امن‌تر و مستندشده می‌سازیم. ViewSet+Router، مجوزهای سطح‌بندی‌شده و JWT سه ستون APIهای تولیدی جنگو هستند.',
    objectives=[
        'با ModelViewSet و DefaultRouter یک CRUD کامل را در چند خط بنویسید.',
        'کلاس مجوز سفارشی (مثلاً «فقط نویسنده») بسازید.',
        'صفحه‌بندی، فیلتر و جست‌وجو را پیکربندی کنید.',
        'با SimpleJWT ورود/تازه‌سازی توکن پیاده کنید.',
        'مستند خودکار OpenAPI (Swagger UI) راه بیندازید.',
    ],
    s1_position='<strong>جایگاه فصل:</strong> ادامه مستقیم فصل ۲۲؛ مجوزها مکمل فصل ۱۳ و JWT مکمل احراز هویت فصل ۱۲ است. فرانت‌اند فصل ۲۸ همین API را مصرف می‌کند.',
    roadmap=[
        ('ViewSet و Router', 'CRUD فشرده.'),
        ('مجوزها و Throttle', 'امنیت و انصاف.'),
        ('فیلتر و صفحه‌بندی', 'داده قابل مدیریت.'),
        ('JWT و مستندات', 'ورود توکنی + Swagger.'),
    ],
    mind_qs=[
        ('ViewSet چه چیزی را حذف می‌کند؟',
         '<p>تکرار «یک مدل = چند ویو»: ListCreate و RetrieveUpdateDestroy ادغام می‌شوند در یک کلاس با اکشن‌های list/create/retrieve/update/destroy. Router هم URLها را <strong>خودکار</strong> از همان اکشن‌ها می‌سازد — دیگر path() دستی برای هر عملیات نیست.</p>'),
        ('Token و JWT چه فرقی دارند؟',
         '<p>Token (TokenAuthentication) یک رشته تصادفی است که <strong>سمت سرور در دیتابیس</strong> ذخیره و هر درخواست lookup می‌شود — ساده و قابل باطل‌سازی فوری. JWT خودش داده (payload: کاربر، انقضا) را <strong>امضاشده</strong> حمل می‌کند؛ سرور بدون دیتابیس اعتبارسنجی می‌کند — مقیاس‌پذیر ولی باطل‌سازی قبل از انقضا سخت.</p>'),
        ('چرا throttling لازم است حتی با احراز هویت؟',
         '<p>احراز هویت می‌گوید «کی هستی»؛ throttling می‌گوید «چقدر حق داری». بدون آن یک کلاینت (حتی لاگین‌شده) می‌تواند با ۱۰۰۰ درخواست در ثانیه سرور را بیندازد یا endpoint گران را بکوبد. لایه انصاف و دفاع هزینه.</p>'),
    ],
    prereq_intro='پیش‌نیازها:',
    prereq=[
        'فصل ۲۲ کامل (سریالایزر، جنریک‌ها، تست APIClient).',
        'نصب: <code class="inline-code">pip install djangorestframework django-filter djangorestframework-simplejwt drf-spectacular</code>.',
        'مدل‌های Post/Comment/Tag و کاربران تستی.',
        'فصل ۱۳: درک permission — اینجا به سطح API می‌آید.',
    ],
    prereq_callout=None,
    concepts=[
        dict(h='۵.۱ ViewSet و Router', body=[
            ('code', 'یک ViewSet = کل CRUD', 'python', '''from rest_framework import viewsets


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(published=True).select_related("author")
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.author)'''),
            ('code', 'Router — URL خودکار', 'python', '''from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("posts", PostViewSet, basename="post")
router.register("comments", CommentViewSet, basename="comment")

urlpatterns = [path("", include(router.urls))]
# → /api/posts/ (list, create)
# → /api/posts/{pk}/ (retrieve, update, partial_update, destroy)'''),
            ('code', 'اکشن سفارشی با @action', 'python', '''from rest_framework.decorators import action


class PostViewSet(viewsets.ModelViewSet):
    ...

    @action(detail=True, methods=["post"])
    def publish(self, request, pk=None):
        """POST /api/posts/{pk}/publish/"""
        post = self.get_object()
        post.published = True
        post.save()
        return Response({"status": "published"})

    @action(detail=False)
    def mine(self, request):
        """GET /api/posts/mine/ — پست‌های خودم"""
        qs = Post.objects.filter(author__user=request.user)
        return Response(self.get_serializer(qs, many=True).data)'''),
            ('callout', 'info', 'ReadOnlyModelViewSet',
             'اگر فقط GET لازم است (مثلاً فهرست عمومی برچسب‌ها)، ReadOnlyModelViewSet تنها list+retrieve می‌دهد — سطح دسترسی از جنس کد.'),
        ]),
        dict(h='۵.۲ مجوزها: از آماده تا سفارشی', body=[
            '<ul>'
            '<li><code class="inline-code">IsAuthenticatedOrReadOnly</code>: عمومی بخوانند، نوشتن با ورود.</li>'
            '<li><code class="inline-code">IsAuthenticated</code> / <code class="inline-code">IsAdminUser</code>: سطح‌های ساده.</li>'
            '<li><code class="inline-code">DjangoModelPermissions</code>: مجوزهای فصل ۱۳ را به API وصل می‌کند.</li></ul>',
            ('code', 'مجوز سفارشی: فقط نویسنده یا مدیر', 'python', '''from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True                       # خواندن آزاد
        return (request.user.is_authenticated and
                (obj.author.user == request.user or
                 request.user.is_staff))'''),
            ('code', 'اتصال', 'python', '''class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]'''),
            ('callout', 'warn', 'has_permission و has_object_permission',
             'has_permission روی <strong>اکشن</strong> (مثلاً POST به فهرست) و has_object_permission روی <strong>شیء خاص</strong> (retrieve/update/delete با get_object) چک می‌شود. مجوز شیء‌محور فقط وقتی get_object صدا زده شود اجرا می‌شود — در list اجرا نمی‌شود، پس queryset را هم محدود کنید.'),
        ]),
        dict(h='۵.۳ صفحه‌بندی، فیلتر، جست‌وجو', body=[
            ('code', 'پیکربندی سراسری + محلی', 'python', '''REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
        "rest_framework.filters.OrderingFilter",
    ],
    "DEFAULT_PAGINATION_CLASS":
        "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
}


class PostViewSet(viewsets.ModelViewSet):
    filterset_fields = ["published"]           # ?published=true
    search_fields = ["title", "body"]          # ?search=django
    ordering_fields = ["created_at", "views_count"]
    ordering = ["-created_at"]'''),
            ('code', 'پاسخ صفحه‌بندی‌شده', 'json', '''{
  "count": 42,
  "next": "http://api/posts/?page=2",
  "previous": null,
  "results": [ ... ]
}'''),
            '<p>برای داده بزرگ، LimitOffsetPagination (?limit=20&offset=40) یا CursorPagination (پایدار برای فیدهای زمان‌مرتبت) انتخاب کنید.</p>',
        ]),
        dict(h='۵.۴ Throttling — محدودسازی نرخ', body=[
            ('code', 'settings.py', 'python', '''REST_FRAMEWORK = {
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {
        "anon": "60/hour",
        "user": "1000/day",
    },
}'''),
            ('code', 'throttle اختصاصی برای endpoint گران', 'python', '''from rest_framework.throttling import ScopedRateThrottle


class ReportViewSet(viewsets.ViewSet):
    throttle_scope = "reports"     # rates: {"reports": "10/minute"}
    throttle_classes = [ScopedRateThrottle]'''),
            '<p>پاسخ در صورت عبور از حد: <strong>429 Too Many Requests</strong> با هدر Retry-After. بک‌اند throttle پیش‌فرض کش است (فصل ۱۹!) — پس CACHES را درست تنظیم کنید.</p>',
        ]),
        dict(h='۵.۵ احراز هویت Token و JWT', body=[
            ('code', 'گزینه ۱: Token ساده (داخلی DRF)', 'python', '''INSTALLED_APPS += ["rest_framework.authtoken"]
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
}
# پس از migrate، ساخت توکن:
# python manage.py drf_create_token USERNAME'''),
            ('code', 'گزینه ۲: SimpleJWT (رایج در فرانت جدا/موبایل)', 'python', '''INSTALLED_APPS += ["rest_framework_simplejwt"]
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
}
# urls:
path("api/auth/token/", TokenObtainPairView.as_view()),
path("api/auth/token/refresh/", TokenRefreshView.as_view()),'''),
            ('code', 'گردش کار JWT در کلاینت', 'bash', '''# ۱) ورود → دو توکن می‌گیریم (access کوتاه + refresh بلند)
curl -X POST /api/auth/token/ -d \'{"username":"ali","password":"..."}\'

# ۲) هر درخواست با هدر:
Authorization: Bearer <access_token>

# ۳) access منقضی شد (401) → بدون رمز، توکن تازه:
curl -X POST /api/auth/token/refresh/ -d \'{"refresh":"<refresh_token>"}\''''),
            ('callout', 'danger', 'امنیت JWT',
             'SECRET_KEY قوی و پایدار (نشت آن = جعل هر توکنی!)، عمر access کوتاه (۵-۱۵ دقیقه)، refresh در <span class="term" data-term="cookie">کوکی</span> HttpOnly اگر مرورگری است. باطل‌سازی: blacklist پکیج simplejwt یا کوتاه نگه‌داشتن عمر.'),
        ]),
        dict(h='۵.۶ مستندسازی خودکار با drf-spectacular', body=[
            ('code', 'تنظیم و مسیرها', 'python', '''INSTALLED_APPS += ["drf_spectacular"]
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS":
        "drf_spectacular.openapi.AutoSchema",
}
SPECTACULAR_SETTINGS = {"TITLE": "Blog API", "VERSION": "1.0.0"}

# urls:
path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema")),'''),
            '<p>/api/docs/ صفحه Swagger UI می‌دهد: همه endpointها، پارامترها، مدل‌ها و <strong>Try it out</strong> تعاملی. مستند با کد همگام می‌ماند چون از خود سریالایزرها/ویوها ساخته می‌شود.</p>',
        ]),
    ],
    example_intro='یک API تولیدی کوچک ولی کامل — «سیستم برچسب‌ها» با همه لایه‌ها:',
    example=[
        ('code', 'serializers.py', 'python', '''class TagSerializer(serializers.ModelSerializer):
    posts_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Tag
        fields = ["id", "name", "slug", "posts_count"]
        read_only_fields = ["id", "slug"]


class PostDetailSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        many=True, slug_field="slug", queryset=Tag.objects.all())

    class Meta:
        model = Post
        fields = ["id", "title", "slug", "body", "published",
                  "tags", "created_at"]'''),
        ('code', 'views.py — ViewSet کامل', 'python', '''class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filterset_fields = ["published", "tags__slug"]
    search_fields = ["title", "body"]
    ordering = ["-created_at"]

    def get_queryset(self):
        return (Post.objects.select_related("author", "author__user")
                .prefetch_related("tags")
                .annotate(posts_count_dummy=Value(0))  # نمونه annotate
                .filter(published=True) if not
                self.request.user.is_staff
                else Post.objects.all())

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.author)'''),
        ('code', 'urls.py', 'python', '''router = DefaultRouter()
router.register("posts", PostViewSet, basename="post")
router.register("tags", ReadOnlyTagViewSet, basename="tag")

urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("rest_framework.urls")),   # ورود کاوشگر
    path("schema/", SpectacularAPIView.as_view()),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema")),
]'''),
        ('code', 'تست مجوز سفارشی', 'python', '''def test_other_author_cannot_edit(self):
    self.client.force_authenticate(user=self.user_b)
    r = self.client.patch(f"/api/posts/{self.post_a.pk}/",
                          {"title": "هک"}, format="json")
    self.assertEqual(r.status_code, 403)   # IsAuthorOrReadOnly'''),
    ],
    workshop_intro='API فصل ۲۲ را به سطح تولید ارتقا دهید:',
    workshop_tasks=[
        '<strong>کارگاه ۱:</strong> ویوهای جنریک فصل قبل را به ModelViewSet + DefaultRouter تبدیل کنید؛ یک <code class="inline-code">@action(detail=True)</code> برای «افزایش بازدید» بنویسید.',
        '<strong>کارگاه ۲:</strong> مجوز IsAuthorOrReadOnly را پیاده و با سه تست پوشش دهید (ناشناس ۴۰۳ روی PATCH، نویسنده ۲۰۰، دیگران ۴۰۳).',
        '<strong>کارگاه ۳:</strong> SimpleJWT راه بیندازید: endpoint ورود، یک درخواست محافظت‌شده با Bearer token (curl) و تنظیم throttle روی ورود (۵/دقیقه).',
    ],
    workshop_answers=[
        ('پاسخ کارگاه ۱',
         '<div class="code-box"><div class="code-head"><span>اکشن افزایش بازدید</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">@action(detail=True, methods=["post"],\n        permission_classes=[AllowAny],\n        throttle_classes=[UserRateThrottle])\ndef view_hit(self, request, pk=None):\n    """POST /api/posts/{pk}/view_hit/ → شمارش بازدید با F""" \n    post = self.get_object()\n    Post.objects.filter(pk=post.pk).update(\n        views_count=F("views_count") + 1)\n    post.refresh_from_db()\n    return Response({"views_count": post.views_count})</code></pre></div>'
         '<p>F() اتمی است (دو کلیک هم‌زمان یکی را نمی‌بلعد — مفهوم ۵.۴ فصل ۱۵). Router خودش URL را ساخت؛ نیازی به path نبود.</p>'),
        ('پاسخ کارگاه ۲',
         '<div class="code-box"><div class="code-head"><span>سه تست مجوز</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">def test_anonymous_patch_403(self):\n    r = self.client.patch(f"/api/posts/{self.post.pk}/",\n                          {"title": "x"}, format="json")\n    self.assertIn(r.status_code, (401, 403))\n\n\ndef test_other_author_forbidden(self):\n    other = User.objects.create_user("b", password="p")\n    self.client.force_authenticate(user=other)\n    r = self.client.patch(f"/api/posts/{self.post.pk}/",\n                          {"title": "x"}, format="json")\n    self.assertEqual(r.status_code, 403)\n\n\ndef test_owner_can_patch(self):\n    self.client.force_authenticate(user=self.post.author.user)\n    r = self.client.patch(f"/api/posts/{self.post.pk}/",\n                          {"title": "ویرایش من"}, format="json")\n    self.assertEqual(r.status_code, 200)\n    self.post.refresh_from_db()\n    self.assertEqual(self.post.title, "ویرایش من")</code></pre></div>'
         '<p>نکته: has_object_permission فقط وقتی get_object صدا زده شود اجرا می‌شود؛ PATCH روی detail دقیقاً همان مسیر است.</p>'),
        ('پاسخ کارگاه ۳',
         '<div class="code-box"><div class="code-head"><span>گردش JWT با curl</span><span class="lang">bash</span></div><pre class="code"><code data-lang="bash"># ورود و گرفتن توکن‌ها\nTOKEN=$(curl -s -X POST http://localhost:8000/api/auth/token/ \\\n  -H "Content-Type: application/json" \\\n  -d \'{"username":"ali","password":"pass12345!"}\' | python3 -c "import sys,json;print(json.load(sys.stdin)[\'access\'])")\n\n# درخواست محافظت‌شده\ncurl http://localhost:8000/api/posts/mine/ \\\n  -H "Authorization: Bearer $TOKEN"\n\n# بدون/با توکن خراب → 401</code></pre></div>'
         '<p>throttle روی ورود: کلاس TokenObtainPairView را subclass کنید و throttle_scope="login" با rate "5/min" بدهید — جلوی brute-force.</p>'),
    ],
    errors=[
        ('خطای «basename is required» در router.register',
         'ViewSet شما queryset صفت کلاسی ندارد (get_queryset پویاست)؛ پارامتر basename="post" را بدهید تا Router نام‌های URL را بسازد.'),
        ('403 روی PATCH حتی برای نویسنده',
         'SessionAuthentication بدون توکن CSRF از مرورگر/کاوشگر درخواست را رد می‌کند. از JWT/Bearer استفاده کنید یا در کاوشگر اول login کنید.'),
        ('مجوز شیء‌محور در list اعمال نمی‌شود',
         'has_object_permission فقط برای retrieve/update/delete است؛ فهرست را با get_queryset محدود کنید (مثلاً فقط پست‌های خودم برای اکشن mine).'),
        ('429 برای همه حتی اولین درخواست',
         'throttle از کش استفاده می‌کند؛ اگر کش خراب/مشترک مانده (کلیدهای قبلی)، cache.clear() بزنید و DEFAULT_THROTTLE_RATES را چک کنید.'),
        ('JWT هر بار «Token is invalid or expired»',
         'SECRET_KEY بین اجراها عوض می‌شود (از env خوانده نشده و تصادفی است) یا ساعت سرور جلو/عقب است (exp/nbf بر پایه زمان است). SECRET_KEY پایدار + NTP.'),
    ],
    errors_callout=None,
    exercises=[
        ('تمرین ۱ — انتخاب ابزار',
         '<p><strong>سوال:</strong> کدام ابزار برای کدام نیاز؟ (الف) endpoint «پست‌های مشابه» روی جزئیات (ب) محدودکردن ساخت حساب به ۳ در ساعت برای هر IP (ج) مستند زنده برای تیم فرانت (د) جست‌وجوی عنوان در فهرست</p>'
         '<p><strong>پاسخ:</strong> الف → @action(detail=True) • ب → AnonRateThrottle با rate مناسب یا ScopedRateThrottle • ج → drf-spectacular/Swagger • د → SearchFilter با search_fields.</p>'),
        ('تمرین ۲ — Token یا JWT؟',
         '<p><strong>سوال:</strong> برای هر سناریو کدام؟ (الف) اپ موبایل با «خروج از همه دستگاه‌ها» (ب) فرانت React روی دامنه دیگر با ورود/انقضای خودکار (ج) اسکریپت داخلی که یک سرور دیگر API ما را صدا می‌زند</p>'
         '<p><strong>پاسخ:</strong> الف → Token دیتابیسی (باطل‌سازی فوری هر ردیف) • ب → JWT (بدون وابستگی به کوکی نشست میان‌دامنه؛ access کوتاه + refresh) • ج → Token یا حتی API-key سفارشی با throttle سخت‌گیرانه.</p>'),
        ('تمرین ۳ — طراحی permission',
         '<p><strong>سوال:</strong> has_object_permission را برای «کامنت: نویسنده کامنت یا مدیر پست بتواند حذف کند» بنویسید (شبه‌کد).</p>'
         '<p><strong>پاسخ:</strong> <code class="inline-code">return request.user.is_staff or obj.name == request.user.username or obj.post.author.user == request.user</code> — SAFE_METHODS را True برگردانید و برای حذف/ویرایش این شرط. دقت: هویت کامنت‌گذار مهمان فقط «نام» است؛ جدی‌اش با user FK (تمرین فصل ۱۲).</p>'),
    ],
    quiz=[
        dict(q='DefaultRouter از یک ModelViewSet چه URLهایی می‌سازد؟',
             opts=['فقط فهرست', 'فهرست (GET/POST) و جزئیات (GET/PUT/PATCH/DELETE) به‌علاوه اکشن‌های @action',
                   'فقط جزئیات', 'باید دستی path نوشت'],
             ans='b', explain='router.register همه اکشن‌های استاندارد و سفارشی را به URL نگاشت می‌کند — حذف کامل تکرار urls.'),
        dict(q='has_object_permission چه زمانی اجرا می‌شود؟',
             opts=['هر درخواست', 'فقط وقتی ویو get_object() را صدا بزند (retrieve/update/delete)',
                   'فقط در list', 'فقط در create'],
             ans='b', explain='مجوز شیء‌محور به شیء نیاز دارد؛ در list باید با get_queryset دسترسی را اعمال کنید.'),
        dict(q='کدام درباره JWT درست است؟',
             opts=['سرور هر توکن را در دیتابیس نگه می‌دارد', 'توکن امضاشده خودش داده کاربر و انقضا را حمل می‌کند؛ اعتبارسنجی بدون دیتابیس',
                   'فقط برای مرورگر است', 'باطل‌سازی فوری‌اش از Token آسان‌تر است'],
             ans='b', explain='payload + امضا با SECRET_KEY؛ مقیاس‌پذیر ولی باطل‌سازی پیش از انقضا نیاز به blacklist/عمر کوتاه دارد.'),
        dict(q='کد وضعیت پاسخ throttling چیست؟',
             opts=['403', '429 Too Many Requests', '401', '503'],
             ans='b', explain='۴۲۹ یعنی «زیاده‌روی کردی»؛ هدر Retry-After زمان مجاز بعدی را می‌دهد.'),
        dict(q='برای فید زمان‌مرتبت با داده زیاد کدام صفحه‌بندی پایدارتر است؟',
             opts=['PageNumber', 'CursorPagination', 'بدون صفحه‌بندی', 'HTML صفحه‌بندی قالب'],
             ans='b', explain='صفحه‌بندی عددی با insert شدن داده جدید جابه‌جا می‌شود؛ cursor بر پایه ترتیب پایدار (مثل created_at+pk) موقعیت را حفظ می‌کند.'),
        dict(q='drf-spectacular مستند را از کجا می‌سازد؟',
             opts=['فایل دستی markdown', 'از خود سریالایزرها، ویوها و type-hintها (طرح OpenAPI خودکار)',
                   'از دیتابیس', 'از تست‌ها'],
             ans='b', explain='همگامی مستند و کد خودکار؛ Swagger UI هم «Try it out» تعاملی می‌دهد.'),
    ],
    project_title='API تولیدی وبلاگ',
    project_intro='همه‌چیز را به یک API منسجم، امن و مستند تبدیل کنید.',
    project_checklist=[
        'ModelViewSet برای Post/Comment/Tag + DefaultRouter.',
        'مجوز سفارشی IsAuthorOrReadOnly + تست سه‌سناریویی.',
        'فیلتر (tags، published)، جست‌وجو، ترتیب و صفحه‌بندی ۱۰ تایی.',
        'JWT: ورود، refresh، یک endpoint محافظت‌شده + throttle روی login.',
        'Swagger روی /api/docs/ و حداقل ۸ تست APIClient سبز.',
    ],
    project_callout=('tip', 'معیار آمادگی تولید',
        'یک توسعه‌دهنده غریبه بتواند فقط با /api/docs/ و بدون پرسش از شما، ورود کند، پست بسازد و کامنت بگذارد.'),
    summary_items=[
        'ModelViewSet + Router = CRUD کامل با کمترین کد؛ @action برای اکشن‌های سفارشی.',
        'مجوز: آماده‌ها + BasePermission سفارشی (has_permission vs has_object_permission).',
        'فیلتر/جست‌وجو/ترتیب/صفحه‌بندی با filter_backs و تنظیمات.',
        'Throttling با کش؛ 429 و Retry-After.',
        'JWT: access کوتاه + refresh؛ Swagger خودکار با drf-spectacular.',
    ],
    golden='در API، امنیت لایه‌لایه است: احراز هویت (کی)، مجوز (چه کاری)، throttle (چقدر) — هیچ‌کدام جای دیگری را نمی‌گیرد.',
    faq=[
        ('CORS برای فرانت جدا لازم است؟',
         '<p>بله — اگر React/Vue روی دامنه/پورت دیگر API را صدا بزند، مرورگر درخواست را با سیاست <span class="term" data-term="cors">CORS</span> چک می‌کند. پکیج django-cors-headers با CORS_ALLOWED_ORIGINS فهرست دامنه‌های مجاز را مدیریت می‌کند (فصل ۲۸ عملی می‌بینیم).</p>'),
        ('Nested resource چطور؟ (کامنت‌های زیر پست)',
         '<p>دو راه: ① فیلتر کامنت‌ها با ?post=5 (ساده و رایج) ② اکشن سفارشی <code class="inline-code">@action(detail=True) def comments(...)</code> روی PostViewSet که /api/posts/5/comments/ می‌دهد. پکیج drf-nested-routers هم برای ساختارهای عمیق هست.</p>'),
        ('API نسخه‌دار با ViewSet چطور است؟',
         '<p>ساده‌ترین: مسیرها را versioned کنید — path("api/v1/", include(router.urls)). برای تغییرات بزرگ، ViewSet/سریالایزر v2 بسازید و v1 را deprecated-mark کنید.</p>'),
    ],
    next_step='API هم‌زمان (synchronous) است؛ کارهای سنگین کاربر را منتظر می‌گذارد. <strong>فصل ۲۴</strong>: <span class="term" data-term="celery">سلری</span> — صف تسک‌های ناهمگام با <span class="term" data-term="redis">Redis</span>.',
),

# ================================================================ فصل ۲۴
dict(
    n=24, icon='🕐', title='تسک‌های ناهمگام با Celery', cat=4, mins=110, lvl_label='پیشرفته',
    hero_desc='کارهای زمان‌بر (ایمیل، پردازش تصویر، گزارش) را از چرخه درخواست بیرون می‌کشیم: <span class="term" data-term="celery">Celery</span> + <span class="term" data-term="broker">بروکر</span> <span class="term" data-term="redis">Redis</span>، تسک‌ها، <span class="term" data-term="celery-beat">زمان‌بندی</span>، تلاش مجدد و پایش.',
    s1_intro='کاربر دکمه «انتشار» را می‌زند و سایت سه ثانیه می‌خوابد تا ایمیل ۵۰۰ دنبال‌کننده برود؟ نه! با صف تسک، ویو فقط پیام را در صف می‌گذارد (میلی‌ثانیه) و کارگرها در پس‌زمینه انجامش می‌دهند. این معماری همه سرویس‌های بزرگ است.',
    objectives=[
        'معماری بروکر/کارگر/نتیجه سلری را رسم کنید.',
        'سلری را به پروژه جنگو وصل و اولین تسک را بنویسید.',
        'delay/apply_async و تسک زمان‌بندی‌شده (<span class="term" data-term="celery-beat">beat</span>) استفاده کنید.',
        'تلاش مجدد (retry)، صف‌های جدا و اولویت را پیکربندی کنید.',
        'الگوهای درست (آرگومان ساده، idempotent بودن) را رعایت کنید.',
    ],
    s1_position='<strong>جایگاه فصل:</strong> Redis فصل ۱۹ اینجا نقش بروکر را بازی می‌کند؛ سیگنال‌های فصل ۱۶ (post_published) مصرف‌کننده طبیعی تسک‌ها هستند. ایمیل واقعی پروژه‌ها از اینجا به بعد.',
    roadmap=[
        ('چرا ناهمگام', 'مشکل کارهای کند در درخواست.'),
        ('اتصال سلری', 'تنظیمات و اولین تسک.'),
        ('اجرا و زمان‌بندی', 'worker و beat.'),
        ('قابلیت اطمینان', 'retry، صف‌ها و پایش.'),
    ],
    mind_qs=[
        ('اگر کارگر سلری خاموش باشد چه می‌شود؟',
         '<p>تسک‌ها در صف (بروکر Redis) <strong>جمع می‌شوند</strong> و سایت همچنان سریع پاسخ می‌دهد؛ وقتی کارگر برگشت، از صف برمی‌دارد. ولی اگر Redis پر شود یا تسک‌ها visibility timeout بخورند، رفتار پیچیده‌تر است — برای همین پایش صف لازم است.</p>'),
        ('چرا نباید شیء مدل را به تسک پاس داد؟',
         '<p>تسک در صف <strong>سریالایز</strong> می‌شود (JSON) و ممکن است دقیقه‌ها بعد، در پروسه‌ای دیگر اجرا شود. شیء زنده دیتابیس قابل سریالایز نیست و کهنه می‌شود. قرارداد: فقط pk بفرستید و داخل تسک تازه از دیتابیس بخوانید.</p>'),
        ('idempotent یعنی چه و چرا حیاتی است؟',
         '<p>یعنی اجرای دوبارهٔ تسک، اثر دوباره نگذارد (ایمیل «خوش‌آمد» دو بار نرود). سلری در شرایط شبکه ممکن است تحویل «حداقل یک‌بار» داشته باشد؛ پس هر تسک باید در برابر تکرار مقاوم باشد — با کلید وضعیت یا get_or_create.</p>'),
    ],
    prereq_intro='پیش‌نیازها:',
    prereq=[
        'Redis در دسترس: <code class="inline-code">docker run -d -p 6379:6379 redis:7</code> یا redis-server محلی.',
        'نصب: <code class="inline-code">pip install celery redis</code>.',
        'فصل ۱۶: سیگنال post_published آماده اتصال.',
        'فصل ۱۹: تنظیمات CACHES با Redis (می‌توان همان سرویس، db متفاوت).',
    ],
    prereq_callout=('warn', 'ویندوز',
        'کارگر سلری روی ویندوز رسمی پشتیبانی نمی‌شود؛ از WSL2 یا داکر استفاده کنید. (برای یادگیری موقت: <code class="inline-code">celery --pool=solo</code> کار می‌کند ولی تک‌رشته است.)'),
    concepts=[
        dict(h='۵.۱ معماری سلری', body=[
            ('code', 'سه نقش', 'text', '''┌──────────┐   تسک را در صف می‌گذارد    ┌─────────┐
│ برنامه   │ ─────────────────────────→ │  بروکر  │  (Redis/RabbitMQ)
│ جنگو     │                            └────┬────┘
└──────────┘                                 │ برمی‌دارد و اجرا می‌کند
      ↑ نتیجه/وضعیت                     ┌────▼────┐
      └─────────────────────────────────│  کارگر  │ (پروسه celery)
              result backend (اختیاری)   └─────────┘'''),
            '<ul>'
            '<li><strong>بروکر (Broker)</strong>: صف پیام — Redis ساده‌ترین انتخاب.</li>'
            '<li><strong>کارگر (Worker)</strong>: پروسه جدا که <span class="term" data-term="async-task">تسک‌ها</span> را اجرا می‌کند.</li>'
            '<li><strong>بک‌اند نتیجه</strong>: ذخیره وضعیت/خروجی تسک (برایAsyncResult) — همان Redis کافی است.</li></ul>',
        ]),
        dict(h='۵.۲ اتصال به جنگو', body=[
            ('code', 'config/celery.py', 'python', '''import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("config")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()          # tasks.py هر اپ را پیدا می‌کند'''),
            ('code', 'config/__init__.py — بارگذاری هنگام شروع', 'python', '''from .celery import app as celery_app

__all__ = ("celery_app",)'''),
            ('code', 'settings.py', 'python', '''CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/1"
CELERY_TASK_SERIALIZER = "json"
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TIMEZONE = "Asia/Tehran"
CELERY_TASK_TRACK_STARTED = True
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.example.com"      # یا سرویس واقعی
EMAIL_HOST_USER = os.environ.get("EMAIL_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASS")
EMAIL_USE_TLS = True'''),
        ]),
        dict(h='۵.۳ نوشتن و صدا زدن تسک', body=[
            ('code', 'blog/tasks.py', 'python', '''from celery import shared_task
from django.core.mail import send_mail


@shared_task(bind=True, max_retries=3, default_retry_delay=30)
def send_publish_email(self, post_id, recipient_emails):
    """ایمیل انتشار پست — آرگومان‌ها فقط داده ساده!"""
    from .models import Post                      # import داخل تسک
    post = Post.objects.select_related("author").get(pk=post_id)

    try:
        send_mail(
            subject=f"پست جدید: {post.title}",
            message=post.body[:500],
            from_email=None,
            recipient_list=recipient_emails[:50],
            fail_silently=False,
        )
        return {"sent": min(len(recipient_emails), 50), "post": post_id}
    except Exception as exc:
        raise self.retry(exc=exc)      # تلاش مجدد با فاصله ۳۰ ثانیه'''),
            ('code', 'صدا زدن از ویو/سیگنال', 'python', '''# ساده‌ترین:
send_publish_email.delay(post.pk, emails)

# با گزینه‌ها:
send_publish_email.apply_async(
    args=[post.pk, emails],
    countdown=10,                # ۱۰ ثانیه بعد شروع
    # eta=..., queue="mail", priority=5

# در سیگنال فصل ۱۶:
@receiver(post_published)
def queue_notifications(sender, post, **kwargs):
    emails = list(Follow.objects.filter(author=post.author)
                  .values_list("follower__email", flat=True))
    if emails:
        send_publish_email.delay(post.pk, emails)'''),
            ('callout', 'tip', 'transaction.on_commit',
             'اگر تسک به رکوردی که در همان تراکنش ساخته شده نیاز دارد، صف‌کردن را به بعد از commit موکول کنید: <code class="inline-code">transaction.on_commit(lambda: my_task.delay(obj.pk))</code> — وگرنه کارگر ممکن است رکورد را نبیند (هنوز commit نشده)!' ),
        ]),
        dict(h='۵.۴ زمان‌بندی دوره‌ای با Celery Beat', body=[
            ('code', 'settings.py — تسک‌های زمان‌بندی‌شده', 'python', '''from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    "rebuild-stats-cache": {
        "task": "blog.tasks.rebuild_stats",
        "schedule": crontab(minute=0, hour="*/6"),   # هر ۶ ساعت
    },
    "clear-expired-sessions": {
        "task": "core.tasks.clear_sessions",
        "schedule": crontab(minute=30, hour=3),      # روزانه ۳:۳۰
    },
    "weekly-digest": {
        "task": "blog.tasks.weekly_digest",
        "schedule": crontab(day_of_week="friday", hour=9, minute=0),
    },
}'''),
            ('code', 'اجرا (دو پروسه لازم است)', 'bash', '''# ترمینال ۱ — کارگر:
celery -A config worker -l info

# ترمینال ۲ — زمان‌بند:
celery -A config beat -l info

# ترمینال ۳ — خود جنگو:
python manage.py runserver'''),
            ('callout', 'info', 'django-celery-beat',
             'اگر می‌خواهید زمان‌بندی را از <strong>ادمین</strong> مدیریت کنید (بدون دیپلوی)، پکیج <span class="term" data-term="celery-beat">django-celery-beat</span> جدول PeriodicTask را می‌دهد. برای شروع، CELERY_BEAT_SCHEDULE در کد ساده‌تر و version-controlled است.'),
        ]),
        dict(h='۵.۵ صف‌ها، پایش و الگوهای اطمینان', body=[
            ('code', 'صف جدا برای کارهای سنگین', 'python', '''# task_routes در settings:
CELERY_TASK_ROUTES = {
    "blog.tasks.process_cover_image": {"queue": "heavy"},
    "blog.tasks.send_*": {"queue": "mail"},
}
# کارگرها جدا: celery -A config worker -Q heavy -c 2
#              celery -A config worker -Q mail  -c 8'''),
            ('code', 'بررسی وضعیت تسک', 'python', '''result = send_publish_email.delay(post.pk, emails)
result.id, result.state        # PENDING → STARTED → SUCCESS/FAILURE
result.get(timeout=5)          # ⚠️ فقط در تست/شل؛ در ویو بلاک نکنید!'''),
            ('code', 'پایش', 'bash', '''celery -A config status            # کارگرها زنده‌اند؟
celery -A config inspect active    # تسک‌های در حال اجرا
pip install flower && celery -A config flower   # داشبورد وب :5555'''),
            ('callout', 'danger', 'سه قانون طلایی تسک',
             '① آرگومان‌ها فقط JSON-ساده (pk، رشته، عدد) — شیء مدل/QuerySet ممنوع. ② تسک باید idempotent باشد (تحویل حداقل یک‌بار). ③ تسک کوتاه و بدون بلاک طولانی؛ کار خیلی سنگین را بشکنید (chord/chain یا صفحه‌بندی).' ),
        ]),
    ],
    example_intro='مسیر کامل یک ویژگی واقعی: «انتشار پست» از کلیک تا ایمیل ۵۰۰ دنبال‌کننده:',
    example=[
        ('code', '۱) ویو — فقط صف‌کردن (میلی‌ثانیه)', 'python', '''def publish(request, pk):
    post = get_object_or_404(Post, pk=pk, author__user=request.user)
    post.published = True
    post.save()
    post_published.send(sender=Post, post=post, by=request.user)
    messages.success(request, "منتشر شد! اعلان‌ها در راه‌اند 📨")
    return redirect(post)'''),
        ('code', '۲) سیگنال → تسک', 'python', '''@receiver(post_published, sender=Post)
def fanout_notifications(sender, post, **kwargs):
    emails = list(Follow.objects.filter(
        author=post.author).values_list("follower__email", flat=True))
    # تکه‌تکه برای صف mail: هر تسک حداکثر ۵۰ گیرنده
    for chunk in [emails[i:i + 50] for i in range(0, len(emails), 50)]:
        transaction.on_commit(
            lambda c=chunk: send_publish_email.delay(post.pk, c))'''),
        ('code', '۳) کارگر لاگ می‌زند', 'text', '''[tasks]
  . blog.tasks.send_publish_email
[2026-01-12 10:00:01] Task blog.tasks.send_publish_email
  [a1b2c3] received
[2026-01-12 10:00:02] Task ...[a1b2c3] succeeded in 0.8s:
  {'sent': 50, 'post': 7}'''),
        '<p>تجربه کاربر: کلیک → پیام موفقیت فوری. ۱۰ تسک ایمیل در پس‌زمینه ظرف چند ثانیه انجام می‌شوند. اگر SMTP موقتاً بخوابد، retry با فاصله ۳۰ ثانیه نجات می‌دهد.</p>',
    ],
    workshop_intro='سه تسک واقعی برای وبلاگ بسازید:',
    workshop_tasks=[
        '<strong>کارگاه ۱:</strong> سلری را وصل کنید و تسک <code class="inline-code">debug_ping</code> بنویسید که لاگ بزند؛ با delay صدا بزنید و اجرای آن را در ترمینال کارگر ببینید.',
        '<strong>کارگاه ۲:</strong> تسک «بازسازی کش آمار» (فصل ۱۹) را با beat هر ۶ ساعت زمان‌بندی کنید و دستی هم trigger بزنید.',
        '<strong>کارگاه ۳:</strong> تسک ایمیل با retry بنویسید؛ یک بار عمداً EMAIL_HOST را خراب کنید و رفتار retry و در نهایت FAILURE را در Flower/ترمینال مشاهده کنید.',
    ],
    workshop_answers=[
        ('پاسخ کارگاه ۱',
         '<div class="code-box"><div class="code-head"><span>اولین تسک</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python"># core/tasks.py\nimport logging\nfrom celery import shared_task\n\nlogger = logging.getLogger(__name__)\n\n\n@shared_task\ndef debug_ping(text="pong"):\n    logger.info("PING تسک اجرا شد: %s", text)\n    return text</code></pre></div>'
         '<div class="code-box"><div class="code-head"><span>صدا زدن از shell</span><span class="lang">bash</span></div><pre class="code"><code data-lang="bash">python manage.py shell\n&gt;&gt;&gt; from core.tasks import debug_ping\n&gt;&gt;&gt; r = debug_ping.delay("سلام")\n&gt;&gt;&gt; r.id          # شناسه تسک در صف\n# در ترمینال کارگر: "PING تسک اجرا شد: سلام"</code></pre></div>'
         '<p>اگر چیزی در کارگر ندیدید: کارگر بالا نیست یا CELERY_BROKER_URL غلط است (redis-cli ping → PONG).</p>'),
        ('پاسخ کارگاه ۲',
         '<div class="code-box"><div class="code-head"><span>بازسازی کش آمار</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">@shared_task\ndef rebuild_stats():\n    context = build_stats_context()          # تابع فصل ۱۹\n    version = cache.get_or_set("stats:version", 1, timeout=None)\n    cache.set(f"stats:context:v{version}", context, timeout=None)\n    return "ok"\n\n# settings.py:\nCELERY_BEAT_SCHEDULE = {\n    "rebuild-stats": {\n        "task": "blog.tasks.rebuild_stats",\n        "schedule": crontab(minute=0, hour="*/6"),\n    },\n}</code></pre></div>'
         '<p>اجرای دستی: <code class="inline-code">rebuild_stats.delay()</code> در شل. beat فقط طبق cron صف می‌کند؛ اجرا همچنان کار کارگر است.</p>'),
        ('پاسخ کارگاه ۳',
         '<div class="code-box"><div class="code-head"><span>تسک با retry</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">@shared_task(bind=True, max_retries=3, default_retry_delay=10)\ndef send_mail_task(self, subject, body, to):\n    try:\n        send_mail(subject, body, None, [to], fail_silently=False)\n        return {"to": to, "ok": True}\n    except Exception as exc:\n        logger.warning("تلاش %s ناموفق: %s", self.request.retries, exc)\n        raise self.retry(exc=exc)</code></pre></div>'
         '<p>با EMAIL_HOST خراب: سه تلاش با فاصله ۱۰ ثانیه در لاگ کارگر دیده می‌شود و در نهایت state=FAILURE. در Flower (نصب اختیاری: pip install flower) نمودار تسک‌ها و retryها زنده است. درس عملی: retry برای خطاهای <strong>گذرا</strong> (شبکه/SMTP)؛ برای خطای منطقی (داده بد) بی‌فایده است.</p>'),
    ],
    errors=[
        ('تسک در صف می‌ماند و اجرا نمی‌شود',
         'کارگر بالا نیست یا اپ اشتباه است: <code class="inline-code">celery -A config worker</code> (config = نام پوشه پروژه که celery.py در آن است). با celery -A config status زنده بودن را چک کنید.'),
        ('NotRegistered: blog.tasks.send_publish_email',
         'autodiscover_tasks فایل tasks.py را پیدا نکرده: نام فایل باید دقیقاً tasks.py در ریشه اپ باشد، یا مسیر کامل تسک در register صریح آمده باشد. نام تسک در beat باید با مسیر واقعی بخواند ("app.tasks.name").'),
        ('Object of type Post is not JSON serializable',
         'شیء مدل را به تسک پاس داده‌اید. فقط pk بفرستید و داخل تسک Post.objects.get(pk=...) کنید.'),
        ('کارگر تسک را دو بار اجرا می‌کند',
         'دو کارگر با صف یکسان روی broker یکسان + acks_late و visibility timeout. معمولاً harmless است اگر idempotent باشید — که باید باشید! برای صف Redis، CELERY_BROKER_TRANSPORT_OPTIONS = {"visibility_timeout": بزرگ‌تر از زمان اجرا} تنظیم کنید.'),
        ('ایمیل در توسعه واقعاً ارسال می‌شود!',
         'EMAIL_BACKEND توسعه را روی console بگذارید: <code class="inline-code">django.core.mail.backends.console.EmailBackend</code>؛ فقط در تولید smtp. این اشتباه در تست‌های واقعی آبروریز است!'),
    ],
    errors_callout=('info', 'RabbitMQ یا Redis؟',
        'برای شروع و اکثر پروژه‌ها Redis کافی و ساده است (همان سرویس کش). RabbitMQ وقتی معنا دارد که صف‌های پیچیده، مسیریابی پیشرفته و تضمین تحویل قوی‌تر لازم باشد.'),
    exercises=[
        ('تمرین ۱ — همگام یا ناهمگام؟',
         '<p><strong>سوال:</strong> کدام کارها به تسک سلری بروند؟ (الف) ارسال ایمیل خوش‌آمد (ب) رندر صفحه فهرست (ج) ساخت بندانگشتی از عکس آپلودی (د) محاسبه جمع سبد خرید در صفحه (ه) تولید گزارش PDF روزانه</p>'
         '<p><strong>پاسخ:</strong> الف ✅ • ب ❌ (کار اصلی درخواست است) • ج ✅ (پردازش سنگین) • د ❌ (فوری و سبک) • ه ✅ + beat روزانه. قاعده: «کاربر منتظر نتیجه است؟ → همگام؛ اثر جانبی یا سنگین است؟ → تسک».</p>'),
        ('تمرین ۲ — طراحی retry',
         '<p><strong>سوال:</strong> برای خطای «SMTP timeout» و «رکورد Post وجود ندارد» رفتار retry درست چیست؟</p>'
         '<p><strong>پاسخ:</strong> SMTP timeout = گذرا → self.retry با max_retries و فاصله فزاینده. Post.DoesNotExist = دائمی → retry بی‌معناست؛ لاگ ERROR و خاتمه (یا حذف تسک کهنه از صف). تفکیک خطای گذرا/دائمی مهارت اصلی تسک‌نویسی است.</p>'),
        ('تمرین ۳ — شمارش با race',
         '<p><strong>سناریو:</strong> تسک «افزایش شمارنده دانلود» هم‌زمان از دو کارگر اجرا می‌شود. چرا obj.count += 1; obj.save() اشتباه و چه جایگزینی درست است؟</p>'
         '<p><strong>پاسخ:</strong> read-modify-write رقابتی: دو کارگر یک مقدار قدیمی می‌خوانند و یکی گم می‌شود. درست: <code class="inline-code">Model.objects.filter(pk=...).update(count=F("count") + 1)</code> — اتمی در سطح SQL (همان درس فصل ۱۵، این بار در دنیای تسک‌ها).</p>'),
    ],
    quiz=[
        dict(q='در معماری سلری، «بروکر» چیست؟',
             opts=['کارگر اجراکننده', 'صف پیامی که تسک‌ها بین برنامه و کارگر در آن قرار می‌گیرند (Redis/RabbitMQ)',
                   'دیتابیس جنگو', 'داشبورد پایش'],
             ans='b', explain='بروکر واسطه صف است؛ جنگو تسک را در آن می‌گذارد و کارگر برمی‌دارد. نتیجه در result backend (اختیاری).'),
        dict(q='کدام آرگومان برای تسک سلری درست است؟',
             opts=['شیء Post', 'post.pk (داده ساده JSON)', 'QuerySet', 'شیء request'],
             ans='b', explain='تسک سریالایز و بعداً در پروسه دیگر اجرا می‌شود؛ فقط داده ساده و شناسه، و خواندن تازه از دیتابیس داخل تسک.'),
        dict(q='my_task.delay(a) معادل چیست؟',
             opts=['my_task(a)', 'my_task.apply_async(args=[a])', 'my_task.run(a)', 'my_task.get(a)'],
             ans='b', explain='delay میان‌بر apply_async بدون گزینه است؛ با apply_async می‌توانید countdown/eta/queue/priority بدهید.'),
        dict(q='Celery Beat چه نقشی دارد؟',
             opts=['تسک‌ها را اجرا می‌کند', 'طبق زمان‌بندی، تسک‌ها را در صف می‌گذارد (اجرا همچنان کار worker است)',
                   'نتایج را ذخیره می‌کند', 'صف را پاک می‌کند'],
             ans='b', explain='beat = زمان‌بند؛ worker = مجری. هر دو پروسه باید بالا باشند تا تسک دوره‌ای واقعاً اجرا شود.'),
        dict(q='چرا تسک باید idempotent باشد؟',
             opts=['برای سرعت', 'چون تحویل ممکن است «حداقل یک‌بار» باشد و اجرای دوباره نباید اثر مضاعف بگذارد',
                   'الزام JSON', 'برای retry لازم نیست'],
             ans='b', explain='شبکه/visibility timeout ممکن است تسک را دو بار به کارگر بدهد؛ طراحی مقاوم به تکرار (get_or_create، کلید وضعیت) اثر دوباره را خنثی می‌کند.'),
        dict(q='transaction.on_commit(lambda: task.delay(pk)) چه مشکلی را حل می‌کند؟',
             opts=['کندی', 'کارگر ممکن است رکوردی که هنوز commit نشده را در دیتابیس نبیند',
                   'سریالایز', 'retry'],
             ans='b', explain='تسک قبل از commit صف شود، کارگر سریع‌تر از دیتابیس می‌رسد و DoesNotExist می‌گیرد؛ on_commit صف‌کردن را به بعد از ثبت قطعی موکول می‌کند.'),
    ],
    project_title='زیرساخت ناهمگام وبلاگ',
    project_intro='همه کارهای پس‌زمینه وبلاگ را به صف منتقل کنید.',
    project_checklist=[
        'اتصال کامل سلری (celery.py، __init__، تنظیمات Redis).',
        'تسک ایمیل انتشار با chunking و retry (مسیر مثال فصل).',
        'تسک ساخت بندانگشتی کاور با Pillow (after upload، با on_commit).',
        'دو زمان‌بندی beat: بازسازی آمار (۶ ساعته) و پاک‌سازی نشست‌ها (روزانه).',
        'Flower یا inspect برای پایش + مستند «چطور محلی اجرا کنیم» در README.',
    ],
    project_callout=('tip', 'در استقرار (فصل ۲۶)',
        'worker و beat باید به‌عنوان سرویس‌های جدا (systemd/supervisor/داکر کامپوز) کنار Gunicorn بالا بمانند — «runserver و یک celery» فقط برای توسعه است.'),
    summary_items=[
        'معماری: برنامه → <span class="term" data-term="broker">بروکر</span> (<span class="term" data-term="redis">Redis</span>) → کارگر؛ نتیجه در backend.',
        'tasks.py با @shared_task؛ آرگومان‌ها فقط داده ساده (pk).',
        'delay/apply_async؛ on_commit برای رکوردهای درون تراکنش.',
        'beat برای دوره‌ای‌ها (crontab)؛ worker+beat دو پروسه‌اند.',
        'retry برای خطای گذرا؛ idempotent برای تحویل تکراری؛ صف جدا برای بارهای متفاوت.',
    ],
    golden='ویو را سریع نگه دارید: هر کاری که کاربر منتظرش نیست، مال صف است.',
    faq=[
        ('برای پروژه کوچک سلری سنگین نیست؟',
         '<p>گزینه سبک‌تر: <strong>django-q2</strong> یا huey (کمتر از سلری پیچیده‌اند). ولی سلری استاندارد صنعت است و یادگیری‌اش قابل حمل. حتی با یک کارگر ساده شروع کنید.</p>'),
        ('چطور بفهمم تسک شکست خورد؟',
         '<p>state=FAILURE با AsyncResult(id)، لاگ کارگر (Traceback کامل)، و در پروژه جدی: ارسال به Sentry (celery integration) + هشدار روی صف طولانی. نتیجه تسک‌ها را با result_backend قابل بررسی نگه دارید.</p>'),
        ('progress bar برای کار طولانی ممکن است؟',
         '<p>بله: داخل تسک self.update_state(state="PROGRESS", meta={"percent": 40}) و در فرانت با polling روی AsyncResult. الگوی رایج برای آپلود/پردازش ویدیو و ایمیل انبوه.</p>'),
    ],
    next_step='سایت تک‌زبانه نیست: <strong>فصل ۲۵</strong> — <span class="term" data-term="i18n">بومی‌سازی</span>: ترجمه قالب‌ها، فرمت تاریخ/عدد فارسی، منطقه‌های زمانی و سایت چندزبانه واقعی.',
),

# ================================================================ فصل ۲۵
dict(
    n=25, icon='🌍', title='چندزبانه‌سازی و بومی‌سازی (i18n/L10n)', cat=4, mins=80, lvl_label='متوسط',
    hero_desc='سایت چندزبانه با <span class="term" data-term="i18n">i18n</span> جنگو: gettext در کد و قالب، فایل‌های .po/.mo، تغییر زبان کاربر، فرمت تاریخ و عدد فارسی و منطقه زمانی.',
    s1_intro='کاربر فارسی‌زبان «۱۴۰۴/۱۰/۲۲» و کاربر انگلیسی «Jan 12, 2026» می‌بیند — از یک کد! بومی‌سازی یعنی جداکردن «متن و فرمت» از «منطق». جنگو ابزار کاملی دارد که حتی ادمین خودش هم با آن فارسی شده.',
    objectives=[
        'زیرساخت i18n جنگو را فعال و LocaleMiddleware را درست جای‌گذاری کنید.',
        'رشته‌ها را با gettext/_ در کد و {% translate %} در قالب علامت بزنید.',
        'با makemessages/compilemessages فایل ترجمه بسازید و پر کنید.',
        'زبان را با کوکی/URL/هدر انتخاب کنید و تعویض زبان بسازید.',
        'فرمت تاریخ/عدد (L10N) و منطقه زمانی را برای فارسی تنظیم کنید.',
    ],
    s1_position='<strong>جایگاه فصل:</strong> قالب‌ها (۱۰)، میدلور (۱۷) و کوکی/نشست (۱۸) مستقیماً استفاده می‌شوند؛ سایت چندزبانه در پروژه نهایی (۳۰) اختیار می‌شود.',
    roadmap=[
        ('فعال‌سازی', 'تنظیمات و میدلور.'),
        ('علامت‌گذاری', '_ در کد، translate در قالب.'),
        ('گردش ترجمه', 'makemessages تا compile.'),
        ('انتخاب زبان و L10N', 'کوکی، URL و فرمت‌ها.'),
    ],
    mind_qs=[
        ('gettext دقیقاً چه می‌کند؟',
         '<p>رشته اصلی (معمولاً انگلیسی) را «کلید» می‌گیرد و در کاتالوگ ترجمه زبان <strong>فعال فعلی</strong> دنبالش می‌گردد؛ اگر بود ترجمه، نبود همان اصلی را برمی‌گرداند. پس بدون فایل ترجمه هم کد کار می‌کند — i18n تدریجی ممکن است.</p>'),
        ('LANGUAGE_CODE = "fa" کافی نیست؟',
         '<p>برای «پیش‌فرض فارسی» بله. ولی برای سایت <strong>چندزبانه</strong> باید زبان هر درخواست تشخیص داده شود: <span class="term" data-term="middleware">LocaleMiddleware</span> به‌ترتیب <span class="term" data-term="url">URL</span> (i18n_patterns)، <span class="term" data-term="cookie">کوکی</span> django_language، هدر Accept-Language و در نهایت LANGUAGE_CODE را چک می‌کند.</p>'),
        ('.po و .mo چه فرقی دارند؟',
         '<p>.po فایل متنی قابل ویرایش ترجمه‌هاست (msgid/msgstr)؛ .mo نسخه باینری کامپایل‌شده است که جنگو <strong>فقط آن</strong> را می‌خواند. پس بعد از هر ویرایش .po باید compilemessages بزنید — وگرنه تغییرات دیده نمی‌شوند (تله رایج!).</p>'),
    ],
    prereq_intro='پیش‌نیازها:',
    prereq=[
        'gettext روی سیستم: در لینوکس <code class="inline-code">sudo apt install gettext</code>؛ در ویندوز به PATH اضافه شود.',
        'پروژه وبلاگ با قالب‌های base/list/detail (فصل ۱۰).',
        'درک میدلور (فصل ۱۷) و کوکی (فصل ۱۸).',
        'آشنایی با ساختار پوشه locale.',
    ],
    prereq_callout=('warn', 'خطای رایج makemessages',
        'اگر <code class="inline-code">CommandError: Can\'t find msguniq</code> گرفتید، gettext نصب نیست. برای زبان فارسی: <code class="inline-code">python manage.py makemessages -l fa</code> (کد زبان دو حرفی، نه fa_IR مگر منطقه خاصی بخواهید).'),
    concepts=[
        dict(h='۵.۱ فعال‌سازی زیرساخت', body=[
            ('code', 'settings.py', 'python', '''from django.utils.translation import gettext_lazy as _

USE_I18N = True                    # ترجمه رشته‌ها
USE_TZ = True                      # منطقه زمانی آگاه
TIME_ZONE = "Asia/Tehran"

LANGUAGE_CODE = "fa"               # پیش‌فرض
LANGUAGES = [
    ("fa", _("فارسی")),
    ("en", _("English")),
]
LOCALE_PATHS = [BASE_DIR / "locale"]

MIDDLEWARE = [
    ...,
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",     # ← بعد از session،
    "django.contrib.auth.middleware.AuthenticationMiddleware",  # ← قبل از auth
    ...,
]'''),
            ('callout', 'warn', 'gettext_lazy در settings',
             'در سطح ماژول <span class="term" data-term="settings">settings</span>/models/forms زبان هنوز «فعال» نشده؛ اگر gettext عادی را صدا بزنید، ترجمه یک‌بار برای همیشه (به زبان پیش‌فرض) ثابت می‌شود. در این جایگاه‌ها همیشه <strong>gettext_lazy</strong> (با alias <code class="inline-code">_</code>).'),
        ]),
        dict(h='۵.۲ علامت‌گذاری رشته‌ها', body=[
            ('code', 'در کد پایتون (ویو، مدل، فرم)', 'python', '''from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "text"]
        labels = {"name": gettext_lazy("نام شما")}   # lazy در فرم/مدل

    def clean_text(self):
        text = self.cleaned_data["text"]
        if "تبلیغ" in text:
            raise forms.ValidationError(
                _("متن تبلیغاتی مجاز نیست."))       # gettext در متد (اجرا)
        return text


def welcome(request):
    messages.success(request, _("خوش آمدید!"))
    # با پارامتر:
    msg = _("شما %(count)s پست دارید") % {"count": n}
    # جمع‌بندی (singular/plural):
    from django.utils.translation import ngettext
    ngettext("%(n)d روز", "%(n)d روز", days) % {"n": days}'''),
            ('code', 'در قالب', 'html', '''{% load i18n %}

<h1>{% translate "پست‌های اخیر" %}</h1>
<p>{% blocktranslate count n=posts|length %}
     یک پست پیدا شد
   {% plural %}
     {{ n }} پست پیدا شد
   {% endblocktranslate %}</p>

{# با متغیر #}
{% translate post.title as title_tr %}

{# کامنت برای مترجم #}
{% translate "Submit" as submit_label %}'''),
            ('callout', 'tip', 'قاعده انگشتی',
             'هر رشته‌ای که <strong>کاربر می‌بیند</strong> علامت بزنید؛ رشته‌های لاگ، کلیدهای داخلی و slug را نه. gettext (اجرا) در ویو/متد؛ gettext_lazy در کلاس/ماژول/فرم/مدل.'),
        ]),
        dict(h='۵.۳ گردش کار ترجمه: po → mo', body=[
            ('code', 'دستورات', 'bash', '''# ۱) استخراج رشته‌ها → locale/fa/LC_MESSAGES/django.po
python manage.py makemessages -l fa

# (اختیاری) برای JS هم: makemessages -d djangojs -l fa

# ۲) ویرایش django.po — هر msgid را ترجمه کنید
# ۳) کامپایل → django.mo (جنگو فقط این را می‌خواند)
python manage.py compilemessages

# بررسی همه زبان‌ها
python manage.py makemessages --all'''),
            ('code', 'ساختار فایل django.po', 'text', '''# locale/fa/LC_MESSAGES/django.po
msgid ""
msgstr ""
"Content-Type: text/plain; charset=UTF-8\\n"
"Plural-Forms: nplurals=2; plural=(n > 1);\\n"

#: blog/views.py:42 templates/blog/post_list.html:8
msgid "پست‌های اخیر"
msgstr "پست‌های اخیر"          # ← فارسی: msgid خودش فارسی باشد

#: blog/forms.py:20
msgid "متن تبلیغاتی مجاز نیست."
msgstr "متن تبلیغاتی مجاز نیست."

msgid "You have %(count)s posts"
msgstr "شما %(count)s پست دارید"'''),
            ('callout', 'info', 'msgid فارسی یا انگلیسی؟',
             'دو مکتب: ① msgid انگلیسی و ترجمه فارسی (استاندارد جهانی، ابزارها راحت‌تر) ② msgid فارسی (زبان پیش‌فرض بدون po کار می‌کند). پروژه شما فارسی‌محور است → مکتب ② منطقی است؛ ولی <strong>یکدست</strong> بمانید.'),
        ]),
        dict(h='۵.۴ انتخاب و تعویض زبان', body=[
            ('code', 'الف) URL زبان‌دار (i18n_patterns)', 'python', '''# config/urls.py
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path("admin/", admin.site.urls),          # بدون پیشوند زبان
]
urlpatterns += i18n_patterns(
    path("", include("blog.urls")),
    path("accounts/", include("accounts.urls")),
)
# → /fa/blog/... و /en/blog/...
# قالب‌ها: {% url "set_language" %} باید بیرون i18n_patterns باشد'''),
            ('code', 'ب) ویوی تعویض زبان (کوکی)', 'python', '''# urls: path("i18n/", include("django.conf.urls.i18n"))
# جنگو set_language آماده دارد (POST با فیلد language):''',),
            ('code', 'قالب: سوییچر زبان', 'html', '''{% load i18n %}
<form action="{% url "set_language" %}" method="post">
  {% csrf_token %}
  <input name="next" type="hidden" value="{{ redirect_to }}">
  <select name="language" onchange="this.form.submit()">
    {% get_current_language as LANGUAGE_CODE %}
    {% get_available_languages as LANGUAGES %}
    {% for code, name in LANGUAGES %}
      <option value="{{ code }}" {% if code == LANGUAGE_CODE %}selected{% endif %}>
        {{ name }}
      </option>
    {% endfor %}
  </select>
</form>'''),
            ('code', 'ج) تنظیم RTL/LTR در قالب پایه', 'html', '''{% load i18n %}
{% get_current_language_bidi as RTL %}
<html lang="{% get_current_language as l %}{{ l }}" dir="{{ RTL|yesno:"rtl,ltr" }}">'''),
        ]),
        dict(h='۵.۵ L10N: فرمت تاریخ، عدد و پول', body=[
            ('code', 'قالب — فرمت‌های محلی', 'html', '''{% load l10n i18n %}

{# تاریخ بر اساس زبان فعال (با formats.py سفارشی‌سازی می‌شود) #}
{{ post.created_at|date }}
{% localize off %}{{ value }}{% endlocalize %}   {# بدون بومی‌سازی #}'''),
            ('code', 'locale/fa/formats.py — فرمت‌های فارسی', 'python', '''DATE_FORMAT = "j F Y"               # ۲۲ دی ۱۴۰۴ (با jdatetime)
DATETIME_FORMAT = "j F Y، ساعت G:i"
SHORT_DATE_FORMAT = "Y/m/d"
THOUSAND_SEPARATOR = "٬"            # جداکننده هزارگان فارسی
DECIMAL_SEPARATOR = "٫"
NUMBER_GROUPING = 3'''),
            ('code', 'تاریخ شمسی در قالب (jdatetime/persian-datetime)', 'python', '''# pip install jdatetime
import jdatetime

def to_jalali(dt):
    jd = jdatetime.datetime.fromgregorian(datetime=dt)
    return jd.strftime("%Y/%m/%d %H:%M")

# در ویو: context["jalali_date"] = to_jalali(post.created_at)
# یا با فیلتر سفارشی قالب (تمرین ۳)'''),
            ('callout', 'info', 'تقویم شمسی در جنگو',
             'i18n خود جنگو تقویم جلالی ندارد؛ تاریخ‌ها میلادی ذخیره و با کتابخانه‌هایی مثل jdatetime یا django-jalali (فیلدهای مدل JalaliDateField) نمایشی تبدیل می‌شوند. ذخیره همیشه UTC/میلادی بماند — تبدیل فقط در نمایش.'),
        ]),
    ],
    example_intro='وبلاگ دوزبانه واقعی — از base.html تا صفحه پست:',
    example=[
        ('code', 'templates/base.html (گزیده)', 'html', '''{% load i18n %}
{% get_current_language as LANG %}
{% get_current_language_bidi as IS_RTL %}
<!doctype html>
<html lang="{{ LANG }}" dir="{% if IS_RTL %}rtl{% else %}ltr{% endif %}">
<head>
  <title>{% block title %}{% translate "وبلاگ من" %}{% endblock %}</title>
  <link rel="stylesheet" href="{% static \'css/style.css\' %}">
</head>
<body>
<nav>
  <a href="{% url \'blog:list\' %}">{% translate "خانه" %}</a>
  <a href="{% url \'blog:about\' %}">{% translate "درباره" %}</a>
  {% include "partials/lang_switcher.html" %}
</nav>
{% block content %}{% endblock %}
</body>
</html>'''),
        ('code', 'views.py', 'python', '''from django.utils.translation import gettext as _


def post_list(request):
    posts = Post.objects.filter(published=True)
    q = request.GET.get("q")
    if q:
        posts = posts.filter(title__icontains=q)
        messages.info(request, _("نتایج جست‌وجو برای «%(q)s»") % {"q": q})
    return render(request, "blog/post_list.html", {"posts": posts})'''),
        ('code', 'گردش کار کامل', 'bash', '''python manage.py makemessages -l fa -l en
# ویرایش locale/en/LC_MESSAGES/django.po (ترجمه انگلیسی رشته‌های فارسی)
python manage.py compilemessages
# ری‌استارت → /en/ سایت انگلیسی، /fa/ فارسی (با i18n_patterns)
# تعویض با سوییچر → کوکی django_language ست می‌شود'''),
        '<p>نکته معماری: <strong>محتوای پست‌ها</strong> (عنوان/بدنه <span class="term" data-term="database">دیتابیس</span>) با gettext ترجمه نمی‌شود! برای محتوای دیتابیسی چندزبانه از django-modeltranslation یا فیلدهای title_en/title_fa استفاده کنید — gettext فقط برای «رشته‌های رابط» است.</p>',
    ],
    workshop_intro='وبلاگ را دوزبانه کنید:',
    workshop_tasks=[
        '<strong>کارگاه ۱:</strong> زیرساخت i18n را فعال کنید، base.html را با get_current_language_bidi دایرکتیک کنید و سوییچر زبان (کوپیی از مثال) بگذارید.',
        '<strong>کارگاه ۲:</strong> ده رشته رابط (ناوبری، عنوان صفحه فهرست، پیام‌های فرم کامنت، دکمه‌ها) را علامت بزنید، makemessages -l en بزنید و ترجمه انگلیسی را پر کنید.',
        '<strong>کارگاه ۳:</strong> یک فیلتر سفارشی قالب بنویسید: <code class="inline-code">{{ post.created_at|jalali:"%Y/%m/%d" }}</code> با jdatetime و آن را در صفحه جزئیات استفاده کنید.',
    ],
    workshop_answers=[
        ('پاسخ کارگاه ۱',
         '<p>تنظیمات ۵.۱ + الگوی ۵.۴ج را کپی کنید؛ i18n_patterns را در urls اصلی بپیچید. سوییچر: فایل partials/lang_switcher.html از مفهوم ۵.۴ب را include کنید. تست سریع: صفحه را با /en/ باز کنید — اگر dir=ltr شد و متن‌های translate‌شده عوض شدند، زیرساخت سالم است.</p>'
         '<p><strong>دام رایج:</strong> بعد از افزودن i18n_patterns، همه URLهای قبلی (مثل /blog/) به /fa/blog/ ریدایرکت می‌شوند؛ لینک‌های سخت‌کدشده در قالب/جاوااسکریپت را با {% url %} جایگزین کنید تا خودکار درست شوند.</p>'),
        ('پاسخ کارگاه ۲',
         '<div class="code-box"><div class="code-head"><span>نمونه علامت‌گذاری و po</span><span class="lang">text</span></div><pre class="code"><code data-lang="text"># قالب:\n&lt;h1&gt;{% translate "پست‌های اخیر" %}&lt;/h1&gt;\n&lt;button&gt;{% translate "ارسال نظر" %}&lt;/button&gt;\n\n# forms.py:\nraise forms.ValidationError(_("متن تبلیغاتی مجاز نیست."))\n\n# بعد از makemessages -l en در django.po:\nmsgid "پست‌های اخیر"\nmsgstr "Recent Posts"\n\nmsgid "ارسال نظر"\nmsgstr "Submit Comment"\n\nmsgid "متن تبلیغاتی مجاز نیست."\nmsgstr "Advertising text is not allowed."\n\n# compilemessages + ری‌استارت</code></pre></div>'
         '<p>اگر ترجمه دیده نشد: ① compilemessages زده‌اید؟ ② .mo کنار همان .po در locale/en/LC_MESSAGES است؟ ③ زبان فعال واقعاً en است؟ (با {{ LANGUAGE_CODE }} در قالب یا get_language() در شل چک کنید.) ④ رشته <strong>دقیقاً</strong> مثل msgid است (فاصله/نیم‌فاصله!).</p>'),
        ('پاسخ کارگاه ۳',
         '<div class="code-box"><div class="code-head"><span>blog/templatetags/jalali.py</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">import jdatetime\nfrom django import template\n\nregister = template.Library()\n\n\n@register.filter(name="jalali")\ndef jalali(value, fmt="%Y/%m/%d"):\n    """تبدیل datetime میلادی (UTC-aware) به رشته شمسی"""\n    if value is None:\n        return ""\n    jd = jdatetime.datetime.fromgregorian(datetime=value)\n    return jd.strftime(fmt)\n\n# قالب: {% load jalali %} → {{ post.created_at|jalali }}\n# با ساعت: {{ post.created_at|jalali:"%Y/%m/%d %H:%M" }}</code></pre></div>'
         '<p>ساختار templatetags را از فصل ۱۰ می‌شناسید (پوشه + __init__.py + register). جdatetime خودش timezone-aware را به تهران تبدیل نمی‌کند؛ اگر USE_TZ دارید اول با timezone.localtime(value) محلی کنید بعد تبدیل — وگرنه ساعت ۳:۳۰ UTC را ۳:۳۰ شمسی نشان می‌دهد!</p>'),
    ],
    errors=[
        ('ترجمه‌ها اعمال نمی‌شوند',
         'زنجیره را چک کنید: ① compilemessages اجرا و django.mo ساخته شده؟ ② LOCALE_PATHS درست است؟ ③ LocaleMiddleware در MIDDLEWARE هست؟ ④ msgid دقیقاً برابر رشته کد است (نیم‌فاصله‌ها!)؟ ۹۰٪ موارد = فراموشی compile.'),
        ('msguniq/msgmerge not found',
         'gettext نصب نیست: apt install gettext (لینوکس) یا باینری ویندوز در PATH. روی برخی ویندوزها python manage.py makemessages -l fa --no-location هم لازم می‌شود.'),
        ('رشته در settings/models ترجمه نمی‌شود یا همیشه یک زبان است',
         'gettext عادی به‌جای gettext_lazy در سطح ماژول/کلاس استفاده شده؛ رشته یک‌بار در زمان import ارزیابی و ثابت شده. اصلاح به lazy (و در قالب با {% translate %} که lazy-safe است).'),
        ('با i18n_patterns همه لینک‌ها ۴۰۴ شدند',
         'لینک‌های سخت‌کد (href="/blog/") یا reverse در جاوااسکریپت بدون پیشوند زبان‌اند. همه را {% url %} کنید؛ برای JS از javascript_catalog یا data-attribute استفاده کنید.'),
        ('ساعت‌ها ۳:۳۰ اختلاف دارند',
         'TIME_ZONE یا تبدیل UTC: تاریخ‌ها در دیتابیس UTC ذخیره می‌شوند (USE_TZ=True)؛ برای نمایش timezone.localtime() یا در قالب، جنگو خودش محلی می‌کند — مگر در فیلتر سفارشی jdatetime که دستی لازم است (کارگاه ۳).'),
    ],
    errors_callout=None,
    exercises=[
        ('تمرین ۱ — gettext یا lazy؟',
         '<p><strong>سوال:</strong> کدام نوع در هر جایگاه؟ (الف) verbose_name فیلد مدل (ب) messages.success داخل ویو (ج) label فیلد فرم در Meta (د) رشته در بدنه تابع clean</p>'
         '<p><strong>پاسخ:</strong> الف → lazy (کلاس/ماژول) • ب → gettext عادی (زمان اجرا) • ج → lazy (Meta کلاس است) • د → gettext عادی. قاعده: «سطح کلاس/ماژول = lazy، داخل تابع = عادی».</p>'),
        ('تمرین ۲ — طراحی URL دوزبانه',
         '<p><strong>سوال:</strong> مزایا/معایب سه طرح: ① پیشوند مسیر /en/blog/ (ب) زیردامنه en.site.com (ج) فقط کوکی بدون تغییر URL؟</p>'
         '<p><strong>پاسخ:</strong> ① ساده‌ترین با جنگو (i18n_patterns)، SEO خوب با hreflang — پیشنهاد ما • ② جداسازی تمیزتر ولی نیاز به تنظیمات دامنه/میزبانی • ③ بدون هزینه URL ولی اشتراک‌گذاری لینک زبان را منتقل نمی‌کند و SEO ضعیف (یک URL دو محتوا).</p>'),
        ('تمرین ۳ — محتوا یا رابط؟',
         '<p><strong>سوال:</strong> کدام با gettext و کدام با راه‌حل دیتابیسی؟ (الف) عنوان صفحه «تماس با ما» (ب) عنوان یک پست خاص در دیتابیس (ج) پیام خطای فرم (د) نام دسته‌بندی‌ها که مدیر سایت فارسی/انگلیسی‌شان را وارد می‌کند</p>'
         '<p><strong>پاسخ:</strong> الف ✅ gettext • ب ❌ مدل ترجمه‌پذیر (django-modeltranslation یا فیلد title_en) • ج ✅ gettext • د ❌ دیتابیس (فیلد دوزبانه در مدل Category). مرز: «رشته‌های کد = gettext؛ رکوردهای دیتابیس = ترجمه مدل».</p>'),
    ],
    quiz=[
        dict(q='gettext_lazy کجا ضروری است؟',
             opts=['داخل بدنه ویوها', 'در سطح ماژول/کلاس (settings، verbose_name مدل، Meta فرم‌ها)',
                   'در قالب‌ها', 'فقط در تست‌ها'],
             ans='b', explain='در import زمان فعال‌بودن زبان معلوم نیست؛ lazy ارزیابی را به زمان استفاده موکول می‌کند. داخل توابع gettext عادی کافی است.'),
        dict(q='ترتیب makemessages → compilemessages چرا است؟',
             opts=['فرقی ندارد', 'makemessages رشته‌ها را در django.po استخراج می‌کند؛ ترجمه دستی؛ compilemessages نسخه باینری django.mo را می‌سازد که جنگو می‌خواند',
                   'compile اول است', 'هر دو خودکار ترجمه می‌کنند'],
             ans='b', explain='po = متنی قابل ویرایش، mo = باینری مصرفی. بدون compile ترجمه‌ها اثر نمی‌کنند — رایج‌ترین تله فصل.'),
        dict(q='LocaleMiddleware زبان کاربر را با چه اولویتی تشخیص می‌دهد؟',
             opts=['همیشه LANGUAGE_CODE', 'پیشوند URL (i18n_patterns) ← کوکی django_language ← هدر Accept-Language ← LANGUAGE_CODE',
                   'نشست کاربر', 'تصادفی'],
             ans='b', explain='اول صریح‌ترین سیگنال (URL)، بعد انتخاب قبلی کاربر (کوکی)، بعد ترجیح مرورگر و در نهایت پیش‌فرض.'),
        dict(q='برای ترجمه «عنوان پست‌ها» (رکورد دیتابیس) چه باید کرد؟',
             opts=['gettext روی post.title', 'راه‌حل ترجمه مدل: django-modeltranslation یا فیلدهای title_fa/title_en',
                   'compilemessages', 'ممکن نیست'],
             ans='b', explain='gettext فقط رشته‌های ثابت کد را ترجمه می‌کند؛ محتوای دیتابیس ساختار خودش را می‌خواهد (فیلد به‌ازای زبان).'),
        dict(q='get_current_language_bidi در قالب چه می‌دهد؟',
             opts=['نام زبان', 'True/False راست‌به‌چپ بودن زبان فعال — برای dir=rtl',
                   'فهرست زبان‌ها', 'ترجمه رشته'],
             ans='b', explain='فارسی/عربی → True؛ با آن dir و استایل‌های جهت‌دار را شرطی می‌کنید — کلید قالب‌های دوزبانه RTL/LTR.'),
        dict(q='با USE_TZ=True تاریخ‌ها در دیتابیس چطور ذخیره می‌شوند؟',
             opts=['به وقت تهران', 'UTC — و هنگام نمایش به منطقه زمانی فعال تبدیل می‌شوند',
                   'بدون منطقه زمانی', 'به وقت سرور'],
             ans='b', explain='ذخیره UTC استاندارد جهانی است؛ timezone.localtime و قالب‌ها برای نمایش تبدیل می‌کنند. TIME_ZONE و ترجیح کاربر فقط نمایش را عوض می‌کند.'),
    ],
    project_title='وبلاگ دوزبانه فارسی/انگلیسی',
    project_intro='سایت را کاملاً دوزبانه کنید — همان پروژه‌ای که در فصل ۳۰ گسترش می‌یابد.',
    project_checklist=[
        'i18n_patterns + LocaleMiddleware + سوییچر زبان در navbar.',
        'حداقل ۲۵ رشته رابط علامت‌خورده (ناوبری، فرم‌ها، پیام‌ها، خطاهای 404).',
        'فایل‌های po پرشده برای fa و en + compile شده.',
        'قالب با dir پویا و تست دستی هر دو زبان (اسکرین‌شات).',
        'نمایش تاریخ شمسی با فیلتر jalali در صفحه جزئیات.',
    ],
    project_callout=('tip', 'hreflang برای SEO',
        'در base.html برای هر زبان لینک متناوب بگذارید: <code class="inline-code">&lt;link rel="alternate" hreflang="en" href="...&gt;</code> تا موتورهای جست‌وجو نسخه درست را به کاربر نشان دهند.'),
    summary_items=[
        'USE_I18N + LocaleMiddleware + LANGUAGES + LOCALE_PATHS زیرساخت است.',
        'در کد gettext/_ و در قالب {% translate %}؛ سطح کلاس = lazy.',
        'گردش: makemessages → ویرایش po → compilemessages (mo).',
        'انتخاب زبان: <span class="term" data-term="url">URL</span> ← <span class="term" data-term="cookie">کوکی</span> ← Accept-Language ← پیش‌فرض.',
        'L10N: formats.py، جداکننده فارسی، تاریخ شمسی با jdatetime؛ محتوای دیتابیس راه حل جدا می‌خواهد.',
    ],
    golden='منطق یک‌بار نوشته می‌شود؛ زبان و فرمت، لایه نمایشی‌اند که کاربر انتخاب می‌کند.',
    faq=[
        ('چطور زبان را در پروفایل کاربر ذخیره کنم؟',
         '<p>فیلد language در <span class="term" data-term="model">مدل</span> Profile؛ در ویوی تنظیمات پروفایل، هم کوکی set_language را ست کنید و هم ترجمه‌ها را با translation.activate(lang) برای همان درخواست. ورود: در سیگنال user_logged_in زبان پروفایل را activate کنید.</p>'),
        ('po را با چه ابزاری ویرایش کنم؟',
         '<p>ویرایشگر متنی کافی است، ولی ابزارهای گرافیکی مثل Poedit یا وب‌اپ‌هایی مثل Weblate/Transifex برای تیم مترجم عالی‌اند (fuzzy-marking، حافظه ترجمه).</p>'),
        ('ترجمه رشته‌های خود جنگو (ادمین، پیام‌های اعتبارسنجی) چطور می‌آید؟',
         '<p>خودکار! جنگو کاتالوگ ترجمه داخلی دارد و پیام‌های آماده (مثل "This field is required.") با makemessages در po شما هم ظاهر می‌شوند (به‌عنوان ارجاع) — کافی است LANGUAGE_CODE/LANGUAGES را داشته باشید؛ ادمین فارسی جنگو نمونه‌اش است.</p>'),
    ],
    next_step='سایت چندزبانه آماده پرواز است: <strong>فصل ۲۶</strong> — <span class="term" data-term="deployment">استقرار</span> واقعی با Gunicorn، Nginx، Postgres و داکر روی VPS.',
),
]
