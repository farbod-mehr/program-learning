# -*- coding: utf-8 -*-
"""داده محتوای فصل‌های ۷ تا ۱۲ — بخش 📐 ساختار و Views"""

CHAPTERS = [

# ================================================================ فصل ۷
dict(
    n=7, icon='🧭', title='URLها و مسیریابی (Routing)', cat=2, mins=90, lvl_label='مبتدی',
    hero_desc='کامل‌ترین آموزش <span class="term" data-term="routing">مسیریابی</span>: تابع path و تبدیل‌کننده‌های نوع، پارامترهای پویا، include، نام‌گذاری و reverse، فضای نام و re_path — با مثال‌های واقعی وبلاگ.',
    s1_intro='URLها دروازه ورود به سایت شما هستند. در این فصل از «/» ساده به مسیرهای پویا و حرفه‌ای مثل <code class="inline-code">/blog/2026/hello-django/</code> می‌رسیم و الگوهای نام‌گذاری استاندارد صنعت را یاد می‌گیریم.',
    objectives=[
        'با تابع <code class="inline-code">path()</code> و تبدیل‌کننده‌های int، str، slug و uuid مسیر پویا بسازید.',
        'پارامتر مسیر را در <span class="term" data-term="view">ویو</span> دریافت کنید.',
        'مسیریابی را با <code class="inline-code">include()</code> بین اپ‌ها تقسیم کنید.',
        'با <code class="inline-code">name</code> و <code class="inline-code">reverse</code>، URLها را از کد و قالب ارجاع دهید.',
        'با re_path الگویregex بنویسید و بدانید کجا لازم است.',
    ],
    s1_position='<strong>جایگاه فصل:</strong> پایهٔ همه فصل‌های ویو (۸ و ۹) و API (۲۲ و ۲۳). الگوهای این فصل در تمام پروژه‌های دوره تکرار می‌شود.',
    roadmap=[
        ('path و تبدیل‌کننده‌ها', 'مسیرهای ثابت و پویا.'),
        ('include و سازمان‌دهی', 'تقسیم مسیریابی بین اپ‌ها.'),
        ('name و reverse', 'ارجاع نام‌ها به‌جای رشته URL.'),
        ('re_path و نکات پیشرفته', 'regex، ترتیب و فضای نام.'),
    ],
    mind_qs=[
        ('چرا <code class="inline-code">/blog/7/</code> بهتر از <code class="inline-code">/blog/post.php?id=7</code> است؟',
         '<p>خوانایی برای کاربر، <strong>سئو</strong> بهتر برای موتورهای جست‌وجو و انعطاف برای ما: <span class="term" data-term="django">جنگو</span> پشت همین <span class="term" data-term="url">URL</span> تمیز، شناسه را به ویو می‌دهد. به این‌ها «URLهای زیبا» (Pretty URLs) می‌گویند.</p>'),
        ('اگر دو الگوی مسیر با یک URL مطابقت کنند، کدام برنده است؟',
         '<p><strong>اولین</strong> الگو در ترتیب urlpatterns. جنگو از بالا به پایین امتحان می‌کند و به اولین تطبیق، ویو را صدا می‌زند. برای همین الگوهای خاص‌تر را <strong>بالاتر</strong> می‌گذارند.</p>'),
        ('چرا باید به مسیرها name بدهیم و در قالب از {% url %} استفاده کنیم؟',
         '<p>تا اگر روزی نشانی را عوض کردید (مثلاً /blog/ شد /articles/)، <strong>فقط urls.py عوض شود</strong>؛ همه لینک‌های قالب‌ها و کدها خودکار به‌روز می‌مانند. Hardcode کردن URL بدهی فنی است.</p>'),
    ],
    prereq_intro='پیش‌نیازها:',
    prereq=[
        'پروژه وبلاگ با مدل‌های Post (دارای slug) و ویوهای ساده فصل‌های ۳ و ۴.',
        'فایل‌های <code class="inline-code">config/urls.py</code> و <code class="inline-code">blog/urls.py</code> از قبل وجود داشته باشند.',
        'مفهوم <span class="term" data-term="request">درخواست</span>/<span class="term" data-term="response">پاسخ</span> و <span class="term" data-term="routing">مسیریابی</span> از فصل ۱.',
        'چند پست نمونه در دیتابیس (برای تست مسیرهای پویا).',
    ],
    prereq_callout=None,
    concepts=[
        dict(h='۵.۱ تابع path و تبدیل‌کننده‌های نوع', body=[
            '<p>هر الگو سه جزء دارد: <strong>رشته مسیر</strong>، <strong><span class="term" data-term="view">ویو</span></strong> و <strong>نام اختیاری</strong>. داخل رشته مسیر می‌توان «گرفتنی» (capture) با تبدیل‌کننده نوع گذاشت:</p>',
            ('code', 'blog/urls.py', 'python', '''from django.urls import path

from . import views

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("post/<int:pk>/", views.post_detail, name="post_detail"),
    path("post/<slug:slug>/", views.post_by_slug, name="post_by_slug"),
    path("author/<int:pk>/", views.author_detail, name="author_detail"),
]'''),
            '<p>تبدیل‌کننده‌های داخلی:</p>',
            '<ul>'
            '<li><code class="inline-code">str</code> — هر متن بدون اسلش (پیش‌فرض).</li>'
            '<li><code class="inline-code">int</code> — فقط عدد صحیح مثبت؛ به ویو <strong>int</strong> می‌دهد.</li>'
            '<li><span class="inline-code"><code>slug</code></span> — حروف، رقم، خط تیره و زیرخط.</li>'
            '<li><code class="inline-code">uuid</code> — شناسه یکتای استاندارد.</li>'
            '<li><code class="inline-code">path</code> — هر متنی <strong>با</strong> اسلش (برای مسیر فایل).</li></ul>',
        ]),
        dict(h='۵.۲ دریافت پارامتر در ویو', body=[
            '<p>هر چه در <code class="inline-code">&lt;...&gt;</code> گرفته شود، به‌عنوان آرگومان کلیدواژه‌ای به ویو پاس می‌شود — <strong>نام‌ها باید یکی باشند</strong>:</p>',
            ('code', 'blog/views.py', 'python', '''from django.shortcuts import get_object_or_404, render

from .models import Post


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, published=True)
    return render(request, "blog/post_detail.html", {"post": post})


def post_by_slug(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    return render(request, "blog/post_detail.html", {"post": post})'''),
            ('callout', 'info', 'get_object_or_404 یعنی چه؟',
             'رکورد را پیدا کن؛ اگر نبود، به‌جای خطای ۵۰۰، صفحه <span class="term" data-term="status-code">404</span> استاندارد نشان بده. تقریباً همیشه در ویوهای جزئیات از آن استفاده می‌شود.'),
        ]),
        dict(h='۵.۳ include و سازمان‌دهی چند اپی', body=[
            '<p>هر اپ urls.py خودش را دارد و ریشه پروژه آن‌ها را با include زیر «پیشوندهای مسیر» می‌چسباند:</p>',
            ('code', 'config/urls.py', 'python', '''from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls")),
    path("shop/", include("shop.urls")),
    path("", include("pages.urls")),
]'''),
            '<p>نتیجه: <code class="inline-code">/blog/post/5/</code> = پیشوند <code class="inline-code">blog/</code> از ریشه + الگوی <code class="inline-code">post/&lt;int:pk&gt;/</code> از اپ. با این تقسیم، هر تیم/اپ مسیرهای خودش را مستقل مدیریت می‌کند.</p>',
        ]),
        dict(h='۵.۴ name، reverse و تگ url', body=[
            '<p>به هر مسیر <strong>نام</strong> بدهید و هیچ‌جا URL را hardcode نکنید:</p>',
            ('code', 'ارجاع نام‌ها در پایتون و قالب', 'python', '''# در پایتون:
from django.urls import reverse
from django.shortcuts import redirect

url = reverse("post_detail", args=[post.pk])       # "/blog/post/5/"
url = reverse("post_by_slug", kwargs={"slug": "hello"})
return redirect("post_list")                        # redirect با نام!'''),
            ('code', 'در قالب‌ها (فصل ۱۰ کامل‌تر)', 'html', '''<a href="{% url \'post_list\' %}">همه نوشته‌ها</a>
<a href="{% url \'post_by_slug\' post.slug %}">{{ post.title }}</a>'''),
            ('callout', 'warn', 'نام یکتا',
             'نام‌ها در کل پروژه باید یکتا باشند، وگرنه reverse گیج می‌شود. قرارداد حرفه‌ای: استفاده از <strong>فضای نام اپ</strong> — در ادامه.'),
        ]),
        dict(h='۵.۵ فضای نام (namespace) و re_path', body=[
            ('code', 'app_name در blog/urls.py', 'python', '''app_name = "blog"

urlpatterns = [
    path("", views.post_list, name="list"),
    path("post/<slug:slug>/", views.detail, name="detail"),
]'''),
            ('code', 'ارجاع با فضای نام', 'python', '''reverse("blog:detail", args=["hello-django"])'''),
            ('code', 'در قالب', 'html', '''<a href="{% url \'blog:detail\' post.slug %}">{{ post.title }}</a>'''),
            '<p>و در موارد خاص که تبدیل‌کننده‌ها کافی نیستند، regex:</p>',
            ('code', 're_path — فقط وقتی لازم است', 'python', '''from django.urls import re_path

urlpatterns = [
    # آرشیو سالانه: /blog/archive/2026/
    re_path(r"^archive/(?P<year>[0-9]{4})/$", views.year_archive, name="year_archive"),
]'''),
            '<p>در re_path نام گرفتنی به شکل <code class="inline-code">(?P&lt;name&gt;pattern)</code> است. تا وقتی path کارتان را راه می‌اندازد، سراغ regex نروید!</p>',
        ]),
    ],
    example_intro='ساخت مسیرهای کامل یک وبلاگ حرفه‌ای با آرشیو زمانی:',
    example=[
        ('code', 'blog/urls.py نهایی', 'python', '''from django.urls import path, re_path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.post_list, name="list"),
    path("archive/<int:year>/", views.year_archive, name="year_archive"),
    path("tag/<slug:tag>/", views.tag_posts, name="tag_posts"),
    path("<slug:slug>/", views.post_detail, name="detail"),   # خاص‌ترها بالا؛ این عمومی‌ترین، آخر
]'''),
        ('code', 'blog/views.py', 'python', '''from django.shortcuts import get_object_or_404, render

from .models import Post, Tag


def post_list(request):
    posts = Post.objects.filter(published=True)
    return render(request, "blog/post_list.html", {"posts": posts})


def year_archive(request, year):
    posts = Post.objects.filter(published=True, created_at__year=year)
    return render(request, "blog/post_list.html", {"posts": posts, "year": year})


def tag_posts(request, tag):
    t = get_object_or_404(Tag, slug=tag)
    posts = t.posts.filter(published=True)
    return render(request, "blog/post_list.html", {"posts": posts, "tag": t})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    return render(request, "blog/post_detail.html", {"post": post})'''),
        '<p>به ترتیب دقت کنید: اگر <code class="inline-code">&lt;slug:slug&gt;</code> را اول می‌گذاشتیم، «archive» و «tag» هم به‌عنوان slug تفسیر می‌شدند!</p>',
    ],
    workshop_intro='مسیریابی یک فروشگاه را کامل کنید:',
    workshop_tasks=[
        '<strong>کارگاه ۱:</strong> برای اپ shop مسیرهای زیر را بسازید: فهرست محصولات <code class="inline-code">/shop/</code>، دسته‌بندی <code class="inline-code">/shop/category/&lt;slug&gt;/</code>، محصول <code class="inline-code">/shop/product/&lt;int:pk&gt;/&lt;slug&gt;/</code> (هر دو پارامتر!).',
        '<strong>کارگاه ۲:</strong> به همه مسیرها name با فضای نام <code class="inline-code">shop:</code> بدهید و در ویوی محصول، بعد از ثبت نظر کاربر با <code class="inline-code">redirect("shop:product", ...)</code> به همان صفحه برگردید.',
        '<strong>کارگاه ۳:</strong> مسیری <code class="inline-code">/shop/archive/&lt;year&gt;/</code> بسازید که سال فقط ۴ رقم معتبر باشد (با re_path).',
    ],
    workshop_answers=[
        ('پاسخ کارگاه ۱ و ۲',
         '<div class="code-box"><div class="code-head"><span>shop/urls.py</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">from django.urls import path, re_path\nfrom . import views\n\napp_name = "shop"\n\nurlpatterns = [\n    path("", views.product_list, name="list"),\n    path("category/&lt;slug:slug&gt;/", views.category_detail, name="category"),\n    path("product/&lt;int:pk&gt;/&lt;slug:slug&gt;/", views.product_detail, name="product"),\n]</code></pre></div>'
         '<div class="code-box"><div class="code-head"><span>ویو با دو پارامتر و redirect</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">def product_detail(request, pk, slug):\n    product = get_object_or_404(Product, pk=pk, slug=slug)\n    if request.method == "POST":\n        ...  # ثبت نظر\n        return redirect("shop:product", pk=pk, slug=slug)\n    return render(request, "shop/product_detail.html", {"product": product})</code></pre></div>'
         '<p>نکته: آوردن slug کنار pk هم سئو را بهتر می‌کند هم از حدس زدن pk جلوگیری می‌کند.</p>'),
        ('پاسخ کارگاه ۳',
         '<div class="code-box"><div class="code-head"><span>re_path برای سال</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">re_path(r"^archive/(?P&lt;year&gt;[0-9]{4})/$", views.year_archive, name="archive"),</code></pre></div>'
         '<p>با path معمولی هم <code class="inline-code">archive/&lt;int:year&gt;/</code> ممکن است، ولی int هر طول عددی را می‌پذیرد (مثل ۲۶!)؛ اگر اعتبار ۴ رقم مهم است، یا re_path یا بررسی دستی در ویو.</p>'),
    ],
    errors=[
        ('صفحه 404 می‌گیرم ولی ویو را نوشته‌ام',
         'چک کنید: ① include درست وصل است؟ ② اسلش ابتدا/انتهای مسیر دقیق است؟ ③ <strong>ترتیب</strong> الگوها — شاید الگوی عمومی‌تر بالاتر است و درخواست را می‌رباید. صفحه 404 جنگو با DEBUG=True همه الگوهای امتحان‌شده را نشان می‌دهد؛ بخوانیدش!'),
        ('خطای <code>NoReverseMatch</code>',
         'نام مسیر اشتباه است، یا فضای نام جا افتاده (<code class="inline-code">blog:list</code> نه <code class="inline-code">list</code>)، یا args/kwargs لازم را به {% url %} نداده‌اید.'),
        ('خطای <code>post_detail() missing 1 required positional argument: \'pk\'</code>',
         'نام گرفتنی در URL با نام پارامتر ویو نمی‌خواند. <code class="inline-code">&lt;int:pk&gt;</code> باید به <code class="inline-code">def post_detail(request, pk)</code> وصل شود.'),
        ('<code>/about</code> کار می‌کند ولی <code>/about/</code> نه (یا برعکس)',
         'تنظیم APPEND_SLASH (پیش‌فرض True) فقط برای <strong>redirect</strong> به نسخه اسلش‌دار کار می‌کند و آن هم وقتی که مسیر بی‌اسلش هیچ‌جا تعریف نشده باشد. عادت حرفه‌ای: همه مسیرها با اسلش انتهایی.'),
    ],
    errors_callout=None,
    exercises=[
        ('تمرین ۱ — تطبیق الگو',
         '<p><strong>سوال:</strong> الگوی <code class="inline-code">path("post/&lt;int:pk&gt;/", ...)</code> با کدام‌ها مطابقت می‌کند؟ الف) /post/5/ ب) /post/hello/ ج) /post/5 د) /blog/post/5/</p>'
         '<p><strong>پاسخ:</strong> فقط الف. ب → int نیست؛ ج → اسلش انتهایی ندارد؛ د → پیشوند blog باید با include اضافه شود.</p>'),
        ('تمرین ۲ — reverse',
         '<p><strong>سوال:</strong> خروجی <code class="inline-code">reverse("blog:detail", kwargs={"slug": "my-post"})</code> با include روی <code class="inline-code">"blog/"</code> چیست؟</p>'
         '<p><strong>پاسخ:</strong> <code class="inline-code">/blog/my-post/</code> — reverse پیشوند include + الگو + آرگومان‌ها را سرهم می‌کند.</p>'),
        ('تمرین ۳ — طراحی URL',
         '<p><strong>سوال:</strong> برای «ویرایش پست شماره ۳ در پنل کاربری» یک URL استاندارد طراحی کنید.</p>'
         '<p><strong>پاسخ نمونه:</strong> <code class="inline-code">/accounts/posts/3/edit/</code> با name="accounts:post_edit". الگوهای رایج RESTمانند: منبع جمع، شناسه، سپس فعل.</p>'),
    ],
    quiz=[
        dict(q='تبدیل‌کننده <code>&lt;slug:...&gt;</code> کدام ورودی را می‌پذیرد؟',
             opts=['فقط عدد', 'حروف، رقم، خط تیره و زیرخط', 'هر متنی با اسلش', 'فقط حروف فارسی'],
             ans='b', explain='slug برای شناسه‌های خوانای URL طراحی شده؛ مثال: hello-django یا post_1.'),
        dict(q='اگر دو الگو با یک درخواست مطابقت کنند، کدام اجرا می‌شود؟',
             opts=['خاص‌تر', 'اولین مورد در ترتیب urlpatterns', 'آخرین مورد', 'تصادفی'],
             ans='b', explain='جنگو از بالا به پایین می‌رود و به اولین تطبیق بسنده می‌کند؛ پس الگوهای خاص‌تر را بالاتر بگذارید.'),
        dict(q='فایده اصلی name در path چیست؟',
             opts=['سریع‌تر شدن سایت', 'ارجاع به مسیر با reverse و تگ url؛ بدون hardcode کردن نشانی',
                   'زیباتر شدن URL', 'اجباری بودن برای همه مسیرها'],
             ans='b', explain='با نام‌گذاری، تغییر ساختار URL فقط در urls.py انجام می‌شود و همه لینک‌ها خودکار درست می‌مانند.'),
        dict(q='کار include("blog.urls") در ریشه پروژه چیست؟',
             opts=['فایل urls اپ را حذف می‌کند', 'مسیرهای اپ را زیر یک پیشوند به ریشه مسیریابی وصل می‌کند',
                   'اپ را در INSTALLED_APPS ثبت می‌کند', 'قالب‌های اپ را بارگذاری می‌کند'],
             ans='b', explain='include یعنی «ادامه مسیریابی را از فایل اپ بخوان»؛ با پیشوند path("blog/", ...) همه مسیرهای اپ زیر /blog/ می‌نشینند.'),
        dict(q='app_name = "blog" چه چیزی می‌سازد؟',
             opts=['نام اپ در دیتابیس', 'فضای نام برای reverse مثل blog:list',
                   'پوشه templates', 'کلید SECRET جدید'],
             ans='b', explain='فضای نام از برخورد نام مسیرها بین اپ‌ها جلوگیری می‌کند: {% url "blog:list" %}.'),
        dict(q='کجا واقعاً به re_path نیاز داریم؟',
             opts=['همیشه به‌جای path', 'وقتی الگو فراتر از تبدیل‌کننده‌های داخلی است؛ مثل سال ۴ رقمی',
                   'فقط برای admin', 'برای مسیرهای فارسی'],
             ans='b', explain='اولویت با path ساده و خواناست؛ regex فقط برای قواعد پیچیده مثل ^archive/(?P&lt;year&gt;[0-9]{4})/$.'),
    ],
    project_title='نقشه URL سایت چندبخشی',
    project_intro='مسیریابی کامل یک سایت «مجله آنلاین» را طراحی و پیاده‌سازی کنید.',
    project_checklist=[
        'صفحات ثابت (pages): /، /about/، /contact/.',
        'وبلاگ با فضای نام: فهرست، جزئیات با slug، آرشیو سال/ماه، برچسب.',
        'فروشگاه با فضای نام: فهرست، دسته (تودرتو با دو slug)، محصول.',
        'همه لینک‌های قالب‌ها فقط با {% url %} — هیچ URL دستی!',
        'جدول «URL → name → ویو» را در یادداشت‌ها مستند کنید.',
    ],
    project_callout=('tip', 'الگوی طلایی نام‌گذاری',
        'نام‌ها را فعلی و کوتاه انتخاب کنید: list، detail، create، update، delete، archive. با فضای نام اپ، تکراری‌ها مشکل‌ساز نمی‌شوند.'),
    summary_items=[
        'تابع path با تبدیل‌کننده‌های str/int/slug/uuid/path مسیر پویا می‌سازد.',
        'پارامترهای مسیر با نام یکسان به ویو پاس می‌شوند.',
        'include مسیریابی را بین اپ‌ها تقسیم و سازمان‌دهی می‌کند.',
        'name + reverse + {% url %} = خداحافظی با URL هاردکد.',
        'app_name فضای نام می‌سازد؛ re_path برای regexهای خاص؛ ترتیب الگوها حیاتی است.',
    ],
    golden='هر URL یک قرارداد عمومی است: خوانا برای کاربر، نام‌دار برای کد، خاص‌ترها بالاتر.',
    faq=[
        ('URL فارسی (مثل /مقالات/) اشکالی دارد؟',
         '<p>فنی کار می‌کند (با re_path یا تبدیل‌کننده str و allow_unicode در SlugField) ولی برای سئو و اشتراک‌گذاری، اسلاگ انگلیسی-فینگلیش یا ترجمه کوتاه رایج‌تر است. تصمیم پروژه‌ای است.</p>'),
        ('چطور صفحه خطای ۴۰۴ سفارشی بسازم؟',
         '<p>فایل <code class="inline-code">templates/404.html</code> بسازید؛ با DEBUG=False خودکار استفاده می‌شود. برای handler سفارشی‌تر: <code class="inline-code">handler404 = "mysite.views.my_404"</code> در urls ریشه. در فصل ۲۱ بیشتر می‌بینیم.</p>'),
        ('هر مسیر را با تریم اسلش بنویسم؟',
         '<p>قرارداد جنگو: مسیرها <strong>با</strong> اسلش انتهایی (به‌جز ریشه ""). یک‌دستی در کل پروژه مهم‌تر از سلیقه است.</p>'),
    ],
    next_step='مسیرها آماده‌اند و به ویوهای ساده وصل شده‌اند. در <strong>فصل ۸</strong> ویوهای تابعی (FBV) را حرفه‌ای و کامل یاد می‌گیریم: request، render، redirect و پاسخ‌های JSON.',
),

# ================================================================ فصل ۸
dict(
    n=8, icon='🎯', title='ویوها — ویوی تابعی (FBV)', cat=2, mins=100, lvl_label='مبتدی',
    hero_desc='<span class="term" data-term="request">درخواست</span> و <span class="term" data-term="response">پاسخ</span>، تابع render با <span class="term" data-term="template">قالب</span> و <span class="term" data-term="context">بافت</span>، redirect، get_object_or_404، کلاس‌های HttpResponse و JsonResponse و روش‌های GET و POST — قلب پروژه‌های جنگو.',
    s1_intro='ویو جایی است که منطق صفحه زندگی می‌کند. در این فصل ویوی تابعی (Function-Based View) را از ساده تا واقعی کامل می‌کنیم؛ الگوهایی که تا آخرین فصل دوره استفاده می‌شوند.',
    objectives=[
        'شیء request و پرکاربردترین ویژگی‌هایش (GET، POST، user، META) را به کار ببرید.',
        'با render پاسخ HTML و با redirect پاسخ هدایت بسازید.',
        'تفاوت GET و POST را بدانید و الگوی استاندارد ویوی فرم‌دار را بنویسید.',
        'با JsonResponse داده ساختاریافته برگردانید.',
        'الگوی PRG (Post-Redirect-Get) را توضیح و پیاده کنید.',
    ],
    s1_position='<strong>جایگاه فصل:</strong> مستقیماً بعد از مسیریابی (فصل ۷) و قبل از CBV (فصل ۹) و فرم‌ها (فصل ۱۱).',
    roadmap=[
        ('شیء request', 'GET/POST/user/META و پارامترها.'),
        ('ساخت پاسخ', 'render، HttpResponse، JsonResponse.'),
        ('redirect و PRG', 'الگوی طلایی فرم‌ها.'),
        ('خطاها', '404، 403 و صفحه‌های خطا.'),
    ],
    mind_qs=[
        ('چرا بعد از ثبت موفق فرم، باید redirect کنیم و نه render؟',
         '<p>چون اگر render کنیم، با رفرش کاربر <strong>دوباره POST می‌شود</strong> (هشدار مرورگر: «دوباره ارسال شود؟») و داده تکراری ثبت می‌شود. الگوی PRG: بعد از POST موفق → redirect → کاربر با GET صفحه نتیجه را می‌بیند و رفرش بی‌خطر است.</p>'),
        ('request.GET و request.POST چه تفاوتی دارند؟',
         '<p>GET = داده‌های <strong>کوئری در URL</strong> (?q=django&page=2) برای خواندن/فیلتر؛ POST = داده‌های <strong>بدنه درخواست</strong> برای ایجاد/تغییر. GET در بوک‌مارک و تاریخچه می‌ماند؛ پس رمز و داده حساس هرگز در GET نیاید.</p>'),
        ('JsonResponse با HttpResponse چه فرقی دارد؟',
         '<p>JsonResponse دیکشنری پایتون را به <span class="term" data-term="json">JSON</span> سریال و هدر Content-Type را application/json می‌گذارد؛ یعنی پاسخ برای مصرف <strong>برنامه</strong> (جاوااسکریپت/اپ) است نه چشم انسان.</p>'),
    ],
    prereq_intro='پیش‌نیازها:',
    prereq=[
        'مسیریابی فصل ۷ (path، include، name، reverse).',
        'مدل‌های Post/Comment و داده نمونه در دیتابیس.',
        'آشنایی با HTML فرم (تگ form و input) — در ۵.۳ از پایه مرور می‌کنیم.',
        'سرور توسعه در حال اجرا.',
    ],
    prereq_callout=None,
    concepts=[
        dict(h='۵.۱ شیء request: آنچه جنگو به ویو می‌دهد', body=[
            ('code', 'آناتومی request', 'python', '''def inspect(request):
    method = request.method                 # "GET" یا "POST"
    q = request.GET.get("q", "")            # /search/?q=django
    page = request.GET.get("page", 1)       # همیشه رشته است!
    name = request.POST.get("name")         # داده فرم POST
    user = request.user                     # کاربر فعلی (فصل ۱۲)
    ip = request.META.get("REMOTE_ADDR")    # سرآیندها و متاداده
    path = request.path                     # "/blog/post/5/"
    ...'''),
            ('callout', 'warn', 'همه‌چیز رشته است',
             'مقادیر request.GET و request.POST همیشه <strong>str</strong> هستند؛ قبل از محاسبات عددی تبدیل کنید: <code class="inline-code">page = int(request.GET.get("page", 1))</code> — و برای ورودی کاربر try/except بگذارید.'),
        ]),
        dict(h='۵.۲ ساخت پاسخ: render و HttpResponse', body=[
            ('code', 'انواع پاسخ', 'python', '''from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def page(request):
    # ۱) HTML از قالب (رایج‌ترین)
    return render(request, "blog/post_list.html", {"posts": posts})

def raw_text(request):
    # ۲) پاسخ متنی مستقیم
    return HttpResponse("سلام!", content_type="text/plain; charset=utf-8")

def api_status(request):
    # ۳) پاسخ JSON برای مصرف برنامه‌ها
    return JsonResponse({"status": "ok", "count": posts.count()})'''),
            '<p><span class="term" data-term="render">render</span> در واقع میان‌بر است: ترکیب <span class="term" data-term="template">قالب</span> + <span class="term" data-term="context">بافت</span> و پیچیدن نتیجه در HttpResponse با نوع text/html.</p>',
        ]),
        dict(h='۵.۳ الگوی طلایی ویوی فرم‌دار (GET/POST) و PRG', body=[
            '<p>استانداردترین الگویی که در جنگو خواهید نوشت:</p>',
            ('code', 'ویوی ثبت کامنت', 'python', '''from django.shortcuts import get_object_or_404, redirect, render

from .models import Comment, Post


def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk, published=True)

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        text = request.POST.get("text", "").strip()
        if name and text:
            Comment.objects.create(post=post, name=name, text=text)
            return redirect("blog:detail", slug=post.slug)   # ← PRG!
        # خطا: برگرداندن فرم با پیام
        return render(request, "blog/add_comment.html", {
            "post": post, "error": "نام و متن الزامی است.",
        })

    return render(request, "blog/add_comment.html", {"post": post})'''),
            ('code', 'قالب فرم', 'html', '''<form method="post">
  {% csrf_token %}
  <input name="name" placeholder="نام شما">
  <textarea name="text" placeholder="متن نظر"></textarea>
  <button type="submit">ثبت نظر</button>
</form>
{% if error %}<p style="color:red">{{ error }}</p>{% endif %}'''),
            ('callout', 'danger', 'بدون {% csrf_token %} فرم POST کار نمی‌کند',
             'جنگو در برابر حمله <span class="term" data-term="csrf">CSRF</span> از شما توکن می‌خواهد؛ فراموشش یعنی خطای 403. فصل ۱۱ مکانیزمش را کامل می‌بینیم — فعلاً همیشه بگذاریدش.'),
        ]),
        dict(h='۵.۴ redirectها', body=[
            ('code', 'انواع هدایت', 'python', '''from django.shortcuts import redirect

redirect("blog:list")                       # با نام مسیر (reverse خودکار)
redirect("blog:detail", slug="hello")       # با آرگومان
redirect("/blog/")                          # با URL مستقیم (ترجیح ندهید)
redirect(post)                              # با شیء → از get_absolute_url()
HttpResponseRedirect(url, status=302)       # سطح پایین'''),
            '<p>اگر مدل <code class="inline-code">get_absolute_url()</code> داشته باشد، <code class="inline-code">redirect(obj)</code> تمیزترین حالت است:</p>',
            ('code', 'در models.py', 'python', '''from django.urls import reverse

class Post(models.Model):
    ...
    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})'''),
        ]),
        dict(h='۵.۵ خطاها: 404 و 403', body=[
            ('code', 'خطاهای استاندارد', 'python', '''from django.http import Http404, HttpResponseForbidden
from django.shortcuts import get_object_or_404


def detail(request, pk):
    # روش راحت: خودش Http404 می‌دهد
    post = get_object_or_404(Post, pk=pk)

    # روش دستی:
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404("پست پیدا نشد")'''),
            '<p>صفحه‌های خطای سفارشی: فایل‌های <code class="inline-code">templates/404.html</code> و <code class="inline-code">templates/500.html</code> را بسازید تا با DEBUG=False همان‌ها نمایش داده شوند.</p>',
        ]),
    ],
    example_intro='یک ویوی جست‌وجوی کامل با صفحه‌بندی دستی — همهٔ مفاهیم فصل در یک مثال:',
    example=[
        ('code', 'blog/views.py', 'python', '''def post_search(request):
    q = request.GET.get("q", "").strip()
    posts = Post.objects.filter(published=True)

    if q:
        posts = posts.filter(title__icontains=q)

    # صفحه‌بندی دستی (نسخه حرفه‌ای با Paginator در فصل ۹)
    page = max(1, int(request.GET.get("page", 1) or 1))
    per_page = 5
    start = (page - 1) * per_page
    items = posts[start:start + per_page]

    return render(request, "blog/search.html", {
        "q": q, "posts": items, "page": page,
        "total": posts.count(),
    })'''),
        ('code', 'templates/blog/search.html', 'html', '''<form method="get">
  <input name="q" value="{{ q }}" placeholder="جست‌وجو...">
  <button type="submit">بگرد</button>
</form>

<p>{{ total }} نتیجه برای «{{ q }}» (صفحه {{ page }})</p>
{% for post in posts %}
  <h3><a href="{{ post.get_absolute_url }}">{{ post.title }}</a></h3>
{% empty %}
  <p>نتیجه‌ای پیدا نشد.</p>
{% endfor %}

{% if page > 1 %}<a href="?q={{ q }}&page={{ page|add:-1 }}">قبلی</a>{% endif %}
<a href="?q={{ q }}&page={{ page|add:1 }}">بعدی</a>'''),
        '<p>فرم جست‌وجو با <strong>GET</strong> است تا نتیجه در URL بماند و قابل اشتراک/بوکمارک باشد.</p>',
    ],
    workshop_intro='سه ویوی واقعی بنویسید:',
    workshop_tasks=[
        '<strong>کارگاه ۱:</strong> ویوی <code class="inline-code">post_detail</code> که علاوه بر نمایش پست، هر بازدید <code class="inline-code">views_count</code> را یکی زیاد کند (با F expression تا رقابت‌امن باشد: <code class="inline-code">F("views_count") + 1</code>).',
        '<strong>کارگاه ۲:</strong> ویوی ثبت کامنت با الگوی PRG + اعتبارسنجی ساده (نام و متن اجباری، حداکثر طول ۵۰۰).',
        '<strong>کارگاه ۳:</strong> یک <span class="term" data-term="endpoint">نقطه پایانه</span> کوچک JSON: مسیر <code class="inline-code">/blog/api/posts/</code> که عنوان و اسلاگ ۱۰ پست آخر را با JsonResponse برگرداند.',
    ],
    workshop_answers=[
        ('پاسخ کارگاه ۱',
         '<div class="code-box"><div class="code-head"><span>شمارنده بازدید</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">from django.db.models import F\n\n\ndef post_detail(request, slug):\n    post = get_object_or_404(Post, slug=slug, published=True)\n    Post.objects.filter(pk=post.pk).update(views_count=F("views_count") + 1)\n    post.refresh_from_db()\n    return render(request, "blog/post_detail.html", {"post": post})</code></pre></div>'
         '<p><span class="term" data-term="f-expression">F</span> افزایش را در خود دیتابیس انجام می‌دهد؛ دو بازدید هم‌زمان همدیگر را پاک نمی‌کنند.</p>'),
        ('پاسخ کارگاه ۲',
         '<div class="code-box"><div class="code-head"><span>کامنت با PRG</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">def add_comment(request, slug):\n    post = get_object_or_404(Post, slug=slug, published=True)\n    error = None\n    if request.method == "POST":\n        name = request.POST.get("name", "").strip()\n        text = request.POST.get("text", "").strip()\n        if not name or not text:\n            error = "نام و متن الزامی است."\n        elif len(text) > 500:\n            error = "متن نظر حداکثر ۵۰۰ نویسه."\n        else:\n            Comment.objects.create(post=post, name=name, text=text)\n            return redirect("blog:detail", slug=slug)\n    return render(request, "blog/add_comment.html",\n                  {"post": post, "error": error})</code></pre></div>'),
        ('پاسخ کارگاه ۳',
         '<div class="code-box"><div class="code-head"><span>نقطه JSON ساده</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">from django.http import JsonResponse\n\n\ndef posts_api(request):\n    posts = Post.objects.filter(published=True).order_by("-created_at")[:10]\n    data = [{"title": p.title, "slug": p.slug} for p in posts]\n    return JsonResponse({"posts": data}, json_dumps_params={"ensure_ascii": False})</code></pre></div>'
         '<p>بدون ensure_ascii=False حروف فارسی به \\uXXXX تبدیل می‌شوند. این نقطه شروع API است؛ فصل ۲۲ ابزار حرفه‌ای‌اش (DRF) را می‌بینیم.</p>'),
    ],
    errors=[
        ('خطای 403 CSRF verification failed',
         'در فرم POST تگ <code class="inline-code">{% csrf_token %}</code> نیست. همیشه داخل تگ form بگذاریدش. اگر فرم را با جاوااسکریپت می‌فرستید، هدر X-CSRFToken لازم است (فصل ۲۸).'),
        ('ویو چیزی برنمی‌گرداند: <code>The view ... didn\'t return an HttpResponse</code>',
         'هر شاخه کد ویو باید return داشته باشد. رایج‌ترین حالت: if روش POST را نوشته‌اید ولی بعد از آن return render جا افتاده.'),
        ('خطای <code>MultiValueDictKeyError</code>',
         'از request.POST["name"] استفاده کرده‌اید در حالی که فیلد در فرم نبود. همیشه .get("name") با مقدار پیش‌فرض یا بررسی وجود کلید.'),
        ('<code>int()</code> روی پارامتر GET خطا می‌دهد',
         'کاربر می‌تواند ?page=abc بفرستد! ورودی URL را هرگز باور نکنید: try/except ValueError یا تمیزکاری دستی.'),
        ('با رفرش، کامنت دوباره ثبت می‌شود',
         'PRG را رعایت نکرده‌اید: بعد از POST موفق باید redirect برگردانید، نه render.'),
    ],
    errors_callout=None,
    exercises=[
        ('تمرین ۱ — GET یا POST؟',
         '<p><strong>سوال:</strong> برای هر مورد کدام متد؟ (الف) جست‌وجوی محصولات (ب) ثبت سفارش (ج) صفحه‌بندی فهرست (د) تغییر رمز عبور</p>'
         '<p><strong>پاسخ:</strong> الف → GET (قابل اشتراک) • ب → POST (ایجاد داده) • ج → GET • د → POST (تغییر حساس).</p>'),
        ('تمرین ۲ — اصلاح ویو',
         '<p><strong>سناریو:</strong> ویویی بعد از ساخت موفق پست، render صفحه موفقیت را برمی‌گرداند. چه مشکلی دارد و اصلاحش چیست؟</p>'
         '<p><strong>پاسخ:</strong> با رفرش، فرم دوباره POST و پست تکراری ساخته می‌شود. اصلاح: <code class="inline-code">return redirect("blog:detail", slug=post.slug)</code> (الگوی PRG).</p>'),
        ('تمرین ۳ — JsonResponse',
         '<p><strong>سوال:</strong> چه فرقی است بین <code class="inline-code">JsonResponse({"a": 1})</code> و <code class="inline-code">HttpResponse(\'{"a": 1}\')</code>؟</p>'
         '<p><strong>پاسخ:</strong> دومی هدر Content-Type را text/html می‌گذارد (و سریال‌سازی/امنیت ندارد)؛ اولی application/json با سریال‌سازی استاندارد و ensure_ascii. برای داده ساختاریافته همیشه JsonResponse (یا DRF).</p>'),
    ],
    quiz=[
        dict(q='مقادیر request.GET چه نوعی هستند؟',
             opts=['خودکار به int/bool تبدیل می‌شوند', 'همیشه رشته (str) هستند',
                   'دیکشنری از هر نوع', 'بایت'],
             ans='b', explain='پارامترهای URL رشته‌اند؛ تبدیل و اعتبارسنجی به عهده شماست: int(request.GET.get("page", 1)).'),
        dict(q='الگوی PRG کدام توالی است؟',
             opts=['Post → Render → Get', 'Post → Redirect → Get',
                   'Get → Post → Render', 'Redirect → Post → Get'],
             ans='b', explain='بعد از POST موفق، redirect برگردانید تا مرورگر با GET نتیجه را بگیرد؛ رفرش بی‌خطر و بدون ثبت تکراری.'),
        dict(q='get_object_or_404 چه می‌کند؟',
             opts=['شیء را می‌سازد یا 404 می‌دهد', 'شیء را پیدا می‌کند و در نبودش صفحه 404 استاندارد برمی‌گرداند',
                   'همیشه None برمی‌گرداند', 'کوئری را کش می‌کند'],
             ans='b', explain='معادل try/get/except DoesNotExist → raise Http404؛ کوتاه و استاندارد برای ویوهای جزئیات.'),
        dict(q='برای برگرداندن داده ساختاریافته به جاوااسکریپت کدام مناسب است؟',
             opts=['render', 'HttpResponse متنی', 'JsonResponse', 'redirect'],
             ans='c', explain='JsonResponse دیکشنری را JSON سریال و Content-Type درست را تنظیم می‌کند.'),
        dict(q='چرا فرم ثبت نظر باید {% csrf_token %} داشته باشد؟',
             opts=['برای سرعت', 'جنگو درخواست POST بدون توکن معتبر را با 403 رد می‌کند (ضد حمله CSRF)',
                   'برای اعتبارسنجی متن نظر', 'اجباری نیست؛ اختیاری است'],
             ans='b', explain='توکن ثابت می‌کند فرم از سایت خودتان ارسال شده، نه از سایت مخرب سوم — مکانیزم ضد CSRF.'),
        dict(q='redirect(post) روی یک شیء مدل از کجا نشانی را می‌فهمد؟',
             opts=['از name فیلد', 'از متد get_absolute_url() مدل',
                   'از slug به‌طور خودکار', 'از پنل ادمین'],
             ans='b', explain='اگر مدل get_absolute_url داشته باشد، redirect شیء را به آن نشانی هدایت می‌کند — تمیزترین الگو.'),
    ],
    project_title='ویوهای کامل وبلاگ',
    project_intro='لایه ویوی وبلاگ را با الگوهای استاندارد این فصل کامل کنید.',
    project_checklist=[
        'post_list با صفحه‌بندی دستی ۵ تایی.',
        'post_detail با get_absolute_url، شمارنده بازدید با F و نمایش کامنت‌های تأییدشده.',
        'add_comment با PRG و اعتبارسنجی (نام ≤ ۵۰، متن ≤ ۵۰۰).',
        'post_search با GET و نمایش «نتیجه‌ای نیست».',
        'یک نقطه JSON که آمار سایت (تعداد پست/کامنت) را برمی‌گرداند.',
    ],
    project_callout=('tip', 'معیار کیفیت',
        'هیچ‌کدام از ویوها نباید با ورودی عجیب کاربر (رشته خالی، عدد منفی، پارامتر جاافتاده) خطای ۵۰۰ بدهند — همه را امتحان کنید!'),
    summary_items=[
        'ویوی تابعی: request بگیر، response برگردان — به همین سادگی.',
        'request.GET/POST رشته‌اند؛ همیشه تمیزکاری و تبدیل کنید.',
        'render برای HTML، JsonResponse برای داده، redirect برای هدایت.',
        'الگوی طلایی فرم: if POST → پردازش → redirect (PRG)؛ else → نمایش فرم.',
        'get_object_or_404 و {% csrf_token %} دو یار همیشگی ویوهای واقعی.',
    ],
    golden='ویوی فرم‌دار استاندارد = دو شاخه: POST پردازش و هدایت، GET نمایش فرم.',
    faq=[
        ('FBV یاد بگیرم یا مستقیم بروم سراغ CBV؟',
         '<p>اول FBV! درک request/response و الگوها با تابع شفاف‌تر است. CBV (فصل ۹) همان مفاهیم را با ارث‌بری بسته‌بندی می‌کند. حرفه‌ای‌ها هر دو را می‌شناسند و بر اساس پیچیدگی انتخاب می‌کنند.</p>'),
        ('ویوهایم طولانی شده‌اند؛ چه کنم؟',
         '<p>منطق کسب‌وکار را از ویو بیرون بکشید: توابع خدماتی در services.py، منطق داده در متدهای مدل یا QuerySet سفارشی. ویو باید لاغر بماند: ورودی بگیر، صدا بزن، پاسخ بده.</p>'),
        ('Paginator داخلی جنگو چیست؟',
         '<p>کلاس آماده صفحه‌بندی که صفحه‌بندی دستی مثال بالا را تمیزتر می‌کند؛ در فصل ۹ با ListView (که paginate_by دارد) عملاً استفاده‌اش می‌کنیم.</p>'),
    ],
    next_step='بسیاری از ویوها تکراری‌اند (فهرست، جزئیات، ایجاد...). در <strong>فصل ۹</strong> با <span class="term" data-term="cbv">ویوهای کلاسی</span> همان کارها را با کد بسیار کمتر و ساختار استاندارد می‌نویسیم.',
),

# ================================================================ فصل ۹
dict(
    n=9, icon='⚙️', title='ویوها — ویوی کلاسی (CBV)', cat=2, mins=105, lvl_label='مبتدی',
    hero_desc='ویوهای آماده TemplateView، ListView، DetailView، CreateView، UpdateView و DeleteView با مثال کامل؛ مقایسه <span class="term" data-term="fbv">FBV</span> با <span class="term" data-term="cbv">CBV</span>، تابع as_view و شخصی‌سازی با get_context_data.',
    s1_intro='اگر FBV «رانندگی با دنده دستی» باشد، CBV «گیربکس اتوماتیک» است: الگوهای تکراری (گرفتن لیست، پیدا کردن شیء، ساختن فرم...) از قبل نوشته شده‌اند و شما فقط تفاوت‌های پروژه‌تان را اعلام می‌کنید.',
    objectives=[
        'بگویید CBV چه زمانی کد را کم و خوانا می‌کند.',
        'با ListView فهرست + صفحه‌بندی و با DetailView صفحه جزئیات بسازید.',
        'سه‌گانه <span class="term" data-term="crud">CRUD</span> — CreateView، UpdateView، DeleteView — را با <span class="term" data-term="modelform">ModelForm</span> پیاده کنید.',
        'با get_context_data و متدهای hook، ویوی آماده را شخصی‌سازی کنید.',
        'نقش as_view() در urls.py را توضیح دهید.',
    ],
    s1_position='<strong>جایگاه فصل:</strong> جایگزین/مکمل فصل ۸. DRF (فصل ۲۲) هم روی همین تفکر کلاسی ساخته شده.',
    roadmap=[
        ('چرا کلاس؟', 'ساختار dispatch و مزایا.'),
        ('ویوهای نمایشی', 'TemplateView، ListView، DetailView.'),
        ('ویوهای ویرایشی', 'Create/Update/DeleteView.'),
        ('شخصی‌سازی', 'hookها، mixinها و انتخاب FBV/CBV.'),
    ],
    mind_qs=[
        ('ListView چطور می‌فهمد چه چیزی را فهرست کند؟',
         '<p>از ویژگی <code class="inline-code">model</code> یا <code class="inline-code">queryset</code> که شما اعلام می‌کنید. بقیه کارها (اجرای کوئری، پاس دادن به قالب با نام پیش‌فرض <code class="inline-code">object_list</code>) خودش انجام می‌شود.</p>'),
        ('CreateView بدون تعریف فرم چطور فرم می‌سازد؟',
         '<p>با <code class="inline-code">fields = [...]</code> خودش یک <span class="term" data-term="modelform">ModelForm</span> درجا می‌سازد. برای کنترل بیشتر، فرم اختصاصی با <code class="inline-code">form_class</code> می‌دهید (فصل ۱۱).</p>'),
        ('چرا در urls.py می‌نویسیم PostList.as_view()؟',
         '<p>چون path() یک <strong>تابع</strong> می‌خواهد، ولی ویوی ما <strong>کلاس</strong> است. متد as_view() آن کلاس را به تابعی تبدیل می‌کند که نمونه می‌سازد و dispatch را صدا می‌زند؛ dispatch هم متد HTTP (GET/POST) را به هندلر مربوطه (get/post) وصل می‌کند.</p>'),
    ],
    prereq_intro='پیش‌نیازها:',
    prereq=[
        'فصل ۸: درک کامل request/response و الگوی فرم.',
        'مدل Post با get_absolute_url (کارگاه فصل ۸).',
        'آشنایی مقدماتی با کلاس و ارث‌بری پایتون.',
        'قالب‌های فصل قبل برای مقایسه.',
    ],
    prereq_callout=None,
    concepts=[
        dict(h='۵.۱ ساختار یک CBV', body=[
            ('code', 'ساده‌ترین CBV', 'python', '''from django.http import HttpResponse
from django.views import View


class HelloView(View):
    def get(self, request):
        return HttpResponse("سلام از ویوی کلاسی!")

    def post(self, request):
        return HttpResponse("پست دریافت شد")'''),
            ('code', 'اتصال در urls.py', 'python', '''path("hello/", HelloView.as_view(), name="hello"),'''),
            '<p>جریان: درخواست → <code class="inline-code">dispatch()</code> → بر اساس متد HTTP به <code class="inline-code">get()</code> یا <code class="inline-code">post()</code> می‌رود. تمام قدرت CBVها از همین ساختار + <span class="term" data-term="mixin">میکسین</span>‌ها می‌آید.</p>',
        ]),
        dict(h='۵.۲ ویوهای نمایشی: TemplateView، ListView، DetailView', body=[
            ('code', 'blog/views.py', 'python', '''from django.views.generic import DetailView, ListView, TemplateView

from .models import Post


class AboutView(TemplateView):
    template_name = "pages/about.html"


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"   # پیش‌فرض: blog/post_list.html
    context_object_name = "posts"           # نام متغیر در قالب
    paginate_by = 10

    def get_queryset(self):                 # شخصی‌سازی کوئری
        return Post.objects.filter(published=True)


class PostDetailView(DetailView):
    model = Post                            # قالب: blog/post_detail.html
    # شیء در قالب با نام post (و object) در دسترس است'''),
            ('code', 'urls.py', 'python', '''path("", PostListView.as_view(), name="list"),
path("<slug:slug>/", PostDetailView.as_view(), name="detail"),'''),
            ('callout', 'info', 'نام‌های پیش‌فرض قالب',
             'ListView به‌طور پیش‌فرض دنبال <code class="inline-code">blog/post_list.html</code> و DetailView دنبال <code class="inline-code">blog/post_detail.html</code> می‌گردد (نام اپ + نام مدل + نقش). اگر همین قرارداد را رعایت کنید، حتی template_name هم لازم نیست.'),
            '<p>صفحه‌بندی در قالب: متغیر <code class="inline-code">page_obj</code> در دسترس است (فصل ۱۰ نحوه نمایش).</p>',
        ]),
        dict(h='۵.۳ ویوهای ویرایشی: Create، Update، Delete', body=[
            ('code', 'سه‌گانه CRUD', 'python', '''from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ("title", "slug", "body", "tags")
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user   # نویسنده = کاربر فعلی
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ("title", "body", "tags")


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("blog:list")'''),
            '<ul>'
            '<li>CreateView و UpdateView می‌توانند <strong>یک قالب مشترک</strong> post_form.html داشته باشند.</li>'
            '<li>بعد از موفقیت، به <code class="inline-code">get_absolute_url()</code> مدل هدایت می‌شود (یا success_url).</li>'
            '<li>reverse_lazy چون URLها موقع تعریف کلاس هنوز بارگذاری نشده‌اند — lazy لازم است.</li>'
            '<li><span class="term" data-term="mixin">LoginRequiredMixin</span> دسترسی را به کاربران واردشده محدود می‌کند (فصل ۱۲).</li></ul>',
        ]),
        dict(h='۵.۴ شخصی‌سازی: get_context_data و hookها', body=[
            ('code', 'افزودن داده به بافت قالب', 'python', '''class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related_posts"] = Post.objects.filter(
            published=True, tags__in=self.object.tags.all()
        ).exclude(pk=self.object.pk).distinct()[:4]
        return context'''),
            '<p>hookهای پرکاربرد: <code class="inline-code">get_queryset()</code> (کوئری)، <code class="inline-code">get_object()</code> (شیء)، <code class="inline-code">get_context_data()</code> (بافت)، <code class="inline-code">form_valid()/form_invalid()</code> (فرم)، <code class="inline-code">get_success_url()</code>.</p>',
        ]),
        dict(h='۵.۵ FBV یا CBV؟ جدول تصمیم', body=[
            '<div class="table-wrap"><table class="compare"><thead><tr><th>موقعیت</th><th>پیشنهاد</th></tr></thead><tbody>'
            '<tr><td>ویوی ساده و یک‌بارمصرف</td><td>FBV — شفاف و مستقیم</td></tr>'
            '<tr><td>فهرست/جزئیات/CRUD استاندارد</td><td>CBV — ۸۰٪ کد کمتر</td></tr>'
            '<tr><td>منطق شاخه‌ای پیچیده در یک متد</td><td>FBV — خواناتر</td></tr>'
            '<tr><td>ترکیب رفتارهای تکراری (لاگین، کش، مجوز)</td><td>CBV + میکسین</td></tr>'
            '<tr><td>APIهای DRF</td><td>کلاس‌محور (فصل ۲۲ و ۲۳)</td></tr>'
            '</tbody></table></div>',
            ('callout', 'tip', 'قاعده تیمی',
             'بدترین حالت، ترکیب بی‌قاعده است. در پروژه تیمی یک قرارداد بگذارید: مثلاً «CRUDها با CBV، بقیه با FBV».'),
        ]),
    ],
    example_intro='تبدیل کامل ویوهای دستی فصل ۸ به CBV — تفاوت حجم کد را ببینید:',
    example=[
        ('code', 'قبل (FBV) — فصل ۸', 'python', '''def post_list(request):
    posts = Post.objects.filter(published=True)
    # صفحه‌بندی دستی: ۱۵ خط...
    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    Post.objects.filter(pk=post.pk).update(views_count=F("views_count") + 1)
    return render(request, "blog/post_detail.html", {"post": post})'''),
        ('code', 'بعد (CBV)', 'python', '''class PostListView(ListView):
    queryset = Post.objects.filter(published=True)
    context_object_name = "posts"
    paginate_by = 10


class PostDetailView(DetailView):
    model = Post

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        Post.objects.filter(pk=self.object.pk).update(
            views_count=F("views_count") + 1)
        return response'''),
        '<p>صفحه‌بندی، 404 خودکار، پیدا کردن با slug و بافت قالب — همه آماده بودند. فقط منطق یکتای خودمان (شمارنده بازدید) را اضافه کردیم.</p>',
    ],
    workshop_intro='CRUD کامل یک موجودیت جدید:',
    workshop_tasks=[
        '<strong>کارگاه ۱:</strong> برای مدل Category (name, slug) هر چهار ویوی Create/Update/Delete/ListView را با CBV بسازید؛ حذف با صفحه تأیید.',
        '<strong>کارگاه ۲:</strong> در PostListView با get_context_data فهرست دسته‌ها را برای سایدبار به قالب اضافه کنید.',
        '<strong>کارگاه ۳:</strong> یک CBV بنویسید که فقط کاربران واردشده بتوانند CreateView پست را ببینند (راهنما: LoginRequiredMixin را قبل از CreateView در ارث‌بری بگذارید).',
    ],
    workshop_answers=[
        ('پاسخ کارگاه ۱',
         '<div class="code-box"><div class="code-head"><span>CRUD دسته‌ها</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">class CategoryListView(ListView):\n    model = Category\n\n\nclass CategoryCreateView(CreateView):\n    model = Category\n    fields = ("name", "slug")\n\n\nclass CategoryUpdateView(UpdateView):\n    model = Category\n    fields = ("name", "slug")\n\n\nclass CategoryDeleteView(DeleteView):\n    model = Category\n    success_url = reverse_lazy("blog:category_list")</code></pre></div>'
         '<p>چهار مسیر در urls.py با as_view() وصل کنید. قالب تأیید حذف: category_confirm_delete.html با یک فرم POST.</p>'),
        ('پاسخ کارگاه ۲',
         '<div class="code-box"><div class="code-head"><span>get_context_data</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">class PostListView(ListView):\n    queryset = Post.objects.filter(published=True)\n    context_object_name = "posts"\n    paginate_by = 10\n\n    def get_context_data(self, **kwargs):\n        context = super().get_context_data(**kwargs)\n        context["categories"] = Category.objects.all()\n        return context</code></pre></div>'),
        ('پاسخ کارگاه ۳',
         '<div class="code-box"><div class="code-head"><span>میکسین ورود</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">class PostCreateView(LoginRequiredMixin, CreateView):\n    model = Post\n    fields = ("title", "slug", "body")</code></pre></div>'
         '<p><strong>ترتیب مهم است</strong>: میکسین سمت <u>چپ</u> (اول) می‌آید تا بررسی ورود قبل از منطق CreateView اجرا شود. کاربر ناشناس به login_url هدایت می‌شود.</p>'),
    ],
    errors=[
        ('خطای <code>ImproperlyConfigured: ... fields or form_class</code>',
         'در CreateView/UpdateView نه <code class="inline-code">fields</code> داده‌اید نه <code class="inline-code">form_class</code>. یکی را مشخص کنید.'),
        ('قالب پیدا نمی‌شود (TemplateDoesNotExist)',
         'نام پیش‌فرض قالب با ساختار شما نمی‌خواند. یا template_name صریح بگذارید یا فایل را طبق قرارداد (app/model_role.html) بسازید.'),
        ('<code>reverse_lazy</code> را با <code>reverse</code> عوض کردم و خطا گرفتم',
         'در سطح کلاس (ویژگی success_url) هنوز URLconf بارگذاری نشده؛ حتماً reverse_lazy. داخل متدها reverse معمولی هم کار می‌کند.'),
        ('form_valid صدا زده نمی‌شود / نویسنده ست نمی‌شود',
         'احتمالاً super().form_valid(form) را return نکرده‌اید یا فرم نامعتبر است (form_invalid مسیر می‌رود). خطاهای فرم را در قالب با {{ form.errors }} نمایش دهید تا ببینید مشکل کجاست.'),
        ('DeleteView با لینک GET کار نمی‌کند',
         'طراحی عمدی است: حذف فقط با POST (امنیت در برابر حذف با خزنده‌ها/پیش‌نمایش لینک‌ها). در قالب، فرم POST با دکمه «حذف» بگذارید.'),
    ],
    errors_callout=None,
    exercises=[
        ('تمرین ۱ — انتخاب ویو',
         '<p><strong>سوال:</strong> برای هر نیاز کدام GenericView؟ (الف) صفحه «قوانین سایت» بدون داده (ب) آرشیو پست‌های یک سال (ج) فرم ویرایش پروفایل (د) صفحه تأیید حذف</p>'
         '<p><strong>پاسخ:</strong> الف → TemplateView • ب → ListView با get_queryset فیلتر سال • ج → UpdateView • د → DeleteView (قالب confirm_delete).</p>'),
        ('تمرین ۲ — context_object_name',
         '<p><strong>سوال:</strong> اگر context_object_name = "posts" نگذاریم، در قالب با چه نام‌هایی به داده می‌رسیم؟</p>'
         '<p><strong>پاسخ:</strong> <code class="inline-code">object_list</code> (و برای DetailView: <code class="inline-code">object</code> + نام کوچک مدل مثل <code class="inline-code">post</code>). نام‌گذاری صریح، قالب را خواناتر می‌کند.</p>'),
        ('تمرین ۳ — ترتیب میکسین',
         '<p><strong>سوال:</strong> چرا <code class="inline-code">class V(LoginRequiredMixin, CreateView)</code> درست است و برعکسش نه؟</p>'
         '<p><strong>پاسخ:</strong> MRO پایتون از چپ به راست است؛ میکسین باید «قبل از» ویوی اصلی بیاید تا رفتارش (بررسی ورود) زودتر اعمال شود. برعکس، ممکن است بررسی هرگز اجرا نشود.</p>'),
    ],
    quiz=[
        dict(q='تابع as_view() چه می‌کند؟',
             opts=['قالب را رندر می‌کند', 'کلاس ویو را به تابع قابل استفاده در path() تبدیل می‌کند',
                   'ویو را کش می‌کند', 'مسیر URL را می‌سازد'],
             ans='b', explain='path() تابع می‌خواهد؛ as_view() کارخانه‌ای است که از کلاس، تابع درخواست→پاسخ می‌سازد.'),
        dict(q='ListView به‌طور پیش‌فرض داده را با چه نامی در قالب می‌گذارد؟',
             opts=['items', 'object_list', 'posts', 'data'],
             ans='b', explain='نام پیش‌فرض object_list است؛ با context_object_name نام دلخواه (مثل posts) می‌دهیم.'),
        dict(q='کدام hook برای محدود کردن فهرست به پست‌های منتشرشده مناسب است؟',
             opts=['get_context_data', 'get_queryset', 'form_valid', 'dispatch'],
             ans='b', explain='get_queryset کوئری پایه ویو را برمی‌گرداند؛ جای استاندارد فیلترهای سراسری ویو است.'),
        dict(q='برای success_url در سطح کلاس از چه استفاده می‌کنیم؟',
             opts=['reverse()', 'reverse_lazy()', 'redirect()', 'resolve()'],
             ans='b', explain='موقع تعریف کلاس، URLconf هنوز آماده نیست؛ reverse_lazy محاسبه را به زمان درخواست موکول می‌کند.'),
        dict(q='CreateView بعد از ذخیره موفق، کاربر را به کجا می‌برد؟',
             opts=['همیشه صفحه اصلی', 'get_absolute_url() مدل یا success_url',
                   'صفحه ویرایش دوباره', 'پنل ادمین'],
             ans='b', explain='اولویت با get_success_url/success_url است؛ اگر نباشد، get_absolute_url مدل صدا زده می‌شود.'),
        dict(q='ترتیب درست ارث‌بری برای «ایجاد فقط با ورود» کدام است؟',
             opts=['CreateView, LoginRequiredMixin', 'LoginRequiredMixin, CreateView',
                   'فقط LoginRequiredMixin', 'ترتیب مهم نیست'],
             ans='b', explain='میکسین‌ها سمت چپ (اول) می‌آیند تا رفتارشان قبل از ویوی اصلی اعمال شود (MRO چپ‌به‌راست).'),
    ],
    project_title='CRUD کامل وبلاگ با CBV',
    project_intro='همه ویوهای وبلاگ را به ویوهای کلاسی منتقل کنید و بخش «نویسنده» را کامل کنید.',
    project_checklist=[
        'ListView با paginate_by=5 و نمایش page_obj در قالب.',
        'DetailView با related_posts در get_context_data.',
        'Create/Update با قالب مشترک post_form.html و اختصاص author در form_valid.',
        'DeleteView با صفحه تأیید و success_url.',
        'هر چهار مسیر با فضای نام blog و لینک‌دهی کامل در قالب‌ها.',
    ],
    project_callout=None,
    summary_items=[
        'CBV = کلاس ویو + as_view() در مسیرها + dispatch بر اساس متد HTTP.',
        'ویوهای نمایشی: TemplateView، ListView (paginate_by)، DetailView.',
        'ویوهای ویرایشی: CreateView/UpdateView با fields یا form_class و DeleteView با تأیید POST.',
        'شخصی‌سازی با hookها: get_queryset، get_context_data، form_valid.',
        'میکسین‌ها سمت چپ ارث‌بری؛ reverse_lazy در سطح کلاس.',
    ],
    golden='CBV یعنی «تفاوت‌هایت را اعلام کن، نه تکراری‌ها را» — بقیه‌اش با جنگو.',
    faq=[
        ('CBVها جادو نمی‌کنند؟ کد داخلی‌شان کجاست؟',
         '<p>همه در django/views/generic/ متن‌باز است. خواندن کد منبع ListView (کمتر از ۵۰ خط) بهترین تمرین برای درک hookهاست؛ ابزارهایی مثل ccbrowser هم ساختار کلاس‌ها را مصور می‌کنند.</p>'),
        ('کدام را برای مصاحبه کاری باید بهتر بلد باشم؟',
         '<p>هر دو. سوال رایج: «تفاوت FBV و CBV و کجا کدام؟» — پاسخ فصل (جدول ۵.۵) را با مثال خودتان تمرین کنید.</p>'),
        ('Mixinها را خودم هم می‌توانم بنویسم؟',
         '<p>بله و خیلی ساده‌اند: کلاسی با یک متد (مثلاً dispatch یا get_context_data) که رفتاری را اضافه می‌کند. در فصل ۱۳ یک PermissionMixin سفارشی می‌نویسیم.</p>'),
    ],
    next_step='ویوها قالب را صدا می‌زنند — وقت آن است که خود <span class="term" data-term="template">قالب</span>ها را حرفه‌ای کنیم. در <strong>فصل ۱۰</strong> موتور قالب جنگو: ارث‌بری، تگ‌ها، فیلترها و امنیت XSS.',
),

# ================================================================ فصل ۱۰
dict(
    n=10, icon='🎨', title='قالب‌ها (Templates)', cat=2, mins=100, lvl_label='مبتدی',
    hero_desc='موتور قالب جنگو: متغیرها، تگ‌ها، فیلترها، حلقه و شرط، include، ارث‌بری با extends و block، ساختار حرفه‌ای base.html و امنیت <span class="term" data-term="xss">XSS</span>.',
    s1_intro='قالب لایه «ظاهر» در MTV است. با ارث‌بری قالب‌ها، یک اسکلت مشترک (هدر/فوتر) می‌سازید و هر صفحه فقط محتوای خودش را پر می‌کند — بدون حتی یک خط HTML تکراری.',
    objectives=[
        'متغیرها <code class="inline-code">{{ }}</code> و فیلترها <code class="inline-code">|</code> را به کار ببرید.',
        'با تگ‌های <span class="term" data-term="template">{% if %}، {% for %}</span> منطق نمایشی بنویسید.',
        'با extends/block یک base.html حرفه‌ای بسازید.',
        'قطعه‌های تکراری را با include جدا کنید.',
        'Auto-escaping و امنیت <span class="term" data-term="xss">XSS</span> را توضیح دهید.',
    ],
    s1_position='<strong>جایگاه فصل:</strong> مکمل فصل‌های ۸ و ۹؛ فایل‌های ایستا (CSS) در فصل ۱۴ و صفحه‌بندی پیشرفته در فصل ۹ دیدید.',
    roadmap=[
        ('متغیرها و فیلترها', '{{ post.title|truncatewords:20 }}'),
        ('تگ‌های منطقی', 'if/for و حلقه‌های تو در تو.'),
        ('ارث‌بری قالب', 'base.html و block.'),
        ('include و امنیت', 'قطعه‌های مشترک و XSS.'),
    ],
    mind_qs=[
        ('چرا نباید منطق پیچیده (کوئری، محاسبه) را در قالب نوشت؟',
         '<p>قالب فقط برای <strong>نمایش</strong> است؛ زبان قالب عمداً محدود ساخته شده. منطق در <span class="term" data-term="view">ویو</span>/<span class="term" data-term="model">مدل</span> بماند تا قابل تست و استفاده مجدد باشد. «قالب احمق، ویوی باهوش».</p>'),
        ('با extends چه اتفاقی برای blockهای تعریف‌نشده می‌افتد؟',
         '<p>محتوای <strong>پیش‌فرض</strong> base (اگر داشته باشد) نمایش داده می‌شود یا خالی می‌ماند. این یعنی صفحه فقط blockهایی را override می‌کند که لازم دارد.</p>'),
        ('اگر کاربر در کامنتش <code class="inline-code">&lt;script&gt;</code> بنویسد چه می‌شود؟',
         '<p>جنگو به‌طور پیش‌فرض <strong>escape</strong> می‌کند: به‌جای اجرای اسکریپت، متنش نمایش داده می‌شود. این محافظ خودکار <span class="term" data-term="xss">XSS</span> است؛ با فیلتر <code class="inline-code">|safe</code> خودتان می‌توانید بازش کنید — با احتیاط!</p>'),
    ],
    prereq_intro='پیش‌نیازها:',
    prereq=[
        'پروژه وبلاگ با ListView/DetailView فصل ۹.',
        'آشنایی اولیه HTML (تگ‌های div, a, ul, h1...).',
        'درک <span class="term" data-term="context">بافت</span>: دیکشنری‌ای که ویو به قالب می‌دهد.',
        'پوشه templates هر اپ ساخته شده باشد.',
    ],
    prereq_callout=None,
    concepts=[
        dict(h='۵.۱ متغیرها، جست‌وجوی نقطه‌ای و فیلترها', body=[
            ('code', 'متغیرها در قالب', 'html', '''{{ post.title }}            ← کلید دیکشنری یا ویژگی شیء
{{ post.author.name }}      ← پیمایش رابطه با نقطه
{{ post.tags.all|length }}  ← فیلتر
{{ post.created_at|date:"Y/m/d H:i" }}
{{ post.body|truncatewords:30 }}
{{ missing_var|default:"—" }}'''),
            '<p>فیلترهای پرکاربرد: <code class="inline-code">date</code>، <code class="inline-code">length</code>، <code class="inline-code">truncatewords/chars</code>، <code class="inline-code">default</code>، <code class="inline-code">upper/lower</code>، <code class="inline-code">join</code>، <code class="inline-code">linebreaks</code>، <code class="inline-code">slugify</code>، <code class="inline-code">add</code>. فیلترها با <code class="inline-code">|</code> زنجیر می‌شوند.</p>',
        ]),
        dict(h='۵.۲ تگ‌ها: if و for', body=[
            ('code', 'شرط و مقایسه', 'html', '''{% if user.is_authenticated %}
  <a href="{% url \'blog:post_create\' %}">نوشته جدید</a>
{% elif perms.blog.change_post %}
  <p>شما فقط ویرایش‌کارید.</p>
{% else %}
  <a href="{% url \'login\' %}">ورود</a>
{% endif %}'''),
            ('code', 'حلقه و متغیرهای forloop', 'html', '''{% for post in posts %}
  <article>
    <h2>{{ forloop.counter }}. {{ post.title }}</h2>
    <p>{{ post.body|truncatewords:25 }}</p>
    {% if not forloop.last %}<hr>{% endif %}
  </article>
{% empty %}
  <p>هنوز نوشته‌ای منتشر نشده است.</p>
{% endfor %}'''),
            '<p>درون حلقه: <code class="inline-code">forloop.counter</code> (از ۱)، <code class="inline-code">counter0</code>، <code class="inline-code">first/last</code>، <code class="inline-code">revcounter</code>. شاخه <code class="inline-code">{% empty %}</code> برای فهرست خالی است.</p>',
        ]),
        dict(h='۵.۳ ارث‌بری قالب: base.html', body=[
            ('code', 'templates/base.html', 'html', '''<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
  <meta charset="utf-8">
  <title>{% block title %}وبلاگ من{% endblock %}</title>
</head>
<body>
  {% include "partials/navbar.html" %}

  <main class="container">
    {% block content %}{% endblock %}
  </main>

  {% include "partials/footer.html" %}
  {% block scripts %}{% endblock %}
</body>
</html>'''),
            ('code', 'templates/blog/post_list.html', 'html', '''{% extends "base.html" %}

{% block title %}نوشته‌ها | وبلاگ من{% endblock %}

{% block content %}
  <h1>همه نوشته‌ها</h1>
  {% for post in posts %}
    <h2><a href="{{ post.get_absolute_url }}">{{ post.title }}</a></h2>
  {% endfor %}
{% endblock %}'''),
            ('callout', 'info', 'قانون طلایی extends',
             'فایل فرزند <strong>فقط</strong> می‌تواند block تعریف کند؛ هر متن/تگی بیرون از block در فرزند نادیده گرفته می‌شود. extends هم باید <strong>اولین</strong> تگ فایل باشد.'),
        ]),
        dict(h='۵.۴ صفحه‌بندی در قالب', body=[
            ('code', 'partials/pagination.html — کار با page_obj', 'html', '''{% if page_obj.has_other_pages %}
<nav class="pagination">
  {% if page_obj.has_previous %}
    <a href="?page={{ page_obj.previous_page_number }}">قبلی</a>
  {% endif %}

  <span>صفحه {{ page_obj.number }} از {{ page_obj.paginator.num_pages }}</span>

  {% if page_obj.has_next %}
    <a href="?page={{ page_obj.next_page_number }}">بعدی</a>
  {% endif %}
</nav>
{% endif %}'''),
        ]),
        dict(h='۵.۵ امنیت: Auto-escaping و XSS', body=[
            '<p>هر <code class="inline-code">{{ ... }}</code> به‌طور خودکار <strong>escape</strong> می‌شود: <code class="inline-code">&lt;</code> به <code class="inline-code">&amp;lt;</code> تبدیل می‌شود تا HTML تزریق‌شده اجرا نشود (دفاع اصلی در برابر <span class="term" data-term="xss">XSS</span>).</p>',
            ('code', 'استثناها — با احتیاط!', 'html', '''{{ post.body_html|safe }}        ← escape نکن (فقط برای محتوای اعتمادشده)
{% autoescape off %} ... {% endautoescape %}'''),
            ('callout', 'danger', 'هرگز |safe روی ورودی کاربر',
             'اگر کاربر می‌تواند آن محتوا را بنویسد، |safe یعنی دعوت‌نامه XSS! برای متن غنی کاربر از پاک‌سازی‌کننده‌هایی مثل bleach یا django-bleach استفاده کنید.'),
        ]),
    ],
    example_intro='قالب کامل صفحه جزئیات پست با همه اجزا:',
    example=[
        ('code', 'templates/blog/post_detail.html', 'html', '''{% extends "base.html" %}

{% block title %}{{ post.title }} | وبلاگ من{% endblock %}

{% block content %}
<article>
  <h1>{{ post.title }}</h1>
  <p class="meta">
    ✍️ {{ post.author.name }} •
    📅 {{ post.created_at|date:"j F Y" }} •
    👁 {{ post.views_count }} بازدید
  </p>

  {% for tag in post.tags.all %}
    <a class="badge" href="{% url \'blog:tag_posts\' tag.slug %}">#{{ tag.name }}</a>
  {% endfor %}

  <div class="body">{{ post.body|linebreaks }}</div>
</article>

<section>
  <h3>نظرات ({{ post.comments.count }})</h3>
  {% for comment in post.comments.all %}
    <div class="comment">
      <b>{{ comment.name }}</b> <small>{{ comment.created_at|date:"Y/m/d" }}</small>
      <p>{{ comment.text|linebreaks }}</p>
    </div>
  {% empty %}
    <p>اولین نفری باشید که نظر می‌دهد!</p>
  {% endfor %}
  <a href="{% url \'blog:add_comment\' post.slug %}">➕ ثبت نظر</a>
</section>

{% if related_posts %}
<section>
  <h3>مطالب مرتبط</h3>
  <ul>
    {% for rp in related_posts %}
      <li><a href="{{ rp.get_absolute_url }}">{{ rp.title }}</a></li>
    {% endfor %}
  </ul>
</section>
{% endif %}
{% endblock %}'''),
        '<p>به <code class="inline-code">post.comments.count</code> دقت کنید: دسترسی معکوس related_name + متد بدون پرانتز (قالب خودش صدا می‌زند). خطاها هم با escape خودکار، امن نمایش داده می‌شوند.</p>',
    ],
    workshop_intro='ظاهر وبلاگ را کامل کنید:',
    workshop_tasks=[
        '<strong>کارگاه ۱:</strong> base.html با سه block (title، content، scripts) و دو partial (navbar, footer) بسازید و همه قالب‌های موجود را به آن وصل کنید.',
        '<strong>کارگاه ۲:</strong> در navbar، وضعیت ورود کاربر را نشان دهید: اگر وارد شده «خوش آمدید، {{ user.username }} + خروج»، وگرنه لینک ورود/ثبت‌نام.',
        '<strong>کارگاه ۳:</strong> صفحه آرشیو بسازید که پست‌ها را <strong>گروه‌بندی‌شده بر اساس سال</strong> نمایش دهد (راهنما: از ویو یک دیکشنری {سال: [پست‌ها]} پاس دهید و در قالب دو حلقه تودرتو بزنید).',
    ],
    workshop_answers=[
        ('پاسخ کارگاه ۱',
         '<p>ساختار: <code class="inline-code">templates/base.html</code> + <code class="inline-code">templates/partials/navbar.html</code> + <code class="inline-code">templates/partials/footer.html</code>. برای اینکه templates ریشه دیده شود، در settings: <code class="inline-code">"DIRS": [BASE_DIR / "templates"]</code> در تنظیم TEMPLATES. هر صفحه: <code class="inline-code">{% extends "base.html" %}</code> و فقط blockهای لازم.</p>'),
        ('پاسخ کارگاه ۲',
         '<div class="code-box"><div class="code-head"><span>partials/navbar.html</span><span class="lang">HTML</span></div><pre class="code"><code data-lang="html">&lt;nav&gt;\n  &lt;a href="{% url \'blog:list\' %}"&gt;خانه&lt;/a&gt;\n  {% if user.is_authenticated %}\n    &lt;span&gt;خوش آمدید، {{ user.username }}&lt;/span&gt;\n    &lt;form method="post" action="{% url \'logout\' %}" style="display:inline"&gt;\n      {% csrf_token %}&lt;button type="submit"&gt;خروج&lt;/button&gt;\n    &lt;/form&gt;\n  {% else %}\n    &lt;a href="{% url \'login\' %}"&gt;ورود&lt;/a&gt; |\n    &lt;a href="{% url \'signup\' %}"&gt;ثبت‌نام&lt;/a&gt;\n  {% endif %}\n&lt;/nav&gt;</code></pre></div>'
         '<p>user در همه قالب‌ها هست (<span class="term" data-term="context">context processor</span>). خروج در جنگو ۵ باید POST باشد.</p>'),
        ('پاسخ کارگاه ۳',
         '<div class="code-box"><div class="code-head"><span>ویو</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">def archive(request):\n    grouped = {}\n    for post in Post.objects.filter(published=True).order_by("-created_at"):\n        grouped.setdefault(post.created_at.year, []).append(post)\n    return render(request, "blog/archive.html", {"grouped": grouped})</code></pre></div>'
         '<div class="code-box"><div class="code-head"><span>قالب — حلقه تودرتو</span><span class="lang">HTML</span></div><pre class="code"><code data-lang="html">{% for year, posts in grouped.items %}\n  &lt;h2&gt;{{ year }} ({{ posts|length }})&lt;/h2&gt;\n  &lt;ul&gt;{% for post in posts %}&lt;li&gt;&lt;a href="{{ post.get_absolute_url }}"&gt;{{ post.title }}&lt;/a&gt;&lt;/li&gt;{% endfor %}&lt;/ul&gt;\n{% endfor %}</code></pre></div>'),
    ],
    errors=[
        ('خطای <code>TemplateSyntaxError: Invalid block tag</code>',
         'تگی را بسته‌اید جا افتاده ({% endif %} یا {% endfor %}) یا نام تگ غلط است. خطای جنگو <strong>شماره خط</strong> را نشان می‌دهد — از همان‌جا شروع کنید.'),
        ('TemplateDoesNotExist برای base.html',
         'پوشه templates ریشه در DIRS تنظیمات نیست: <code class="inline-code">"DIRS": [BASE_DIR / "templates"]</code> را در TEMPLATES اضافه کنید.'),
        ('متغیر چیزی چاپ نمی‌کند (خالی است)',
         'قالب بی‌صداست: متغیر اشتباه/جای‌نیفتاده خطا نمی‌دهد! نام را در context ویو چک کنید. برای دیباگ، موقتاً <code class="inline-code">{{ posts }}</code> را چاپ کنید تا مقدارش را ببینید.'),
        ('HTML در خروجی به‌صورت متن دیده می‌شود (&lt;p&gt;)',
         'escape خودکار کارش را کرده. اگر محتوا واقعاً HTML امن است: |safe یا linebreaks برای متن ساده با enter.'),
        ('extends کار نمی‌کند و کل صفحه خالی است',
         'extends باید اولین تگ باشد و همه محتوا داخل blockها. متن بیرون block در فرزند نادیده گرفته می‌شود.'),
    ],
    errors_callout=None,
    exercises=[
        ('تمرین ۱ — فیلتر درست',
         '<p><strong>سوال:</strong> کدام فیلتر برای هر نیاز؟ (الف) «۱۴۰۵/۰۴/۲۱» از DateTimeField (ب) ۳۰ حرف اول متن (ج) تبدیل enterها به پاراگراف (د) مقدار جایگزین برای None</p>'
         '<p><strong>پاسخ:</strong> الف → |date:"Y/m/d" • ب → |truncatechars:30 • ج → |linebreaks • د → |default:"—"</p>'),
        ('تمرین ۲ — block یا include؟',
         '<p><strong>سوال:</strong> برای (الف) هدر مشترک همه صفحات (ب) بخشی که هر صفحه محتوای متفاوتش را دارد، کدام مکانیزم؟</p>'
         '<p><strong>پاسخ:</strong> الف → include (قطعه ثابت مشترک) • ب → block (جای خالی که فرزند پر می‌کند). قاعده: «تکراری ثابت = include، متغیر = block».</p>'),
        ('تمرین ۳ — امنیت',
         '<p><strong>سناریو:</strong> کاربری در فیلد «بیوگرافی» پروفایلش می‌نویسد: <code class="inline-code">&lt;script&gt;alert(1)&lt;/script&gt;</code>. در صفحه پروفایل چه می‌بینیم؟ اگر |safe گذاشته باشیم چه؟</p>'
         '<p><strong>پاسخ:</strong> حالت عادی: خودِ متن به‌صورت escape‌شده (بی‌خطر) نمایش داده می‌شود. با |safe: اسکریپت اجرا می‌شود = حمله XSS موفق. نتیجه: روی داده کاربر هرگز |safe نزنید.</p>'),
    ],
    quiz=[
        dict(q='کدام نوشته در قالب جنگو یک «فیلتر» است؟',
             opts=['{{ post.title }}', '{{ post.title|upper }}', '{% if post %}', '{{ post.title.upper() }}'],
             ans='b', explain='فیلترها با | بعد از متغیر می‌آیند؛ فراخوانی متد با پرانتز در زبان قالب مجاز نیست.'),
        dict(q='تگ extends چه محدودیتی برای فایل فرزند می‌سازد؟',
             opts=['فرزند نمی‌تواند include داشته باشد', 'محتوای فرزند فقط باید داخل blockها باشد',
                   'فرزند باید همه blockها را پر کند', 'extends فقط یک سطح کار می‌کند'],
             ans='b', explain='در فرزندِ extends، هر چیزی بیرون از {% block %} نادیده گرفته می‌شود؛ ساختار کلی از والد می‌آید.'),
        dict(q='Auto-escaping از چه حمله‌ای جلوگیری می‌کند؟',
             opts=['SQL Injection', 'XSS (اسکریپت‌نویسی میان‌وبگاهی)',
                   'CSRF', 'حمله DDoS'],
             ans='b', explain='escape کردن < > & باعث می‌شود HTML/JS تزریق‌شده در داده کاربر اجرا نشود، فقط نمایش داده شود.'),
        dict(q='در حلقه for، برای حالت «فهرست خالی» از چه استفاده می‌شود؟',
             opts=['{% if not posts %}', '{% empty %} داخل for',
                   '{% null %}', '{% else %} بعد از endfor'],
             ans='b', explain='شاخه {% empty %}...{% endfor %} وقتی فهرست خالی باشد رندر می‌شود.'),
        dict(q='forloop.counter از چه عددی شروع می‌شود؟',
             opts=['۰', '۱', 'بستگی به ترتیب دارد', 'هیچ — باید دستی بشماریم'],
             ans='b', explain='counter از ۱ و counter0 از ۰ شروع می‌شود؛ first/last هم بولی‌اند.'),
        dict(q='چرا {{ post.comments.count }} پرانتز ندارد؟',
             opts=['غلط است و کار نمی‌کند', 'زبان قالب متدهای بدون آرگومان را خودش صدا می‌زند',
                   'count یک فیلتر است', 'باید {{ post.comments.count() }} بنویسیم'],
             ans='b', explain='جست‌وجوی نقطه‌ای قالب، ویژگی/متد/کلید/ایندکس را امتحان و متدهای بدون آرگومان را خودکار فراخوانی می‌کند.'),
    ],
    project_title='قالب کامل وبلاگ',
    project_intro='مجموعه قالب‌های وبلاگ را با ارث‌بری و اجزای مشترک بازنویسی کنید.',
    project_checklist=[
        'base.html با blockهای title/content/scripts + navbar و footer به‌صورت include.',
        'post_list با کارت پست‌ها + pagination partial + حالت خالی.',
        'post_detail با متا، برچسب‌ها، نظرات و مطالب مرتبط.',
        'صفحه‌های خطای سفارشی 404.html و 500.html در templates ریشه.',
        'یک CSS ساده برای مرتب‌سازی ظاهر (فصل ۱۴ حرفه‌ای‌اش می‌کند).',
    ],
    project_callout=('tip', 'بازاستفاده‌پذیری',
        'هر قطعه‌ای که دو بار تکرار شد (کارت پست، پیام خطا، دکمه) را به partial تبدیل کنید. نام‌گذاری: templates/partials/post_card.html.'),
    summary_items=[
        '{{ }} متغیر و فیلتر، {% %} تگ و منطق — زبان قالب عمداً ساده است.',
        'فیلترهای پرکاربرد: date، truncatewords، linebreaks، default، length.',
        'ارث‌بری: base.html + block؛ قطعه‌های مشترک با include.',
        'page_obj همه امکانات صفحه‌بندی را در قالب می‌دهد.',
        'Auto-escape سپر اصلی XSS است؛ |safe فقط برای محتوای اعتمادشده.',
    ],
    golden='قالب خوب = اسکلت مشترک (extends) + قطعه‌های کوچک (include) + صفر منطق تجاری.',
    faq=[
        ('می‌توانم از Jinja2 استفاده کنم؟',
         '<p>بله؛ جنگو از چند موتور قالب پشتیبانی می‌کند و Jinja2 قابل فعال‌سازی است. ولی DTL برای بیشتر پروژه‌ها کافی و یکپارچه‌تر است (تگ csrf، url و... داخلی).</p>'),
        ('کجا قالب بگذارم: templates اپ یا ریشه؟',
         '<p>قالب‌های مخصوص اپ داخل <code class="inline-code">app/templates/app/</code> (برای استفاده مجدد) و base/صفحات خطا/partials مشترک در <code class="inline-code">templates/</code> ریشه. DIRS قبل از APP_DIRS جست‌وجو می‌شود — برای override قالب اپ‌های ثالث عالی است.</p>'),
        ('رندر قالب کند است؟',
         '<p>معمولاً خیر؛ گلوگاه واقعی تقریباً همیشه کوئری‌های دیتابیس است. برای قطعات پرهزینه، تگ {% cache %} در فصل ۱۹ معرفی می‌شود.</p>'),
    ],
    next_step='کاربران باید بتوانند داده وارد کنند! در <strong>فصل ۱۱</strong> <span class="term" data-term="form">فرم</span>های جنگو: اعتبارسنجی خودکار، ModelForm، ویجت‌ها و مدیریت خطاها.',
),
]
