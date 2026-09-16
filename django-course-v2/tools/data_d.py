# -*- coding: utf-8 -*-
"""داده محتوای فصل‌های ۱۶ تا ۲۰ — سیگنال، میدلور، نشست، کش، تست"""

CHAPTERS = [

# ================================================================ فصل ۱۶
dict(
    n=16, icon='🔔', title='سیگنال‌ها (Signals) — مدیریت رویدادها', cat=3, mins=80, lvl_label='متوسط',
    hero_desc='<span class="term" data-term="signal">سیگنال</span>های آماده جنگو: pre_save، post_save، pre_delete، post_delete و m2m_changed؛ ساخت پروفایل خودکار هنگام ثبت‌نام با receiver، مهاجرت داده و کاربردهای واقعی.',
    s1_intro='سیگنال‌ها سامانه «اعلان رویداد» جنگو هستند: وقتی رکوردی ذخیره یا حذف می‌شود، هر کدی که به آن رویداد گوش داده، خودکار اجرا می‌شود. ابزاری قدرتمند که اگر نابجا استفاده شود، کد را غیرقابل ردیابی می‌کند — پس «کی استفاده کنیم» را هم دقیق یاد می‌گیریم.',
    objectives=[
        'مکانیزم فرستنده/گیرنده (sender/receiver) سیگنال‌ها را توضیح دهید.',
        'با <span class="term" data-term="decorator">@receiver</span> به post_save و pre_delete گوش دهید.',
        'سیگنال‌های سفارشی برای رویدادهای دامنه کسب‌وکار بسازید.',
        'signals.py را درست بارگذاری کنید (apps.py ready).',
        'بدانید کجا سیگنال <strong>نزنید</strong> و به‌جایش صریح کد بنویسید.',
    ],
    s1_position='<strong>جایگاه فصل:</strong> از پروفایل خودکار فصل ۱۲ استفاده می‌کند؛ پاک‌سازی فایل در فصل ۱۴ و اعلان‌ها در پروژه‌ها به آن تکیه دارند.',
    roadmap=[
        ('مفهوم سیگنال', 'رویداد، فرستنده و گیرنده.'),
        ('سیگنال‌های آماده', 'save/delete/m2m و کاربردها.'),
        ('اجرا و بارگذاری', 'signals.py و ready().'),
        ('کی و کی نه', 'الگوهای درست و نادرست.'),
    ],
    mind_qs=[
        ('پروفایل خودکار فصل ۱۲ با سیگنال ساخته می‌شد؛ چرا بعضی‌ها می‌گویند سیگنال ضدالگو است؟',
         '<p>چون جریان برنامه را <strong>نامرئی</strong> می‌کند: خوانندهٔ کد نمی‌بیند که save() چه کارهای دیگری را برمی‌انگیزد. قاعده: اگر منطق «بخش اصلی» کسب‌وکار است، صریح بنویسید؛ سیگنال برای اثرهای جانبیِ واقعاً جانبی (ساخت پروفایل، پاک‌سازی فایل، ارسال اعلان).</p>'),
        ('چرا سیگنال‌ها را در signals.py می‌گذارند و نه models.py؟',
         '<p>جداسازی مسئولیت‌ها + جلوگیری از import حلقوی. ولی فایل signals.py باید <strong>جایی import شود</strong> وگرنه receiverها ثبت نمی‌شوند — مکان استاندارد: متد ready() در apps.py.</p>'),
        ('post_save چند بار برای یک save() اجرا می‌شود؟',
         '<p>یک بار. ولی مراقب باشید: در توسعه، <span class="term" data-term="runserver">runserver</span> دو پروسه دارد (autoreloader) و اگر آماده‌سازی‌تان idempotent نباشد، اثرات دوبرابر به نظر می‌رسد. همچنین اگر داخل گیرنده دوباره همان مدل را save کنید، <strong>بازگشت بی‌نهایت</strong> می‌گیرد!</p>'),
    ],
    prereq_intro='پیش‌نیازها:',
    prereq=[
        'فصل ۱۲ (مدل Profile و سیگنال نمونه) و فصل ۱۴ (ImageField).',
        'درک دکوریتور پایتون (@syntax).',
        'آشنایی با ساختار اپ: apps.py و کلاس AppConfig.',
        'پروژه وبلاگ در حال اجرا.',
    ],
    prereq_callout=None,
    concepts=[
        dict(h='۵.۱ سیگنال چیست؟', body=[
            '<p>الگوی «ناشر-مشترک» در سطح اپلیکیشن: <strong>فرستنده</strong> (معمولاً یک <span class="term" data-term="model">مدل</span>) هنگام رخدادی سیگنال می‌فرستد و <strong>گیرنده‌ها</strong> (توابع ثبت‌شده) صدا زده می‌شوند. همه‌چیز هم‌زمان (synchronous) و در همان تراکنش است.</p>',
            ('code', 'اجزای یک گیرنده', 'python', '''from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Post)        # سیگنال + فرستنده (اختیاری)
def notify_admins(sender, instance, created, **kwargs):
    if created:                           # فقط موقع «ایجاد»
        ...
# آرگومان‌ها: sender=کلاس مدل، instance=نمونه، created=آیا جدید بود'''),
        ]),
        dict(h='۵.۲ سیگنال‌های آمادهٔ پرکاربرد', body=[
            '<ul>'
            '<li><code class="inline-code">pre_save</code> / <code class="inline-code">post_save</code> — قبل/بعد از ذخیره رکورد (created بولی دارد).</li>'
            '<li><code class="inline-code">pre_delete</code> / <code class="inline-code">post_delete</code> — قبل/بعد از حذف.</li>'
            '<li><code class="inline-code">m2m_changed</code> — تغییرات <span class="term" data-term="many-to-many">رابطه چندبه‌چند</span> (add/remove با action مشخص).</li>'
            '<li>سیگنال‌های درخواست: <code class="inline-code">request_started/finished</code> — کمتر استفاده می‌شوند.</li></ul>',
            ('code', 'مثال ۱: پروفایل خودکار (فصل ۱۲)', 'python', '''@receiver(post_save, sender=User)
def ensure_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)


@receiver(post_save, sender=User)
def save_profile_with_user(sender, instance, **kwargs):
    if hasattr(instance, "profile"):
        instance.profile.save()'''),
            ('code', 'مثال ۲: پاک‌سازی فایل آپلودی هنگام حذف', 'python', '''@receiver(pre_delete, sender=Post)
def delete_cover_file(sender, instance, **kwargs):
    if instance.cover:
        instance.cover.delete(save=False)'''),
            ('code', 'مثال ۳: به‌روزرسانی شمارنده با m2m_changed', 'python', '''@receiver(m2m_changed, sender=Post.tags.through)
def update_tag_count(sender, instance, action, **kwargs):
    if action in ("post_add", "post_remove", "post_clear"):
        for tag in instance.tags.all():
            tag.posts_count = tag.posts.count()
            tag.save()'''),
        ]),
        dict(h='۵.۳ سیگنال سفارشی برای رویداد کسب‌وکار', body=[
            ('code', 'blog/signals.py', 'python', '''import django.dispatch

post_published = django.dispatch.Signal()      # رویداد «پست منتشر شد»
order_paid = django.dispatch.Signal()          # (برای فروشگاه)'''),
            ('code', 'فرستادن سیگنال در ویو/سرویس', 'python', '''from .signals import post_published


def publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.published = True
    post.save()
    post_published.send(sender=Post, post=post, by=request.user)
    return redirect(post)'''),
            ('code', 'گیرنده‌ها — هر اپ مسئولیت خودش', 'python', '''@receiver(post_published, sender=Post)
def notify_subscribers(sender, post, by, **kwargs):
    ...  # ایمیل به دنبال‌کنندگان (با سلری، فصل ۲۴)


@receiver(post_published, sender=Post)
def clear_cache(sender, post, **kwargs):
    cache.delete(f"post_{post.pk}")'''),
            ('callout', 'info', 'چرا این الگو زیباست؟',
             'اپ «اعلان‌ها» بدون اینکه وبلاگ بشناسدش، به رویداد انتشار وصل می‌شود — <strong>جداسازی (Decoupling)</strong> واقعی بین اپ‌ها.'),
        ]),
        dict(h='۵.۴ بارگذاری درست: apps.py و ready()', body=[
            ('code', 'blog/apps.py', 'python', '''from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "blog"

    def ready(self):
        from . import signals  # noqa: F401  — فقط ثبت receiverها'''),
            '<p>ready() یک‌بار موقع بالا آمدن جنگو اجرا می‌شود؛ import کردن signals باعث اجرای @receiverها و ثبتشان می‌شود. بدون این کار، سیگنال‌ها <strong>بی‌صدا کار نمی‌کنند</strong> — از آن باگ‌های گیج‌کننده!</p>',
            ('callout', 'warn', 'قواعد ready()',
             'داخل ready() فقط import و ثبت‌نام انجام دهید؛ کوئری دیتابیس یا منطق سنگین ممنوع (هنوز همه‌چیز آماده نیست و در مهاجرت‌ها اجرا می‌شود).'),
        ]),
        dict(h='۵.۵ کی سیگنال و کی نه؟', body=[
            '<div class="table-wrap"><table class="compare"><thead><tr><th>مناسب سیگنال ✅</th><th>نامناسب — صریح بنویسید ❌</th></tr></thead><tbody>'
            '<tr><td>اثر جانبی کوچک و مستقل (پروفایل، پاک‌سازی فایل)</td><td>منطق اصلی کسب‌وکار (محاسبه قیمت سفارش)</td></tr>'
            '<tr><td>اعلان بین اپ‌ها (انتشار → ایمیل)</td><td>کاری که باید در همان تراکنش و قابل ردیابی باشد</td></tr>'
            '<tr><td><span class="term" data-term="cache">کش</span>‌زدایی بعد از تغییر</td><td><span class="term" data-term="validation">اعتبارسنجی</span> داده (جای آن فرم/مدل است)</td></tr>'
            '<tr><td>لاگ‌گیری رویدادها</td><td>ویرایش رکوردی که خود سیگنال را برانگیخته (بازگشت بی‌نهایت!)</td></tr>'
            '</tbody></table></div>',
            ('callout', 'danger', 'دو تله مرگبار',
             '① <code class="inline-code">queryset.update()</code> سیگنال <strong>نمی‌فرستد</strong> (فصل ۱۵) — منطق حیاتی را به سیگنال نبندید اگر ممکن است update دسته‌ای شود. ② save() داخل گیرندهٔ post_save همان مدل = بازگشت بی‌نهایت؛ از update() یا پرچم استفاده کنید.'),
        ]),
    ],
    example_intro='یک «تاریخچه فعالیت» (Activity Log) کامل با سیگنال سفارشی:',
    example=[
        ('code', 'audit/models.py', 'python', '''class Activity(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    action = models.CharField(max_length=50)
    detail = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]'''),
        ('code', 'blog/signals.py', 'python', '''import django.dispatch
from django.db.models.signals import post_save
from django.dispatch import receiver

from audit.models import Activity
from .models import Post

post_published = django.dispatch.Signal()


@receiver(post_published)
def log_publish(sender, post, by, **kwargs):
    Activity.objects.create(
        user=by, action="publish",
        detail=f"«{post.title}» منتشر شد",
    )


@receiver(post_save, sender=Post)
def log_new_post(sender, instance, created, **kwargs):
    if created:
        Activity.objects.create(
            user=instance.author, action="create",
            detail=f"«{instance.title}» ساخته شد",
        )'''),
        ('code', 'audit/apps.py + اتصال در ویو', 'python', '''# apps.py → ready(): from blog import signals  # noqa

# views.py → بعد از انتشار:
post_published.send(sender=Post, post=post, by=request.user)'''),
        '<p>نتیجه: <span class="term" data-term="app">اپ</span> audit بدون اینکه blog به آن اشاره‌ای کند، همه رویدادها را ثبت می‌کند. حذف اپ audit هم هیچ‌چیز را در blog نمی‌شکند.</p>',
    ],
    workshop_intro='سه سناریوی سیگنالی پیاده کنید:',
    workshop_tasks=[
        '<strong>کارگاه ۱:</strong> با pre_save، اسلاگ پست را اگر خالی بود از عنوان بسازید (slugify با allow_unicode) و یکتایی‌اش را تضمین کنید.',
        '<strong>کارگاه ۲:</strong> با post_delete روی Comment، یک سیگنال سفارشی comment_removed بفرستید و در گیرنده‌ای آمار را در لاگ ثبت کنید.',
        '<strong>کارگاه ۳:</strong> باگ بازگشت بی‌نهایت بسازید! داخل post_save همان مدل را save() کنید و خطا را ببینید؛ سپس با update() یا پرچم created اصلاحش کنید.',
    ],
    workshop_answers=[
        ('پاسخ کارگاه ۱',
         '<div class="code-box"><div class="code-head"><span>اسلاگ خودکار با pre_save</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">from django.utils.text import slugify\n\n\n@receiver(pre_save, sender=Post)\ndef ensure_slug(sender, instance, **kwargs):\n    if not instance.slug:\n        base = slugify(instance.title, allow_unicode=True) or "post"\n        slug, i = base, 1\n        while Post.objects.filter(slug=slug).exclude(pk=instance.pk).exists():\n            i += 1\n            slug = f"{base}-{i}"\n        instance.slug = slug</code></pre></div>'
         '<p>تغییر instance در pre_save <strong>مجاز</strong> است (هنوز save نشده) — برخلاف post_save. exclude(pk=...) تا رکورد با اسلاگ خودش نزدد.</p>'),
        ('پاسخ کارگاه ۲',
         '<div class="code-box"><div class="code-head"><span>سیگنال سفارشی حذف کامنت</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">comment_removed = django.dispatch.Signal()\n\n\n@receiver(post_delete, sender=Comment)\ndef announce_removal(sender, instance, **kwargs):\n    comment_removed.send(sender=Comment, post=instance.post, text=instance.text)\n\n\n@receiver(comment_removed)\ndef log_removal(sender, post, text, **kwargs):\n    Activity.objects.create(\n        user=post.author, action="comment_removed",\n        detail=f"نظری از «{post.title}» حذف شد",\n    )</code></pre></div>'),
        ('پاسخ کارگاه ۳',
         '<div class="code-box"><div class="code-head"><span>بازگشت بی‌نهایت و اصلاح</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python"># ❌ باگ:\n@receiver(post_save, sender=Post)\ndef bad(sender, instance, **kwargs):\n    instance.title = instance.title.strip()\n    instance.save()          # → post_save دوباره → بی‌نهایت → RecursionError\n\n\n# ✅ اصلاح با update (سیگنال نمی‌فرستد):\n@receiver(post_save, sender=Post)\ndef good(sender, instance, created, **kwargs):\n    clean = instance.title.strip()\n    if clean != instance.title:\n        Post.objects.filter(pk=instance.pk).update(title=clean)</code></pre></div>'
         '<p>درس: در post_save برای تغییر همان رکورد از update() یا بهتر از همه، تمیزکاری در pre_save استفاده کنید.</p>'),
    ],
    errors=[
        ('سیگنال ثبت شده ولی اجرا نمی‌شود',
         'signals.py هیچ‌جا import نشده! در apps.py متد ready() را بنویسید و مطمئن شوید AppConfig درست ارجاع شده (default_app_config یا نام اپ در INSTALLED_APPS با مسیر AppConfig).' ),
        ('RecursionError: maximum recursion depth exceeded',
         'داخل گیرنده post_save همان مدل را save() کرده‌اید. اصلاح با update() یا انتقال منطق به pre_save (الگوی کارگاه ۳).'),
        ('گیرنده دو بار اجرا می‌شود',
         'دو علت رایج: ① signals.py هم در ready و هم جای دیگر (مثل __init__.py) import شده — dispatch_uid بدهید یا import دوباره را حذف کنید. ② در توسعه، autoreloader دو پروسه دارد که طبیعی است و اثر جانبی تکراری ندارد (هر پروسه یک گیرنده).'),
        ('بعد از حذف دسته‌ای، پاک‌سازی انجام نشد',
         '<code class="inline-code">queryset.delete()</code> برای هر شیء سیگنال می‌فرستد ولی <code class="inline-code">queryset.update()</code> نه؛ همچنین حذف آبشاری (CASCADE) سیگنال مدل فرزند را می‌فرستد. منطق را متناسب با مسیرهای واقعی حذف طراحی کنید.'),
        ('در تست‌ها سیگنال مزاحم است',
         'می‌توانید موقتاً قطعش کنید: <code class="inline-code">post_save.disconnect(handler, sender=Post)</code> در setUp و connect مجدد در tearDown؛ یا با mock آن را بررسی کنید (فصل ۲۰).'),
    ],
    errors_callout=None,
    exercises=[
        ('تمرین ۱ — انتخاب رویداد',
         '<p><strong>سوال:</strong> برای هر کار کدام سیگنال؟ (الف) پرکردن فیلد قبل از ذخیره (ب) ارسال ایمیل خوش‌آمد بعد از ثبت‌نام (ج) حذف فایل عکس با حذف پست (د) شمارش برچسب بعد از افزودن تگ</p>'
         '<p><strong>پاسخ:</strong> الف → pre_save • ب → post_save با created=True (یا سیگنال سفارشی) • ج → pre_delete (قبل از رفتن رکورد، تا مسیر فایل موجود باشد) • د → m2m_changed با action="post_add".</p>'),
        ('تمرین ۲ — dispatch_uid',
         '<p><strong>سوال:</strong> پارامتر dispatch_uid در @receiver چه مشکلی را حل می‌کند؟</p>'
         '<p><strong>پاسخ:</strong> از ثبت <strong>دوباره</strong> یک گیرنده جلوگیری می‌کند (وقتی ماژول بیش از یک بار import/اجرا شود). <code class="inline-code">@receiver(post_save, sender=Post, dispatch_uid="ensure_slug")</code> — هر uid فقط یک بار ثبت می‌شود.</p>'),
        ('تمرین ۳ — ردیابی',
         '<p><strong>سناریو:</strong> همکار شما می‌گوید «رکورد را save کردم ولی یک ایمیل هم رفت! از کجا؟». چطور پیدایش می‌کنید؟</p>'
         '<p><strong>پاسخ:</strong> جست‌وجوی گیرنده‌ها: همه @receiverها و .connectها را در پروژه grep کنید؛ مخصوصاً post_save همان مدل. بعد apps.py ready()ها را ببینید که کدام ماژول signals بارگذاری می‌شود. درس طراحی: مستند کنید چه سیگنال‌هایی در پروژه فعال‌اند.</p>'),
    ],
    quiz=[
        dict(q='آرگومان created در گیرنده post_save چه می‌گوید؟',
             opts=['رکورد حذف شده', 'آیا این save یک «ایجاد» بوده یا «به‌روزرسانی»',
                   'سیگنال سفارشی است', 'زمان ساخت مدل'],
             ans='b', explain='created=True یعنی رکورد تازه insert شده؛ برای واکنش‌های «فقط بار اول» حیاتی است.'),
        dict(q='کدام مسیرها سیگنال post_save را اجرا نمی‌کنند؟',
             opts=['model.save()', 'queryset.update()', 'ایجاد با objects.create()', 'save(force_update=True)'],
             ans='b', explain='update() کوئری مستقیم SQL است و save را صدا نمی‌زند؛ پس سیگنالی هم نیست — تله معروف فصل.'),
        dict(q='signals.py کجا باید import شود تا گیرنده‌ها ثبت شوند؟',
             opts=['در urls.py', 'در apps.py متد ready()', 'در settings.py', 'نیازی به import نیست'],
             ans='b', explain='ready() موقع راه‌اندازی جنگو اجرا می‌شود؛ import signals در آن باعث اجرای @receiverها و ثبتشان می‌شود.'),
        dict(q='چرا ذخاره کردن رکورد در گیرنده post_save همان رکورد خطرناک است؟',
             opts=['کند است', 'بازگشت بی‌نهایت: save → post_save → save → ...',
                   'سیگنال پاک می‌شود', 'تراکنش بسته می‌شود'],
             ans='b', explain='هر save دوباره post_save را برمی‌انگیزد؛ نتیجه RecursionError. اصلاح: pre_save یا queryset.update().'),
        dict(q='سیگنال سفارشی چطور ساخته و ارسال می‌شود؟',
             opts=['Signal() و my_signal.send(sender=..., ...)', 'def signal(): ...',
                   'register_signal(...)', 'در settings تعریف می‌شود'],
             ans='a', explain='django.dispatch.Signal یک شیء سیگنال می‌سازد؛ send/send_robust آن را با آرگومان‌های کلیدواژه‌ای منتشر می‌کند.'),
        dict(q='کدام مورد استفاده «درست» از سیگنال است؟',
             opts=['محاسبه قیمت نهایی سفارش', 'اعتبارسنجی فرم ثبت‌نام',
                   'پاک‌کردن فایل کاور هنگام حذف پست', 'ساخت خود کاربر'],
             ans='c', explain='سیگنال برای اثرهای جانبی مستقل و غیرحیاتی عالی است؛ منطق اصلی باید صریح و قابل ردیابی بماند.'),
    ],
    project_title='سامانه رویدادها و تاریخچه',
    project_intro='یک سیستم Activity Log واقعی با سیگنال‌های سفارشی بسازید.',
    project_checklist=[
        'اپ audit با مدل Activity.',
        'سیگنال‌های سفارشی: post_published و comment_added.',
        'گیرنده‌های ثبت تاریخچه + پاک‌سازی کش پست.',
        'بارگذاری درست در ready() و تست دستی هر رویداد.',
        'صفحه «فعالیت‌های من» برای کاربر واردشده (۲۰ مورد آخر).',
    ],
    project_callout=('tip', 'نگاه به آینده',
        'ارسال ایمیل در گیرنده سیگنال، کاربر را منتظر می‌گذارد! در فصل ۲۴ همین گیرنده را به یک <span class="term" data-term="celery">تسک سلری</span> تبدیل می‌کنیم تا ناهمگام شود.'),
    summary_items=[
        'سیگنال = اعلان رویداد؛ @receiver گیرنده را ثبت می‌کند.',
        'post_save با created، pre_delete برای پاک‌سازی، m2m_changed برای روابط.',
        'signals.py باید در apps.py→ready() ایمپورت شود.',
        'سیگنال سفارشی با Signal() و send() برای رویدادهای کسب‌وکار.',
        'تله‌ها: update() سیگنال ندارد؛ save در post_save = بازگشت بی‌نهایت.',
    ],
    golden='سیگنال برای «اثرهای جانبی جانبی» است؛ هرچه منطق حیاتی‌تر، کد صریح‌تر.',
    faq=[
        ('send یا send_robust؟',
         '<p>send: استثنا در یک گیرنده، بقیه را متوقف و خطا را پخش می‌کند. send_robust: استثناها را می‌گیرد و به‌صورت لیست نتیجه برمی‌گرداند — برای گیرنده‌های غیرحیاتی (مثل لاگ) امن‌تر.</p>'),
        ('می‌شود سیگنال را موقتاً غیرفعال کرد؟',
         '<p>بله: <code class="inline-code">post_save.disconnect(receiver, sender=Model)</code> و بعداً connect مجدد. در اسکریپت‌های دادهٔ دسته‌جمعی (bulk) کاربرد دارد.</p>'),
        ('سیگنال‌ها در تراکنش دیتابیس چطورند؟',
         '<p>هم‌زمان با save اجرا می‌شوند (داخل همان تراکنش). اگر گیرنده کار بیرونی می‌کند (ایمیل/HTTP) و تراکنش rollback شود، کار بیرونی برگشت‌ناپذیر است! برای این موارد transaction.on_commit(lambda: ...) را استفاده کنید تا بعد از commit قطعی اجرا شود.</p>'),
    ],
    next_step='یک لایه به بیرون می‌آییم: در <strong>فصل ۱۷</strong> <span class="term" data-term="middleware">میان‌افزار</span> — کدی که روی <strong>همه</strong> درخواست‌ها/پاسخ‌های سایت اجرا می‌شود.',
),

# ================================================================ فصل ۱۷
dict(
    n=17, icon='🛂', title='میان‌افزار (Middleware)', cat=3, mins=85, lvl_label='متوسط',
    hero_desc='زنجیره پردازش درخواست، ساخت <span class="term" data-term="middleware">میان‌افزار</span> سفارشی، ثبت در MIDDLEWARE، اهمیت ترتیب و کاربردهای واقعی: زمان‌سنجی، لاگ‌گیری، نگهداری و مسدودسازی IP.',
    s1_intro='هر درخواستی که به سایت شما می‌رسد، قبل از ویو از یک «زنجیره» عبور می‌کند: نشست‌ها، امنیت، احراز هویت... این‌ها همه میدلور هستند. در این فصل زنجیره را می‌شکافیم و حلقه خودمان را می‌سازیم.',
    objectives=[
        'مسیر رفت و برگشت درخواست/پاسخ در زنجیره MIDDLEWARE را رسم کنید.',
        'میدلور به سبک جدید (تابعی/کلاسی با __call__) بنویسید.',
        'اثر <strong>ترتیب</strong> میدلورها را توضیح دهید.',
        'میدلورهای پیش‌فرض جنگو و نقش هرکدام را نام ببرید.',
        'چهار میدلور کاربردی (زمان‌سنج، نگهداری، IP، لاگ) پیاده کنید.',
    ],
    s1_position='<strong>جایگاه فصل:</strong> درک request.user (فصل ۱۲) و session (فصل ۱۸) بدون شناخت میدلور کامل نیست؛ کاربردهای امنیتی در فصل ۲۶.',
    roadmap=[
        ('زنجیره میدلور', 'رفت: قبل از ویو؛ برگشت: بعد از ویو.'),
        ('ساخت میدلور', 'الگوی استاندارد __call__.'),
        ('ترتیب و پیش‌فرض‌ها', 'چه چیزی کجا ثبت شود.'),
        ('چهار مثال واقعی', 'از هدر ساده تا حالت نگهداری.'),
    ],
    mind_qs=[
        ('چرا request.user در هر ویویی آماده است؟',
         '<p>چون <code class="inline-code">AuthenticationMiddleware</code> قبل از رسیدن درخواست به ویو، از روی <span class="term" data-term="session">نشست</span> کاربر را پیدا و به request الصاق می‌کند. بدون آن میدلور، request.user وجود نداشت!</p>'),
        ('اگر میدلوری پاسخ را برگرداند و next را صدا نزند چه می‌شود؟',
         '<p>زنجیره <strong>همان‌جا کوتاه می‌شود</strong>: ویو و میدلورهای بعدی هرگز اجرا نمی‌شوند. این مکانیزم «رد درخواست» است — مثل مسدودسازی IP یا حالت نگهداری.</p>'),
        ('چرا ترتیب MIDDLEWARE مهم است؟',
         '<p>چون هر میدلور به کار میدلورهای <strong>قبلی</strong> تکیه می‌کند: AuthenticationMiddleware باید بعد از SessionMiddleware باشد (چون به request.session نیاز دارد). ترتیب غلط = صفت‌های غایب یا خطا.</p>'),
    ],
    prereq_intro='پیش‌نیازها:',
    prereq=[
        'درک چرخه درخواست/پاسخ از فصل ۱ و ۸.',
        'فهرست MIDDLEWARE در settings.py جلوی چشمتان باشد.',
        'آشنایی با کلاس و __init__/__call__ در پایتون.',
        'سرور توسعه برای مشاهده اثر میدلورها.',
    ],
    prereq_callout=None,
    concepts=[
        dict(h='۵.۱ زنجیره میدلور: پوسته‌های پیاز', body=[
            '<p>MIDDLEWARE را مثل لایه‌های پیاز تصور کنید؛ درخواست از بیرون به درون (به سمت ویو) و پاسخ از درون به بیرون برمی‌گردد:</p>',
            ('code', 'مسیر یک درخواست', 'text', '''درخواست
   ↓ SecurityMiddleware        (هدرهای امنیتی، ریدایرکت HTTPS)
   ↓ SessionMiddleware         (request.session)
   ↓ CommonMiddleware          (APPEND_SLASH، هدرهای معمول)
   ↓ CsrfViewMiddleware        (بررسی توکن CSRF)
   ↓ AuthenticationMiddleware  (request.user)
   ↓ MessageMiddleware         (پیام‌های flash)
   ↓ XFrameOptionsMiddleware   (کلیک‌جاکی)
   → VIEW اجرا می‌شود → پاسخ
   ↑ همان لایه‌ها، این بار در مسیر برگشت پاسخ'''),
            '<p>پس هر میدلور دو فرصت دارد: <strong>قبل از ویو</strong> (روی request) و <strong>بعد از ویو</strong> (روی response).</p>',
        ]),
        dict(h='۵.۲ آناتومی یک میدلور سفارشی', body=[
            ('code', 'myapp/middleware.py', 'python', '''import time


class RequestTimingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response   # لایه بعدی زنجیره

    def __call__(self, request):
        start = time.perf_counter()

        response = self.get_response(request)   # ← ادامه زنجیره (و ویو)

        duration = time.perf_counter() - start
        response["X-Request-Time"] = f"{duration * 1000:.1f}ms"
        return response'''),
            ('code', 'ثبت در settings.py', 'python', '''MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    ...
    "myapp.middleware.RequestTimingMiddleware",   # ← افزودن
]'''),
            ('callout', 'info', 'get_response چیست؟',
             'تابعی که «بقیه زنجیره + ویو» را اجرا و پاسخ را برمی‌گرداند. هر کد <strong>قبل</strong> از آن = پردازش روی request؛ هر کد <strong>بعد</strong> از آن = پردازش روی response. اگر get_response را صدا نزنید و خودتان پاسخ برگردانید، زنجیره قطع می‌شود.'),
        ]),
        dict(h='۵.۳ قطع زنجیره: رد کردن درخواست', body=[
            ('code', 'حالت نگهداری (Maintenance Mode)', 'python', '''from django.http import JsonResponse


class MaintenanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if settings.MAINTENANCE_MODE and not request.user.is_staff:
            return JsonResponse(
                {"detail": "سایت در حال به‌روزرسانی است 🛠"}, status=503)
        return self.get_response(request)'''),
            '<p>نکته ظریف: در این مثال request.user فقط وقتی موجود است که این میدلور <strong>بعد از</strong> AuthenticationMiddleware ثبت شده باشد — اهمیت ترتیب!</p>',
        ]),
        dict(h='۵.۴ hookهای دیگر: process_view و process_exception', body=[
            ('code', 'میدلور با hookهای اختیاری', 'python', '''class MyMiddleware:
    def __init__(self, get_response): ...
    def __call__(self, request): ...

    def process_view(self, request, view_func, view_args, view_kwargs):
        # قبل از ویو، بعد از تشخیص اینکه کدام ویو اجرا می‌شود
        # اگر response برگردانید، ویو اجرا نمی‌شود
        return None

    def process_exception(self, request, exception):
        # اگر ویو استثنا داد — مثلاً لاگ و صفحه خطای سفارشی
        return None

    def process_template_response(self, request, response):
        # بعد از ویوهای TemplateResponse (مثل admin و CBVها)
        return response'''),
        ]),
        dict(h='۵.۵ میدلورهای پیش‌فرض و ترتیب درست', body=[
            '<ul>'
            '<li><strong>SecurityMiddleware</strong>: هدرهای امنیتی، ریدایرکت HTTP→HTTPS، HSTS (اول باشد).</li>'
            '<li><strong>SessionMiddleware</strong>: request.session را می‌سازد (قبل از Auth!).</li>'
            '<li><strong>CommonMiddleware</strong>: APPEND_SLASH و هدرهای معمول.</li>'
            '<li><strong>CsrfViewMiddleware</strong>: توکن <span class="term" data-term="csrf">CSRF</span> را در POSTها اعتبارسنجی می‌کند.</li>'
            '<li><strong>AuthenticationMiddleware</strong>: request.user (بعد از Session).</li>'
            '<li><strong>MessageMiddleware</strong>: پیام‌های یک‌بارمصرف (messages.success و...).</li>'
            '<li><strong>XFrameOptionsMiddleware</strong>: جلوگیری از کلیک‌جکینگ.</li></ul>',
            ('callout', 'warn', 'میدلور خودمان کجا؟',
             'اگر به request.user/session نیاز دارد → بعد از Authentication/Session. اگر می‌خواهد همه چیز را زمان‌سنجی کند → اول فهرست (بیرونی‌ترین لایه). قاعده کلی: میدلورهای عمومی هرچه بیرونی‌تر، پوشش بیشتر.'),
        ]),
    ],
    example_intro='چهار میدلور کاربردی که می‌توانید امروز در پروژه واقعی استفاده کنید:',
    example=[
        ('code', '۱) هدر درخواست-زمان + لاگ کندترین‌ها', 'python', '''class TimingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.perf_counter()
        response = self.get_response(request)
        ms = (time.perf_counter() - start) * 1000
        if ms > 500:
            logger.warning("کند: %s → %.0fms", request.path, ms)
        response["X-Request-Time"] = f"{ms:.0f}ms"
        return response'''),
        ('code', '۲) مسدودسازی IP', 'python', '''class BlockIPMiddleware:
    BLOCKED = {"1.2.3.4"}

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get("REMOTE_ADDR")
        if ip in self.BLOCKED:
            return HttpResponseForbidden("دسترسی مسدود است.")
        return self.get_response(request)'''),
        ('code', '۳) افزودن درخواست به بافت قالب (context processor مکمل)', 'python', '''class SiteVersionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.site_version = "2.0.1"
        return self.get_response(request)'''),
        ('code', '۴) اجبار زبان فارسی بر اساس دامنه (پیش‌درآمد فصل ۲۵)', 'python', '''class ForceFaLocaleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        translation.activate("fa")
        request.LANGUAGE_CODE = "fa"
        return self.get_response(request)'''),
    ],
    workshop_intro='میدلورهای وبلاگ خودتان را بنویسید:',
    workshop_tasks=[
        '<strong>کارگاه ۱:</strong> میدلوری که به همه پاسخ‌ها هدر <code class="inline-code">X-Served-By: my-blog</code> اضافه کند.',
        '<strong>کارگاه ۲:</strong> میدلور «ساعات کاری»: خارج از ۸ تا ۲۲، کاربران غیرstaff پیام «سایت در دسترس نیست» (503) بگیرند.',
        '<strong>کارگاه ۳:</strong> میدلور لاگ‌گیر: برای هر درخواست یک خط لاگ (متد، مسیر، کد وضعیت، زمان) با ماژول logging بنویسید و خروجی را در ترمینال ببینید.',
    ],
    workshop_answers=[
        ('پاسخ کارگاه ۱',
         '<div class="code-box"><div class="code-head"><span>هدر ساده</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">class ServedByMiddleware:\n    def __init__(self, get_response):\n        self.get_response = get_response\n\n    def __call__(self, request):\n        response = self.get_response(request)\n        response["X-Served-By"] = "my-blog"\n        return response</code></pre></div>'
         '<p>در DevTools مرورگر → Network → Headers پاسخ، هدر را ببینید.</p>'),
        ('پاسخ کارگاه ۲',
         '<div class="code-box"><div class="code-head"><span>ساعات کاری</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">from datetime import datetime\nfrom django.http import HttpResponse\n\n\nclass WorkingHoursMiddleware:\n    def __init__(self, get_response):\n        self.get_response = get_response\n\n    def __call__(self, request):\n        hour = datetime.now().hour\n        is_staff = getattr(request, "user", None) and request.user.is_staff\n        if not (8 <= hour < 22) and not is_staff:\n            return HttpResponse("سایت خارج از ساعات کاری است ⏰", status=503)\n        return self.get_response(request)</code></pre></div>'
         '<p><strong>باید بعد از AuthenticationMiddleware ثبت شود</strong> تا request.user وجود داشته باشد؛ getattr برای احتیاط است.</p>'),
        ('پاسخ کارگاه ۳',
         '<div class="code-box"><div class="code-head"><span>لاگ درخواست‌ها</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">import logging\nimport time\n\nlogger = logging.getLogger("requests")\n\n\nclass RequestLogMiddleware:\n    def __init__(self, get_response):\n        self.get_response = get_response\n\n    def __call__(self, request):\n        start = time.perf_counter()\n        response = self.get_response(request)\n        ms = (time.perf_counter() - start) * 1000\n        logger.info("%s %s → %s (%.0fms)",\n                    request.method, request.path,\n                    response.status_code, ms)\n        return response</code></pre></div>'
         '<p>برای دیدن خروجی، در LOGGING یک هندلر console به logger "requests" بدهید (فصل ۲۱ کامل). <span class="term" data-term="logging">لاگ</span> درخواست‌ها در تولید معمولاً کار Nginx است — این میدلور برای توسعه عالی است.</p>'),
    ],
    errors=[
        ('AttributeError: \'WSGIRequest\' object has no attribute \'user\'',
         'میدلورتان قبل از AuthenticationMiddleware ثبت شده (یا request.user را قبل از get_response می‌خوانید). آن را بعد از auth در فهرست ببرید و در مسیر درخواست (نه پاسخ) استفاده کنید.'),
        ('میدلور اجرا نمی‌شود',
         'مسیر دات‌دار در MIDDLEWARE اشتباه است (myapp.middleware.MyMW)، یا سرور reload نشده، یا استثنا در __init__ خورده. با print/لاگ در __call__ مطمئن شوید صدا زده می‌شود.'),
        ('CSRF همه فرم‌ها شکست بعد از تغییر میدلورها',
         'CsrfViewMiddleware را حذف/جابه‌جا کرده‌اید یا میدلور شما پاسخ را دستکاری و توکن را خراب می‌کند. ترتیب پیش‌فرض را برنگردانید مگر بدانید چرا.'),
        ('هر درخواست دو بار لاگ می‌شود',
         'میدلور را دوبار در MIDDLEWARE گذاشته‌اید، یا در توسعه autoreloader دو پروسه دارد (طبیعی) ولی لاگ تکراری واقعاً از فهرست تکراری می‌آید — MIDDLEWARE را بشمارید!'),
    ],
    errors_callout=None,
    exercises=[
        ('تمرین ۱ — ترتیب',
         '<p><strong>سوال:</strong> این سه میدلور را به ترتیب صحیح بچینید: AuthenticationMiddleware، SessionMiddleware، TimingMiddleware(کل سایت).</p>'
         '<p><strong>پاسخ:</strong> Timing (اول/بیرونی‌ترین تا همه‌چیز را ببیند) ← Session ← Authentication (به session نیاز دارد).</p>'),
        ('تمرین ۲ — رفت یا برگشت؟',
         '<p><strong>سوال:</strong> هر کار در کدام فاز است؟ (الف) افزودن request.site_version (ب) ست‌کردن هدر روی response (ج) برگرداندن 503 برای IP مسدود (د) لاگ زمان اجرا</p>'
         '<p><strong>پاسخ:</strong> الف → قبل از get_response • ب و د → بعد از get_response • ج → قبل از get_response (و هرگز صدایش نمی‌زنیم = قطع زنجیره).</p>'),
        ('تمرین ۳ — میدلور یا دکوریتور؟',
         '<p><strong>سناریو:</strong> می‌خواهیم (الف) همه پاسخ‌ها هدر X-Frame-Options بگیرند (ب) فقط ویوی گزارش‌ها به کاربران premium محدود شود. کدام ابزار؟</p>'
         '<p><strong>پاسخ:</strong> الف → میدلور (سراسری و یک‌نواخت) • ب → دکوریتور/میکسین روی همان ویو (محدود و محلی). قاعده: «همه درخواست‌ها = میدلور؛ بعضی ویوها = دکوریتور».</p>'),
    ],
    quiz=[
        dict(q='میدلور چه موقعیت‌هایی برای اجرا دارد؟',
             opts=['فقط قبل از ویو', 'فقط بعد از ویو',
                   'هم در مسیر درخواست (قبل از ویو) هم در مسیر پاسخ (بعد از ویو)', 'فقط هنگام خطا'],
             ans='c', explain='کد قبل از get_response روی request و کد بعد از آن روی response اثر می‌گذارد — دو فاز یک میدلور.'),
        dict(q='اگر میدلوری بدون صدا زدن get_response پاسخ برگرداند چه می‌شود؟',
             opts=['خطای 500', 'ویو و میدلورهای بعدی اجرا نمی‌شوند؛ همان پاسخ برمی‌گردد',
                   'زنجیره از ابتدا اجرا می‌شود', 'پاسخ نادیده گرفته می‌شود'],
             ans='b', explain='این «قطع زنجیره» است؛ مکانیزم اصلی رد درخواست (مسدودی، نگهداری، ریدایرکت سراسری).'),
        dict(q='چرا AuthenticationMiddleware باید بعد از SessionMiddleware باشد؟',
             opts=['ترتیب مهم نیست', 'چون request.user را از داده نشست می‌سازد و request.session باید موجود باشد',
                   'چون CSRF اول باید بررسی شود', 'به دلیل سرعت'],
             ans='b', explain='auth هویت را از sessionid کوکی/نشست می‌خواند؛ پس session باید اول ساخته شود. ترتیب = وابستگی.'),
        dict(q='پارامتر get_response در __init__ چیست؟',
             opts=['پاسخ نهایی', 'تابعی که بقیه زنجیره و ویو را اجرا می‌کند',
                   'شیء request', 'تنظیمات میدلور'],
             ans='b', explain='جنگو زنجیره را با get_response به هم می‌بافد؛ صدا زدنش یعنی «برو لایه بعدی».'),
        dict(q='process_view چه زمانی اجرا می‌شود؟',
             opts=['بعد از ویو', 'بعد از تعیین ویو ولی قبل از اجرای آن',
                   'فقط هنگام استثنا', 'به‌جای __call__'],
             ans='b', explain='hook اختیاری که view_func و آرگومان‌هایش را می‌گیرد؛ برگرداندن response در آن، ویو را اجرا نمی‌کند.'),
        dict(q='برای زمان‌سنجی «کل» پردازش درخواست، میدلور را کجا ثبت می‌کنیم؟',
             opts=['آخر فهرست MIDDLEWARE', 'اول فهرست (بیرونی‌ترین لایه)',
                   'وسط', 'فرقی نمی‌کند'],
             ans='b', explain='اول فهرست = بیرونی‌ترین لایه پیاز؛ همه میدلورهای دیگر و ویو داخل بازه زمانی‌اش می‌افتند.'),
    ],
    project_title='میدلورهای عملیاتی وبلاگ',
    project_intro='مجموعه‌ای از میدلورها که سایت را «قابل مشاهده» می‌کند.',
    project_checklist=[
        'TimingMiddleware با هدر X-Request-Time + لاگ هشدار برای >۵۰۰ms.',
        'RequestLogMiddleware با فرمت منظم (متد، مسیر، وضعیت، زمان، IP).',
        'MaintenanceMiddleware با کلید در settings (و دور زدن برای staff).',
        'مستندسازی ترتیب انتخابی‌تان در کامنت settings.py.',
        'تست: حالت نگهداری را روشن/خاموش کنید و رفتار staff و عادی را مقایسه کنید.',
    ],
    project_callout=('tip', 'مرز میدلور و ابزار آماده',
        'برای لاگ درخواست در تولید، Nginx access log استاندارد است؛ میدلور لاگ بیشتر برای دیباگ توسعه و متریک‌های اپلیکیشنی. هر دو را هم‌زمان در تولید روشن نگذارید.'),
    summary_items=[
        'میدلور = لایه پیازی اطراف ویو؛ رفت (request) و برگشت (response).',
        'الگو: __init__(get_response) + __call__ با صدا زدن get_response.',
        'قطع زنجیره = رد درخواست (۵۰۳، مسدودی، ریدایرکت).',
        'hookهای اختیاری: process_view، process_exception، process_template_response.',
        'ترتیب فهرست = ترتیب وابستگی‌ها؛ میدلورهای خودتان را آگاهانه جای‌گذاری کنید.',
    ],
    golden='میدلور جای «قوانین سراسری» سایت است؛ هر چیزی که برای همه درخواست‌ها صادق است.',
    faq=[
        ('میدلور یا context processor؟',
         '<p>اگر فقط می‌خواهید متغیری به <strong>همه قالب‌ها</strong> بدهید (مثل سایت نسخه ۲)، context processor سبک‌تر و دقیق‌تر است. میدلور برای دستکاری درخواست/پاسخ و قطع زنجیره.</p>'),
        ('میدلور ناهمگام (async) هم داریم؟',
         '<p>بله؛ از جنگو ۳.۱ میدلور می‌تواند async باشد (acapable). برای پروژه متداول WSGI همان سینک کافی است. در استقرار <span class="term" data-term="asgi">ASGI</span> (فصل ۲۶/۲۹) موضوعیت پیدا می‌کند.</p>'),
        ('چطور میدلور را در تست غیرفعال کنم؟',
         '<p>با override_settings(MIDDLEWARE=[...]) در تست می‌توانید فهرست را موقتاً عوض کنید؛ یا میدلورتان را طوری بنویسید که با یک تنظیم (feature flag) قابل خاموش کردن باشد — مثل MaintenanceMiddleware مثال.</p>'),
    ],
    next_step='میدلور SessionMiddleware هر درخواست request.session می‌دهد — اما نشست واقعاً چطور کار می‌کند؟ <strong>فصل ۱۸</strong>: <span class="term" data-term="session">Session</span> و <span class="term" data-term="cookie">کوکی</span>، و ساخت سبد خرید بدون ثبت‌نام.',
),

# ================================================================ فصل ۱۸
dict(
    n=18, icon='🍪', title='نشست (Session) و کوکی‌ها', cat=3, mins=80, lvl_label='متوسط',
    hero_desc='ذخیره اطلاعات بین <span class="term" data-term="request">درخواست</span>ها با request.session، تفاوت <span class="term" data-term="session">نشست</span> و <span class="term" data-term="cookie">کوکی</span>، نمونه سبد خرید، تنظیمات عمر نشست و امنیت آن‌ها.',
    s1_intro='HTTP «بی‌حالت» است: هر درخواست، غریبه‌ای تازه است! نشست و کوکی دو مکانیزمی‌اند که به سایت «حافظه» می‌دهند — از سبد خرید مهمان تا نگه‌داشتن ورود کاربر. این فصل آن حافظه را کالبدشکافی می‌کند.',
    objectives=[
        'تفاوت کوکی (سمت کاربر) و نشست (سمت سرور) را توضیح دهید.',
        'با request.session مثل دیکشنری کار کنید.',
        'سبد خرید مهمان (بدون ثبت‌نام) بسازید.',
        'تنظیمات عمر نشست (SESSION_COOKIE_AGE و...) را پیکربندی کنید.',
        'پرچم‌های امنیتی کوکی (HttpOnly، Secure، SameSite) را بدانید.',
    ],
    s1_position='<strong>جایگاه فصل:</strong> درک عمیق‌تر سازوکار ورود فصل ۱۲؛ سبد خرید پایهٔ پروژه فروشگاه فصل ۳۰.',
    roadmap=[
        ('کوکی و نشست', 'کی کجا ذخیره می‌شود.'),
        ('request.session', 'API دیکشنری‌مانند.'),
        ('سبد خرید', 'پروژه کلاسیک نشست‌محور.'),
        ('تنظیمات و امنیت', 'عمر، پرچم‌ها و پاک‌سازی.'),
    ],
    mind_qs=[
        ('چرا سبد خرید را در کوکی نگه نمی‌داریم؟',
         '<p>کوکی سمت کاربر است: قابل ویرایش/حذف، محدود به ~4KB و با هر درخواست جابه‌جا می‌شود. کاربر می‌تواند قیمت را در کوکی دستکاری کند! داده <strong>قابل اعتماد</strong> باید سمت سرور (نشست یا دیتابیس) بماند.</p>'),
        ('نشست جنگو کجا ذخیره می‌شود؟',
         '<p>پیش‌فرض: جدول django_session در همان <span class="term" data-term="database">پایگاه داده</span>. در کوکی کاربر فقط یک <strong>شناسه</strong> (sessionid) است. بک‌اندهای دیگر: فایل، کش/Redis (سریع‌تر).</p>'),
        ('وقتی کاربر «مرا به خاطر بسپار» را می‌زند چه فرق می‌کند؟',
         '<p>عمر کوکی نشست تغییر می‌کند: حالت عادی «کوکی نشست» است که با بستن مرورگر می‌رود؛ با remember-me، کوکی تا مثلاً دو هفته ماندگار می‌شود (SESSION_EXPIRE_AT_BROWSER_CLOSE=False و age مشخص).</p>'),
    ],
    prereq_intro='پیش‌نیازها:',
    prereq=[
        'فصل ۱۷: بدانید SessionMiddleware هر درخواست request.session می‌دهد.',
        'DevTools مرورگر را بشناسید (تب Application → Cookies) — ابزار اصلی این فصل.',
        'مدل Product ساده (name, price) برای سبد خرید.',
        'درک دیکشنری و JSON پایتون.',
    ],
    prereq_callout=None,
    concepts=[
        dict(h='۵.۱ کوکی در برابر نشست', body=[
            '<div class="table-wrap"><table class="compare"><thead><tr><th></th><th>کوکی (Cookie)</th><th>نشست (Session)</th></tr></thead><tbody>'
            '<tr><td>محل ذخیره</td><td>مرورگر کاربر</td><td>سرور (دیتابیس/کش)</td></tr>'
            '<tr><td>امنیت داده</td><td>کاربر می‌بیند/تغییر می‌دهد</td><td>داده از دید کاربر پنهان</td></tr>'
            '<tr><td>ظرفیت</td><td>~4KB هر کوکی</td><td>عملاً نامحدود</td></tr>'
            '<tr><td>هزینه</td><td>با هر درخواست ارسال می‌شود</td><td>یک کوکی کوچک sessionid</td></tr>'
            '<tr><td>کاربرد</td><td>ترجیحات ساده (تم، زبان)، ردیابی</td><td>ورود کاربر، سبد خرید، داده حساس</td></tr>'
            '</tbody></table></div>',
            '<p>نشست جنگو در واقع <strong>ترکیب هر دو</strong> است: شناسه در کوکی، داده در سرور. شناسه امضاشده نیست ولی داده سمت سرور است، پس دستکاری‌ناپذیر.</p>',
        ]),
        dict(h='۵.۲ کار با request.session', body=[
            ('code', 'مثل یک دیکشنری', 'python', '''def view(request):
    # خواندن
    theme = request.session.get("theme", "light")
    visits = request.session.get("visits", 0)

    # نوشتن
    request.session["visits"] = visits + 1
    request.session["last_page"] = request.path

    # حذف
    del request.session["last_page"]
    request.session.pop("temp", None)

    # کل نشست (خروج کامل)
    request.session.flush()

    # تغییر در شناسه (جلوگیری از Session Fixation)
    request.session.cycle_key()'''),
            ('callout', 'warn', 'چه چیزی در نشست نگذاریم؟',
             'داده‌های حجیم (نشست در <strong>هر</strong> درخواست خوانده/نوشته می‌شود)، رمز عبور، و اطلاعاتی که در دیتابیس جای بهتری دارند. نشست = حافظه موقت کوچک و سریع.'),
        ]),
        dict(h='۵.۳ کوکی‌های مستقیم (کمتر رایج)', body=[
            ('code', 'ست و خواندن کوکی خام', 'python', '''def set_pref(request):
    response = render(request, "prefs.html")
    response.set_cookie(
        "ui_theme", "dark",
        max_age=60 * 60 * 24 * 30,   # ۳۰ روز
        httponly=False,               # جاوااسکریپت بتواند بخواند
        samesite="Lax",
    )
    return response


def read_pref(request):
    theme = request.COOKIES.get("ui_theme", "light")'''),
            '<p>تفاوت کلیدی با نشست: کوکی خام <strong>در مرورگر خواندنی/نوشتنی</strong> است. برای ترجیحات بی‌خطر (تم، زبان) خوب است؛ برای هویت و داده حساس هرگز.</p>',
        ]),
        dict(h='۵.۴ سبد خرید مهمان — الگوی کلاسیک', body=[
            ('code', 'cart/cart.py — کلاس سبد', 'python', '''class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get("cart")
        if cart is None:
            cart = self.session["cart"] = {}    # {product_id: qty}

    def add(self, product, qty=1):
        pid = str(product.pk)
        self.cart_data = self.session["cart"]
        self.cart_data[pid] = self.cart_data.get(pid, 0) + qty
        self.session.modified = True

    def remove(self, product):
        self.cart_data = self.session["cart"]
        self.cart_data.pop(str(product.pk), None)
        self.session.modified = True

    def __iter__(self):
        ids = self.session["cart"].keys()
        products = Product.objects.filter(pk__in=ids)
        for p in products:
            qty = self.session["cart"][str(p.pk)]
            yield {"product": p, "qty": qty,
                   "total": p.price * qty}

    def total_price(self):
        return sum(item["total"] for item in self)

    def __len__(self):
        return sum(self.session["cart"].values())'''),
            ('code', 'ویوها', 'python', '''def cart_add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        qty = int(request.POST.get("qty", 1))
        Cart(request).add(product, min(qty, 10))
    return redirect("cart:detail")


def cart_detail(request):
    return render(request, "cart/detail.html", {"cart": Cart(request)})'''),
            ('callout', 'info', 'session.modified = True چرا؟',
             'وقتی فقط <strong>داخل</strong> یک مقدار نشست را تغییر می‌دهید (cart[pid] += 1)، جنگو متوجه «تغییر» نمی‌شود. با SESSION_SAVE_EVERY_REQUEST=False (پیش‌فرض) باید دستی modified=True بگذارید تا ذخیره شود. اگر کل مقدار را دوباره assign کنید، لازم نیست.'),
        ]),
        dict(h='۵.۵ تنظیمات و امنیت نشست', body=[
            ('code', 'settings.py', 'python', '''SESSION_COOKIE_AGE = 60 * 60 * 24 * 14   # ۱۴ روز
SESSION_EXPIRE_AT_BROWSER_CLOSE = False   # با بستن مرورگر نرود
SESSION_SAVE_EVERY_REQUEST = False        # فقط در تغییر ذخیره شود
SESSION_COOKIE_HTTPONLY = True            # JS نتواند sessionid بخواند (پیش‌فرض)
SESSION_COOKIE_SECURE = True              # فقط HTTPS (در تولید!)
SESSION_COOKIE_SAMESITE = "Lax"           # ضد CSRF میان‌سایتی
SESSION_ENGINE = "django.contrib.sessions.backends.db"   # یا cached_db'''),
            '<ul>'
            '<li><strong>HttpOnly</strong>: جلوی دزدی sessionid با <span class="term" data-term="xss">XSS</span> را می‌گیرد.</li>'
            '<li><strong>Secure</strong>: کوکی فقط روی HTTPS ارسال شود (شنود شبکه را بی‌اثر می‌کند).</li>'
            '<li><strong>SameSite</strong>: مرورگر کوکی را در درخواست‌های میان‌سایتی نفرستد (لایه ضد CSRF).</li>'
            '<li>پاک‌سازی نشست‌های منقضی: <code class="inline-code">python manage.py clearsessions</code> (کرون/تسک دوره‌ای).</li></ul>',
        ]),
    ],
    example_intro='شمارنده بازدید + ترجیح زبان کاربر در یک مثال جمع‌وجور:',
    example=[
        ('code', 'ویوی صفحه با حافظه', 'python', '''def home(request):
    session = request.session

    # شمارنده بازدید
    visits = session.get("visits", 0) + 1
    session["visits"] = visits

    # اولین بازدید؟ خوش‌آمد ویژه
    first_time = "first_seen" not in session
    if first_time:
        session["first_seen"] = timezone.now().isoformat()

    # ترجیح زبان از کوکی (یا نشست)
    lang = request.COOKIES.get("lang", "fa")

    response = render(request, "home.html", {
        "visits": visits, "first_time": first_time, "lang": lang,
    })
    if request.GET.get("lang"):
        response.set_cookie("lang", request.GET["lang"], max_age=31536000)
    return response'''),
        ('code', 'قالب', 'html', '''{% if first_time %}
  <div class="welcome">👋 خوش آمدید! اولین بازدید شما ثبت شد.</div>
{% else %}
  <p>بازدید شمارهٔ {{ visits }} شما از امسال!</p>
{% endif %}
<a href="?lang=fa">فارسی</a> | <a href="?lang=en">English</a>'''),
        '<p>در DevTools → Application → Cookies مقدار sessionid و lang را ببینید؛ سپس در جدول django_session ردیف نشست و داده رمزینه‌شده (base64) آن را بررسی کنید.</p>',
    ],
    workshop_intro='فروشگاه کوچک نشست‌محور بسازید:',
    workshop_tasks=[
        '<strong>کارگاه ۱:</strong> کلاس Cart را برای مدل Product خودتان پیاده کنید: افزودن با فرم POST، حذف، تغییر تعداد و نمایش جمع کل.',
        '<strong>کارگاه ۲:</strong> در navbar، تعداد اقلام سبد را با <code class="inline-code">len(cart)</code> نشان دهید (context processor بنویسید تا در همه قالب‌ها باشد).',
        '<strong>کارگاه ۳:</strong> «ادغام سبد مهمان با سبد کاربر»: هنگام ورود، اگر کاربر سبد مهمان داشت، اقلامش را به سبد دیتابیسی کاربر واردشده منتقل کنید.',
    ],
    workshop_answers=[
        ('پاسخ کارگاه ۱',
         '<p>کلاس Cart مفهوم ۵.۴ را کپی کنید و ویوها:</p>'
         '<div class="code-box"><div class="code-head"><span>cart/views.py</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">def cart_add(request, pk):\n    product = get_object_or_404(Product, pk=pk, available=True)\n    if request.method == "POST":\n        qty = max(1, min(int(request.POST.get("qty", 1)), 10))\n        Cart(request).add(product, qty)\n        messages.success(request, f"«{product.name}» به سبد اضافه شد.")\n    return redirect("shop:product_detail", pk=pk)\n\n\ndef cart_update(request, pk):\n    product = get_object_or_404(Product, pk=pk)\n    if request.method == "POST":\n        qty = int(request.POST.get("qty", 0))\n        cart = Cart(request)\n        cart.set_qty(product, qty)   # qty=0 → حذف\n    return redirect("cart:detail")</code></pre></div>'
         '<p>متد set_qty را به کلاس اضافه کنید: اگر qty صفر شد remove، وگرنه مقداردهی مستقیم + session.modified=True. نکته امنیتی: قیمت را <strong>هرگز</strong> از نشست نخوانید؛ همیشه در رندر از دیتابیس بگیرید (کاربر می‌تواند... نه! نشست سمت سرور است — ولی قیمت باید به‌روز بماند، پس از product.price زمان نمایش).</p>'),
        ('پاسخ کارگاه ۲',
         '<div class="code-box"><div class="code-head"><span>cart/context_processors.py</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">def cart_summary(request):\n    return {"cart_count": len(Cart(request))}</code></pre></div>'
         '<p>ثبت در settings → TEMPLATES → OPTIONS → context_processors: <code class="inline-code">"cart.context_processors.cart_summary"</code>. حالا در هر قالب: <code class="inline-code">{{ cart_count }}</code>.</p>'),
        ('پاسخ کارگاه ۳',
         '<div class="code-box"><div class="code-head"><span>ادغام با سیگنال user_logged_in</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">from django.contrib.auth.signals import user_logged_in\nfrom django.dispatch import receiver\n\n\n@receiver(user_logged_in)\ndef merge_guest_cart(sender, request, user, **kwargs):\n    guest = request.session.get("cart", {})\n    if not guest:\n        return\n    for pid, qty in guest.items():\n        item, _ = CartItem.objects.get_or_create(\n            user=user, product_id=pid,\n            defaults={"qty": qty})\n        if _ is False:\n            item.qty += qty\n            item.save()\n    del request.session["cart"]</code></pre></div>'
         '<p>user_logged_in سیگنال آماده جنگو است — ترکیب زیبای فصل ۱۶ و ۱۸! سبد دائمی کاربر در مدل CartItem (user, product, qty) نگهداری می‌شود.</p>'),
    ],
    errors=[
        ('تغییرات سبد ذخیره نمی‌شوند',
         'مقدار تودرتو را درجا تغییر داده‌اید بدون <code class="inline-code">request.session.modified = True</code>. یا کل دیکشنری را دوباره assign کنید یا modified را ست کنید.'),
        ('نشست بعد از بستن مرورگر می‌پرد/نمی‌پرد برخلاف انتظار',
         'SESSION_EXPIRE_AT_BROWSER_CLOSE و SESSION_COOKIE_AGE را چک کنید. True + بدون max_age = کوکی نشست (با بستن مرورگر می‌رود).'),
        ('sessionid در HTTPS کار نمی‌کند',
         'SESSION_COOKIE_SECURE=True ولی سایت را با HTTP باز کرده‌اید (یا پروکسی HTTPS را درست forward نکرده). در توسعه روی HTTP باید Secure=False بماند.'),
        ('جدول django_session بزرگ شده',
         'نشست‌های منقضی پاک نشده‌اند: <code class="inline-code">python manage.py clearsessions</code> را زمان‌بندی کنید (کرون یا سلری‌بیت فصل ۲۴).'),
        ('دو کاربر یک سبد را می‌بینند!',
         'احتمالاً داده سبد را در متغیر سراسری/کش مشترک ریخته‌اید نه نشست هر کاربر. هر request.session مختص همان کاربر است؛ کد سراسری = باگ امنیتی جدی.'),
    ],
    errors_callout=None,
    exercises=[
        ('تمرین ۱ — کوکی یا نشست؟',
         '<p><strong>سوال:</strong> برای هر داده کدام؟ (الف) تم روشن/تاریک (ب) آیتم‌های سبد خرید مهمان (ج) شناسه ورود کاربر (د) زبان رابط</p>'
         '<p><strong>پاسخ:</strong> الف → کوکی خام (جاوااسکریپت هم لازم دارد) • ب → نشست • ج → خودِ سازوکار نشست جنگو (کوکی sessionid + داده سرور) • د → کوکی (مثل django_language) یا نشست.</p>'),
        ('تمرین ۲ — سناریوی امنیتی',
         '<p><strong>سوال:</strong> مهاجم sessionid کاربری را در کافه‌نت روی مرورگر خودش ست می‌کند. چه حمله‌ای است و کدام تنظیمات خطر را کم می‌کنند؟</p>'
         '<p><strong>پاسخ:</strong> Session Hijacking. سپرها: SESSION_COOKIE_SECURE (فقط HTTPS → شنود سخت)، HttpOnly (دزدی با XSS سخت)، age کوتاه‌تر، و cycle_key() بعد از ورود (جلوگیری از Session Fixation — جنگو در login خودش انجامش می‌دهد).</p>'),
        ('تمرین ۳ — حجم نشست',
         '<p><strong>سوال:</strong> چرا نگه‌داشتن «فهرست کامل ۵۰۰ محصول» در نشست اشتباه است؟</p>'
         '<p><strong>پاسخ:</strong> هر درخواست کل نشست را از دیتابیس می‌خواند/رمزگشایی می‌کند؛ داده حجیم = کندی سراسری. در نشست فقط <strong>شناسه‌ها و تعداد</strong> را نگه دارید ({product_id: qty}) و جزئیات را زمان نمایش با یک کوئری بگیرید — همان طراحی کلاس Cart.</p>'),
    ],
    quiz=[
        dict(q='داده نشست جنگو به‌طور پیش‌فرض کجا ذخیره می‌شود؟',
             opts=['داخل کوکی مرورگر', 'جدول django_session در پایگاه داده',
                   'فایل لاگ', 'حافظه ویو'],
             ans='b', explain='کوکی فقط شناسه (sessionid) دارد؛ داده سمت سرور در دیتابیس (یا کش با SESSION_ENGINE مناسب) است.'),
        dict(q='کدام درباره کوکی خام درست است؟',
             opts=['برای رمز عبور مناسب است', 'کاربر می‌تواند ببیند و تغییرش دهد؛ فقط داده بی‌خطر',
                   'ظرفیت نامحدود دارد', 'سمت سرور ذخیره می‌شود'],
             ans='b', explain='کوکی کاملاً در اختیار کاربر است (~4KB)؛ هرگز داده حساس یا قابل‌اعتمادِ تجاری در آن نگذارید.'),
        dict(q='چرا بعد از تغییر تودرتوی دیکشنری نشست، session.modified=True لازم است؟',
             opts=['برای امنیت', 'جنگو تغییرات «داخل» مقدار را تشخیص نمی‌دهد و ذخیره نمی‌کند',
                   'اجباری در همه حالات است', 'برای رمزنگاری'],
             ans='b', explain='مقایسه «تغییر کرد؟» روی ارجاع مقدار نشانه‌گذاری شده انجام می‌شود؛ mutation درجا دیده نمی‌شود مگر دستی اعلام کنید.'),
        dict(q='فلگ HttpOnly روی کوکی نشست چه می‌کند؟',
             opts=['کوکی را رمزنگاری می‌کند', 'جاوااسکریپت نمی‌تواند آن را بخواند (کاهش خطر دزدی با XSS)',
                   'عمر کوکی را کم می‌کند', 'کوکی فقط خواندنی می‌شود'],
             ans='b', explain='document.cookie دیگر sessionid را نشان نمی‌دهد؛ حتی اگر XSS رخ دهد، دزدی شناسه سخت‌تر می‌شود.'),
        dict(q='cycle_key() چه زمانی استفاده می‌شود؟',
             opts=['هر درخواست', 'بعد از ارتقای سطح دسترسی (مثل ورود) برای جلوگیری از Session Fixation',
                   'هنگام خروج', 'برای پاک کردن سبد'],
             ans='b', explain='شناسه نشست عوض و داده حفظ می‌شود؛ جنگو داخل login() خودکار انجامش می‌دهد.'),
        dict(q='سبد خرید مهمان بهتر است چه چیزی را در نشست نگه دارد؟',
             opts=['کل شیء‌های محصول', 'فقط شناسه محصول و تعداد — جزئیات موقع نمایش از دیتابیس',
                   'قیمت‌ها برای جمع زدن', 'HTML سبد'],
             ans='b', explain='نشست کوچک و به‌روز می‌ماند؛ قیمت/نام از دیتابیس یعنی همیشه معتبر (محصول حذف/گران شده باشد هم درست است).'),
    ],
    project_title='فروشگاه با سبد خرید مهمان',
    project_intro='سبد خرید کامل بدون نیاز به ثبت‌نام — هستهٔ فروشگاه فصل ۳۰.',
    project_checklist=[
        'کلاس Cart با add/remove/set_qty/total و پوشش تست دستی.',
        'صفحه سبد با جدول اقلام، فرم تغییر تعداد و حذف.',
        'context_processor تعداد اقلام در navbar.',
        'ادغام سبد مهمان با حساب کاربری هنگام ورود (سیگنال).',
        'تنظیمات امنیتی نشست (HttpOnly, SameSite, Age) مستندشده.',
    ],
    project_callout=('tip', 'ارتقای طبیعی',
        'بعداً سبد را به مدل دیتابیس منتقل کنید (Cart/CartItem با OneToOne به کاربر) تا بین دستگاه‌ها همگام بماند — سبد نشست فقط برای مهمان‌ها.'),
    summary_items=[
        'HTTP بی‌حالت است؛ کوکی (کلاینت) و نشست (سرور) حافظه می‌دهند.',
        'request.session دیکشنری‌مانند است؛ mutation درجا → modified=True.',
        'سبد خرید: فقط id/qty در نشست، جزئیات از دیتابیس.',
        'کوکی خام برای ترجیحات بی‌خطر؛ هرگز داده حساس.',
        'امنیت: HttpOnly + Secure + SameSite + cycle_key + clearsessions.',
    ],
    golden='قانون طلایی حافظه وب: هرچه کاربر نباید ببیند یا دست ببرد، سمت سرور بماند.',
    faq=[
        ('SESSION_ENGINE کش برای چه وقتی خوب است؟',
         '<p>سایت‌های پربازدید: <code class="inline-code">cached_db</code> (کش با fallback دیتابیس) خواندن نشست را از دیتابیس به <span class="term" data-term="redis">Redis</span> منتقل می‌کند. برای شروع، همان db ساده و قابل اتکاست.</p>'),
        ('نشست نامحدود عمر کند ممکن است؟',
         '<p>SESSION_COOKIE_AGE را بزرگ بگذارید؛ ولی امن نیست. ترکیب رایج: age دو هفته + SESSION_EXPIRE_AT_BROWSER_CLOSE=False + «مرا به خاطر بسپار» اختیاری.</p>'),
        ('چطور همه نشست‌های یک کاربر را ببینم/باطل کنم؟',
         '<p>جنگو Session objects manager را می‌دهد ولی decode دستی لازم دارد. برای مدیریت جدی «دستگاه‌های فعال/خروج از همه‌جا»، الگوهای آماده‌ای با ذخیره user در داده نشست وجود دارد (پکیج‌هایی مثل django-sessions هم کمک می‌کنند).</p>'),
    ],
    next_step='حالا که حافظه را داریم، سرعت را اضافه می‌کنیم: <strong>فصل ۱۹</strong> — <span class="term" data-term="cache">کش</span>: از cache_page تا Redis و استراتژی‌های باطل‌سازی.',
),

# ================================================================ فصل ۱۹
dict(
    n=19, icon='⚡', title='کش کردن (Cache)', cat=4, mins=85, lvl_label='متوسط',
    hero_desc='چرا <span class="term" data-term="cache">کش</span>؟ بک‌اندهای کش (LocalMemory، پایگاه داده، فایل، <span class="term" data-term="redis">Redis</span>)، کش ویو با cache_page، تگ {% cache %}، کش دستی با cache.set/get و باطل‌سازی هوشمند.',
    s1_intro='سریع‌ترین کوئری، کوئری‌ای است که اجرا نمی‌شود! کش یعنی «نتیجه آماده را نگه دار». ولی هر کشی یک قیمت دارد: داده ممکن است کهنه شود. این فصل هم شتاب را یاد می‌دهد هم مدیریت کهنگی را.',
    objectives=[
        'بک‌اندهای کش را مقایسه و پیکربندی کنید.',
        'با cache_page کل خروجی <span class="term" data-term="view">ویو</span> را کش کنید.',
        'با cache.set/get منطق کش دستی بنویسید.',
        'قطعه‌های قالب را با {% cache %} کش کنید.',
        'استراتژی باطل‌سازی (Invalidation) برای داده تغییرپذیر طراحی کنید.',
    ],
    s1_position='<strong>جایگاه فصل:</strong> مکمل QuerySet (۱۵) و پایهٔ بهینه‌سازی فصل ۲۷؛ Redis اینجا دوباره در فصل ۲۴ (سلری) برمی‌گردد.',
    roadmap=[
        ('بک‌اندها', 'از LocMem تا Redis.'),
        ('کش ویو و قالب', 'cache_page و {% cache %}.'),
        ('کش دستی', 'set/get/delete و الگوهای کلید.'),
        ('باطل‌سازی', 'هاردترین بخش کش!'),
    ],
    mind_qs=[
        ('چرا LocalMemoryCache برای تولید چندکاربره بد است؟',
         '<p>چون هر پروسه ورکر کش <strong>خودش</strong> را دارد: داده در ورکر A کش شده، درخواست بعدی به ورکر B می‌رود و کش ندارد؛ حتی باطل‌سازی هم فقط همان ورکر را پاک می‌کند. برای تولید: کش <strong>مشترک</strong> (Redis/Memcached).</p>'),
        ('کش ۵ دقیقه‌ای یعنی چه هزینه‌ای؟',
         '<p>داده تا ۵ دقیقه <strong>کهنه</strong> نمایش داده می‌شود. سوال طراحی: «کاربر چقدر تأخیر در دیدن تغییر را تحمل می‌کند؟» آمار بازدید: عالی برای کش. موجودی انبار: خطرناک!</p>'),
        ('سخت‌ترین مسئله علوم کامپیوتر در این فصل کدام است؟',
         '<p>نام‌گذاری و <strong>باطل‌سازی کش</strong> (شوخی معروف Phil Karlton که جدی است!). وقتی پست ویرایش شد، کدام کلیدهای کش باید پاک شوند؟ فهرست‌ها، صفحه جزئیات، آمار، صفحه نویسنده... طراحی کلید این را ممکن می‌کند.</p>'),
    ],
    prereq_intro='پیش‌نیازها:',
    prereq=[
        'پروژه وبلاگ با ویوهای فهرست/جزئیات/آمار (فصل ۱۵).',
        'فصل ۱۵: درک هزینه کوئری‌ها و N+1.',
        'اختیاری ولی توصیه‌شده: نصب Redis محلی یا داکر (<code class="inline-code">docker run -p 6379:6379 redis</code>).',
        'ابزار اندازه‌گیری: هدر X-Request-Time میدلور فصل ۱۷!',
    ],
    prereq_callout=None,
    concepts=[
        dict(h='۵.۱ بک‌اندهای کش و تنظیمات', body=[
            ('code', 'settings.py — سه پیکربندی رایج', 'python', '''# ۱) توسعه: حافظه محلی (ساده، ولی هر پروسه جدا)
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}

# ۲) تولید ساده: Redis (پیشنهاد ما)
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
    }
}

# ۳) بدون زیرساخت اضافه: کش دیتابیسی
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "my_cache_table",   # ← python manage.py createcachetable
    }
}'''),
            ('callout', 'info', 'انتخاب بک‌اند',
             'یادگیری/توسعه: LocMem کافی است. تولید: <span class="term" data-term="redis">Redis</span> (هم کش، هم بعداً <span class="term" data-term="broker">بروکر</span> <span class="term" data-term="celery">سلری</span> — یک تیر دو نشان). DatabaseCache وقتی Redis ندارید و حجم کم است.'),
        ]),
        dict(h='۵.۲ کش سطح ویو: cache_page', body=[
            ('code', 'ساده‌ترین کش ممکن', 'python', '''from django.views.decorators.cache import cache_page


@cache_page(60 * 10)          # ۱۰ دقیقه
def stats_dashboard(request):
    # کوئری‌های سنگین فصل ۱۵...
    return render(request, "blog/stats.html", context)'''),
            '<p>یا در urls.py برای CBVها:</p>',
            ('code', 'urls.py', 'python', '''path("stats/", cache_page(600)(StatsView.as_view()), name="stats"),'''),
            ('callout', 'warn', 'هشدار شخصی‌سازی',
             'cache_page کل پاسخ را کش می‌کند — <strong>برای صفحه‌ای که محتوای کاربر-محور دارد خطرناک است</strong> (navbar «خوش آمدید سارا» به کاربر بعدی نشان داده می‌شود!). فقط برای صفحات کاملاً عمومی: آمار، درباره ما، فید.'),
        ]),
        dict(h='۵.۳ کش دستی: API سطح پایین', body=[
            ('code', 'الگوی cache-aside (رایج‌ترین)', 'python', '''from django.core.cache import cache


def get_popular_posts():
    key = "blog:popular_posts:v1"
    posts = cache.get(key)
    if posts is None:                          # کش miss
        posts = list(
            Post.objects.filter(published=True)
            .order_by("-views_count")
            .values("id", "title", "slug")[:10]
        )
        cache.set(key, posts, timeout=300)     # ۵ دقیقه
    return posts'''),
            '<ul>'
            '<li>کلیدها را <strong>ساختاریافته و نسخه‌دار</strong> نام بزنید: <code class="inline-code">app:entity:action:v1</code> — تغییر ساختار داده با bump نسخه حل می‌شود.</li>'
            '<li>cache.add فقط اگر نبود؛ cache.get_or_set ترکیب آماده؛ cache.incr/decr شمارنده اتمی.</li>'
            '<li>داده باید <strong>سریال‌شدنی</strong> باشد (pickle)؛ ویو/شیء زنده نگذارید — list(values()) عالی است.</li></ul>',
        ]),
        dict(h='۵.۴ کش قالب با {% cache %}', body=[
            ('code', 'کش قطعه پرهزینه در قالب', 'html', '''{% load cache %}

{# کش ۱۵ دقیقه‌ای، به‌ازای هر زبان جدا #}
{% cache 900 sidebar_popular request.LANGUAGE_CODE %}
  <aside>
    {% for post in popular_posts %}
      <li><a href="{{ post.get_absolute_url }}">{{ post.title }}</a></li>
    {% endfor %}
  </aside>
{% endcache %}'''),
            '<p>آرگومان‌های بعد از نام قطعه (request.LANGUAGE_CODE) بخشی از <strong>کلید</strong> می‌شوند — برای هر مقدار، کش جدا. می‌توانید post.pk هم بدهید تا قطعه هر پست جدا کش شود.</p>',
        ]),
        dict(h='۵.۵ باطل‌سازی: وقتی داده عوض شد', body=[
            ('code', 'باطل‌سازی هدفمند با سیگنال (فصل ۱۶!)', 'python', '''from django.core.cache import cache
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from .models import Post


@receiver([post_save, post_delete], sender=Post)
def clear_post_caches(sender, instance, **kwargs):
    cache.delete(f"blog:post_detail:{instance.pk}:v1")
    cache.delete("blog:popular_posts:v1")
    # فهرست‌ها: نسخه را بالا ببر (ارزان‌تر از deleteهای زیاد)
    cache.incr("blog:version", delta=1) if cache.get("blog:version") \\
        else cache.set("blog:version", 1)'''),
            ('code', 'الگوی «کش نسخه‌دار»', 'python', '''def popular_key():
    version = cache.get_or_set("blog:version", 1, timeout=None)
    return f"blog:popular_posts:v{version}"


posts = cache.get_or_set(popular_key(), compute_popular, timeout=300)'''),
            ('callout', 'info', 'سه استراتژی باطل‌سازی',
             '① <strong>TTL</strong>: فقط زمان انقضا (ساده؛ کهنگی تا TTL). ② <strong>هدفمند</strong>: delete کلیدهای مرتبط در سیگنال/ویو (دقیق؛ نیازمند انضباط کلیدها). ③ <strong>نسخه‌دار</strong>: بالا بردن نسخه، کل دسته را بی‌اثر می‌کند (بی‌نیاز از حذف تک‌تک). ترکیب ①+③ متداول‌ترین است.'),
        ]),
    ],
    example_intro='بهینه‌سازی واقعی صفحه آمار فصل ۱۵ — با اندازه‌گیری قبل/بعد:',
    example=[
        ('code', 'قبل از کش (۴ کوئری سنگین)', 'python', '''def stats_dashboard(request):
    totals = Post.objects.aggregate(...)
    top_authors = Author.objects.annotate(...)[:5]
    top_tags = Tag.objects.annotate(...)[:8]
    popular = Post.objects.filter(...).select_related(...)[:10]
    return render(request, "blog/stats.html", {...})'''),
        ('code', 'بعد: کش نسخه‌دار کل بافت', 'python', '''def stats_dashboard(request):
    version = cache.get_or_set("stats:version", 1, timeout=None)
    key = f"stats:context:v{version}"
    context = cache.get(key)
    if context is None:
        context = {
            "totals": Post.objects.aggregate(...),
            "top_authors": list(Author.objects.annotate(...)[:5]),
            "top_tags": list(Tag.objects.annotate(...)[:8]),
            "popular": list(Post.objects.filter(...).values(
                "title", "slug", "views_count", "author__name")[:10]),
        }
        cache.set(key, context, timeout=600)
    return render(request, "blog/stats.html", context)


@receiver([post_save, post_delete], sender=Post)
def bump_stats(sender, **kwargs):
    cache.incr("stats:version") if cache.get("stats:version") else None'''),
        ('code', 'اندازه‌گیری با میدلور فصل ۱۷', 'text', '''بدون کش:  X-Request-Time: 240ms  (۴ کوئری)
با کش miss: 245ms
با کش hit:   12ms   ← ۲۰ برابر سریع‌تر 🚀'''),
    ],
    workshop_intro='سه سناریوی کش روی وبلاگ پیاده کنید:',
    workshop_tasks=[
        '<strong>کارگاه ۱:</strong> ویو آمار را با الگوی cache-aside کش کنید (TTL=۵ دقیقه) و با هدر زمان، تفاوت hit/miss را اندازه بگیرید.',
        '<strong>کارگاه ۲:</strong> باطل‌سازی هدفمند: با انتشار/ویرایش/حذف پست، کلیدهای آمار و popular پاک شوند (سیگنال).',
        '<strong>کارگاه ۳:</strong> سایدبار «مطالب محبوب» را در قالب با {% cache %} کش کنید و بررسی کنید که برای کاربران مختلف یک نتیجه کش‌شده می‌آید (چرا اینجا اشکالی ندارد؟).',
    ],
    workshop_answers=[
        ('پاسخ کارگاه ۱',
         '<div class="code-box"><div class="code-head"><span>cache-aside</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">def stats_dashboard(request):\n    key = "blog:stats:v1"\n    context = cache.get(key)\n    if context is None:\n        context = build_stats_context()      # همان ۴ کوئری فصل ۱۵\n        cache.set(key, context, timeout=300)\n    return render(request, "blog/stats.html", context)</code></pre></div>'
         '<p>دو بار پشت‌سرهم صفحه را باز کنید: اولی miss (کند)، دومی hit (سریع). مقدار QuerySet را مستقیم نکشید؛ list(values(...)) یا داده ساده سریال‌پذیر بگذارید.</p>'),
        ('پاسخ کارگاه ۲',
         '<div class="code-box"><div class="code-head"><span>باطل‌سازی با سیگنال</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">@receiver([post_save, post_delete], sender=Post)\ndef clear_blog_caches(sender, instance=None, **kwargs):\n    cache.delete_many(["blog:stats:v1", "blog:popular_posts:v1"])\n    # برای کش قطعه قالب، کلیدش: "template.cache.sidebar_popular...."\n    # نسخه‌گذاری (کارگاه مفهوم ۵.۵) راه تمیزتر است.</code></pre></div>'
         '<p>تله رایج: {% cache %} قالب کلید خودش را دارد؛ یا از استراتژی نسخه استفاده کنید یا TTL کوتاه برای قطعه قالب و delete برای داده‌های دستی.</p>'),
        ('پاسخ کارگاه ۳',
         '<p><code class="inline-code">{% cache 600 sidebar_popular %}</code> بدون آرگومان کاربرمحور → یک کش برای همه. اشکالی ندارد چون «مطالب محبوب» <strong>شخصی‌سازی‌نشده</strong> است. اگر داخل قطعه چیزی مثل user.username بود، باید آرگانی مثل request.user.pk به کلید اضافه می‌کردید (و حجم کش ضرب‌در تعداد کاربران می‌شد — هزینه آگاهانه).</p>'),
    ],
    errors=[
        ('کش کار می‌کند ولی داده قدیمی می‌بینم',
         'باطل‌سازی ندارید! یا TTL را کوتاه کنید، یا در مسیرهای تغییر (save/delete ویوها یا سیگنال) delete/نسخه‌بump بگذارید. دیباگ: cache.get(key) را در شل چک کنید.'),
        ('در production کش به نظر نمی‌رسد',
         'LocMemCache با چند ورکر Gunicorn = هر ورکر کش خودش (missهای مداوم). بک‌اند مشترک (Redis) تنظیم کنید.'),
        ('PicklingError هنگام cache.set',
         'شیء غیرسریال‌شدنی (مثل QuerySet تنبل یا شیء با اتصال دیتابیس) گذاشته‌اید. به داده ساده تبدیل کنید: list(qs.values(...)).'),
        ('صفحه با cache_page محتوای کاربر دیگر را نشان می‌دهد',
         'صفحه شخصی‌سازی‌شده را کش سراسری کرده‌اید — خطر امنیتی/UX! فقط صفحات عمومی cache_page شوند؛ بخش‌های خصوصی با {% cache %} جدا یا Vary.'),
        ('Redis وصل نمی‌شود: Connection refused',
         'سرور Redis بالا نیست یا LOCATION اشتباه است (پورت/db). با redis-cli ping بررسی کنید → PONG. در داکر: نگاشت پورت 6379.'),
    ],
    errors_callout=('tip', 'اول اندازه، بعد کش',
        'کش را فقط جایی بگذارید که <strong>اندازه‌گیری</strong> گلوگاه نشان داده (فصل ۲۷). کش بی‌مورد = پیچیدگی و باگ کهنگی بدون سود.'),
    exercises=[
        ('تمرین ۱ — انتخاب سطح کش',
         '<p><strong>سوال:</strong> برای هر مورد کدام مکانیزم؟ (الف) صفحه «درباره ما» کاملاً ثابت (ب) فهرست پربازدیدها در سایدبار همه صفحات (ج) نتیجه یک محاسبه سنگین در یک ویو (د) کل صفحه آمار عمومی</p>'
         '<p><strong>پاسخ:</strong> الف → cache_page با TTL بلند • ب → {% cache %} در قالب • ج → cache.get_or_set دستی • د → cache_page یا کش بافت دستی.</p>'),
        ('تمرین ۲ — طراحی کلید',
         '<p><strong>سوال:</strong> کلیدهای مناسب برای «جزئیات پست ۵» و «فهرست پست‌های صفحه ۲ دسته python» طراحی کنید.</p>'
         '<p><strong>پاسخ نمونه:</strong> <code class="inline-code">blog:post:5:v1</code> و <code class="inline-code">blog:list:cat=python:page=2:v1</code> — ساختار app:entity:params:version. از کلیدهای مبهم مثل "data1" بپرهیزید.</p>'),
        ('تمرین ۳ — کهنگی قابل قبول',
         '<p><strong>سوال:</strong> برای هر داده TTL پیشنهادی و چرا؟ (الف) آمار بازدید (ب) قیمت محصول در فروشگاه (ج) فهرست پست‌های منتشرشده</p>'
         '<p><strong>پاسخ نمونه:</strong> الف → ۵-۱۵ دقیقه (کهنگی بی‌ضرر) • ب → بدون TTL + باطل‌سازی هدفمند فوری (کهنگی = ضرر مالی!) • ج → ۱ دقیقه + باطل‌سازی با سیگنال انتشار (تعادل تازگی/سرعت).</p>'),
    ],
    quiz=[
        dict(q='چرا LocMemCache برای تولید چندورکری مناسب نیست؟',
             opts=['کند است', 'کش هر پروسه جداست؛ اشتراک و باطل‌سازی سراسری ممکن نیست',
                   'داده را رمزنگاری نمی‌کند', 'ظرفیتش کم است'],
             ans='b', explain='Gunicorn چند ورکر دارد؛ کش درون‌حافظه‌ای هر ورکر مستقل است → miss زیاد و رفتار ناهمسان. Redis/Memcached مشترک است.'),
        dict(q='@cache_page(600) روی ویویی با navbar شخصی‌سازی‌شده چه خطری دارد؟',
             opts=['کند می‌شود', 'محتوای کاربر A ممکن است به کاربر B نشان داده شود',
                   'هیچ — امن است', 'CSRF را می‌شکند'],
             ans='b', explain='cache_page کل پاسخ را فارغ از کاربر کش می‌کند؛ فقط برای صفحات کاملاً عمومی استفاده شود.'),
        dict(q='الگوی cache-aside کدام است؟',
             opts=['همیشه اول کش پاک شود', 'بخوان از کش؛ اگر نبود، محاسبه کن، در کش بگذار، برگردان',
                   'کش توسط دیتابیس پر شود', 'هر نوشتن، کش را پر کند'],
             ans='b', explain='رایج‌ترین الگو: get → miss → compute → set. ساده و پیش‌بینی‌پذیر.'),
        dict(q='آرگومان‌های اضافه تگ {% cache 900 name user.pk %} چه نقشی دارند؟',
             opts=['زمان انقضا', 'بخشی از کلید کش — به‌ازای هر مقدار، کش جداگانه',
                   'نام قالب', 'فقط مستندسازی'],
             ans='b', explain='کلید = نام قطعه + آرگومان‌ها؛ با user.pk هر کاربر کش خودش را می‌گیرد (دقت و هزینه بیشتر).'),
        dict(q='ارزان‌ترین راه باطل‌سازی یک «دسته» کلید چیست؟',
             opts=['delete تک‌تک کلیدها', 'بالا بردن نسخه در کلیدها (version bump)',
                   'flush کل Redis', 'TTL یک ثانیه'],
             ans='b', explain='تغییر شماره نسخه، همه کلیدهای قدیمی را بی‌مصرف می‌کند بدون حذف فیزیکی؛ کلیدهای جدید خودکار ساخته می‌شوند.'),
        dict(q='کدام داده برای cache_page با TTL ده دقیقه مناسب‌تر است؟',
             opts=['موجودی انبار', 'صفحه «درباره ما»',
                   'داشبورد شخصی کاربر', 'سبد خرید'],
             ans='b', explain='صفحه عمومی و کم‌تغییر؛ بقیه یا شخصی‌اند یا کهنگی‌شان پرهزینه است.'),
    ],
    project_title='لایه کش وبلاگ',
    project_intro='استراتژی کش کامل و مستندشده برای وبلاگ طراحی و پیاده کنید.',
    project_checklist=[
        'انتخاب و پیکربندی بک‌اند (Redis یا DatabaseCache) + ایجاد جدول/سرویس.',
        'کش بافت صفحه آمار با الگوی نسخه‌دار.',
        'باطل‌سازی با سیگنال روی Post (save/delete) و Comment.',
        '{% cache %} برای سایدبار محبوب‌ها.',
        'گزارش اندازه‌گیری قبل/بعد (اسکرین‌شات هدر X-Request-Time) در یادداشت‌ها.',
    ],
    project_callout=('tip', 'سنجه موفقیت',
        'صفحه آمار از ~۲۰۰ms به زیر ۲۰ms برسد و بعد از انتشار پست جدید، حداکثر یک رفرش بعد تغییرات دیده شوند.'),
    summary_items=[
        'بک‌اند: توسعه LocMem، تولید <span class="term" data-term="redis">Redis</span> مشترک.',
        'cache_page برای صفحات کاملاً عمومی؛ خطر شخصی‌سازی را بشناسید.',
        'cache.get_or_set و کلیدهای ساختاریافته/نسخه‌دار.',
        '{% cache %} برای قطعه‌های قالب با کلید پارامتری.',
        'باطل‌سازی: TTL + هدفمند (سیگنال) + نسخه‌دار — و همیشه اول اندازه‌گیری.',
    ],
    golden='کش معامله است: سرعت در برابر تازگی. نرخ معامله را آگاهانه انتخاب کنید.',
    faq=[
        ('Memcached یا Redis؟',
         '<p>برای کش خالص هر دو عالی‌اند. Redis را ترجیح می‌دهیم چون در فصل ۲۴ به‌عنوان بروکر <span class="term" data-term="celery">سلری</span> هم به کار می‌آید — یک سرویس، دو نقش.</p>'),
        ('کش را چطور در تست‌ها خنثی کنم؟',
         '<p>در تست از بک‌اند DummyCache استفاده کنید: override_settings(CACHES={"default": {"BACKEND": "django.core.cache.backends.dummy.DummyCache"}}) — همیشه miss، نتایج قطعی.</p>'),
        ('فشار روی Redis زیاد شد چه کنم؟',
         '<p>maxmemory + سیاست eviction (allkeys-lru) تنظیم کنید، TTLهای نامحدود ندهید، کلیدهای حجیم را بشکنید و در فصل ۲۷ ابزارهای پایش (INFO، redis-cli --latency) را می‌بینیم.</p>'),
    ],
    next_step='سرعت را دیدیم؛ حالا «درستی» را تضمین می‌کنیم. <strong>فصل ۲۰</strong>: <span class="term" data-term="test">تست‌نویسی</span> — جایی که کد فصل‌های قبل زیر ذره‌بین خودکار می‌رود.',
),

# ================================================================ فصل ۲۰
dict(
    n=20, icon='🧪', title='تست‌نویسی (Testing) در جنگو', cat=4, mins=95, lvl_label='متوسط',
    hero_desc='چرا تست؟ TestCase و <span class="term" data-term="test-client">TestClient</span>، تست مدل‌ها، ویوها و فرم‌ها، setUp، assertهای کاربردی، اجرای تست‌ها و الگوی <span class="term" data-term="tdd">TDD</span> ساده.',
    s1_intro='تست خودکار یعنی «شبکه اطمینان»: با خیال راحت ریفکتور کنید، دیپلوی کنید و بخوابید! جنگو ابزار تست داخلی دارد (بر پایه unittest) و از فصل قبل هر منطقی که نوشتیم را می‌توانیم تست‌پذیر کنیم.',
    objectives=[
        'انواع تست (واحد، دیدگاه ویو، یکپارچگی) را تشخیص دهید.',
        'با TestCase و setUp داده تست بسازید.',
        '<span class="term" data-term="view">ویوها</span> را با <span class="term" data-term="test-client">self.client</span> تست کنید (GET/POST، redirect، <span class="term" data-term="template">قالب</span>).',
        'مدل‌ها، متدها و فرم‌ها را با assertهای دقیق بسنجید.',
        'یک چرخه <span class="term" data-term="tdd">TDD</span> کامل (قرمز → سبز → بازآرایی) را تجربه کنید.',
    ],
    s1_position='<strong>جایگاه فصل:</strong> مهارت «حرفه‌ای‌ساز» دوره؛ تست مجوزها (۱۳)، کش (۱۹) و API (۲۲-۲۳) در پروژه‌ها به همین ابزارها تکیه دارد.',
    roadmap=[
        ('چرا و چه چیزی', 'هرم تست و انتخاب هدف.'),
        ('ابزارها', 'TestCase، setUp و assertها.'),
        ('تست ویو', 'client، POST و احراز هویت.'),
        ('TDD عملی', 'یک ویژگی از صفر با تست.'),
    ],
    mind_qs=[
        ('تست‌ها روی دیتابیس واقعی اجرا می‌شوند؟',
         '<p>نه! جنگو یک <strong>دیتابیس تست جدا</strong> (test_...) می‌سازد، هر TestCase را در تراکنشی اجرا و <strong>rollback</strong> می‌کند. داده واقعی دست‌نخورده می‌ماند — با خیال راحت delete بنویسید!</p>'),
        ('چه چیزی را تست کنیم و چه چیزی را نه؟',
         '<p>منطق خودتان را: متدهای مدل، clean_های فرم، مسیرهای ویو (مخصوصاً مجوز و POST). چیزهای جنگو را نه: اینکه ListView کار می‌کند تست جنگوست، نه شما. «تست رفتار، نه پیاده‌سازی».</p>'),
        ('چرا می‌گویند تست گران نیست، باگ گران است؟',
         '<p>یک تست ۵ دقیقه‌ای، همان سناریو را هر دیپلوی دوباره چک می‌کند. باگی که در تولید پیدا شود، ده‌ها برابر هزینه دارد (داده خراب، اعتماد از دست رفته). تست = بیمه ارزان.</p>'),
    ],
    prereq_intro='پیش‌نیازها:',
    prereq=[
        'پروژه وبلاگ کامل (مدل، ویو، فرم، احراز هویت، مجوزها).',
        'فایل tests.py هر اپ (خودکار ساخته شده).',
        'آشنایی با assert پایتون و دکوریتور.',
        'دیتابیس تست ساخته می‌شود؛ فضای خالی و زمان کافی (اولین اجرا کمی طول می‌کشد).',
    ],
    prereq_callout=None,
    concepts=[
        dict(h='۵.۱ هرم تست و اولین تست', body=[
            '<ul>'
            '<li><strong>واحد (Unit)</strong>: یک تابع/متد تنها — زیاد و سریع.</li>'
            '<li><strong>یکپارچگی (Integration)</strong>: ویو + قالب + دیتابیس با هم — کمتر.</li>'
            '<li><strong>رابط کاربری (E2E)</strong>: مرورگر واقعی (Selenium/Playwright) — حداقل.</li></ul>',
            ('code', 'blog/tests.py — ساده‌ترین تست', 'python', '''from django.test import TestCase

from .models import Author, Post


class PostModelTest(TestCase):
    def test_str_returns_title(self):
        author = Author.objects.create(name="سارا")
        post = Post.objects.create(
            title="سلام", slug="salam", body="...", author=author)
        self.assertEqual(str(post), "سلام")'''),
            ('code', 'اجرا', 'bash', '''python manage.py test                  # همه
python manage.py test blog             # فقط اپ blog
python manage.py test blog.tests.PostModelTest.test_str_returns_title
python manage.py test --keepdb -v 2    # سریع‌تر + پرورbose'''),
        ]),
        dict(h='۵.۲ setUp و ساخت داده', body=[
            ('code', 'الگوی استاندارد', 'python', '''class PostViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # یک‌بار برای همه تست‌های کلاس (سریع‌تر)
        cls.author = Author.objects.create(name="سارا")
        cls.post = Post.objects.create(
            title="پست عمومی", slug="public", body="x",
            author=cls.author, published=True)
        cls.draft = Post.objects.create(
            title="پست خصوصی", slug="draft", body="x",
            author=cls.author, published=False)

    def setUp(self):
        # قبل از «هر» متد تست
        self.user = User.objects.create_user(
            "ali", password="pass12345!")'''),
            ('callout', 'info', 'setUpTestData یا setUp؟',
             'setUpTestData برای داده <strong>فقط‌خواندنی</strong> یک‌بار ساخته می‌شود (سرعت)؛ setUp برای داده‌ای که تست تغییرش می‌دهد (مثل کاربر ورود/خروج). ترکیب هر دو رایج است.'),
        ]),
        dict(h='۵.۳ تست ویوها با client', body=[
            ('code', 'GET، قالب، بافت و وضعیت', 'python', '''    def test_list_shows_only_published(self):
        response = self.client.get(reverse("blog:list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post_list.html")
        self.assertContains(response, "پست عمومی")
        self.assertNotContains(response, "پست خصوصی")
        self.assertEqual(len(response.context["posts"]), 1)

    def test_draft_detail_is_404(self):
        url = reverse("blog:detail", args=[self.draft.slug])
        self.assertEqual(self.client.get(url).status_code, 404)'''),
            ('code', 'POST و احراز هویت', 'python', '''    def test_comment_post_creates_and_redirects(self):
        url = reverse("blog:add_comment", args=[self.post.slug])
        response = self.client.post(url, {
            "name": "رضا", "text": "عالی بود! واقعاً",
        })
        self.assertRedirects(response, self.post.get_absolute_url())
        self.assertEqual(self.post.comments.count(), 1)

    def test_create_post_requires_login(self):
        url = reverse("blog:post_create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertIn("/accounts/login/", response.url)

    def test_author_can_edit_own_post(self):
        self.client.login(username="ali", password="pass12345!")
        # ... ساخت پست متعلق به ali و درخواست ویرایش
        response = self.client.post(url, {"title": "جدید", "body": "..."})
        self.post.refresh_from_db()'''),
        ]),
        dict(h='۵.۴ تست فرم و متدهای سفارشی', body=[
            ('code', 'فرم‌ها مستقیم تست می‌شوند', 'python', '''class CommentFormTest(TestCase):
    def test_valid_form(self):
        form = CommentForm(data={"name": "رضا", "text": "متنی بلندتر از ده"})
        self.assertTrue(form.is_valid())

    def test_ad_text_rejected(self):
        form = CommentForm(data={"name": "رضا",
                                 "text": "این تبلیغ است و بلند هم هست!"})
        self.assertFalse(form.is_valid())
        self.assertIn("text", form.errors)

    def test_empty_name_invalid(self):
        form = CommentForm(data={"name": "", "text": "متنی بلندتر از ده"})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["name"], ["This field is required."])'''),
        ]),
        dict(h='۵.۵ چرخه TDD و نکات اجرایی', body=[
            ('code', 'ویژگی جدید: «پست‌های پیشنهادی نویسنده»', 'python', '''# ۱) قرمز — اول تست (ویژگی وجود ندارد؛ تست شکست می‌خورد)
    def test_related_by_author_shown(self):
        Post.objects.create(title="دیگر", slug="other",
                            body="x", author=self.author, published=True)
        response = self.client.get(
            reverse("blog:detail", args=[self.post.slug]))
        self.assertEqual(len(response.context["related_posts"]), 1)

# ۲) سبز — حداقل کد در ویو:
#    context["related_posts"] = Post.objects.filter(
#        author=post.author, published=True).exclude(pk=post.pk)[:3]

# ۳) بازآرایی — تمیزکاری با خیال راحت (تست پاس می‌ماند)'''),
            ('code', 'اجرای حرفه‌ای', 'bash', '''python manage.py test --parallel 4      # موازی
python manage.py test --keepdb          # دیتابیس تست را نگه دار (سریع)
python manage.py test --failfast        # اولین شکست، توقف

# پوشش کد:
pip install coverage
coverage run manage.py test && coverage report -m'''),
            ('callout', 'tip', 'چه چیزی را حتماً تست کنیم',
             '① هر مسیر مجوز (ناشناس/کاربر/مدیر) ② هر POST با داده نامعتبر ③ منطق پولی/عددی ④ باطل‌سازی‌های مهم (کش/سیگنال). تست‌های شکننده (وابسته به ترتیب/زمان واقعی) را با freezegun و ترتیب‌ناپذیری اصلاح کنید.'),
        ]),
    ],
    example_intro='مجموعه تست کامل برای یک ویژگی واقعی — «انتشار پست فقط توسط ویراستار»:',
    example=[
        ('code', 'blog/tests/test_publish.py', 'python', '''from django.contrib.auth.models import Group, Permission
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from ..models import Author, Post


class PublishPermissionTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author_user = User.objects.create_user("writer", password="p")
        cls.editor_user = User.objects.create_user("editor", password="p")
        perm = Permission.objects.get(codename="publish_post")
        cls.editor_user.user_permissions.add(perm)

        cls.author = Author.objects.create(name="A")
        cls.post = Post.objects.create(
            title="t", slug="t", body="b", author=cls.author, published=False)

    def url(self):
        return reverse("blog:publish", args=[self.post.pk])

    def test_anonymous_redirected_to_login(self):
        r = self.client.get(self.url())
        self.assertEqual(r.status_code, 302)

    def test_writer_forbidden(self):
        self.client.login(username="writer", password="p")
        r = self.client.post(self.url())
        self.assertEqual(r.status_code, 403)   # raise_exception=True
        self.post.refresh_from_db()
        self.assertFalse(self.post.published)

    def test_editor_can_publish(self):
        self.client.login(username="editor", password="p")
        r = self.client.post(self.url())
        self.post.refresh_from_db()
        self.assertTrue(self.post.published)

    def test_get_not_allowed(self):
        self.client.login(username="editor", password="p")
        r = self.client.get(self.url())
        self.assertIn(r.status_code, (403, 405))'''),
        ('code', 'اجرا', 'bash', '''python manage.py test blog.tests.test_publish -v 2
# test_anonymous_redirected_to_login ... ok
# test_editor_can_publish ... ok
# test_get_not_allowed ... ok
# test_writer_forbidden ... ok'''),
        '<p>چهار تست، همه مسیرهای دسترسی و دو حالت متد را پوشش می‌دهند. اگر فردا ویو را ریفکتور کنید، این تست‌ها اخطار می‌دهند.</p>',
    ],
    workshop_intro='شبکه اطمینان وبلاگ خودتان را ببافید:',
    workshop_tasks=[
        '<strong>کارگاه ۱:</strong> برای هر ویوی عمومی (list, detail, search) حداقل دو تست بنویسید: وضعیت ۲۰۰ + صحت داده نمایشی (فقط منتشرشده‌ها).',
        '<strong>کارگاه ۲:</strong> برای فرم کامنت: داده معتبر، متن تبلیغاتی (رد)، و فیلد خالی — سه تست با بررسی form.errors.',
        '<strong>کارگاه ۳:</strong> یک ویژگی جدید با TDD کامل: «دکمه کپی لینک فقط برای پست‌های منتشرشده» — اول تست، بعد کد.',
    ],
    workshop_answers=[
        ('پاسخ کارگاه ۱',
         '<div class="code-box"><div class="code-head"><span>تست ویوهای عمومی</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">def test_list_ok_and_only_published(self):\n    r = self.client.get(reverse("blog:list"))\n    self.assertEqual(r.status_code, 200)\n    slugs = [p.slug for p in r.context["posts"]]\n    self.assertIn("public", slugs)\n    self.assertNotIn("draft", slugs)\n\n\ndef test_detail_of_published(self):\n    r = self.client.get(reverse("blog:detail", args=["public"]))\n    self.assertEqual(r.status_code, 200)\n    self.assertEqual(r.context["post"].slug, "public")\n\n\ndef test_detail_of_draft_404(self):\n    r = self.client.get(reverse("blog:detail", args=["draft"]))\n    self.assertEqual(r.status_code, 404)\n\n\ndef test_search_filters(self):\n    r = self.client.get(reverse("blog:search"), {"q": "عمومی"})\n    self.assertContains(r, "پست عمومی")</code></pre></div>'),
        ('پاسخ کارگاه ۲',
         '<div class="code-box"><div class="code-head"><span>تست فرم کامنت</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">def test_valid(self):\n    f = CommentForm({"name": "رضا", "text": "یک نظر کاملاً معمولی"})\n    self.assertTrue(f.is_valid(), f.errors)\n\n\ndef test_ad_rejected(self):\n    f = CommentForm({"name": "رضا", "text": "این تبلیغ محصول است!"})\n    self.assertFalse(f.is_valid())\n    self.assertIn("text", f.errors)\n\n\ndef test_required_fields(self):\n    f = CommentForm({"name": "", "text": ""})\n    self.assertFalse(f.is_valid())\n    self.assertIn("name", f.errors)</code></pre></div>'
         '<p>نکته: <code class="inline-code">self.assertTrue(f.is_valid(), f.errors)</code> — پاس دادن errors به‌عنوان پیام، دیباگ شکست را راحت می‌کند.</p>'),
        ('پاسخ کارگاه ۳',
         '<p><strong>قرمز:</strong></p>'
         '<div class="code-box"><div class="code-head"><span>تست ابتدا</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">def test_copy_button_only_for_published(self):\n    r = self.client.get(reverse("blog:detail", args=["public"]))\n    self.assertContains(r, "data-copy-link")\n    r = self.client.get(reverse("blog:detail", args=["draft"]))  # 404\n\n\ndef test_draft_copy_not_in_author_view(self):\n    # برای نویسنده، draft با 200 ولی بدون دکمه نمایش داده شود\n    ...</code></pre></div>'
         '<p><strong>سبز:</strong> در قالب <code class="inline-code">{% if post.published %}&lt;button data-copy-link&gt;کپی لینک&lt;/button&gt;{% endif %}</code>. <strong>بازآرایی:</strong> اگر شرط‌ها زیاد شدند، به یک متد/property مثل post.is_shareable منتقل کنید — تست‌ها محافظتتان می‌کنند.</p>'),
    ],
    errors=[
        ('خطای <code>Table ... doesn\'t exist</code> یا داده پیدا نمی‌شود',
         'داده را خارج از TestCase (مثلاً در ماژول) ساخته‌اید یا از دیتابیس واقعی می‌خوانید. همه ساخت‌و‌ساز داخل setUpTestData/setUp/متد تست باشد — دیتابیس تست خالی شروع می‌شود.'),
        ('client.login کار نمی‌کند (302 به login)',
         'رمز اشتباه است (create_user رمز را هش می‌کند؛ login با رمز خام). در تست رمز را یک‌جا تعریف کنید. همچنین username نه email — مگر backend عوض کرده باشید.'),
        ('POST خطای 403 CSRF می‌دهد',
         'خودکار نیست! client جنگو CSRF را bypass می‌کند. اگر 403 دیدید، احتمالاً middleware دست‌کاری شده یا با Requests/مرورگر تست می‌کنید نه self.client.'),
        ('تست‌ها به ترتیب پاس می‌شوند و تنها شکست می‌خورند',
         'وابستگی بین تست‌ها (داده مشترک تغییرپذیر). هر تست باید مستقل باشد: داده خودش را بسازد. setUpTestData را فقط برای داده فقط‌خواندنی.'),
        ('تست‌ها خیلی کندند',
         '--keepdb و --parallel را فعال کنید، دیتابیس تست را ساده نگه دارید و از ساخت داده سنگین در هر تست بپرهیزید (factory_boy کمک می‌کند).'),
    ],
    errors_callout=None,
    exercises=[
        ('تمرین ۱ — assert درست',
         '<p><strong>سوال:</strong> کدام assert برای هر بررسی؟ (الف) کد وضعیت ۳۰۲ (ب) وجود متن در پاسخ (ج) استفاده از قالب مشخص (د) برابرسی دو مقدار (ه) رد شدن به نشانی خاص با پارامتر next</p>'
         '<p><strong>پاسخ:</strong> الف → assertEqual(r.status_code, 302) یا assertRedirects • ب → assertContains • ج → assertTemplateUsed • د → assertEqual • ه → assertRedirects(r, "/login/?next=/blog/new/").</p>'),
        ('تمرین ۲ — دامنه تست',
         '<p><strong>سوال:</strong> این‌ها را تست می‌کنید یا نه؟ (الف) اینکه Django LoginView کار می‌کند (ب) اینکه ویوی شما فقط مالک را راه می‌دهد (ج) اینکه sqlite درست نصب شده (د) اینکه slugify شما اسلاگ یکتا می‌سازد</p>'
         '<p><strong>پاسخ:</strong> الف → نه (تست خود جنگو) • ب → بله (منطق دسترسی شما) • ج → نه (زیرساخت) • د → بله (منطق سفارشی کارگاه فصل ۱۱).</p>'),
        ('تمرین ۳ — TDD معکوس',
         '<p><strong>سناریو:</strong> باگی گزارش شده: «کاربر عادی می‌تواند پست دیگران را حذف کند». اولین قدم TDD چیست؟</p>'
         '<p><strong>پاسخ:</strong> اول یک تست <strong>شکست‌خورنده</strong> که باگ را بازتولید کند بنویسید (user B حذف پست user A → انتظار 403/404). سپس کد را اصلاح تا تست سبز شود. تست باگ = نگهبان همیشگی در برابر بازگشت باگ (regression).</p>'),
    ],
    quiz=[
        dict(q='دیتابیس تست جنگو چه ویژگی دارد؟',
             opts=['همان دیتابیس توسعه است', 'جدا ساخته می‌شود و هر TestCase با rollback ایزوله است',
                   'فقط خواندنی است', 'باید دستی ساخت'],
             ans='b', explain='جنگو test_ database می‌سازد، مهاجرت می‌زند و داده هر تست را برمی‌گرداند؛ داده واقعی امن است.'),
        dict(q='setUpTestData چه مزیتی بر setUp دارد؟',
             opts=['هر متد تست داده تازه می‌گیرد', 'یک‌بار برای کل کلاس ساخته می‌شود — سریع‌تر (برای داده فقط‌خواندنی)',
                   'اجباری است', 'روی دیتابیس واقعی می‌نویسد'],
             ans='b', explain='داده فقط‌خواندنی یک‌بار ساخته و بین تست‌ها اشتراک می‌شود؛ داده تغییرپذیر در setUp تا هر تست نسخه تمیز بگیرد.'),
        dict(q='self.client در تست چیست؟',
             opts=['مرورگر واقعی', 'کلاینت ساختگی که بدون شبکه به ویوها درخواست می‌زند',
                   'کاربر ناشناس', 'ابزار دیتابیس'],
             ans='b', explain='TestClient کل پشته جنگو (urls, middleware, view, template) را در حافظه اجرا می‌کند — تست یکپارچگی بدون سرور.'),
        dict(q='بعد از client.post برای بررسی «داده ذخیره شد» چه می‌کنیم؟',
             opts=['فقط status_code را چک می‌کنیم', 'شیء را از دیتابیس دوباره می‌خوانیم و assertEqual می‌گیریم',
                   'response.content را می‌خوانیم', 'به assert نیازی نیست'],
             ans='b', explain='تست باید اثر ماندگار را بسنجد: obj.refresh_from_db() یا کوئری مجدد + assert روی مقدار.'),
        dict(q='ترتیب صحیح چرخه TDD کدام است؟',
             opts=['کد → تست → مستند', 'تست شکست‌خورنده → حداقل کد تا سبز → بازآرایی',
                   'بازآرایی → تست → کد', 'تست سبز → کد → حذف تست'],
             ans='b', explain='قرمز (تست ویژگی ناموجود) → سبز (ساده‌ترین پیاده‌سازی) → بازآرایی (تمیزکاری با اطمینان تست).'),
        dict(q='کدام گزینه تست نوشتن «ارزش» دارد؟',
             opts=['اینکه path() در urls کار می‌کند', 'منطق مجوز، فرم و متدهای سفارشی خودمان',
                   'عملکرد داخلی ORM', 'اینکه sqlite فایل می‌سازد'],
             ans='b', explain='تست روی کد و رفتار خودتان؛ اجزای فریم‌ورک توسط تست‌های خود جنگو پوشش داده شده‌اند.'),
    ],
    project_title='شبکه اطمینان وبلاگ',
    project_intro='مجموعه تستی بسازید که با خیال راحت بتوانید وبلاگ را دیپلوی کنید.',
    project_checklist=[
        'تست مدل‌ها: __str__، get_absolute_url، متدهای سفارشی.',
        'تست فرم‌ها: معتبر، نامعتبر، clean سفارشی.',
        'تست ویوها: عمومی/محافظت‌شده، GET/POST، redirect و ۴۰۴.',
        'تست مجوزها: ناشناس/نویسنده/ویراستار (الگوی فصل).',
        'اجرا با coverage و هدف ≥۷۰٪ برای اپ blog.',
    ],
    project_callout=('tip', 'ساختار حرفه‌ای',
        'tests را به پکیج تبدیل کنید: blog/tests/__init__.py + test_models.py + test_views.py + test_forms.py — پیدا کردن و موازی‌سازی راحت‌تر.'),
    summary_items=[
        'جنگو دیتابیس تست جدا و ایزوله می‌سازد؛ TestCase با rollback.',
        'setUpTestData (فقط‌خواندنی) + setUp (تغییرپذیر) الگوی داده است.',
        'client.get/post + assertRedirects/Contains/TemplateUsed برای ویوها.',
        'فرم‌ها مستقیم با data تست می‌شوند؛ errors را assert کنید.',
        'TDD: قرمز → سبز → بازآرایی؛ --parallel و --keepdb برای سرعت.',
    ],
    golden='تست خوب، رفتار را از دید «کاربر کد» می‌سنجد — نه جزئیات پیاده‌سازی را.',
    faq=[
        ('pytest بهتر نیست؟',
         '<p>pytest-django همان ابزارها را با نحو تمیزتر (fixture، assert ساده) می‌دهد و بسیار رایج است. یادگیری unittest داخلی هیچ‌وقت هدر نمی‌رود؛ مهاجرت بعداً آسان است.</p>'),
        ('چند تست کافی است؟',
         '<p>عدد جادویی نیست. معیار عملی: هر باگی که پیدا می‌شود یک تست بگیرد؛ هر ویژگی جدید با تست بیاید. پوشش ۷۰-۸۰٪ روی کد خودتان هدف سالمی است.</p>'),
        ('تست APIها چطور است؟',
         '<p><span class="term" data-term="drf">DRF</span> ابزار اختصاصی APIClient می‌دهد (با format="json" و احراز هویت راحت‌تر) — در فصل ۲۲ می‌بینیم. منطق یکسان است.</p>'),
    ],
    next_step='تست‌ها پاس شدند؛ حالا اگر جایی در تولید خراب شد چطور ریشه‌یابی کنیم؟ <strong>فصل ۲۱</strong>: <span class="term" data-term="logging">لاگ</span>، pdb، Debug Toolbar و متدولوژی اشکال‌زدایی حرفه‌ای.',
),
]
