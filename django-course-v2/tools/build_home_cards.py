# -*- coding: utf-8 -*-
"""
تولید خودکار کارت فصل‌های صفحه اصلی از داده واقعی دوره.

منبع حقیقت: tools/data_chapters.py (که خودش از data_a تا data_f می‌خواند)
به‌علاوه فصل ۱ که دست‌نویس است و داده‌اش در CARD_ONE آمده.

خروجی: _cards_fragment.html  — بعداً داخل index.html جای‌گذاری می‌شود.
اجرا:  cd tools && python3 build_home_cards.py
"""

import re

import data_chapters as dc

CATS = [
    (1, "🧱 مبانی و اصول پایه", "از صفر شروع کنید؛ این ۶ فصل پایه‌های جنگو است."),
    (2, "📐 ساختار و Views", "مسیریابی، ویوها، قالب‌ها، فرم‌ها و کاربران."),
    (3, "⚡ پیشرفته‌ها و ابزارها", "مجوزها، فایل‌ها، QuerySet پیشرفته، سیگنال‌ها، میان‌افزار و نشست."),
    (4, "🎨 بهینه‌سازی و API", "کش، تست، اشکال‌زدایی و ساخت API حرفه‌ای."),
    (5, "🚀 استقرار و پروژه‌های عملی", "زبان‌سازی، استقرار، کارایی و پروژه‌های واقعی."),
]

# lvl_label فارسی → کلاس و برچسب نمایشی
LEVEL = {
    "صفر مطلق": 'lvl-0">🎓 صفر مطلق',
    "مبتدی":    'lvl-1">🎓 مبتدی',
    "متوسط":    'lvl-2">🎓 متوسط',
    "پیشرفته":  'lvl-3">🎓 پیشرفته',
}

# فصل ۱ دست‌نویس است؛ توصیف و کلیدواژه‌های جست‌وجویش اینجا نگهداری می‌شود
CARD_ONE = dict(
    n=1, cat=1, icon="🌱", title="آشنایی با جنگو", mins=75, lvl_label="صفر مطلق",
    desc=("وب و HTTP چیست؟ چرا فریم‌ورک؟ معماری MTV، تاریخچه جنگو، تفاوت با Flask "
          "و معرفی کامل اکوسیستم آن — بدون نیاز به هیچ پیش‌نیازی."),
    keywords="django چیست, mtv, mvc, flask, فریمورک وب, http, python, معماری, اکوسیستم",
)

# کلیدواژه‌های جست‌وجوی فصل‌های ۲ تا ۳۰ (بیرون از توصیف، برای جست‌وجوی بهتر)
KEYWORDS = {
    2:  "نصب django, venv, pip, runserver, manage.py, شروع پروژه, محیط مجازی, ترمینال",
    3:  "startapp, installed_apps, اپلیکیشن, views, urls, پروژه, ساختار",
    4:  "models, orm, sqlite, فیلدها, foreignkey, manytomany, دیتابیس, __str__, شل",
    5:  "migration, makemigrations, migrate, showmigrations, sqlmigrate, بازگشت, مهاجرت",
    6:  "admin, createsuperuser, list_display, list_filter, search_fields, پنل مدیریت, ابرکاربر",
    7:  "urls, path, re_path, include, namespace, reverse, مسیریابی, converter, routing",
    8:  "views, fbv, httpresponse, render, redirect, get_object_or_404, context, request, jsonresponse",
    9:  "cbv, listview, detailview, templateview, createview, as_view, class based views, get_context_data",
    10: "template, extends, block, include, filter, tag, base.html, xss, موتور قالب",
    11: "forms, modelform, widget, clean, as_p, csrf, اعتبارسنجی, validation, فرم",
    12: "user, login, logout, authentication, login_required, usercreationform, پروفایل, ثبت نام, احراز هویت",
    13: "group, permission, permission_required, مجوز, دسترسی, امنیت, perms, authorization",
    14: "static, media, collectstatic, filefield, imagefield, آپلود فایل, فایل استاتیک, static_url",
    15: "queryset, filter, exclude, q objects, aggregate, annotate, select_related, prefetch_related, n+1, f expression",
    16: "signal, post_save, pre_save, receiver, m2m_changed, رویداد, سیگنال",
    17: "middleware, میان افزار, request response, لاگینگ, امنیت, زنجیره درخواست",
    18: "session, cookie, request.session, سبد خرید, نشست, کوکی, امنیت نشست",
    19: "cache, redis, cache_page, کش, بهینه سازی, invalidate, بک اند کش",
    20: "test, testcase, testclient, tdd, assert, setup, تست نویسی, آزمون خودکار",
    21: "debug, logging, pdb, debug toolbar, خطا, اشکال زدایی, دیباگ, traceback",
    22: "drf, rest, api, serializer, apiview, json, rest framework, modelserializer, endpoint",
    23: "viewset, router, jwt, token, throttling, permissions, filtering, authentication, drf پیشرفته, openapi",
    24: "celery, redis, task, beat, ایمیل, async, کار زمان بندی, broker, worker, ناهمگام",
    25: "i18n, l10n, ترجمه, translate, blocktranslate, makemessages, چند زبانه, بومی سازی, فارسی سازی, jdatetime",
    26: "deployment, gunicorn, nginx, docker, استقرار, allowed_hosts, whitenoise, environment, vps, debug, https, certbot",
    27: "performance, بهینه سازی, index, n+1, select_related, prefetch_related, cdn, سرعت سایت, پایش, gzip",
    28: "htmx, react, vue, tailwind, frontend, فرانت اند, api frontend, django react, cors, spa",
    29: "django 5.2, django 6.0, ارتقا, upgrade, lts, ویژگی های جدید, template partials, tasks, csp",
    30: "پروژه عملی, پروژه نهایی, وبلاگ, فروشگاه, مدیریت وظایف, بازار کار, رزومه, دیپلوی",
}


