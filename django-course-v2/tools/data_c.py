# -*- coding: utf-8 -*-
"""داده محتوای فصل‌های ۱۱ تا ۱۵ — فرم‌ها، احراز هویت، مجوزها، فایل‌ها، QuerySet"""

CHAPTERS = [

# ================================================================ فصل ۱۱
dict(
    n=11, icon='📝', title='فرم‌ها (Forms) در جنگو', cat=2, mins=110, lvl_label='متوسط',
    hero_desc='کلاس forms.Form و <span class="term" data-term="modelform">ModelForm</span>، انواع فیلد فرم، <span class="term" data-term="widget">ویجت</span>ها، اعتبارسنجی با clean_، نمایش فرم و مدیریت خطاها — به‌همراه <span class="term" data-term="csrf">CSRF</span>.',
    s1_intro='در فصل ۸ فرم را دستی با request.POST خواندیم؛ حالا ابزار حرفه‌ای جنگو را یاد می‌گیریم که هم HTML فرم را می‌سازد، هم <span class="term" data-term="validation">اعتبارسنجی</span> می‌کند و هم داده تمیز (clean) تحویل می‌دهد.',
    objectives=[
        'با forms.Form فیلد، ویجت و اعتبارسنج تعریف کنید.',
        'الگوی استاندارد فرم در ویو (Bound/Unbound) را بنویسید.',
        'متد <code class="inline-code">clean_&lt;field&gt;</code> و <code class="inline-code">clean()</code> برای اعتبارسنجی سفارشی بنویسید.',
        'با ModelForm فرم را مستقیم از مدل بسازید و save() کنید.',
        'خطاهای فرم را زیبا در قالب نمایش دهید.',
    ],
    s1_position='<strong>جایگاه فصل:</strong> پایهٔ ثبت‌نام (فصل ۱۲)، CRUDهای CreateView (فصل ۹) و فرم‌های DRF (فصل ۲۲).',
    roadmap=[
        ('forms.Form', 'فیلدها، ویجت‌ها و اعتبارسنج‌ها.'),
        ('الگوی ویو', 'Bound در برابر Unbound و is_valid.'),
        ('اعتبارسنجی سفارشی', 'clean_field و clean.'),
        ('ModelForm', 'فرم مستقیم از مدل + widgets.'),
    ],
    mind_qs=[
        ('چرا اعتبارسنجی فقط در مرورگر (جاوااسکریپت) کافی نیست؟',
         '<p>چون کاربر می‌تواند جاوااسکریپت را خاموش کند یا با ابزارهایی مثل curl <strong>مستقیم</strong> به سرور درخواست بفرستد. اعتبارسنجی مرورگر برای تجربه کاربری است؛ اعتبارسنجی سرور برای <strong>امنیت و صحت داده</strong> — همیشه هر دو.</p>'),
        ('فرم Bound و Unbound یعنی چه؟',
         '<p><strong>Unbound</strong>: فرم خالی برای اولین نمایش (بدون داده). <strong>Bound</strong>: فرمی که با داده (معمولاً POST) ساخته شده؛ می‌تواند is_valid شود و در صورت خطا، داده‌های قبلی و خطاها را نشان دهد.</p>'),
        ('ModelForm چه چیزی را از مدل «ارث» می‌برد؟',
         '<p>فیلدها، محدودیت‌ها (max_length و...)، <strong>اعتبارسنج‌های سطح مدل</strong> (مثل unique) و help_text. یعنی یک تعریف، دو جا استفاده: دیتابیس و فرم.</p>'),
    ],
    prereq_intro='پیش‌نیازها:',
    prereq=[
        'فصل ۸: الگوی GET/POST و نقش {% csrf_token %}.',
        'مدل‌های Post و Comment آماده.',
        'آشنایی با کلاس پایتون (فرم‌ها هم کلاس‌اند!).',
        'قالب base.html از فصل ۱۰.',
    ],
    prereq_callout=None,
    concepts=[
        dict(h='۵.۱ ساخت فرم با forms.Form', body=[
            ('code', 'blog/forms.py', 'python', '''from django import forms


class CommentForm(forms.Form):
    name = forms.CharField(
        label="نام شما", max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "نام"}),
    )
    email = forms.EmailField(label="ایمیل", required=False)
    text = forms.CharField(
        label="متن نظر",
        widget=forms.Textarea(attrs={"rows": 4, "maxlength": 500}),
    )
    agree = forms.BooleanField(label="قوانین را پذیرفته‌ام")'''),
            '<p>فیلدهای رایج: CharField، EmailField، IntegerField، BooleanField، ChoiceField، DateField، FileField. هر فیلد هم <strong>ویجت</strong> (ظاهر HTML) دارد هم <strong>اعتبارسنج</strong> (منطق).</p>',
        ]),
        dict(h='۵.۲ الگوی استاندارد فرم در ویو', body=[
            ('code', 'ویوی فرم‌دار', 'python', '''from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CommentForm
from .models import Post


def add_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        form = CommentForm(request.POST)          # Bound
        if form.is_valid():
            data = form.cleaned_data               # داده تمیز و تبدیل‌شده
            post.comments.create(
                name=data["name"], text=data["text"],
            )
            messages.success(request, "نظر شما ثبت شد!")
            return redirect(post.get_absolute_url())  # PRG
    else:
        form = CommentForm()                       # Unbound

    return render(request, "blog/add_comment.html", {"form": form, "post": post})'''),
            ('callout', 'info', 'cleaned_data چیست؟',
             'خروجی <span class="term" data-term="validation">اعتبارسنجی</span>: همه فیلدها به نوع درست تبدیل شده‌اند («۵» شده 5، رشته‌ها trim شده). <strong>هرگز</strong> مستقیم از request.POST برای ذخیره استفاده نکنید؛ فقط cleaned_data.'),
        ]),
        dict(h='۵.۳ نمایش فرم در قالب', body=[
            ('code', 'add_comment.html — سه سبک نمایش', 'html', '''<form method="post">
  {% csrf_token %}

  {# سبک ۱: دستی، فیلد به فیلد (زیباترین کنترل) #}
  <div class="field">
    {{ form.name.label_tag }}
    {{ form.name }}
    {{ form.name.errors }}
  </div>

  {# سبک ۲: نیمه‌دستی با حلقه #}
  {% for field in form %}
    <div class="field">
      {{ field.label_tag }} {{ field }}
      {% if field.help_text %}<small>{{ field.help_text }}</small>{% endif %}
      {{ field.errors }}
    </div>
  {% endfor %}

  {# سبک ۳: یک‌خطی (فقط تست سریع) #}
  {{ form.as_p }}

  <button type="submit">ثبت نظر</button>
</form>'''),
            '<p>فرم Boundِ ناموفق، داده‌های قبلی کاربر و خطاها را نگه می‌دارد — لازم نیست چیزی اضافه کنید.</p>',
        ]),
        dict(h='۵.۴ اعتبارسنجی سفارشی: clean_', body=[
            ('code', 'فرم با منطق اختصاصی', 'python', '''from django import forms
from django.core.exceptions import ValidationError


class CommentForm(forms.Form):
    name = forms.CharField(max_length=50)
    text = forms.CharField(widget=forms.Textarea)
    website = forms.URLField(required=False)

    def clean_name(self):
        name = self.cleaned_data["name"].strip()
        if name.lower() in ("admin", "مدیر"):
            raise ValidationError("این نام رزرو شده است.")
        return name                        # حتماً مقدار را برگردانید!

    def clean(self):
        cleaned = super().clean()
        text = cleaned.get("text", "")
        if "http" in text and not cleaned.get("website"):
            self.add_error("website", "اگر لینک دارید، در فیلد سایت بنویسید.")
        return cleaned'''),
            '<ul>'
            '<li><code class="inline-code">clean_&lt;field&gt;</code> — اعتبارسنجی <strong>یک فیلد</strong>.</li>'
            '<li><code class="inline-code">clean()</code> — منطق <strong>چندفیلدی</strong> (مقایسه رمز و تکرارش، تاریخ شروع/پایان).</li>'
            '<li>اعتبارسنج‌های آماده: <code class="inline-code">MinLengthValidator</code>، <code class="inline-code">RegexValidator</code> و... در <code class="inline-code">validators=[...]</code>.</li></ul>',
        ]),
        dict(h='۵.۵ ModelForm: فرم مستقیم از مدل', body=[
            ('code', 'فرم ساخت/ویرایش پست', 'python', '''from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "slug", "body", "tags")   # یا exclude
        widgets = {
            "body": forms.Textarea(attrs={"rows": 10}),
        }
        labels = {"slug": "نشانی (انگلیسی)"}
        help_texts = {"slug": "مثلاً: hello-django"}

    def clean_title(self):
        title = self.cleaned_data["title"]
        if len(title) < 5:
            raise forms.ValidationError("عنوان حداقل ۵ نویسه باشد.")
        return title'''),
            ('code', 'ویو — یک فرم برای ساخت و ویرایش', 'python', '''def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)   # ذخیره نکن؛ اول تکمیل
            post.author = request.user
            post.save()
            form.save_m2m()                  # روابط چندبه‌چند حالا
            return redirect(post.get_absolute_url())
    else:
        form = PostForm()
    return render(request, "blog/post_form.html", {"form": form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)   # ← instance!
        if form.is_valid():
            form.save()
            return redirect(post.get_absolute_url())
    else:
        form = PostForm(instance=post)
    return render(request, "blog/post_form.html", {"form": form, "post": post})'''),
            ('callout', 'warn', 'commit=False را بشناسید',
             '<code class="inline-code">form.save(commit=False)</code> شیء را می‌سازد ولی ذخیره نمی‌کند — فرصت می‌دهد فیلدهایی مثل author را از request.user ست کنید. اگر فرم M2M دارد، بعد از save() حتماً <code class="inline-code">form.save_m2m()</code> را صدا بزنید.'),
        ]),
    ],
    example_intro='یک فرم تماس کامل با اعتبارسنجی چندفیلدی و ذخیره در مدل:',
    example=[
        ('code', 'models و forms', 'python', '''class ContactMessage(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    subject = models.CharField(max_length=120)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class ContactForm(forms.ModelForm):
    confirm_email = forms.EmailField(label="تکرار ایمیل")

    class Meta:
        model = ContactMessage
        fields = ("name", "email", "subject", "body")

    def clean(self):
        cleaned = super().clean()
        if cleaned.get("email") != cleaned.get("confirm_email"):
            self.add_error("confirm_email", "ایمیل و تکرار آن یکی نیستند.")
        return cleaned'''),
        ('code', 'ویو و قالب', 'python', '''def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "پیام شما ارسال شد 🌿")
            return redirect("pages:contact")
    else:
        form = ContactForm()
    return render(request, "pages/contact.html", {"form": form})'''),
        '<p>نکته امنیتی: ایمیل در مدل ذخیره می‌شود ولی confirm_email فیلد <strong>فرم-only</strong> است (در Meta.fields نیست) — مقایسه‌اش صرفاً اعتبارسنجی است.</p>',
    ],
    workshop_intro='فرم‌های وبلاگ را حرفه‌ای کنید:',
    workshop_tasks=[
        '<strong>کارگاه ۱:</strong> فرم نظر (CommentForm) را با forms.Form بسازید: نام (اجباری، ≥۳ نویسه)، ایمیل (اختیاری ولی معتبر)، متن (۱۰ تا ۵۰۰ نویسه) و ویجت‌های class="form-control".',
        '<strong>کارگاه ۲:</strong> اعتبارسنج سفارشی: اگر متن نظر شامل «تبلیغ» یا لینک بود، ValidationError با پیام فارسی بدهد.',
        '<strong>کارگاه ۳:</strong> PostForm را با ModelForm بنویسید و ویوهای post_create/post_edit فصل را به آن وصل کنید؛ slug خودکار از عنوان ساخته شود (در clean یا در مدل).',
    ],
    workshop_answers=[
        ('پاسخ کارگاه ۱',
         '<div class="code-box"><div class="code-head"><span>CommentForm</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">class CommentForm(forms.Form):\n    name = forms.CharField(label="نام", min_length=3, max_length=50,\n                           widget=forms.TextInput(attrs={"class": "form-control"}))\n    email = forms.EmailField(label="ایمیل", required=False,\n                             widget=forms.EmailInput(attrs={"class": "form-control"}))\n    text = forms.CharField(label="متن نظر", min_length=10, max_length=500,\n                           widget=forms.Textarea(attrs={"class": "form-control", "rows": 4}))</code></pre></div>'
         '<p>min/max_length خودکار اعتبارسنجی و پیام خطای فارسی‌شده می‌دهند (با تنظیم LANGUAGE_CODE="fa").</p>'),
        ('پاسخ کارگاه ۲',
         '<div class="code-box"><div class="code-head"><span>clean_text ضد تبلیغ</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">BANNED = ("تبلیغ", "خرید اینترنتی", "bit.ly")\n\n\ndef clean_text(self):\n    text = self.cleaned_data["text"]\n    lowered = text.lower()\n    if any(word in text or word in lowered for word in BANNED):\n        raise forms.ValidationError("نظر شما شامل محتوای تبلیغاتی است.")\n    if "http://" in lowered or "https://" in lowered:\n        raise forms.ValidationError("درج لینک در نظر مجاز نیست.")\n    return text</code></pre></div>'
         '<p>این «فیلتر محتوای» ساده است؛ در پروژه‌های جدی، پاک‌سازی و بررسی دقیق‌تر (یا تأیید دستی توسط مدیر — فیلد approved فصل ۶) توصیه می‌شود.</p>'),
        ('پاسخ کارگاه ۳',
         '<div class="code-box"><div class="code-head"><span>PostForm با slug خودکار</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">from django.utils.text import slugify\n\n\nclass PostForm(forms.ModelForm):\n    class Meta:\n        model = Post\n        fields = ("title", "body", "tags")   # slug را از کاربر نگیریم!\n\n    def save(self, commit=True):\n        post = super().save(commit=False)\n        if not post.slug:\n            base = slugify(post.title, allow_unicode=True)\n            slug, i = base, 1\n            while Post.objects.filter(slug=slug).exists():\n                i += 1\n                slug = f"{base}-{i}"\n            post.slug = slug\n        if commit:\n            post.save()\n            self.save_m2m()\n        return post</code></pre></div>'
         '<p>slugify با allow_unicode=True اسلاگ فارسی می‌سازد؛ حلقه، یکتایی را با افزودن شماره تضمین می‌کند.</p>'),
    ],
    errors=[
        ('فرم همیشه نامعتبر است ولی نمی‌فهمم چرا',
         'خطاها را ببینید! در قالب {{ form.errors }} یا در شل/دیباگ: <code class="inline-code">form.errors.as_data()</code>. رایج‌ترین علت: نام فیلد فرم با name ورودی HTML نمی‌خواند.'),
        ('خطای <code>The \'post\' field is required</code> در ModelForm',
         'فیلدی که در مدل null=False و بدون default است در فرم اجباری می‌شود. برای فیلدهای سیستمی (author، created_at) آن‌ها را از Meta.fields حذف یا با commit=False پر کنید.'),
        ('cleaned_data KeyError',
         'در clean() به cleaned_data["field"] دسترسی مستقیم کرده‌اید ولی فیلد قبلاً رد شده. از <code class="inline-code">cleaned.get("field")</code> استفاده کنید.'),
        ('فرم با فایل (تصویر) آپلود نمی‌شود',
         'دو نکته: ① در تگ form: <code class="inline-code">enctype="multipart/form-data"</code> ② در ویو: <code class="inline-code">Form(request.POST, request.FILES)</code>. فایل‌ها در request.FILES جدا می‌آیند.'),
        ('پیام خطاها انگلیسی است',
         'در settings: <code class="inline-code">LANGUAGE_CODE = "fa"</code> و USE_I18N=True. پیام‌های داخلی جنگو ترجمه فارسی دارند (فصل ۲۵).'),
    ],
    errors_callout=None,
    exercises=[
        ('تمرین ۱ — انتخاب نوع فرم',
         '<p><strong>سوال:</strong> برای هر مورد forms.Form یا ModelForm؟ (الف) فرم تماس (ذخیره در مدل) (ب) فرم جست‌وجو (ج) فرم ورود (د) فرم ثبت پست</p>'
         '<p><strong>پاسخ:</strong> الف → ModelForm (مدل ContactMessage) • ب → Form ساده (یا حتی GET دستی) • ج → فرم آماده AuthenticationForm (فصل ۱۲) • د → ModelForm.</p>'),
        ('تمرین ۲ — clean یا clean_field؟',
         '<p><strong>سوال:</strong> بررسی «تاریخ پایان باید بعد از تاریخ شروع باشد» در کدام متد؟</p>'
         '<p><strong>پاسخ:</strong> در <code class="inline-code">clean()</code> — چون به <strong>دو فیلد</strong> نیاز دارد. با self.add_error("end_date", ...) خطا را به فیلد درست نسبت دهید.</p>'),
        ('تمرین ۳ — widget در برابر field',
         '<p><strong>سوال:</strong> تفاوت <code class="inline-code">forms.ChoiceField</code> و <code class="inline-code">forms.Select</code> چیست؟</p>'
         '<p><strong>پاسخ:</strong> ChoiceField <strong>منطق</strong> است (اعتبارسنجی یکی از گزینه‌ها)؛ Select <strong>ویجت</strong> است (نمایش dropdown). ChoiceField به‌طور پیش‌فرض ویجت Select دارد؛ می‌توان به RadioSelect عوضش کرد.</p>'),
    ],
    quiz=[
        dict(q='form.is_valid() چه می‌کند؟',
             opts=['فرم را در دیتابیس ذخیره می‌کند', 'اعتبارسنجی همه فیلدها و ساخت cleaned_data',
                   'HTML فرم را می‌سازد', 'خطاها را پاک می‌کند'],
             ans='b', explain='is_valid تمام اعتبارسنج‌ها (و clean_های سفارشی) را اجرا می‌کند؛ اگر همه قبول شدند cleaned_data آماده است.'),
        dict(q='فرم Bound چه زمانی ساخته می‌شود؟',
             opts=['وقتی با داده ساخته شود: CommentForm(request.POST)', 'وقتی خالی نمایش داده شود',
                   'وقتی is_valid شود', 'هرگز — فقط Unbound داریم'],
             ans='a', explain='دادن data به سازنده، فرم را Bound می‌کند؛ فرم Bound داده و خطاها را در رندر نگه می‌دارد.'),
        dict(q='خروجی تمیز و تبدیل‌شده فرم کجاست؟',
             opts=['form.data', 'form.cleaned_data', 'request.POST', 'form.fields'],
             ans='b', explain='cleaned_data فقط بعد از is_valid موفق وجود دارد؛ form.data همان ورودی خام (و نامطمئن) است.'),
        dict(q='در ModelForm، نقش instance در فرم ویرایش چیست؟',
             opts=['قالب را مشخص می‌کند', 'فرم را به رکورد موجود وصل می‌کند تا save() به‌روزش کند',
                   'اعتبارسنجی را غیرفعال می‌کند', 'فیلدها را حذف می‌کند'],
             ans='b', explain='PostForm(request.POST, instance=post) یعنی همین رکورد را با داده جدید به‌روزرسانی کن؛ بدون instance، رکورد جدید ساخته می‌شود.'),
        dict(q='form.save(commit=False) چه وقتی لازم است؟',
             opts=['همیشه', 'وقتی باید فیلدهایی مثل author را قبل از ذخیره از request.user پر کنیم',
                   'فقط در DeleteView', 'وقتی فرم نامعتبر است'],
             ans='b', explain='commit=False شیء ذخیره‌نشده برمی‌گرداند؛ پس از تکمیل فیلدها save() و در صورت M2M، save_m2m() صدا زده می‌شود.'),
        dict(q='کدام گزینه درباره اعتبارسنجی سمت مرورگر درست است؟',
             opts=['کافی است و سرور لازم نیست', 'فقط برای تجربه کاربری است؛ سرور همیشه باید مستقل اعتبارسنجی کند',
                   'امنیت را تأمین می‌کند', 'جنگو آن را خودکار انجام می‌دهد'],
             ans='b', explain='کلاینت قابل اعتماد نیست؛ forms جنگو لایه اطمینان سمت سرور است.'),
    ],
    project_title='سامانه نظرات با فرم حرفه‌ای',
    project_intro='سیستم نظردهی وبلاگ را کاملاً فرم‌محور بازنویسی کنید.',
    project_checklist=[
        'CommentForm با اعتبارسنج‌های طول و ایمیل اختیاری.',
        'clean_text ضد لینک/تبلیغ + پیام‌های فارسی.',
        'ویوی PRG با messages.success/error.',
        'نمایش field-by-field با classهای Bootstrapمانند و highlight خطاها.',
        'فرم پست (ModelForm) با ساخت/ویرایش و slug خودکار.',
    ],
    project_callout=('tip', 'تست دستی فرم',
        'هر بار: یک‌بار خالی، یک‌بار داده غلط، یک‌بار داده درست submit کنید. سه مسیر ویو (GET، POST ناموفق، POST موفق) همه باید کار کنند.'),
    summary_items=[
        'فرم جنگو = تعریف فیلدها + اعتبارسنجی + رندر HTML در یک کلاس.',
        'الگوی ویو: POST → Bound → is_valid → cleaned_data → PRG؛ GET → Unbound.',
        'clean_&lt;field&gt; برای تک‌فیلد و clean() برای منطق چندفیلدی.',
        'ModelForm فرم را از مدل مشتق می‌کند؛ instance برای ویرایش، commit=False برای تکمیل دستی.',
        'فایل‌ها: request.FILES + enctype="multipart/form-data".',
    ],
    golden='هرگز به ورودی کاربر اعتماد نکن؛ forms جنگو همان لایه‌ای است که اعتماد را «اعتبارسنجی» می‌کند.',
    faq=[
        ('کریسپی‌فرم‌ها (crispy-forms) چیست؟',
         '<p>بسته django-crispy-forms رندر فرم را به قالب Bootstrap/Tailwind واگذار می‌کند و کد قالب را تمیزتر می‌سازد. برای شروع، حلقه {% for field in form %} کافی است.</p>'),
        ('Formset برای چه زمانی است؟',
         '<p><span class="term" data-term="formset">مجموعه فرم</span> وقتی لازم است که تعداد نمونه‌ها پویا باشد: مثل «افزودن چند تصویر به یک محصول». مدیریت پیشوندهای فیلد و فرم‌های خالی/اضافی را خودش انجام می‌دهد.</p>'),
        ('چطور فیلد را فقط در ویرایش نشان دهم نه ایجاد؟',
         '<p>دو فرم مجزا (PostCreateForm/PostUpdateForm) یا حذف فیلد در __init__ بر اساس self.instance.pk. دو فرم صریح‌تر و خواناتر است.</p>'),
    ],
    next_step='فرم‌ها آماده‌اند؛ حالا در <strong>فصل ۱۲</strong> مهم‌ترین فرم‌های هر سایت را می‌سازیم: ثبت‌نام، ورود و خروج با سیستم <span class="term" data-term="authentication">احراز هویت</span> داخلی جنگو.',
),

# ================================================================ فصل ۱۲
dict(
    n=12, icon='🔐', title='احراز هویت (Authentication) و کاربران', cat=2, mins=105, lvl_label='متوسط',
    hero_desc='مدل User، ثبت‌نام با UserCreationForm، ورود و خروج با LoginView و LogoutView، محافظت صفحه‌ها با <span class="term" data-term="decorator">@login_required</span> و LoginRequiredMixin و ساخت پروفایل کاربری.',
    s1_intro='«کاربر» مرکز اکثر وب‌سایت‌هاست. خوشبختانه جنگو یکی از کامل‌ترین سیستم‌های احراز هویت آماده را دارد: مدل کاربر، هش امن رمز، نشست‌ها و ویوهای ورود/خروج — ما فقط وصل و شخصی‌سازی می‌کنیم.',
    objectives=[
        'مدل User داخلی و فیلدهایش را بشناسید.',
        'صفحه ثبت‌نام با UserCreationForm بسازید.',
        'ورود/خروج با ویوهای آماده و قالب registration/login.html.',
        'با @login_required و LoginRequiredMixin دسترسی را محدود کنید.',
        'پروفایل کاربر را با OneToOne و <span class="term" data-term="signal">سیگنال</span> بسازید.',
    ],
    s1_position='<strong>جایگاه فصل:</strong> بعد از فرم‌ها (۱۱). مجوزهای ریزتر در فصل ۱۳ و احراز هویت API در فصل ۲۳.',
    roadmap=[
        ('سیستم auth جنگو', 'User، رمز هش‌شده، نشست.'),
        ('ثبت‌نام', 'UserCreationForm و ورود خودکار.'),
        ('ورود/خروج', 'LoginView، LogoutView و تنظیمات.'),
        ('پروفایل', 'OneToOne + سیگنال + محافظت صفحه‌ها.'),
    ],
    mind_qs=[
        ('رمز عبور در دیتابیس چطور ذخیره می‌شود؟',
         '<p><strong>هش شده</strong> با الگوریتم PBKDF2 (به‌همراه salt یکتا). حتی خودِ سایت هم رمز اصلی را نمی‌بیند؛ فقط «آیا هش ورودی با هش ذخیره‌شده می‌خواند». برای همین «بازیابی رمز» یعنی «تنظیم رمز جدید».</p>'),
        ('بعد از ورود موفق، جنگو چطور می‌فهمد این درخواست از همان کاربر است؟',
         '<p>با <span class="term" data-term="session">نشست</span>: یک شناسه نشست در کوکی کاربر ذخیره و داده نشست (شامل user_id) سمت سرور نگه داشته می‌شود. میان‌افزار AuthenticationMiddleware در هر درخواست request.user را از روی آن پر می‌کند.</p>'),
        ('چرا مدل User را «کاستوم» نکنیم مگر مجبور باشیم؟',
         '<p>تغییر مدل کاربر <strong>بعد از</strong> شروع پروژه پرهزینه است (مهاجرت‌های پیچیده). اگر فیلد اضافه می‌خواهید، اول پروفایل OneToOne را در نظر بگیرید؛ کاستوم‌کردن را از روز اول پروژه تصمیم بگیرید.</p>'),
    ],
    prereq_intro='پیش‌نیازها:',
    prereq=[
        'فصل ۱۱: کار با ModelForm و الگوی ویوی فرم.',
        'اپ <code class="inline-code">accounts</code> بسازید: <code class="inline-code">python manage.py startapp accounts</code> و ثبت در INSTALLED_APPS.',
        'آشنایی با رابطه OneToOneField (مشابه ForeignKey با محدودیت یکی).',
        'قالب base.html با جای navbar (کارگاه فصل ۱۰).',
    ],
    prereq_callout=None,
    concepts=[
        dict(h='۵.۱ سیستم auth داخلی جنگو', body=[
            '<p>اپ <code class="inline-code">django.contrib.auth</code> این‌ها را آماده می‌دهد:</p>',
            '<ul>'
            '<li>مدل <code class="inline-code">User</code>: username، password (هش)، email، first/last_name، is_active، is_staff، is_superuser، last_login.</li>'
            '<li>توابع: <code class="inline-code">authenticate()</code>، <code class="inline-code">login()</code>، <code class="inline-code">logout()</code>.</li>'
            '<li><span class="term" data-term="cbv">ویوهای آماده</span>: LoginView، LogoutView، PasswordChangeView و... .</li>'
            '<li>Group و <span class="term" data-term="permission">Permission</span> (فصل ۱۳).</li></ul>',
            ('code', 'request.user در هر ویو', 'python', '''def dashboard(request):
    if request.user.is_authenticated:
        name = request.user.username
    else:
        ...  # کاربر ناشناس (AnonymousUser)'''),
        ]),
        dict(h='۵.۲ صفحه ثبت‌نام', body=[
            ('code', 'accounts/forms.py', 'python', '''from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True, label="ایمیل")

    class Meta:
        model = User
        fields = ("username", "email")

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("این ایمیل قبلاً ثبت شده است.")
        return email'''),
            ('code', 'accounts/views.py', 'python', '''from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SignupForm


class SignupView(CreateView):
    form_class = SignupForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("blog:list")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)   # ورود خودکار بعد از ثبت‌نام
        return response'''),
            '<p><span class="term" data-term="form">UserCreationForm</span> خودش username + password1 + password2 و بررسی شباهت رمز را دارد؛ ما فقط email افزودیم.</p>',
        ]),
        dict(h='۵.۳ ورود و خروج با ویوهای آماده', body=[
            ('code', 'accounts/urls.py', 'python', '''from django.contrib.auth import views as auth_views
from django.urls import path

app_name = "accounts"

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", auth_views.LoginView.as_view(
        template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("password-change/", auth_views.PasswordChangeView.as_view(
        template_name="registration/password_change_form.html",
        success_url=reverse_lazy("blog:list")), name="password_change"),
]'''),
            ('code', 'registration/login.html', 'html', '''{% extends "base.html" %}
{% block content %}
<h1>ورود</h1>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">ورود</button>
</form>
<p>حساب ندارید؟ <a href="{% url \'accounts:signup\' %}">ثبت‌نام</a></p>
{% endblock %}'''),
            ('code', 'تنظیمات لازم در settings.py', 'python', '''LOGIN_URL = "accounts:login"          # @login_required به کجا بفرستد
LOGIN_REDIRECT_URL = "blog:list"      # بعد از ورود موفق
LOGOUT_REDIRECT_URL = "blog:list"     # بعد از خروج'''),
            ('callout', 'warn', 'خروج فقط با POST',
             'از جنگو ۵ به بعد LogoutView فقط POST را می‌پذیرد (جلوگیری از خروج اجباری با لینک). پس «خروج» باید یک فرم POST کوچک باشد، نه <code class="inline-code">&lt;a href&gt;</code>.'),
        ]),
        dict(h='۵.۴ محافظت از صفحه‌ها', body=[
            ('code', 'دکوریتور برای FBV', 'python', '''from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    ...
# کاربر ناشناس → redirect به LOGIN_URL?next=/dashboard/'''),
            ('code', 'میکسین برای CBV', 'python', '''from django.contrib.auth.mixins import LoginRequiredMixin


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ("title", "body")'''),
            '<p>پارامتر <code class="inline-code">?next=</code> باعث می‌شود بعد از ورود، کاربر دقیقاً به همان صفحه‌ای برگردد که می‌خواست — LoginView خودش مدیریتش می‌کند.</p>',
        ]),
        dict(h='۵.۵ پروفایل کاربر با OneToOne و سیگنال', body=[
            ('code', 'accounts/models.py', 'python', '''from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True, max_length=500)
    avatar = models.ImageField(upload_to="avatars/", blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return f"پروفایل {self.user.username}"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)'''),
            '<p>حالا همیشه <code class="inline-code">request.user.profile.bio</code> در دسترس است. توضیح کامل <span class="term" data-term="signal">سیگنال</span>ها فصل ۱۶ است؛ اینجا فقط استفاده می‌کنیم.</p>',
            ('callout', 'info', 'settings.AUTH_USER_MODEL',
             'در کدهای جدید به‌جای import مستقیم User، از این تنظیم استفاده کنید؛ اگر روزی مدل کاربر کاستوم شد، کد شما نمی‌شکند.'),
        ]),
    ],
    example_intro='جریان کامل یک کاربر جدید — از ثبت‌نام تا پروفایل:',
    example=[
        ('code', '۱) ثبت‌نام', 'bash', '''# کاربر در /accounts/signup/ فرم را پر می‌کند
# → SignupView کاربر را می‌سازد (رمز هش می‌شود)
# → سیگنال post_save پروفایل خالی می‌سازد
# → login() خودکار: نشست شروع می‌شود'''),
        ('code', '۲) ویرایش پروفایل', 'python', '''class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ("bio", "avatar", "website")
    template_name = "accounts/profile_form.html"
    success_url = reverse_lazy("accounts:profile")

    def get_object(self):
        return self.request.user.profile   # فقط پروفایل خودش!


@login_required
def profile(request):
    return render(request, "accounts/profile.html",
                  {"profile": request.user.profile})'''),
        ('code', '۳) تست در شل', 'python', '''>>> from django.contrib.auth.models import User
>>> u = User.objects.first()
>>> u.password[:30]      # هش، نه رمز اصلی!
\'pbkdf2_sha256$870000$Xk2...\'
>>> u.profile.bio = "سلام!"
>>> u.profile.save()'''),
    ],
    workshop_intro='سیستم کاربران وبلاگ را کامل کنید:',
    workshop_tasks=[
        '<strong>کارگاه ۱:</strong> صفحات signup/login/logout/password-change را با ویوهای آماده بسازید و لینک‌هایشان را در navbar بگذارید (خروج با فرم POST).',
        '<strong>کارگاه ۲:</strong> ویوهای ایجاد/ویرایش/حذف پست را محافظت کنید و در post_list، برای کاربر واردشده دکمه «نوشته جدید» نشان دهید.',
        '<strong>کارگاه ۳:</strong> صفحه پروفایل عمومی بسازید: <code class="inline-code">/accounts/user/&lt;username&gt;/</code> که بیو و فهرست پست‌های همان نویسنده را نشان دهد.',
    ],
    workshop_answers=[
        ('پاسخ کارگاه ۱',
         '<p>urls طبق مفهوم ۵.۳ + در navbar:</p>'
         '<div class="code-box"><div class="code-head"><span>partials/navbar.html</span><span class="lang">HTML</span></div><pre class="code"><code data-lang="html">{% if user.is_authenticated %}\n  &lt;a href="{% url \'accounts:profile\' %}"&gt;پروفایل من&lt;/a&gt;\n  &lt;form method="post" action="{% url \'accounts:logout\' %}" style="display:inline"&gt;\n    {% csrf_token %}&lt;button&gt;خروج&lt;/button&gt;\n  &lt;/form&gt;\n{% else %}\n  &lt;a href="{% url \'accounts:login\' %}"&gt;ورود&lt;/a&gt;\n  &lt;a href="{% url \'accounts:signup\' %}"&gt;ثبت‌نام&lt;/a&gt;\n{% endif %}</code></pre></div>'),
        ('پاسخ کارگاه ۲',
         '<div class="code-box"><div class="code-head"><span>محافظت CBVها</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">class PostCreateView(LoginRequiredMixin, CreateView): ...\nclass PostUpdateView(LoginRequiredMixin, UpdateView): ...\nclass PostDeleteView(LoginRequiredMixin, DeleteView): ...\n\n# و محدودسازی به پست‌های خود کاربر:\nclass PostUpdateView(LoginRequiredMixin, UpdateView):\n    model = Post\n    fields = ("title", "body")\n\n    def get_queryset(self):\n        return Post.objects.filter(author=self.request.user)</code></pre></div>'
         '<p>get_queryset روی author فیلتر می‌کند تا کاربر A نتواند پست کاربر B را با حدس زدن pk ویرایش کند (وگرنه 404 می‌گیرد).</p>'),
        ('پاسخ کارگاه ۳',
         '<div class="code-box"><div class="code-head"><span>پروفایل عمومی</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">def public_profile(request, username):\n    user = get_object_or_404(User, username=username)\n    posts = user.posts.filter(published=True)\n    return render(request, "accounts/public_profile.html",\n                  {"profile_user": user, "posts": posts})</code></pre></div>'
         '<p>مسیر: <code class="inline-code">path("user/&lt;str:username&gt;/", views.public_profile, name="public_profile")</code>. در قالب: بیو از <code class="inline-code">profile_user.profile.bio</code>.</p>'),
    ],
    errors=[
        ('حلقه redirect بی‌نهایت روی صفحه ورود',
         'LOGIN_URL به مسیری اشاره می‌کند که خودش login_required دارد یا نامش غلط است. LOGIN_URL باید دقیقاً مسیر صفحه ورود باشد (accounts:login).'),
        ('بعد از ورود موفق به صفحه اصلی نمی‌روم',
         'LOGIN_REDIRECT_URL تنظیم نشده (پیش‌فرض /accounts/profile/ است که شاید وجود نداشته باشد → 404). در settings تنظیمش کنید.'),
        ('خطای 405 Method Not Allowed هنگام خروج',
         'خروج را با لینک GET صدا زده‌اید؛ LogoutView جنگو ۵+ فقط POST می‌پذیرد. فرم POST با csrf_token بگذارید.'),
        ('request.user همیشه AnonymousUser است',
         'میان‌افزارهای SessionMiddleware و AuthenticationMiddleware از MIDDLEWARE حذف شده‌اند (یا ترتیبشان خراب است). settings پیش‌فرض را دست نزنید.'),
        ('Profile.DoesNotExist برای بعضی کاربران',
         'کاربرانی که <strong>قبل از</strong> افزودن سیگنال ساخته شده‌اند پروفایل ندارند. یک‌بار در شل برای همه بسازید: <code class="inline-code">[Profile.objects.get_or_create(user=u) for u in User.objects.all()]</code>.'),
    ],
    errors_callout=('danger', 'هرگز رمز را این‌گونه نسازید',
        '<code class="inline-code">user.password = "1234"</code> رمز را <strong>رمزنگاری‌نشده</strong> ذخیره می‌کند و کاربر هرگز نمی‌تواند وارد شود! همیشه <code class="inline-code">user.set_password("1234")</code> و بعد save().'),
    exercises=[
        ('تمرین ۱ — جریان ورود',
         '<p><strong>سوال:</strong> مراحل ورود موفق را مرتب کنید: ساخت/به‌روزرسانی نشست • چک کردن هش رمز • دریافت username/password • پر شدن request.user در درخواست‌های بعدی.</p>'
         '<p><strong>پاسخ:</strong> دریافت داده → authenticate (چک هش) → login() (ساخت نشست + کوکی sessionid) → درخواست‌های بعدی: request.user پرشده.</p>'),
        ('تمرین ۲ — انتخاب ابزار',
         '<p><strong>سوال:</strong> برای هر مورد: (الف) محافظت FBV (ب) محافظت CBV (ج) تغییر مسیر کاربر غیرمجازه به صفحه خطا به‌جای لاگین (د) چک «آیا این کاربر نویسنده همان پست است؟»</p>'
         '<p><strong>پاسخ:</strong> الف → @login_required • ب → LoginRequiredMixin • ج → @user_passes_test یا permission_required (فصل ۱۳) • د → بررسی دستی در ویو یا فیلتر get_queryset (کارگاه ۲).</p>'),
        ('تمرین ۳ — OneToOne یا ForeignKey؟',
         '<p><strong>سوال:</strong> برای پروفایل چرا OneToOneField نه ForeignKey؟</p>'
         '<p><strong>پاسخ:</strong> چون هر کاربر باید <strong>دقیقاً یک</strong> پروفایل داشته باشد. با FK، user.profile چند مقدار برمی‌گرداند و یکتایی تضمین نمی‌شود؛ OneToOne هم یکتایی دیتابیس می‌دهد هم دسترسی user.profile تک‌مقداری.</p>'),
    ],
    quiz=[
        dict(q='رمز عبور کاربر در پایگاه داده چطور ذخیره می‌شود؟',
             opts=['متن ساده برای بازیابی', 'هش یک‌طرفه با salt (مثل PBKDF2)',
                   'رمزنگاری دوطرفه با SECRET_KEY', 'اصلاً ذخیره نمی‌شود'],
             ans='b', explain='هش یک‌طرفه است: از هش نمی‌توان رمز را بازیافت؛ ورود = مقایسه هش‌ها. set_password() همین کار را می‌کند.'),
        dict(q='LOGIN_URL چه نقشی دارد؟',
             opts=['نشانی خروج', 'مقصد redirect برای کاربر ناشناسی که به صفحه محافظت‌شده می‌رسد',
                   'صفحه ثبت‌نام', 'صفحه پروفایل'],
             ans='b', explain='login_required و LoginRequiredMixin کاربر ناشناس را به LOGIN_URL با پارامتر ?next= می‌فرستند.'),
        dict(q='بعد از ثبت‌نام موفق می‌خواهیم کاربر بدون ورود دستی ادامه دهد. کدام تابع؟',
             opts=['authenticate()', 'login(request, user)', 'request.user = user', 'create_session()'],
             ans='b', explain='login() نشست را برای کاربرِ (احراز هویت‌شده) شروع می‌کند؛ معمولاً در form_valid بعد از super().form_valid.'),
        dict(q='خروج (logout) در جنگو ۵+ با کدام متد HTTP انجام می‌شود؟',
             opts=['GET با لینک', 'POST با فرم و csrf_token', 'DELETE', 'هر کدام فرقی ندارد'],
             ans='b', explain='POST بودن، خروج اجباری از راه لینک‌های خارجی (نوعی CSRF) را خنثی می‌کند.'),
        dict(q='برای افزودن فیلد «شماره تلفن» به کاربر، کم‌هزینه‌ترین راه در پروژه موجود چیست؟',
             opts=['تغییر مدل User به کاستوم', 'ساخت مدل Profile با OneToOneField به User',
                   'ذخیره در session', 'افزودن به settings'],
             ans='b', explain='مدل پروفایل بدون مهاجرت‌های سنگین auth کار می‌کند؛ User کاستوم باید از روز اول پروژه تصمیم گرفته می‌شد.'),
        dict(q='request.user برای کاربر واردنشده چیست؟',
             opts=['None و خطا می‌دهد', 'شیء AnonymousUser با is_authenticated=False',
                   'User خالی', 'رشته "guest"'],
             ans='b', explain='AnonymousUser رابط User را تقلید می‌کند تا کد شما نیاز به if None نداشته باشد؛ is_authenticated آن False است.'),
    ],
    project_title='حساب‌های کاربری کامل وبلاگ',
    project_intro='اپ accounts را به یک سیستم کاربری واقعی تبدیل کنید.',
    project_checklist=[
        'ثبت‌نام + ورود + خروج + تغییر رمز (همه با ویوهای آماده و قالب فارسی).',
        'پروفایل با سیگنال + ویرایش بیو/آواتار.',
        'صفحه «نوشته‌های من»: فهرست + آمار پست‌های کاربر واردشده.',
        'همه ویوهای نوشتن (ساخت/ویرایش/حذف پست) محافظت‌شده و محدود به مالک.',
        'navbar با وضعیت ورود و لینک‌های contextual.',
    ],
    project_callout=('tip', 'ایمیل تأیید ثبت‌نام',
        'ارسال ایمیل فعال‌سازی یک گام حرفه‌ای بعدی است؛ در فصل ۲۴ با <span class="term" data-term="celery">سلری</span> به‌صورت ناهمگام پیاده‌اش می‌کنیم.'),
    summary_items=[
        'سیستم auth جنگو: مدل User، هش PBKDF2، نشست‌محور.',
        'ثبت‌نام با UserCreationForm + ورود خودکار با login().',
        'LoginView/LogoutView با تنظیمات LOGIN_URL و REDIRECTها.',
        'محافظت: @login_required (تابعی) و LoginRequiredMixin (کلاسی).',
        'پروفایل: OneToOne + post_save + دسترسی user.profile.',
    ],
    golden='احراز هویت = «کیستی» کاربر؛ از این پس هر ویوی نوشتن، هم هویت می‌خواهد هم مالکیت.',
    faq=[
        ('می‌توانم با ایمیل به‌جای username وارد شوم؟',
         '<p>بله؛ یا AuthenticationBackend سفارشی می‌نویسید یا از همان ابتدا مدل کاربر کاستوم با USERNAME_FIELD="email" می‌سازید (پکیج‌هایی مثل django-allauth هم این را آماده دارند).</p>'),
        ('allauth چیست و کجا لازم می‌شود؟',
         '<p>django-allauth مجموعه‌ای کامل: ورود با گوگل/گیت‌هاب، تأیید ایمیل، بازنشانی رمز و 2FA. برای پروژه جدی با «ورود اجتماعی» بهترین انتخاب است؛ برای یادگیری، اول سیستم داخلی را مسلط شوید.</p>'),
        ('چطور کاربر را بعد از N ورود ناموفق قفل کنم؟',
         '<p>داخلی ندارد؛ پکیج django-axes دقیقاً همین کار (ضد Brute-Force) را می‌کند. فصل ۲۶ (استقرار) آن را در چک‌لیست امنیت داریم.</p>'),
    ],
    next_step='حالا که «کیستی» روشن شد، در <strong>فصل ۱۳</strong> «چه اجازه‌ای دارد» را حل می‌کنیم: گروه‌ها، <span class="term" data-term="permission">مجوزها</span> و نقش‌های کاربری.',
),

# ================================================================ فصل ۱۳
dict(
    n=13, icon='🛡️', title='گروه‌ها و مجوزها (Permissions)', cat=3, mins=95, lvl_label='متوسط',
    hero_desc='سامانه مجوزهای جنگو: Group و <span class="term" data-term="permission">Permission</span>، ساخت گروه در پنل، <span class="term" data-term="decorator">@permission_required</span> و PermissionRequiredMixin، مجوز سفارشی در Meta و بررسی perms در قالب.',
    s1_intro='فصل قبل «کیستی» را حل کردیم؛ این فصل «<span class="term" data-term="authorization">مجوزدهی</span>» است: کدام کاربر چه کاری allowed است. با نقش‌های درست، یک سایت چندکاربره امن و قابل توسعه می‌سازید.',
    objectives=[
        'ساختار مجوزهای خودکار جنگو (add/change/delete/view) را توضیح دهید.',
        'با Group نقش بسازید و کاربران را عضو کنید.',
        'با @permission_required و PermissionRequiredMixin ویوها را محدود کنید.',
        'مجوز <strong>سفارشی</strong> در Meta تعریف و بررسی کنید.',
        'در قالب با تگ perms رابط کاربری را شرطی کنید.',
    ],
    s1_position='<strong>جایگاه فصل:</strong> بعد از احراز هویت (۱۲)؛ پنل ادمین (فصل ۶) هم از همین مجوزها استفاده می‌کند.',
    roadmap=[
        ('مدل مجوزها', 'Permission، Group و رابطه‌شان.'),
        ('نقش‌سازی در پنل', 'ساخت گروه ویراستار و نویسنده.'),
        ('اعمال در ویو', 'دکوریتور و میکسین.'),
        ('مجوز سفارشی', 'Meta.permissions و perms در قالب.'),
    ],
    mind_qs=[
        ('چرا به‌جای <code class="inline-code">if user.username == "admin"</code> از مجوزها استفاده کنیم؟',
         '<p>چون نقش‌ها باید <strong>داده‌محور</strong> باشند نه کدمحور. با Group، مدیر سایت می‌تواند بدون تغییر کد، <span class="term" data-term="authorization">دسترسی‌ها</span> را عوض کند؛ کد فقط «مجوز» را چک می‌کند نه «شخص» را.</p>'),
        ('مجوز <code class="inline-code">blog.change_post</code> از کجا آمده؟',
         '<p>جنگو برای <strong>هر مدل</strong> به‌طور خودکار چهار مجوز می‌سازد: add، change، delete و view — به قالب <code class="inline-code">app_label.codename</code>. این‌ها همان‌هایی هستند که پنل ادمین چک می‌کند.</p>'),
        ('ابرکاربر (superuser) هم مجوزها را چک می‌کند؟',
         '<p>نه لازم نیست! <code class="inline-code">is_superuser=True</code> یعنی <strong>همه</strong> has_permها True برمی‌گردند. ابرکاربر بالای هرم است.</p>'),
    ],
    prereq_intro='پیش‌نیازها:',
    prereq=[
        'فصل ۱۲ کامل (ورود/خروج و @login_required کار کند).',
        'مدل Post با author و ویوهای CRUD.',
        'دسترسی به پنل ادمین با حساب ابرکاربر.',
        'چند کاربر تستی (می‌توانید در شل بسازید).',
    ],
    prereq_callout=None,
    concepts=[
        dict(h='۵.۱ مدل مجوزها: Permission و Group', body=[
            '<p>سه موجودیت درگیرند:</p>',
            '<ul>'
            '<li><strong>Permission</strong>: یک اجازه مشخص، با codename مثل <code class="inline-code">blog.change_post</code>.</li>'
            '<li><strong>Group</strong>: مجموعه‌ای از مجوزها = یک «نقش» (ویراستار، نویسنده، پشتیبان).</li>'
            '<li><strong>User</strong>: می‌تواند مستقیم مجوز داشته باشد یا از راه عضویت در گروه‌ها.</li></ul>',
            ('code', 'بررسی مجوز در کد', 'python', '''user.has_perm("blog.change_post")        # True/False
user.get_group_permissions()              # مجوزهای گروهی
user.groups.filter(name="Editors").exists()'''),
            '<p>user.has_perm نتایج را در <span class="term" data-term="session">نشست</span> کش می‌کند؛ بعد از تغییر گروه/مجوز کاربرِ آنلاین، با login() مجدد یا انتظار تا نشست بعدی اعمال می‌شود.</p>',
        ]),
        dict(h='۵.۲ ساخت نقش‌ها در پنل ادمین (بدون کد!)', body=[
            '<ol>'
            '<li>در <code class="inline-code">/admin/</code> → Groups → Add: گروه <strong>«ویراستاران»</strong>.</li>'
            '<li>مجوزها را انتخاب کنید: blog | post | Can change post، Can view post، blog | comment | همه.</li>'
            '<li>ذخیره. حالا هر کاربری که عضو این گروه شود، همان دسترسی‌ها را دارد.</li></ol>',
            ('code', 'معادل کدی (مثلاً در Data Migration یا شل)', 'python', '''from django.contrib.auth.models import Group, Permission

editors, _ = Group.objects.get_or_create(name="Editors")
for codename in ("change_post", "view_post", "delete_comment", "change_comment"):
    perm = Permission.objects.get(codename=codename)
    editors.permissions.add(perm)

user.groups.add(editors)'''),
        ]),
        dict(h='۵.۳ اعمال مجوز در ویوها', body=[
            ('code', 'دکوریتور برای FBV', 'python', '''from django.contrib.auth.decorators import permission_required


@permission_required("blog.change_post", raise_exception=True)
def moderate_comments(request):
    ...
# raise_exception=False (پیش‌فرض) → ابتدا به صفحه ورود هدایت می‌شود
# raise_exception=True → مستقیماً 403'''),
            ('code', 'میکسین برای CBV', 'python', '''from django.contrib.auth.mixins import PermissionRequiredMixin


class PostUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = "blog.change_post"
    model = Post
    fields = ("title", "body")'''),
            ('code', 'مالکیت: مجوز سطح ردیف (Row-Level)', 'python', '''def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user and not request.user.has_perm("blog.change_post"):
        raise PermissionDenied           # 403
    ...'''),
            ('callout', 'info', 'دو سطح مجوز',
             'مجوزهای جنگو «نوعی» هستند (آیا کاربر اصلاً اجازهٔ change_post دارد؟). «این رکوردِ خاص مال خودش است؟» را باید دستی چک کنید — مثل کد بالا. پکیج django-guardian مجوز سطح شیء را اضافه می‌کند.'),
        ]),
        dict(h='۵.۴ مجوز سفارشی در Meta', body=[
            ('code', 'models.py', 'python', '''class Post(models.Model):
    ...
    class Meta:
        permissions = [
            ("publish_post", "می‌تواند پست را منتشر کند"),
            ("feature_post", "می‌تواند پست را ویژه کند"),
        ]'''),
            ('code', 'سپس', 'bash', '''python manage.py makemigrations && python manage.py migrate
# مجوزها در پنل ادمین (Groups) ظاهر می‌شوند'''),
            ('code', 'استفاده در ویو', 'python', '''@permission_required("blog.publish_post")
def publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.published = True
    post.save()
    return redirect(post)'''),
        ]),
        dict(h='۵.۵ perms در قالب و user_passes_test', body=[
            ('code', 'رابط کاربری شرطی', 'html', '''{% if perms.blog.change_post %}
  <a href="{% url \'blog:post_edit\' post.pk %}">ویرایش</a>
{% endif %}

{% if perms.blog.delete_post or post.author == user %}
  <form method="post" action="{% url \'blog:post_delete\' post.pk %}">
    {% csrf_token %}<button>حذف</button>
  </form>
{% endif %}'''),
            ('code', 'شرط دلخواه با user_passes_test', 'python', '''from django.contrib.auth.decorators import user_passes_test


def is_editor(user):
    return user.is_authenticated and user.groups.filter(name="Editors").exists()


@user_passes_test(is_editor, login_url="accounts:login")
def editor_dashboard(request):
    ...'''),
            ('callout', 'warn', 'قانون طلایی',
             'پنهان کردن دکمه در قالب <strong>امنیت نیست</strong> (کاربر می‌تواند URL را دستی بزند). شرط قالب فقط UX است؛ حفاظ واقعی همان دکوریتور/میکسین سمت ویو است.'),
        ]),
    ],
    example_intro='سناریوی واقعی: وبلاگ سه‌نقشه — نویسنده، ویراستار، مدیر:',
    example=[
        ('code', 'تعریف نقش‌ها (یک‌بار، در شل یا migration)', 'python', '''ROLES = {
    "Authors":  ["blog.add_post", "blog.view_post"],
    "Editors":  ["blog.view_post", "blog.change_post",
                 "blog.publish_post", "blog.change_comment", "blog.delete_comment"],
    "Managers": ["blog.view_post", "blog.change_post", "blog.delete_post",
                 "blog.publish_post", "blog.add_post"],
}

for name, perms in ROLES.items():
    group, _ = Group.objects.get_or_create(name=name)
    group.permissions.set(Permission.objects.filter(
        content_type__app_label="blog", codename__in=[p.split(".")[1] for p in perms]))'''),
        ('code', 'ویوی انتشار — فقط ویراستار', 'python', '''@permission_required("blog.publish_post", raise_exception=True)
def publish_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.published = True
    post.save()
    messages.success(request, f"«{post.title}» منتشر شد.")
    return redirect("blog:list")'''),
        ('code', 'قالب — دکمه‌ها بر اساس نقش', 'html', '''{% if post.author == user %}
  <a href="{% url \'blog:post_edit\' post.pk %}">ویرایش نوشته من</a>
{% endif %}
{% if perms.blog.publish_post and not post.published %}
  <form method="post" action="{% url \'blog:publish\' post.pk %}">
    {% csrf_token %}<button>انتشار</button>
  </form>
{% endif %}'''),
    ],
    workshop_intro='نقش‌های یک فروشگاه کوچک را پیاده کنید:',
    workshop_tasks=[
        '<strong>کارگاه ۱:</strong> دو گروه «فروشنده» (افزودن/ویرایش محصولات خودش) و «ناظر» (دیدن همه + تغییر وضعیت تأیید محصول) بسازید — با پنل یا کد.',
        '<strong>کارگاه ۲:</strong> مجوز سفارشی <code class="inline-code">approve_product</code> در Meta مدل Product تعریف کنید، مهاجرت بزنید و به گروه ناظر بدهید.',
        '<strong>کارگاه ۳:</strong> ویوی approve را با @permission_required محافظت کنید و در قالب، دکمه تأیید فقط به دارندگان مجوز نشان داده شود.',
    ],
    workshop_answers=[
        ('پاسخ کارگاه ۱ و ۲',
         '<div class="code-box"><div class="code-head"><span>مدل با مجوز سفارشی</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">class Product(models.Model):\n    name = models.CharField(max_length=200)\n    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)\n    approved = models.BooleanField(default=False)\n\n    class Meta:\n        permissions = [("approve_product", "تأیید محصول")]</code></pre></div>'
         '<p>سپس <span class="term" data-term="migration">makemigrations + migrate</span>. در پنل: Group «ناظر» ← تیک approve_product + view/change؛ Group «فروشنده» ← add_product + change_product.</p>'),
        ('پاسخ کارگاه ۳',
         '<div class="code-box"><div class="code-head"><span>ویو و قالب</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">@permission_required("shop.approve_product", raise_exception=True)\ndef approve_product(request, pk):\n    product = get_object_or_404(Product, pk=pk)\n    product.approved = True\n    product.save()\n    return redirect("shop:product_detail", pk=pk)</code></pre></div>'
         '<p>قالب: <code class="inline-code">{% if perms.shop.approve_product and not product.approved %}</code> فرم POST دکمه تأیید. محدودیت «فروشنده فقط محصولات خودش» با فیلتر <code class="inline-code">seller=request.user</code> در get_queryset ویوهای ویرایش.</p>'),
    ],
    errors=[
        ('کاربر عضو گروه است ولی has_perm هنوز False است',
         'نتیجه has_perm در نشست <strong>کش</strong> شده. کاربر را خارج/وارد کنید یا در کد، کش مجوز نشست را نادیده بگیرید. در تست‌ها هم گاهی ساخت کاربر قبل از اختصاص گروه است.'),
        ('فرمت اشتباه مجوز: 403 یا رد نشدن',
         'codename باید به شکل <code class="inline-code">"app_label.codename"</code> باشد: <code class="inline-code">"blog.change_post"</code> نه <code class="inline-code">"change_post"</code> و نه <code class="inline-code">"Blog.ChangePost"</code>.'),
        ('مجوز سفارشی در پنل ظاهر نمی‌شود',
         'بعد از افزودن Meta.permissions باید makemigrations و migrate اجرا شود — مجوزها با مهاجرت ساخته می‌شوند.'),
        ('کاربر ناشناس به‌جای 403 به صفحه ورود می‌رود و گیج شده',
         'رفتار پیش‌فرض permission_required همین است (اول login). برای API یا رفتار صریح: raise_exception=True تا مستقیم 403 بگیرد.'),
        ('ویراستار می‌تواند پست همه را ویرایش کند، ولی باید فقط ...',
         'مجوز نوعی به تنهایی «دامنه» تعیین نمی‌کند. محدودیت مالکیت (سطر) را دستی اضافه کنید: فیلتر author در get_queryset یا بررسی در ویو (مفهوم ۵.۳).'),
    ],
    errors_callout=None,
    exercises=[
        ('تمرین ۱ — codenameها',
         '<p><strong>سوال:</strong> codename مجوزهای خودکار مدل Comment در اپ shop چیست؟</p>'
         '<p><strong>پاسخ:</strong> shop.add_comment، shop.change_comment، shop.delete_comment، shop.view_comment.</p>'),
        ('تمرین ۲ — انتخاب مکانیزم',
         '<p><strong>سوال:</strong> برای هر سناریو کدام ابزار؟ (الف) فقط کاربران واردشده (ب) فقط گروه «ناظم‌ها» (ج) فقط دارای مجوز خاص (د) فقط مالک رکورد</p>'
         '<p><strong>پاسخ:</strong> الف → <span class="term" data-term="authentication">login_required</span> • ب → user_passes_test(بررسی گروه) • ج → permission_required • د → چک دستی author == request.user (سطح ردیف).</p>'),
        ('تمرین ۳ — طراحی نقش',
         '<p><strong>سناریو:</strong> در سایت آموزشی، «مدرس» درس می‌سازد ولی فقط درس‌های خودش را ویرایش می‌کند؛ «مدیر» همه را. طراحی کنید.</p>'
         '<p><strong>پاسخ نمونه:</strong> گروه Teachers با add_course/change_course + فیلتر owner در ویوهای مدرس؛ گروه Admins با مجوزها بدون فیلتر مالکیت. UI با perms شرطی، حفاظت در ویو.</p>'),
    ],
    quiz=[
        dict(q='جنگو به‌طور خودکار برای هر مدل چه مجوزهایی می‌سازد؟',
             opts=['فقط view', 'add، change، delete و view',
                   'read و write', 'هیچ — باید دستی ساخت'],
             ans='b', explain='چهار مجوز پیش‌فرض با codenameهایی مثل app_label.add_model؛ با Meta.permissions قابل گسترش.'),
        dict(q='عضویت کاربر در Group چه اثری دارد؟',
             opts=['فقط نام نمایشی', 'همه مجوزهای آن گروه به کاربر تعلق می‌گیرد',
                   'کاربر staff می‌شود', 'رمزش قوی‌تر می‌شود'],
             ans='b', explain='Group مجموعه‌ای از Permissionهاست؛ get_group_permissions همه را یکجا برمی‌گرداند و has_perm آن‌ها را می‌پذیرد.'),
        dict(q='کدام درباره superuser درست است؟',
             opts=['باید تک‌تک مجوزها را داشته باشد', 'has_perm برای هر مجوزی True برمی‌گرداند',
                   'فقط به پنل ادمین دسترسی دارد', 'مثل بقیه کاربران است'],
             ans='b', explain='is_superuser یعنی دسترسی کامل؛ نیازی به اختصاص مجوز ندارد (و در پنل هم همه را می‌بیند).'),
        dict(q='برای چک مجوز در CBV از چه استفاده می‌کنیم؟',
             opts=['@login_required', 'PermissionRequiredMixin با permission_required',
                   '@user_passes_test', 'get_context_data'],
             ans='b', explain='میکسین PermissionRequiredMixin دقیقاً معادل دکوریتور permission_required برای ویوهای کلاسی است.'),
        dict(q='پنهان کردن دکمه با {% if perms.x %} چه تضمینی می‌دهد؟',
             opts=['امنیت کامل', 'هیچ — فقط UX؛ حفاظت واقعی سمت ویو است',
                   'جلوگیری از CSRF', 'سرعت بیشتر'],
             ans='b', explain='کاربر می‌تواند URL را مستقیم درخواست دهد؛ پس ویو باید دکوریتور/بررسی داشته باشد. شرط قالب مکمل است نه جایگزین.'),
        dict(q='مجوز سفارشی را کجا تعریف و چطور فعال می‌کنیم؟',
             opts=['در views.py — خودکار فعال است', 'در Meta.permissions مدل — با makemigrations و migrate',
                   'در settings.py', 'در urls.py'],
             ans='b', explain='تعریف در Meta.permissions و ساخت با مهاجرت؛ سپس در Groups قابل اختصاص است.'),
    ],
    project_title='نقش‌های وبلاگ چندنویسنده',
    project_intro='وبلاگ را به یک سامانه چندنقشه تبدیل کنید.',
    project_checklist=[
        'گروه‌های Authors، Editors و Managers با مجوزهای مناسب.',
        'مجوز سفارشی publish_post + ویوی انتشار محافظت‌شده.',
        'نویسنده فقط پست‌های خودش را ویرایش/حذف کند (فیلتر مالکیت).',
        'داشبورد ساده ادمین‌طور برای Editors: فهرست پست‌های در انتظار انتشار.',
        'navbar و دکمه‌های قالب کاملاً بر اساس perms شرطی.',
    ],
    project_callout=('tip', 'تست مجوزها',
        'با دو مرورگر (یا حالت ناشناس) هم‌زمان یک نویسنده و یک ویراستار وارد شوید و سناریوها را امتحان کنید — در فصل ۲۰ تست خودکارش را می‌نویسیم.'),
    summary_items=[
        'مجوز = app_label.codename؛ چهار مجوز خودکار برای هر مدل.',
        'Group = نقش؛ کاربر مستقیم یا گروهی مجوز می‌گیرد.',
        'اعمال: @permission_required / PermissionRequiredMixin / has_perm دستی.',
        'مجوز سفارشی در Meta.permissions با مهاجرت ساخته می‌شود.',
        'perms در قالب فقط UX است؛ مالکیت رکورد (سطح ردیف) را دستی چک کنید.',
    ],
    golden='کد را روی «نقش‌ها» بنویسید نه روی «آدم‌ها»؛ گروه‌ها پل بین این دو هستند.',
    faq=[
        ('مجوز سطح شیء (Object-Level) چطور؟',
         '<p>has_perm("x", obj) امضایش را دارد ولی بک‌اند پیش‌فرض پشتیبانی نمی‌کند. راه‌حل‌ها: چک دستی author==user (ساده‌ترین) یا پکیج django-guardian.</p>'),
        ('نقش‌ها را کجا تعریف کنم: کد یا پنل؟',
         '<p>تعریف اولیه نقش‌ها در Data Migration (تکرارپذیر در همه محیط‌ها) و مدیریت اعضا در <span class="term" data-term="admin">پنل ادمین</span>. بدترین حالت: نقش‌سازی دستی در پنل تولید که در محیط توسعه وجود ندارد.</p>'),
        ('کاربر هم‌زمان عضو چند گروه باشد؟',
         '<p>کاملاً مجاز و رایج است؛ مجوزها <strong>اجتماع</strong> گروه‌هاست. مثال: کاربری هم Editor هم Teacher.</p>'),
    ],
    next_step='متن و تصویر در <strong>فصل ۱۴</strong>: مدیریت فایل‌های ایستا (CSS/JS/تصویر) و رسانه‌های آپلودی کاربران با Static و Media.',
),

# ================================================================ فصل ۱۴
dict(
    n=14, icon='🖼️', title='فایل‌های ایستا و رسانه (Static و Media)', cat=3, mins=85, lvl_label='متوسط',
    hero_desc='تفاوت فایل ایستا و رسانه، تنظیمات STATIC_URL و MEDIA_URL، تگ {% static %}، دستور collectstatic و آپلود فایل با FileField و ImageField.',
    s1_intro='CSS، جاوااسکریپت، تصویر لوگو و عکس پروفایل کاربران — همه «فایل» هستند ولی دو جنس کاملاً متفاوت: ایستا (مال ما) و رسانه (مال کاربر). اشتباه گرفتن این دو، منبع کلاسیک باگ‌های استقرار است.',
    objectives=[
        'تفاوت <span class="term" data-term="static-files">Static</span> و Media را توضیح دهید.',
        'پوشه‌ها و تنظیمات STATICFILES_DIRS، STATIC_ROOT و MEDIA_ROOT را پیکربندی کنید.',
        'با تگ {% static %} و {% load static %} به فایل‌ها ارجاع دهید.',
        'FileField/ImageField بسازید و آپلود را در فرم و ویو مدیریت کنید.',
        'نقش collectstatic در استقرار را بگویید.',
    ],
    s1_position='<strong>جایگاه فصل:</strong> مکمل قالب‌ها (۱۰) و فرم‌ها (۱۱)؛ سرو فایل در تولید با WhiteNoise/Nginx در فصل ۲۶.',
    roadmap=[
        ('ایستا در برابر رسانه', 'دو جنس فایل، دو مسیر سرو.'),
        ('تنظیمات و static tag', 'STATIC_*ها و ارجاع در قالب.'),
        ('آپلود کاربر', 'ImageField، request.FILES، نمایش.'),
        ('collectstatic', 'جمع‌آوری برای تولید.'),
    ],
    mind_qs=[
        ('چرا در توسعه MEDIA را دستی به urls اضافه می‌کنیم ولی STATIC را نه؟',
         '<p>چون <span class="term" data-term="app">app</span> ایستای جنگو (staticfiles) در <span class="term" data-term="debug">DEBUG=True</span> خودش فایل‌های ایستا را سرو می‌کند؛ ولی برای رسانه‌های آپلودی هیچ‌کس این کار را نمی‌کند — باید خودمان الگوی URL بدهیم.</p>'),
        ('اگر دو اپ هر دو فایل <code class="inline-code">css/style.css</code> داشته باشند کدام سرو می‌شود؟',
         '<p>اولین موردی که در ترتیب جست‌وجو (STATICFILES_DIRS قبل از appها) پیدا شود! برای همین فایل‌ها را با پیشوند نام اپ می‌گذارند: <code class="inline-code">blog/css/blog.css</code>.</p>'),
        ('در تولید چه کسی فایل‌ها را سرو می‌کند؟',
         '<p>نه runserver (که وجود ندارد!) — یا <span class="term" data-term="nginx">Nginx</span> مستقیم از STATIC_ROOT، یا پکیجی مثل <span class="term" data-term="whitenoise">WhiteNoise</span>، یا <span class="term" data-term="cdn">CDN</span>. collectstatic همه فایل‌ها را در STATIC_ROOT جمع می‌کند تا این سرویس‌ها یک‌جا بردارند.</p>'),
    ],
    prereq_intro='پیش‌نیازها:',
    prereq=[
        'پروژه وبلاگ با base.html (فصل ۱۰) و فرم پست (فصل ۱۱).',
        'برای ImageField: نصب Pillow → <code class="inline-code">pip install pillow</code>.',
        'مدل Post آماده افزودن فیلد تصویر.',
        'درک تفاوت پوشه اپ و پوشه ریشه پروژه.',
    ],
    prereq_callout=None,
    concepts=[
        dict(h='۵.۱ دو جنس فایل: ایستا و رسانه', body=[
            '<div class="table-wrap"><table class="compare"><thead><tr><th></th><th>Static</th><th>Media</th></tr></thead><tbody>'
            '<tr><td>مالک</td><td>توسعه‌دهنده (بخش کد)</td><td>کاربر (آپلود می‌کند)</td></tr>'
            '<tr><td>نمونه</td><td>CSS، JS، لوگو، فونت</td><td>عکس پروفایل، کاور پست، فایل پیوست</td></tr>'
            '<tr><td>تغییر</td><td>فقط با دیپلوی</td><td>هر لحظه توسط کاربر</td></tr>'
            '<tr><td>محل توسعه</td><td>app/static/app/ یا templates/../static/</td><td>MEDIA_ROOT (بیرون از کد!)</td></tr>'
            '<tr><td>تنظیمات</td><td>STATIC_URL, STATICFILES_DIRS, STATIC_ROOT</td><td>MEDIA_URL, MEDIA_ROOT</td></tr>'
            '</tbody></table></div>',
        ]),
        dict(h='۵.۲ تنظیمات و ساختار پوشه‌ها', body=[
            ('code', 'settings.py', 'python', '''from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

# ایستا
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]      # پوشه static ریشه پروژه
STATIC_ROOT = BASE_DIR / "staticfiles"        # مقصد collectstatic (تولید)

# رسانه
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"               # آپلودهای کاربران'''),
            ('code', 'ساختار پوشه‌ها', 'text', '''project/
├── static/            ← ایستاهای مشترک (css/base.css, img/logo.png)
├── media/             ← آپلودها (covers/2026/09/cover.jpg)
├── staticfiles/       ← خروجی collectstatic (در git نباشد)
├── blog/
│   ├── static/blog/   ← ایستاهای مخصوص اپ
│   └── templates/blog/
└── manage.py'''),
        ]),
        dict(h='۵.۳ ارجاع در قالب با {% static %}', body=[
            ('code', 'در base.html', 'html', '''{% load static %}
<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
  <link rel="stylesheet" href="{% static \'css/base.css\' %}">
</head>
<body>
  <img src="{% static \'img/logo.png\' %}" alt="لوگو" width="48">
  ...
  <script src="{% static \'js/main.js\' %}"></script>
</body>
</html>'''),
            ('callout', 'warn', 'هرگز hardcode نکنید',
             '<code class="inline-code">href="/static/css/base.css"</code> شاید امروز کار کند، ولی با تغییر STATIC_URL یا آمدن <span class="term" data-term="cdn">CDN</span> در تولید می‌شکند. همیشه تگ {% static %}.'),
        ]),
        dict(h='۵.۴ آپلود کاربر: ImageField', body=[
            ('code', 'مدل', 'python', '''class Post(models.Model):
    ...
    cover = models.ImageField(upload_to="covers/%Y/%m/", blank=True, null=True)
    attachment = models.FileField(upload_to="files/%Y/%m/", blank=True, null=True)'''),
            ('code', 'فرم و ویو', 'python', '''class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "body", "cover")


def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)   # ← FILES!
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect("blog:list")
    ...'''),
            ('code', 'قالب فرم و نمایش', 'html', '''<form method="post" enctype="multipart/form-data">
  {% csrf_token %}
  {{ form.as_p }}
  <button>انتشار</button>
</form>

{# نمایش کاور #}
{% if post.cover %}
  <img src="{{ post.cover.url }}" alt="{{ post.title }}" width="600">
{% endif %}'''),
            '<p>نکات: <code class="inline-code">upload_to</code> با %Y/%m پوشه‌بندی زمانی می‌سازد؛ <code class="inline-code">.url</code> نشانی سرو فایل است؛ ImageField نوع/ابعاد را با Pillow بررسی می‌کند (validators مثل FileExtensionValidator هم دارید).</p>',
        ]),
        dict(h='۵.۵ سرو Media در توسعه و collectstatic', body=[
            ('code', 'config/urls.py — فقط برای DEBUG', 'python', '''from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [...]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)'''),
            ('code', 'آماده‌سازی تولید', 'bash', '''python manage.py collectstatic
# 142 static files copied to '/srv/project/staticfiles'.'''),
            ('callout', 'info', 'در تولید چه می‌شود؟',
             'فصل ۲۶: Nginx فایل‌های staticfiles/ و media/ را مستقیم (و سریع) سرو می‌کند یا WhiteNoise کار ایستاها را به‌عهده می‌گیرد. جمع‌آوری با collectstatic، تحویل با وب‌سرور — جنگو در حلقه نیست.'),
        ]),
    ],
    example_intro='کاور پست با پیش‌نمایش زنده و پاک‌سازی — یک مثال کامل آپلود:',
    example=[
        ('code', 'مدل با متد پاک‌سازی', 'python', '''class Post(models.Model):
    title = models.CharField(max_length=200)
    cover = models.ImageField(upload_to="covers/%Y/%m/", blank=True)

    def delete(self, *args, **kwargs):
        if self.cover:
            self.cover.delete(save=False)     # فایل هم پاک شود
        super().delete(*args, **kwargs)'''),
        ('code', 'پیش‌نمایش زنده با جاوااسکریپت ساده', 'html', '''<input type="file" name="cover" id="id_cover" accept="image/*">
<img id="preview" hidden width="200">
<script>
  id_cover.addEventListener("change", (e) => {
    const file = e.target.files[0];
    if (file) {
      preview.src = URL.createObjectURL(file);
      preview.hidden = false;
    }
  });
</script>'''),
        ('code', 'اعتبارسنجی سمت سرور', 'python', '''from django.core.exceptions import ValidationError


def validate_cover(image):
    if image.size > 5 * 1024 * 1024:          # حداکثر ۵ مگابایت
        raise ValidationError("حجم تصویر حداکثر ۵ مگابایت باشد.")


cover = models.ImageField(upload_to="covers/%Y/%m/",
                          validators=[validate_cover], blank=True)'''),
    ],
    workshop_intro='ظاهر و رسانه وبلاگ را کامل کنید:',
    workshop_tasks=[
        '<strong>کارگاه ۱:</strong> پوشه static ریشه را بسازید، یک base.css با استایل ساده (رنگ هدر، کارت‌ها) بنویسید و با {% static %} به base.html وصل کنید.',
        '<strong>کارگاه ۲:</strong> فیلد cover (ImageField) را به Post اضافه کنید؛ فرم، ویو و نمایش را کامل کنید و enctype را از یاد نبرید.',
        '<strong>کارگاه ۳:</strong> آواتار را به Profile (فصل ۱۲) اضافه کنید و در navbar تصویر کوچک کاربر واردشده را نشان دهید.',
    ],
    workshop_answers=[
        ('پاسخ کارگاه ۱',
         '<div class="code-box"><div class="code-head"><span>static/css/base.css</span><span class="lang">CSS</span></div><pre class="code"><code data-lang="text">body { font-family: Vazirmatn, Tahoma, sans-serif; background: #f8fafc; }\nheader.site { background: #0f172a; color: #fff; padding: 12px 20px; }\n.card { background: #fff; border-radius: 12px; padding: 16px; margin: 12px 0;\n        box-shadow: 0 2px 8px rgba(0,0,0,.08); }</code></pre></div>'
         '<p>در <span class="term" data-term="settings">settings</span>: STATICFILES_DIRS = [BASE_DIR / "static"] و در base.html: <code class="inline-code">{% load static %}</code> + <code class="inline-code">&lt;link rel="stylesheet" href="{% static \'css/base.css\' %}"&gt;</code>.</p>'),
        ('پاسخ کارگاه ۲',
         '<p>① مدل: <code class="inline-code">cover = ImageField(upload_to="covers/%Y/%m/", blank=True)</code> + makemigrations/migrate (و pip install pillow). ② PostForm: افزودن "cover" به fields. ③ ویو: <code class="inline-code">PostForm(request.POST, request.FILES)</code>. ④ قالب فرم: <code class="inline-code">enctype="multipart/form-data"</code>. ⑤ نمایش: <code class="inline-code">{{ post.cover.url }}</code> با شرط {% if post.cover %}. ⑥ urls: الگوی static() در DEBUG.</p>'),
        ('پاسخ کارگاه ۳',
         '<div class="code-box"><div class="code-head"><span>navbar با آواتار</span><span class="lang">HTML</span></div><pre class="code"><code data-lang="html">{% if user.is_authenticated %}\n  {% if user.profile.avatar %}\n    &lt;img src="{{ user.profile.avatar.url }}" width="28" height="28"\n         style="border-radius:50%" alt="آواتار"&gt;\n  {% endif %}\n  {{ user.username }}\n{% endif %}</code></pre></div>'
         '<p>avatar در Profile: <code class="inline-code">ImageField(upload_to="avatars/", blank=True)</code>. فرم پروفایل هم request.FILES می‌خواهد.</p>'),
    ],
    errors=[
        ('فایل CSS 404 می‌شود',
         'چک کنید: ① {% load static %} بالای قالب ② مسیر دقیقاً مطابق پوشه (static/css/base.css ← {% static "css/base.css" %}) ③ STATICFILES_DIRS درست ④ سرور restart شده.'),
        ('تصویر آپلود شد ولی نمایش داده نمی‌شود',
         'الگوی سرو MEDIA در urls نیست (مفهوم ۵.۵ فقط در DEBUG لازم است) یا MEDIA_ROOT/MEDIA_URL اشتباه است. {{ post.cover.url }} باید چیزی مثل /media/covers/2026/09/x.jpg بدهد.'),
        ('فرم فایل، فایل را ارسال نمی‌کند',
         'enctype="multipart/form-data" روی تگ form نیست یا request.FILES به فرم پاس نشده. هر دو لازم‌اند!'),
        ('خطای ImportError: cannot import name \'PIL\'',
         'Pillow نصب نیست: pip install pillow (داخل venv). ImageField بدون Pillow کار نمی‌کند.'),
        ('بعد از collectstatic، فایل‌های قدیمی نمایش داده می‌شوند',
         'کش مرورگر/CDN. در تولید حرفه‌ای از ManifestStaticFilesStorage استفاده می‌شود که به نام فایل hash اضافه می‌کند (فصل ۲۶/۲۷).'),
    ],
    errors_callout=None,
    exercises=[
        ('تمرین ۱ — طبقه‌بندی',
         '<p><strong>سوال:</strong> هر مورد ایستا است یا رسانه؟ (الف) لوگوی سایت (ب) عکس محصول که فروشنده آپلود کرده (ج) فونت وزیر (د) فایل رزومه کاربر (ه) main.js</p>'
         '<p><strong>پاسخ:</strong> الف، ج، ه → Static (بخش کد) • ب، د → Media (آپلود کاربر).</p>'),
        ('تمرین ۲ — مسیر upload_to',
         '<p><strong>سوال:</strong> با <code class="inline-code">upload_to="covers/%Y/%m/"</code> فایلی در مهر ۱۴۰۵ (≈ 2026/09) آپلود می‌شود؛ مسیر کاملش چیست؟</p>'
         '<p><strong>پاسخ:</strong> <code class="inline-code">MEDIA_ROOT/covers/2026/09/&lt;name&gt;.jpg</code> و URLش <code class="inline-code">/media/covers/2026/09/&lt;name&gt;.jpg</code>. پوشه‌بندی زمانی از انباشته شدن هزاران فایل در یک پوشه جلوگیری می‌کند.</p>'),
        ('تمرین ۳ — نقش STATIC_ROOT',
         '<p><strong>سوال:</strong> چرا در توسعه هیچ‌وقت فایل‌ها را دستی در STATIC_ROOT نمی‌گذاریم؟</p>'
         '<p><strong>پاسخ:</strong> چون STATIC_ROOT فقط «مقصد جمع‌آوری» collectstatic برای تولید است؛ هر فایلی آنجا باید از STATICFILES_DIRS یا app/static آمده باشد. دستی گذاشتن = با اولین collectstatic پاک/بازنویسی شدن یا ناهمگامی محیط‌ها.</p>'),
    ],
    quiz=[
        dict(q='کدام جفت درباره تفاوت Static و Media درست است؟',
             opts=['Static = آپلود کاربر؛ Media = فایل کد', 'Static = فایل‌های خود پروژه؛ Media = آپلودهای کاربران',
                   'هر دو یکی‌اند', 'Static فقط برای CSS است'],
             ans='b', explain='ایستا بخشی از کد و دیپلوی است؛ رسانه دادهٔ زمان اجراست و پشتیبان‌گیری جدا می‌خواهد.'),
        dict(q='برای ارجاع به فایل ایستا در قالب از چه استفاده می‌کنیم؟',
             opts=['{{ "css/x.css" }}', '{% static "css/x.css" %} با {% load static %}',
                   '/static/css/x.css دستی', '{% media "css/x.css" %}'],
             ans='b', explain='تگ static با STATIC_URL و در آینده CDN/manifest سازگار است؛ hardcode شکننده است.'),
        dict(q='فرم آپلود فایل به کدام دو چیز نیاز دارد؟',
             opts=['method="get" و csrf', 'enctype="multipart/form-data" و request.FILES در ویو',
                   'فقط input type=file', 'JSON و fetch'],
             ans='b', explain='بدون enctype، مرورگر فایل را نمی‌فرستد؛ بدون request.FILES، جنگو آن را به فرم نمی‌دهد.'),
        dict(q='کار collectstatic چیست؟',
             opts=['آپلودها را پاک می‌کند', 'همه فایل‌های ایستا را در STATIC_ROOT جمع می‌کند (برای تولید)',
                   'فایل‌ها را فشرده می‌کند', 'مدیا را به ایستا تبدیل می‌کند'],
             ans='b', explain='خروجی یک پوشه واحد است که Nginx/CDN/WhiteNoise بتواند یک‌جا سرو کند؛ معمولاً بخشی از اسکریپت دیپلوی است.'),
        dict(q='ImageField برای کار به چه بسته‌ای نیاز دارد؟',
             opts=['requests', 'Pillow', 'celery', 'redis'],
             ans='b', explain='Pillow کتابخانه پردازش تصویر پایتون است؛ بدون آن ImageField هنگام اعتبارسنجی خطا می‌دهد.'),
        dict(q='سرو URLهای /media/ در محیط توسعه با چیست؟',
             opts=['خودکار مثل static', 'الگوی static(MEDIA_URL, document_root=MEDIA_ROOT) در urls وقتی DEBUG=True',
                   'Nginx', 'collectstatic'],
             ans='b', explain='جنگو در توسعه فقط ایستاها را خودکار سرو می‌کند؛ برای رسانه باید دستی الگو اضافه کنیم (و در تولید حذف است).'),
    ],
    project_title='وبلاگ تصویری',
    project_intro='وبلاگ را با کاور، آواتار و ظاهر مرتب کامل کنید.',
    project_checklist=[
        'static ریشه + base.css + لوگو با {% static %}.',
        'Post.cover با پوشه‌بندی %Y/%m، پیش‌نمایش زنده و اعتبارسنج حجم ≤۵MB.',
        'Profile.avatar و نمایش در navbar و صفحه نویسنده.',
        'پاک‌سازی: با حذف پست، فایل کاور هم حذف شود.',
        'اجرای collectstatic و بررسی پوشه staticfiles.',
    ],
    project_callout=None,
    summary_items=[
        'Static = فایل‌های کد (CSS/JS/تصویر خودمان)؛ Media = آپلود کاربران.',
        'STATICFILES_DIRS منبع توسعه، STATIC_ROOT مقصد تولید، {% static %} ارجاع قالب.',
        'ImageField/FileField + Pillow + upload_to پوشه‌دار.',
        'فرم آپلود: enctype + request.FILES — هر دو.',
        'collectstatic برای تولید؛ سرو واقعی با Nginx/WhiteNoise/CDN (فصل ۲۶).',
    ],
    golden='ایستا با کد دیپلوی می‌شود، رسانه با داده پشتیبان‌گیری — این دو خط را هرگز قاطی نکنید.',
    faq=[
        ('media را هم collectstatic جمع می‌کند؟',
         '<p>خیر! فقط static. رسانه‌ها زمان اجرا تولید می‌شوند و مسیر سرو جدا دارند؛ در تولید، پشتیبان‌گیری دوره‌ای از MEDIA_ROOT (یا آپلود مستقیم به فضای ابری/S3) لازم است.</p>'),
        ('آپلود مستقیم به S3/آروان‌کلادری بهتر نیست؟',
         '<p>برای تولید جدی بله: django-storages فایل‌ها را مستقیم به فضای ابری می‌فرستد و با CDN سرو می‌شوند. برای یادگیری و پروژه کوچک، دیسک سرور کافی است.</p>'),
        ('چطور از آپلود فایل مخرب جلوگیری کنم؟',
         '<p>محدودیت پسوند (FileExtensionValidator)، بررسی نوع واقعی (content_type و ابعاد با Pillow)، حجم مجاز، و ذخیره بیرون از ریشه وب. هیچ‌وقت اجازه اجرای اسکریپت از MEDIA_ROOT ندهید.</p>'),
    ],
    next_step='داده‌ها زیاد می‌شوند و کوئری‌ها پیچیده. در <strong>فصل ۱۵</strong> قدرت کامل <span class="term" data-term="queryset">QuerySet</span>ها را آزاد می‌کنیم: Q، F، aggregate/annotate و حل مشکل N+1.',
),

# ================================================================ فصل ۱۵
dict(
    n=15, icon='🔍', title='مدیریت پیشرفته پایگاه داده — QuerySetها', cat=3, mins=105, lvl_label='متوسط',
    hero_desc='<span class="term" data-term="queryset">QuerySet</span>های حرفه‌ای: filter و exclude، <span class="term" data-term="q-object">شیء Q</span>، order_by، برش، <span class="term" data-term="aggregate">aggregate</span> و <span class="term" data-term="annotate">annotate</span>، select_related و prefetch_related و حل مشکل <span class="term" data-term="n-plus-one">N+1</span>.',
    s1_intro='تفاوت یک توسعه‌دهنده جنگوی معمولی و حرفه‌ای، اغلب در تسلط بر QuerySetهاست. در این فصل از filter ساده به کوئری‌های آماری، ترکیبی و بهینه می‌رسیم.',
    objectives=[
        'Lookups (icontains, gte, in, range و پیمایش رابطه با __) را مسلط شوید.',
        'شرط‌های OR/NOT را با <span class="term" data-term="q-object">Q</span> بسازید.',
        'با <span class="term" data-term="aggregate">aggregate</span> آمار و با <span class="term" data-term="annotate">annotate</span> ستون محاسباتی بسازید.',
        'مشکل <span class="term" data-term="n-plus-one">N+1</span> را تشخیص و با <span class="term" data-term="select-related">select_related</span>/<span class="term" data-term="prefetch-related">prefetch_related</span> حل کنید.',
        'از تنبلی QuerySet و کش نتایج آگاهانه استفاده کنید.',
    ],
    s1_position='<strong>جایگاه فصل:</strong> پایهٔ فصل ۱۹ (کش)، ۲۷ (کارایی) و همه پروژه‌های داده‌محور. مهم‌ترین فصل «عمق فنی» دوره.',
    roadmap=[
        ('فیلتر پیشرفته', 'lookups و Q.'),
        ('آمار و محاسبه', 'aggregate/annotate/F.'),
        ('مشکل N+1', '<span class="term" data-term="select-related">select_related</span> و <span class="term" data-term="prefetch-related">prefetch_related</span>.'),
        ('تنبلی و الگوها', 'ارزیابی، کش و متدهای مفید.'),
    ],
    mind_qs=[
        ('<code class="inline-code">Post.objects.filter(x)</code> فوراً به دیتابیس می‌رود؟',
         '<p>نه — QuerySet <strong>تنبل (Lazy)</strong> است. اولین «ارزیابی» (حلقه، len، ایندکس، list، if) کوئری را اجرا می‌کند و نتیجه <strong>کش</strong> می‌شود؛ ارزیابی دوم دیگر به دیتابیس نمی‌رود.</p>'),
        ('تفاوت select_related و prefetch_related چیست؟',
         '<p><span class="term" data-term="select-related">select_related</span> با <strong>SQL JOIN</strong> رابطه‌های «یک» (FK/O2O) را در همان کوئری می‌آورد. <span class="term" data-term="prefetch-related">prefetch_related</span> برای «چند» (M2M و معکوس FK) است: یک کوئری جدا می‌زند و در پایتون به هم وصل می‌کند. هر دو N+1 را می‌کشند!</p>'),
        ('<code class="inline-code">.count()</code> یا <code class="inline-code">len(qs)</code>؟',
         '<p>اگر فقط تعداد لازم است: <code class="inline-code">count()</code> → SQL <code class="inline-code">SELECT COUNT(*)</code> سبک. <code class="inline-code">len()</code> همه رکوردها را به حافظه می‌آورد (سنگین) — مگر اینکه QuerySet قبلاً ارزیابی و کش شده باشد.</p>'),
    ],
    prereq_intro='پیش‌نیازها:',
    prereq=[
        'مدل‌های Post/Author/Tag/Comment با داده نمونه (<strong>حداقل ۲۰-۳۰ رکورد</strong> تا تفاوت‌ها حس شود).',
        'فصل ۴: روابط و دسترسی معکوس (related_name).',
        '<span class="term" data-term="django-shell">شل جنگو</span> باز باشد — این فصل کاملاً آزمایشگاهی است!',
        'برای دیدن SQL: تنظیم LOGGING (در ۵.۵ نشان می‌دهیم) یا DEBUG=True.',
    ],
    prereq_callout=None,
    concepts=[
        dict(h='۵.۱ Lookups: زبان فیلتر جنگو', body=[
            ('code', 'انواع lookup', 'python', '''Post.objects.filter(title__icontains="django")     # LIKE %django%
Post.objects.filter(views_count__gte=100)          # >= 100
Post.objects.filter(views_count__lt=10)            # < 10
Post.objects.filter(id__in=[1, 2, 3])              # IN (...)
Post.objects.filter(created_at__range=(d1, d2))    # BETWEEN
Post.objects.filter(created_at__year=2026)         # بخش تاریخ
Post.objects.filter(author__name="سارا")           # پیمایش رابطه (دو زیرخط)
Post.objects.filter(author__name__startswith="س")  # ترکیبی!
Post.objects.exclude(published=False)              # معکوس
Post.objects.filter(tags__isnull=True)             # بدون برچسب'''),
            ('code', 'ترکیب AND و زنجیره', 'python', '''# همه شرایط AND هستند:
Post.objects.filter(published=True, author__name="سارا")
# زنجیره هم AND است:
Post.objects.filter(published=True).filter(views_count__gt=50)'''),
        ]),
        dict(h='۵.۲ شیء Q: شرط‌های OR و NOT', body=[
            ('code', 'کار با Q', 'python', '''from django.db.models import Q

# OR: عنوان یا متن شامل "django"
Post.objects.filter(
    Q(title__icontains="django") | Q(body__icontains="django")
)

# ترکیب پیچیده: منتشرشده AND (مال سارا OR پربازدید)
Post.objects.filter(
    Q(published=True),
    Q(author__name="سارا") | Q(views_count__gte=1000),
)

# NOT:
Post.objects.filter(~Q(author__name="سارا"))'''),
            ('code', 'جست‌وجوی چندفیلدی واقعی', 'python', '''def search(q):
    query = Q()
    for term in q.split():
        query |= Q(title__icontains=term) | Q(body__icontains=term)
    return Post.objects.filter(query, published=True)'''),
        ]),
        dict(h='۵.۳ aggregate و annotate: آمار و ستون محاسباتی', body=[
            ('code', 'aggregate — یک آمار برای کل مجموعه', 'python', '''from django.db.models import Avg, Count, Max, Sum

Post.objects.aggregate(
    total=Count("id"),
    avg_views=Avg("views_count"),
    max_views=Max("views_count"),
)
# → {"total": 42, "avg_views": 133.5, "max_views": 980}'''),
            ('code', 'annotate — یک ستون به ازای هر رکورد', 'python', '''authors = Author.objects.annotate(
    post_count=Count("posts"),
    total_views=Sum("posts__views_count"),
).order_by("-post_count")

for a in authors:
    print(a.name, a.post_count, a.total_views)   # همه در یک کوئری!

# فیلتر روی ستون محاسباتی:
Author.objects.annotate(pc=Count("posts")).filter(pc__gte=5)'''),
            ('callout', 'info', ' تفاوت کلیدی',
             'aggregate یک دیکشنری برمی‌گرداند (خودش ارزیابی می‌شود)؛ annotate یک QuerySet با فیلد(های) اضافه — هنوز تنبل و قابل فیلتر/مرتب‌سازی.'),
        ]),
        dict(h='۵.۴ مشکل N+1 و دو سلاح آن', body=[
            ('code', 'سناریوی کلاسیک N+1', 'python', '''# ۱ کوئری برای پست‌ها + N کوئری برای author هر پست!
for post in Post.objects.all():
    print(post.title, post.author.name)'''),
            ('code', 'حل با select_related (رابطه‌های «یک»)', 'python', '''posts = Post.objects.select_related("author")      # JOIN در همان کوئری
for post in posts:
    print(post.title, post.author.name)            # صفر کوئری اضافه

# زنجیره‌ای و چندتایی:
Comment.objects.select_related("post__author")'''),
            ('code', 'حل با prefetch_related (رابطه‌های «چند»)', 'python', '''posts = Post.objects.prefetch_related("tags", "comments")
for post in posts:
    for tag in post.tags.all():        # بدون کوئری اضافه
        ...
    post.comments.count()              # از کش prefetch (با care)

# prefetch با کوئری سفارشی:
from django.db.models import Prefetch
Post.objects.prefetch_related(
    Prefetch("comments", queryset=Comment.objects.filter(approved=True))
)'''),
            ('code', 'شمارش کوئری‌ها برای اثبات', 'python', '''from django.db import connection, reset_queries
from django.conf import settings

settings.DEBUG = True
reset_queries()
list(Post.objects.select_related("author"))
print(len(connection.queries))     # → 1'''),
        ]),
        dict(h='۵.۵ تنبلی، ارزیابی و الگوهای مفید', body=[
            ('code', 'چه وقتی ارزیابی می‌شود؟', 'python', '''qs = Post.objects.filter(published=True)   # هنوز کوئری نرفته!

list(qs)        # ارزیابی ۱: SELECT اجرا و نتیجه کش شد
len(qs)         # از کش — کوئری جدید نیست
for p in qs:    # از کش
qs[0]           # ارزیابی (LIMIT 1)
bool(qs)        # ارزیابی (EXISTS بهینه)
qs.exists()     # سبک‌ترین بررسی وجود
qs.count()      # SELECT COUNT(*)'''),
            ('code', 'متدهای کاربردی دیگر', 'python', '''Post.objects.filter(...).order_by("-created_at")[:10]   # ۱۰ آخر
Post.objects.values("title", "author__name")            # دیکشنری‌ها
Post.objects.values_list("id", "title", flat=False)     # تاپل‌ها
Post.objects.only("id", "title")                        # ستون‌های مشخص
Post.objects.update(published=False)                    # به‌روزرسانی دسته‌ای (بدون save و سیگنال!)
Post.objects.filter(x).distinct()
Post.objects.filter(x).first() / .last()                # None اگر خالی'''),
            ('callout', 'warn', 'update() و سیگنال‌ها',
             '<code class="inline-code">queryset.update(...)</code> سریع است (یک کوئری UPDATE) ولی <code class="inline-code">save()</code> صدا نمی‌زند؛ پس <span class="term" data-term="signal">سیگنال</span> post_save اجرا نمی‌شود و متدهای سفارشی مدل هم. آگاهانه انتخاب کنید.'),
        ]),
    ],
    example_intro='داشبورد آماری وبلاگ — ترکیب همهٔ ابزارهای فصل در یک ویو:',
    example=[
        ('code', 'ویوی آمار', 'python', '''from django.db.models import Avg, Count, Q, Sum
from django.shortcuts import render

from .models import Author, Post, Tag


def stats_dashboard(request):
    totals = Post.objects.aggregate(
        posts=Count("id"),
        published=Count("id", filter=Q(published=True)),
        avg_views=Avg("views_count"),
    )

    top_authors = Author.objects.annotate(
        post_count=Count("posts"),
        views=Sum("posts__views_count"),
    ).order_by("-views")[:5]

    top_tags = Tag.objects.annotate(
        n=Count("posts", filter=Q(posts__published=True))
    ).filter(n__gt=0).order_by("-n")[:8]

    popular = (Post.objects.filter(published=True)
               .select_related("author")
               .prefetch_related("tags")
               .order_by("-views_count")[:10])

    return render(request, "blog/stats.html", {
        "totals": totals, "top_authors": top_authors,
        "top_tags": top_tags, "popular": popular,
    })'''),
        '<p>دقت کنید: <code class="inline-code">Count("id", filter=Q(...))</code> یعنی «شمارش مشروط» — ویژگی قدرتمندی که خیلی‌ها نمی‌شناسند. کل داشبورد با <strong>۴ کوئری</strong> اجرا می‌شود.</p>',
    ],
    workshop_intro='کوئری‌های یک فروشگاه را بنویسید:',
    workshop_tasks=[
        '<strong>کارگاه ۱:</strong> محصولات گران‌تر از ۵۰۰ هزار تومان از ناشر/دسته «X» که موجودی‌شان تمام نشده — با یک فیلتر ترکیبی.',
        '<strong>کارگاه ۲:</strong> برای هر دسته: نام، تعداد کتاب و میانگین قیمت — با annotate و مرتب‌سازی بر اساس تعداد.',
        '<strong>کارگاه ۳:</strong> صفحه فهرست کتاب‌ها را با select_related("publisher") و prefetch_related("tags") بهینه کنید و قبل/بعد را با شمارش کوئری مقایسه کنید.',
    ],
    workshop_answers=[
        ('پاسخ کارگاه ۱',
         '<div class="code-box"><div class="code-head"><span>فیلتر ترکیبی</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">Book.objects.filter(\n    price__gt=500_000,\n    category__slug="x",\n    stock__gt=0,\n)</code></pre></div>'
         '<p>اگر شرط OR لازم بود (مثلاً دسته x یا y): <code class="inline-code">Q(category__slug="x") | Q(category__slug="y")</code> یا ساده‌تر <code class="inline-code">category__slug__in=["x","y"]</code>.</p>'),
        ('پاسخ کارگاه ۲',
         '<div class="code-box"><div class="code-head"><span>آمار دسته‌ها</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">from django.db.models import Avg, Count\n\nCategory.objects.annotate(\n    book_count=Count("books"),\n    avg_price=Avg("books__price"),\n).order_by("-book_count")</code></pre></div>'
         '<p>در قالب: <code class="inline-code">{{ cat.book_count }}</code> و <code class="inline-code">{{ cat.avg_price|floatformat:0 }}</code>.</p>'),
        ('پاسخ کارگاه ۳',
         '<div class="code-box"><div class="code-head"><span>بهینه‌سازی و اندازه‌گیری</span><span class="lang">Python</span></div><pre class="code"><code data-lang="python">from django.db import connection, reset_queries\n\nqs = Book.objects.select_related("publisher").prefetch_related("tags")\nreset_queries()\nfor b in qs:\n    _ = b.publisher.name\n    _ = [t.name for t in b.tags.all()]\nprint(len(connection.queries))\n# قبل از بهینه‌سازی با ۲۰ کتاب: ~۴۱ کوئری (1 + 20 publisher + 20 tags)\n# بعد: ۲ کوئری (یکی کتاب‌ها+JOIN ناشر، یکی تگ‌ها)</code></pre></div>'),
    ],
    errors=[
        ('صفحه با ۵۰ رکورد، ۱۰۱ کوئری می‌زند!',
         'کلاسیک <span class="term" data-term="n-plus-one">N+1</span>: در حلقه به post.author یا post.tags.all() دسترسی دارید. select_related/prefetch_related اضافه کنید و با شمارش کوئری اثباتش کنید.'),
        ('annotate + values + COUNT نتایج عجیب می‌دهد',
         'JOIN با چند M2M هم‌زمان باعث ضرب کارتزین در شمارش می‌شود. راه‌حل: Count("x", distinct=True) یا جدا کردن annotateها در زیرکوئری (Subquery).'),
        ('کوئری کش‌شده داده قدیمی نشان می‌دهد',
         'QuerySet ارزیابی‌شده نتیجه را کش می‌کند؛ اگر داده عوض شد، QuerySet جدید بسازید (filter روی QuerySet کپی جدید می‌دهد — ولی list کش‌شده همان می‌ماند).'),
        ('order_by روی فیلد annotate خطا می‌دهد یا ترتیب غلط است',
         'نام annotate باید دقیق باشد و قبل از order_by تعریف شده باشد. در Meta.ordering هم اگر ستون annotate لازم دارید، در کوئری annotate‌اش کنید.'),
        ('update() سیگنال post_save را اجرا نکرد',
         'رفتار طراحی‌شده است: update() کوئری مستقیم SQL است. اگر منطق وابسته به save دارید (سیگنال/متد)، حلقه با save() یا بازطراحی منطق.'),
    ],
    errors_callout=None,
    exercises=[
        ('تمرین ۱ — ترجمه به ORM',
         '<p><strong>سوال:</strong> «پست‌های منتشرشدهٔ نویسنده‌ای که نامش با «س» شروع می‌شود، به‌ترتیب بازدید نزولی، ۵ تای اول» را با ORM بنویسید.</p>'
         '<p><strong>پاسخ:</strong> <code class="inline-code">Post.objects.filter(published=True, author__name__startswith="س").order_by("-views_count")[:5]</code></p>'),
        ('تمرین ۲ — Q بسازید',
         '<p><strong>سوال:</strong> «پست‌هایی که یا ویژه‌اند (featured=True) یا بیش از ۱۰۰۰ بازدید دارند، ولی منتشرنشده نباشند».</p>'
         '<p><strong>پاسخ:</strong> <code class="inline-code">Post.objects.filter(Q(featured=True) | Q(views_count__gt=1000), published=True)</code></p>'),
        ('تمرین ۳ — select یا prefetch؟',
         '<p><strong>سوال:</strong> برای هر دسترسی کدام بهینه‌ساز؟ (الف) post.author (ب) post.tags.all() (ج) post.comments.all() (د) comment.post</p>'
         '<p><strong>پاسخ:</strong> الف → select_related("author") • ب → prefetch_related("tags") (M2M) • ج → prefetch_related("comments") (معکوس FK = «چند») • د → select_related("post") (FK = «یک»).</p>'),
    ],
    quiz=[
        dict(q='QuerySet «تنبل» یعنی چه؟',
             opts=['کند اجرا می‌شود', 'تا وقتی لازم نشود (ارزیابی) کوئری به دیتابیس نمی‌فرستد',
                   'نتایج را همیشه کش می‌کند', 'فقط یک‌بار مصرف است'],
             ans='b', explain='ساخت QuerySet رایگان است؛ اولین ارزیابی (حلقه/len/list/...) SQL را اجرا و نتیجه را کش می‌کند.'),
        dict(q='کدام عبارت شرط OR را می‌سازد؟',
             opts=['filter(a=1, b=2)', 'filter(Q(a=1) | Q(b=2))',
                   'filter(a=1).or(b=2)', 'filter([a=1, b=2])'],
             ans='b', explain='آرگومان‌های filter با هم AND هستند؛ OR با عملگر | روی شیء‌های Q ساخته می‌شود.'),
        dict(q='برای «تعداد پست هر نویسنده» از چه استفاده می‌کنیم؟',
             opts=['aggregate(Count("posts"))', 'Author.objects.annotate(post_count=Count("posts"))',
                   'len(author.posts)', 'Count.objects.filter(...)'],
             ans='b', explain='annotate به ازای هر رکورد یک ستون محاسباتی می‌سازد؛ aggregate یک آمار کلی برمی‌گرداند.'),
        dict(q='مشکل N+1 در کدام حالت رخ می‌دهد؟',
             opts=['وقتی ۱۰۱ فیلد داریم', 'یک کوئری فهرست + یک کوئری به ازای هر رکورد برای رابطه‌اش',
                   'وقتی paginate_by زیاد است', 'وقتی DEBUG=True است'],
             ans='b', explain='دسترسی به رابطه در حلقه بدون بهینه‌ساز؛ راه‌حل select_related (JOIN) یا prefetch_related (کوئری جدا + وصل در پایتون).'),
        dict(q='select_related برای کدام روابط مناسب است؟',
             opts=['ManyToMany', 'ForeignKey و OneToOne (سمت «یک»)',
                   'همه روابط', 'فقط معکوس FK'],
             ans='b', explain='select_related با SQL JOIN کار می‌کند و JOIN فقط برای روابط تک‌مقداری معنا دارد؛ «چند»ها با prefetch.'),
        dict(q='کدام برای «فقط تعداد» بهینه‌تر است؟',
             opts=['len(qs)', 'qs.count()', 'list(qs).length', 'qs.aggregate(n=Count("id"))["n"] — فرقی ندارد'],
             ans='b', explain='count() یک SELECT COUNT(*) سبک می‌زند؛ len() همه سطرها را به حافظه می‌آورد. (aggregate هم مثل count است ولی رایج‌تر count() است.)'),
    ],
    project_title='گزارش‌ساز وبلاگ',
    project_intro='یک صفحه گزارش کامل با کوئری‌های بهینه بسازید.',
    project_checklist=[
        'کارت‌های آماری: کل پست‌ها، منتشرشده‌ها، میانگین/جمع بازدیدها (یک aggregate).',
        'جدول ۵ نویسنده برتر با annotate (تعداد پست + جمع بازدید).',
        'فهرست ۱۰ پست محبوب با <span class="term" data-term="select-related">select_related</span> + <span class="term" data-term="prefetch-related">prefetch_related</span>.',
        'جست‌وجوی چندکلمه‌ای با Q (کارگاه فصل).',
        'اثبات بهینگی: شمارش کوئری‌های صفحه ≤ ۵ (با connection.queries یا Debug Toolbar فصل ۲۱).',
    ],
    project_callout=('tip', 'عادت حرفه‌ای',
        'هر صفحه فهرستی که می‌سازید، یک سوال از خودتان بپرسید: «در حلقه به کدام رابطه‌ها دسترسی دارم؟» — همان‌ها را select/prefetch کنید.'),
    summary_items=[
        'Lookups با دو زیرخط: icontains، gte، in، range، year و پیمایش رابطه.',
        'Q برای OR/NOT و جست‌وجوی چندفیلدی؛ آرگومان‌های filter با هم AND.',
        'aggregate = آمار کلی؛ annotate = ستون به ازای رکورد؛ شمارش مشروط با filter=Q().',
        '<span class="term" data-term="n-plus-one">N+1</span> با select_related (یک) و prefetch_related (چند) حل می‌شود.',
        'QuerySet تنبل و کش‌شونده است؛ count/exists/only/values ابزارهای سبک‌سازی.',
    ],
    golden='هر صفحه باید با انگشتان یک دست کوئری بخورد؛ بیشتر از آن یعنی N+1 جایی کمین کرده.',
    faq=[
        ('چطور SQL تولیدشده را ببینم؟',
         '<p>با DEBUG=True: <code class="inline-code">print(qs.query)</code> (تقریبی) یا <code class="inline-code">connection.queries</code> (واقعی). ابزار حرفه‌ای: Django Debug Toolbar در فصل ۲۱.</p>'),
        ('Manager سفارشی چیست؟',
         '<p>کلاسی از models.Manager که متدهای کوئری پرکاربرد را در خود بسته‌بندی می‌کند: <code class="inline-code">Post.objects.published()</code> به‌جای تکرار filter(published=True). با QuerySet سفارشی + <code class="inline-code">objects = PublishedManager.from_queryset(PostQuerySet)()</code> بهترین الگو است.</p>'),
        ('برای جست‌وجوی جدی (مثل گوگل) ORM کافی است؟',
         '<p>تا چند ده هزار رکورد با icontains + ایندکس قابل قبول است. فراتر: جست‌وجوی تمام‌متن خود دیتابیس (SearchVector در PostgreSQL) یا Elasticsearch/Meilisearch. فصل ۲۷ ابزارهای اندازه‌گیری را می‌دهد.</p>'),
    ],
    next_step='تا اینجا «کنش» نوشتیم؛ در <strong>فصل ۱۶</strong> «واکنش» را یاد می‌گیریم: <span class="term" data-term="signal">سیگنال</span>ها — اجرای خودکار کد وقتی رویدادی (مثل ذخیره رکورد) رخ می‌دهد.',
),
]