def to_fa(v):
    return str(v).translate(str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹"))


def strip_terms(html):
    """تگ‌های واژه‌نامه و سایر تگ‌ها را از توصیف حذف می‌کند تا متن ساده بماند."""
    text = re.sub(r"<span class=\"term\"[^>]*>", "", html)
    text = re.sub(r"</span>", "", text)
    text = re.sub(r"<[^>]+>", "", text)
    return re.sub(r"\s+", " ", text).strip()


def card(n, cat, icon, title, mins, lvl_label, desc, keywords):
    cid = "ch-%02d" % n
    search = " ".join([title, desc, keywords]).lower()
    return (
        '<a class="card" data-cat="%d" data-id="%s" data-search="%s" '
        'href="chapters/chapter-%02d/index.html">'
        '<span class="done-mark" data-id="%s"></span>'
        '<h3><span class="ico">%s</span> %s</h3>'
        '<p class="dsc">%s</p>'
        '<div class="card-meta"><span class="pill time">⏱ %s دقیقه</span>'
        '<span class="pill %s</span>'
        '<span class="quiz-badge" data-quiz-for="%s"></span></div>'
        '</a>'
    ) % (cat, cid, search, n, cid, icon, title, desc,
         to_fa(mins), LEVEL[lvl_label], cid)


def build_rows():
    rows = []
    rows.append((
        CARD_ONE["n"], CARD_ONE["cat"], CARD_ONE["icon"], CARD_ONE["title"],
        CARD_ONE["mins"], CARD_ONE["lvl_label"], CARD_ONE["desc"], CARD_ONE["keywords"],
    ))
    for ch in dc.ALL:
        desc = strip_terms(ch["hero_desc"])
        rows.append((
            ch["n"], ch["cat"], ch["icon"], ch["title"], ch["mins"],
            ch["lvl_label"], desc, KEYWORDS.get(ch["n"], ""),
        ))
    return rows


def main():
    rows = build_rows()
    parts = []
    for cat, title, desc in CATS:
        inner = "".join(card(*r) for r in rows if r[1] == cat)
        parts.append(
            '<div class="cat-wrap"><h3 class="cat-title cat-head" id="cat%d">%s</h3>'
            '<p class="cat-desc">%s</p><div class="grid">%s</div></div>'
            % (cat, title, desc, inner)
        )

    fragment = "".join(parts)
    with open("_cards_fragment.html", "w", encoding="utf-8") as f:
        f.write(fragment)

    assert len(rows) == 30, len(rows)
    assert fragment.count('class="card"') == 30
    assert "data-demo" not in fragment
    print("cards:", len(rows), "cats:", len(CATS), "→ _cards_fragment.html")


if __name__ == "__main__":
    main()
