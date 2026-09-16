# -*- coding: utf-8 -*-
"""
تولیدکننده خودکار فصل‌های دوره (۲ تا ۳۰) از داده‌های ساختاریافته
الگو: دقیقاً همان قالب دستی فصل ۱ (۱۶ بخش کامل)
اجرا:  python3 tools/build_chapters.py
"""
import html as H
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))

FA = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")
def fa(v): return str(v).translate(FA)

CAT_NAMES = {
    1: "🧱 مبانی و اصول پایه",
    2: "📐 ساختار و Views",
    3: "⚡ پیشرفته‌ها و ابزارها",
    4: "🎨 بهینه‌سازی و API",
    5: "🚀 استقرار و پروژه‌های عملی",
}

def esc(s): return H.escape(s, quote=False)

def code_box(title, lang, code):
    lang_map = {'python': 'Python', 'bash': 'Bash', 'html': 'HTML', 'text': 'متن', 'json': 'JSON'}
    return (
        '<div class="code-box">\n'
        '          <div class="code-head"><span>' + title + '</span><span class="lang">' + lang_map.get(lang, lang) + '</span></div>\n'
        '          <pre class="code"><code data-lang="' + lang + '">' + esc(code.strip('\n')) + '</code></pre>\n'
        '        </div>'
    )

def callout(kind, title, body):
    icons = {'tip': '💡', 'info': '📌', 'warn': '⚠️', 'danger': '🚨'}
    return ('<div class="callout ' + kind + '">\n'
            '          <b class="title">' + icons.get(kind, '') + ' ' + title + '</b>\n'
            '          ' + body + '\n        </div>')

def chunks_html(chunks, indent='          '):
    """هر chunk یا رشته HTML خام است یا تاپل ('code', title, lang, code) یا ('callout', kind, title, body)"""
    out = []
    for c in chunks:
        if isinstance(c, str):
            out.append(c)
        elif c[0] == 'code':
            out.append(code_box(c[1], c[2], c[3]))
        elif c[0] == 'callout':
            out.append(callout(c[1], c[2], c[3]))
        else:
            raise ValueError('chunk ناشناخته: %r' % (c,))
    return ('\n' + indent).join(out)

def details_answer(summary, body):
    return ('<details class="answer">\n'
            '          <summary>' + summary + '</summary>\n'
            '          <div class="answer-body">' + body + '</div>\n'
            '        </details>')

def build(ch):
    n = ch['n']
    cid = 'ch-%02d' % n
    nxt_n, prev_n = n + 1, n - 1

    # ---------- پیمایش ----------
    if prev_n >= 1:
        prev_html = ('<a class="pager-item prev" id="prev-chap" href="../chapter-%02d/index.html">→ فصل قبلی<br><b>%s فصل %s</b></a>'
                     % (prev_n, ch.get('prev_icon', '📗'), fa(prev_n)))
    else:
        prev_html = '<span class="pager-item prev disabled">→ فصل قبلی<br><b>شروع دوره هستید</b></span>'
    if nxt_n <= 30:
        next_html = ('<a class="pager-item next" id="next-chap" href="../chapter-%02d/index.html">فصل بعدی ←<br><b>%s فصل %s: %s</b></a>'
                     % (nxt_n, ch['next_icon'], fa(nxt_n), ch['next_title']))
    else:
        next_html = '<span class="pager-item next disabled">فصل بعدی ←<br><b>🏆 پایان دوره — آفرین!</b></span>'

    # ---------- بخش ۵: مفاهیم ----------
    concepts = []
    for sub in ch['concepts']:
        concepts.append('        <h3>' + sub['h'] + '</h3>\n' + chunks_html(sub['body']))
    concepts_html = '\n\n'.join(concepts)

    # ---------- بخش ۱۱: آزمون ----------
    quiz_qs = []
    for i, q in enumerate(ch['quiz'], 1):
        opts = ''.join(
            '              <button type="button" class="quiz-opt" data-key="%s">%s</button>\n' % (k, o)
            for k, o in zip('abcd', q['opts'])
        )
        quiz_qs.append(
            '          <div class="quiz-q" data-answer="%s">\n'
            '            <h4 class="quiz-q-text">%s) %s</h4>\n'
            '            <div class="quiz-opts">\n%s            </div>\n'
            '            <div class="quiz-explain">💡 %s</div>\n'
            '          </div>' % (q['ans'], fa(i), q['q'], opts, q['explain'])
        )
    quiz_html = '\n\n'.join(quiz_qs)

    toc = ''.join(
        '        <li><a href="#p%d"><span class="toc-n">%s</span> %s</a></li>\n' % (i, fa(i), t)
        for i, t in enumerate([
            'چشم‌انداز فصل', 'نقشه راه فصل', 'سوالات محرک ذهنی', 'آماده‌سازی و پیش‌نیازها',
            'آموزش گام‌به‌گام: مفاهیم', 'مثال عملی', 'کارگاه عملی', 'پاسخ کامل کارگاه ✅',
            'خطاهای رایج', 'تمرین‌های تثبیت', 'آزمون تعاملی فصل 📝', 'پروژه عملی فصل',
            'جمع‌بندی و دستاوردها', 'سوالات متداول و گام بعدی', 'واژه‌نامه تخصصی فصل 📖',
            'یادداشت‌های من 📓'], 1)
    )

    page = TEMPLATE
    repl = {
        '@@N@@': fa(n),
        '@@ICON@@': ch['icon'],
        '@@TITLE@@': ch['title'],
        '@@CAT@@': CAT_NAMES[ch['cat']],
        '@@MINS@@': fa(ch['mins']),
        '@@LVL@@': ch['lvl_label'],
        '@@QUIZ_COUNT@@': fa(len(ch['quiz'])),
        '@@CID@@': cid,
        '@@HERO_DESC@@': ch['hero_desc'],
        '@@S1_INTRO@@': ch['s1_intro'],
        '@@S1_OBJECTIVES@@': ''.join('<li>%s</li>\n          ' % o for o in ch['objectives']),
        '@@S1_POSITION@@': ch['s1_position'],
        '@@ROADMAP@@': road_steps(ch['roadmap']),
        '@@MIND_QS@@': '\n        '.join(details_answer('🤔 ' + q, a) for q, a in ch['mind_qs']),
        '@@PREREQ_INTRO@@': ch['prereq_intro'],
        '@@PREREQ@@': ''.join('<li>%s</li>\n          ' % p for p in ch['prereq']),
        '@@PREREQ_CALLOUT@@': callout(*ch['prereq_callout']) if ch.get('prereq_callout') else '',
        '@@CONCEPTS@@': concepts_html,
        '@@EXAMPLE_INTRO@@': ch['example_intro'],
        '@@EXAMPLE@@': chunks_html(ch['example']),
        '@@WORKSHOP_INTRO@@': ch['workshop_intro'],
        '@@WORKSHOP@@': ''.join('<li>%s</li>\n          ' % t for t in ch['workshop_tasks']),
        '@@WORKSHOP_ANSWERS@@': '\n        '.join(details_answer('✅ ' + s, b) for s, b in ch['workshop_answers']),
        '@@ERRORS_INTRO@@': ch.get('errors_intro', 'اشتباهات و خطاهای رایج این فصل را بشناسید تا سریع‌تر رفعشان کنید:'),
        '@@ERRORS@@': '\n        '.join(
            '<div class="err-card">\n          <b class="err-title">❌ %s</b>\n          <p>%s</p>\n        </div>' % (t, b)
            for t, b in ch['errors']),
        '@@ERRORS_CALLOUT@@': callout(*ch['errors_callout']) if ch.get('errors_callout') else '',
        '@@EXERCISES@@': '\n        '.join(details_answer('🏋️ ' + s, b) for s, b in ch['exercises']),
        '@@QUIZ_INTRO@@': ch.get('quiz_intro',
            'پرسش‌های چهارگزینه‌ای زیر را پاسخ دهید؛ بلافاصله بعد از انتخاب، پاسخ درست و توضیحش را می‌بینید. حد نصاب قبولی <strong>۶۰٪</strong> است و بهترین نمره‌تان ذخیره می‌شود.'),
        '@@QUIZ@@': quiz_html,
        '@@PROJECT_TITLE@@': ch['project_title'],
        '@@PROJECT_INTRO@@': ch['project_intro'],
        '@@PROJECT_CHECKLIST@@': ''.join('<li>%s</li>\n          ' % c for c in ch['project_checklist']),
        '@@PROJECT_CALLOUT@@': callout(*ch['project_callout']) if ch.get('project_callout') else '',
        '@@SUMMARY_ITEMS@@': ''.join('<li>%s</li>\n          ' % s for s in ch['summary_items']),
        '@@SUMMARY_GOLDEN@@': callout('tip', '✨ یک‌جمله‌ای که باید یادتان بماند', '«' + ch['golden'] + '»'),
        '@@FAQ@@': '\n        '.join(
            '<details class="faq-item"><summary>%s</summary><div class="faq-body">%s</div></details>' % (q, a)
            for q, a in ch['faq']),
        '@@NEXT_STEP@@': callout('info', '🧭 گام بعدی', ch['next_step']),
        '@@PREV@@': prev_html,
        '@@NEXT@@': next_html,
        '@@TOC@@': toc,
    }
    for k, v in repl.items():
        page = page.replace(k, v)
    return page

def road_steps(steps):
    out = []
    for i, (title, desc) in enumerate(steps):
        arrow = '<span class="arrow">←</span>' if i < len(steps) - 1 else ''
        out.append('<div class="step"><span class="badge">گام %s</span><h4>%s</h4><p>%s</p>%s</div>'
                   % (fa(i + 1), title, desc, arrow))
    return '\n          '.join(out)

TEMPLATE = '''<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>فصل @@N@@: @@TITLE@@ | دوره جامع جنگو (Django)</title>
<meta name="description" content="فصل @@N@@ دوره جامع جنگو: @@TITLE@@ — با واژه‌نامه هاور، آزمون تعاملی نمره‌دار، کارگاه عملی با پاسخ و یادداشت شخصی.">
<link rel="stylesheet" href="../../assets/css/style.css">
<script>
  (function(){try{var t=localStorage.getItem('djc_theme_v1');if(!t){t=(window.matchMedia&&window.matchMedia('(prefers-color-scheme: dark)').matches)?'dark':'light';}document.documentElement.setAttribute('data-theme',t);var f=localStorage.getItem('djc_font_v1');if(f)document.documentElement.setAttribute('data-font',f);}catch(e){}})();
</script>
</head>
<body data-page="chapter">
<div id="reading-bar"></div>
<a class="skip-link" href="#p1">پرش به محتوای فصل</a>

<header class="site-header">
  <div class="container topbar">
    <a class="brand" href="../../index.html">🌿 دوره جامع جنگو</a>
    <nav class="nav-links" aria-label="ناوبری اصلی">
      <a href="../../index.html">خانه</a>
      <a href="../../index.html#chapters">فصل‌ها</a>
      <a href="../../glossary.html">واژه‌نامه جامع</a>
      <a href="#p11">آزمون فصل</a>
      <a href="#p15">واژه‌نامه فصل</a>
    </nav>
    <div class="header-tools">
      <button type="button" class="tool-btn" data-theme-toggle aria-label="تغییر حالت روشن/تاریک">🌙</button>
      <button type="button" class="tool-btn" data-shortcuts aria-label="میان‌برهای کیبورد" title="میان‌برهای کیبورد (؟)">⌨️</button>
    </div>
    <p class="header-chapter-title">فصل @@N@@ از ۳۰ — @@TITLE@@</p>
  </div>
</header>

<div class="container">
  <nav class="breadcrumb" aria-label="مسیر صفحه">
    <a href="../../index.html">خانه</a> ← @@CAT@@ ← فصل @@N@@
  </nav>

  <section class="chapter-hero">
    <span class="chap-num">فصل @@N@@ از ۳۰</span>
    <h1>@@ICON@@ @@TITLE@@</h1>
    <p>@@HERO_DESC@@</p>
    <div class="hero-pills">
      <span class="pill">⏱ @@MINS@@ دقیقه</span>
      <span class="pill">🎓 @@LVL@@</span>
      <span class="pill">📑 ۱۶ بخش</span>
      <span class="pill">📖 <span id="chapter-term-count">۰</span> واژه تخصصی</span>
      <span class="pill">📝 آزمون @@QUIZ_COUNT@@ پرسشی</span>
    </div>
    <div class="hero-cta">
      <a class="btn" href="#p5">▶ شروع مطالعه</a>
      <a class="btn ghost" href="#p11">📝 آزمون تعاملی فصل</a>
      <a class="btn ghost" href="#p15">📖 واژه‌نامه فصل</a>
      <a class="btn ghost" href="#p16">📓 یادداشت‌های من</a>
    </div>
  </section>

  <div class="chapter-layout">
    <main>

      <!-- ============ بخش ۱: چشم‌انداز فصل ============ -->
      <section class="part" id="p1">
        <div class="part-head"><span class="part-num">بخش ۱</span><h2>🔭 چشم‌انداز فصل: اهداف و جایگاه</h2></div>
        <p>@@S1_INTRO@@</p>
        <p><strong>اهداف یادگیری — پس از این فصل شما می‌توانید:</strong></p>
        <ul>
          @@S1_OBJECTIVES@@
        </ul>
        <p>@@S1_POSITION@@</p>
      </section>

      <!-- ============ بخش ۲: نقشه راه فصل ============ -->
      <section class="part" id="p2">
        <div class="part-head"><span class="part-num">بخش ۲</span><h2>🗺️ نقشه راه فصل</h2></div>
        <div class="road">
          @@ROADMAP@@
        </div>
      </section>

      <!-- ============ بخش ۳: سوالات محرک ذهنی ============ -->
      <section class="part" id="p3">
        <div class="part-head"><span class="part-num">بخش ۳</span><h2>🤔 سوالات محرک ذهنی</h2></div>
        <p>قبل از خواندن آموزش، چند لحظه به این سوال‌ها فکر کنید؛ حتی اگر جواب را نمی‌دانید، ذهنتان آماده دریافت آن می‌شود:</p>
        @@MIND_QS@@
      </section>

      <!-- ============ بخش ۴: آماده‌سازی و پیش‌نیازها ============ -->
      <section class="part" id="p4">
        <div class="part-head"><span class="part-num">بخش ۴</span><h2>🧰 آماده‌سازی و پیش‌نیازها</h2></div>
        <p>@@PREREQ_INTRO@@</p>
        <ul class="checklist">
          @@PREREQ@@
        </ul>
        @@PREREQ_CALLOUT@@
      </section>

      <!-- ============ بخش ۵: آموزش گام‌به‌گام مفاهیم ============ -->
      <section class="part" id="p5">
        <div class="part-head"><span class="part-num">بخش ۵</span><h2>📖 آموزش گام‌به‌گام: مفاهیم</h2></div>

@@CONCEPTS@@
      </section>

      <!-- ============ بخش ۶: مثال عملی ============ -->
      <section class="part" id="p6">
        <div class="part-head"><span class="part-num">بخش ۶</span><h2>💻 مثال عملی</h2></div>
        <p>@@EXAMPLE_INTRO@@</p>
        @@EXAMPLE@@
        <div class="callout tip"><b class="title">💡 نکته طلایی</b>کدهای بالا را <strong>خودتان تایپ و اجرا کنید</strong>؛ تایپ کردن رمز یادگیری است!</div>
      </section>

      <!-- ============ بخش ۷: کارگاه عملی ============ -->
      <section class="part" id="p7">
        <div class="part-head"><span class="part-num">بخش ۷</span><h2>🛠️ کارگاه عملی</h2></div>
        <p>@@WORKSHOP_INTRO@@</p>
        <ol>
          @@WORKSHOP@@
        </ol>
      </section>

      <!-- ============ بخش ۸: پاسخ کامل کارگاه عملی ============ -->
      <section class="part" id="p8">
        <div class="part-head"><span class="part-num">بخش ۸</span><h2>✅ پاسخ کامل کارگاه عملی</h2></div>
        @@WORKSHOP_ANSWERS@@
      </section>

      <!-- ============ بخش ۹: خطاهای رایج ============ -->
      <section class="part" id="p9">
        <div class="part-head"><span class="part-num">بخش ۹</span><h2>🐞 خطاهای رایج و رفع آن‌ها</h2></div>
        <p>@@ERRORS_INTRO@@</p>
        @@ERRORS@@
        @@ERRORS_CALLOUT@@
      </section>

      <!-- ============ بخش ۱۰: تمرین‌های تثبیت ============ -->
      <section class="part" id="p10">
        <div class="part-head"><span class="part-num">بخش ۱۰</span><h2>🏋️ تمرین‌های تثبیت</h2></div>
        <p>پاسخ‌ها را اول خودتان بنویسید، بعد باز کنید:</p>
        @@EXERCISES@@
      </section>

      <!-- ============ بخش ۱۱: آزمون تعاملی فصل ============ -->
      <section class="part" id="p11">
        <div class="part-head"><span class="part-num">بخش ۱۱</span><h2>📝 آزمون تعاملی فصل</h2></div>
        <p>@@QUIZ_INTRO@@</p>

        <div class="quiz" data-id="@@CID@@" data-title="آزمون فصل @@N@@ — @@TITLE@@" data-pass="60">

@@QUIZ@@

        </div>
      </section>

      <!-- ============ بخش ۱۲: پروژه عملی فصل ============ -->
      <section class="part" id="p12">
        <div class="part-head"><span class="part-num">بخش ۱۲</span><h2>🏗️ پروژه عملی فصل</h2></div>
        <p><strong>پروژه: «@@PROJECT_TITLE@@»</strong> — @@PROJECT_INTRO@@</p>
        <ul class="checklist">
          @@PROJECT_CHECKLIST@@
        </ul>
        @@PROJECT_CALLOUT@@
      </section>

      <!-- ============ بخش ۱۳: جمع‌بندی و دستاوردها ============ -->
      <section class="part" id="p13">
        <div class="part-head"><span class="part-num">بخش ۱۳</span><h2>🎯 جمع‌بندی و دستاوردها</h2></div>
        <p><strong>در این فصل یاد گرفتید:</strong></p>
        <ul>
          @@SUMMARY_ITEMS@@
        </ul>
        @@SUMMARY_GOLDEN@@
      </section>

      <!-- ============ بخش ۱۴: سوالات متداول و گام بعدی ============ -->
      <section class="part" id="p14">
        <div class="part-head"><span class="part-num">بخش ۱۴</span><h2>❓ سوالات متداول و گام بعدی</h2></div>
        @@FAQ@@
        <div style="margin-top:16px">@@NEXT_STEP@@</div>
      </section>

      <!-- ============ بخش ۱۵: واژه‌نامه تخصصی فصل ============ -->
      <section class="part" id="p15">
        <div class="part-head"><span class="part-num">بخش ۱۵</span><h2>📖 واژه‌نامه تخصصی فصل</h2></div>
        <p style="color:var(--muted);font-size:.88rem">
          این فهرست <strong>به‌طور خودکار</strong> از واژه‌های تخصصی به‌کاررفته در همین فصل ساخته شده است.
          روی هر کارت بزنید تا اولین کاربرد آن واژه در متن فصل پیدا و برجسته شود. برای همه واژه‌های دوره،
          <a href="../../glossary.html">واژه‌نامه جامع</a> را ببینید.
        </p>
        <div class="chapter-glossary" data-auto="true"></div>
      </section>

      <!-- ============ بخش ۱۶: یادداشت‌های من ============ -->
      <section class="part" id="p16">
        <div class="part-head"><span class="part-num">بخش ۱۶</span><h2>📓 یادداشت‌های من</h2></div>
        <p style="color:var(--muted);font-size:.88rem">نکته‌ها، پاسخ پروژه عملی و خلاصه‌های شخصی‌تان را اینجا بنویسید؛ <strong>خودکار در همین مرورگر ذخیره می‌شود</strong> و هیچ‌وقت گم نمی‌شود.</p>
        <textarea class="notes-box" data-chapter="@@CID@@" placeholder="نکته‌های شخصی این فصل را اینجا بنویسید..."></textarea>
        <div class="notes-head" style="margin-top:6px">
          <span class="notes-status">یادداشت‌ها خودکار ذخیره می‌شوند.</span>
          <span class="notes-count"></span>
          <button type="button" class="btn small ghost" data-notes-clear>🗑 پاک کردن یادداشت‌ها</button>
        </div>
      </section>

      <!-- ============ نوار پایان فصل ============ -->
      <div class="done-bar">
        <button id="mark-done" type="button" class="btn" data-chapter="@@CID@@">✔️ این فصل را تمام کردم</button>
        <span style="font-size:.82rem;color:var(--muted)">با زدن این دکمه، پیشرفت شما در داشبورد صفحه اصلی ثبت می‌شود.</span>
      </div>

      <nav class="pager" aria-label="پیمایش فصل‌ها">
        @@PREV@@
        <a class="pager-item home-btn" href="../../index.html">🏠<br><b>صفحه اصلی</b></a>
        @@NEXT@@
      </nav>
    </main>

    <!-- ============ فهرست شناور بخش‌ها ============ -->
    <aside class="toc-box" aria-label="فهرست بخش‌های فصل">
      <h4>📑 فهرست فصل <span style="font-weight:400;font-size:.75rem;color:var(--muted)">۱۶ بخش</span></h4>
      <div class="toc-tools">
        <button type="button" id="btn-open-answers">باز کردن همه پاسخ‌ها</button>
        <button type="button" id="btn-close-answers">بستن همه پاسخ‌ها</button>
      </div>
      <ol class="toc-list">
@@TOC@@      </ol>
    </aside>
  </div>
</div>

<footer class="site-footer">
  <div class="container">
    <div class="copyright">© ۱۴۰۵ — دوره جامع جنگو — فصل @@N@@: @@TITLE@@ | <a href="../../index.html">بازگشت به صفحه اصلی</a> • <a href="../../glossary.html">واژه‌نامه جامع</a></div>
  </div>
</footer>

<div class="toolbar" aria-label="ابزارهای نمایش">
  <button type="button" class="tool-btn" data-theme-toggle title="حالت تاریک/روشن">🌙</button>
  <button type="button" class="tool-btn" data-font-plus title="بزرگ‌تر کردن متن">＋</button>
  <button type="button" class="tool-btn" data-font-minus title="کوچک‌تر کردن متن">－</button>
  <button type="button" class="tool-btn" onclick="window.print()" title="چاپ فصل">🖨️</button>
  <button type="button" class="tool-btn" data-shortcuts title="میان‌برهای کیبورد">⌨️</button>
</div>
<button id="toTop" type="button" title="بازگشت به بالا" aria-label="بازگشت به بالا">⬆</button>
<div id="toast-wrap" aria-live="polite"></div>

<div class="modal" id="shortcuts-modal" hidden>
  <div class="modal-box" role="dialog" aria-modal="true" aria-label="میان‌برهای کیبورد">
    <h3>⌨️ میان‌برهای کیبورد</h3>
    <div class="shortcut-row"><span>نمایش/بستن همین راهنما</span><kbd>?</kbd></div>
    <div class="shortcut-row"><span>تغییر حالت تاریک/روشن</span><kbd>D</kbd></div>
    <div class="shortcut-row"><span>فصل بعدی</span><kbd>←</kbd></div>
    <div class="shortcut-row"><span>فصل قبلی</span><kbd>→</kbd></div>
    <div class="shortcut-row"><span>بستن پنجره‌ها و تولتیپ واژه</span><kbd>Esc</kbd></div>
    <button type="button" class="btn" data-close-modal style="width:100%;margin-top:14px">بستن</button>
  </div>
</div>

<script src="../../assets/js/util.js"></script>
<script src="../../assets/js/glossary-data.js"></script>
<script src="../../assets/js/glossary.js"></script>
<script src="../../assets/js/quiz.js"></script>
<script src="../../assets/js/app.js"></script>
</body>
</html>
'''

def validate(ch, glossary_keys):
    """کنترل کیفیت: کلید واژه‌ها، ساختار داده، تعداد پرسش‌ها"""
    errs = []
    n = ch['n']
    text = build(ch)
    for k in set(re.findall(r'data-term="([^"]+)"', text)):
        if k not in glossary_keys:
            errs.append('فصل %d: واژه «%s» در دیکشنری نیست' % (n, k))
    if len(ch['quiz']) < 6:
        errs.append('فصل %d: آزمون کمتر از ۶ پرسش دارد' % n)
    for i, q in enumerate(ch['quiz'], 1):
        if len(q['opts']) != 4 or q['ans'] not in 'abcd':
            errs.append('فصل %d پرسش %d: گزینه‌ها/پاسخ نامعتبر' % (n, i))
    for key in ('workshop_tasks', 'workshop_answers', 'errors', 'exercises', 'faq',
                'summary_items', 'objectives', 'prereq', 'project_checklist', 'roadmap', 'mind_qs'):
        if not ch.get(key):
            errs.append('فصل %d: بخش %s خالی است' % (n, key))
    leftover = re.findall(r'@@[A-Z0-9_]+@@', text)
    if leftover:
        errs.append('فصل %d: جای‌گذاری‌های پرنشده %s' % (n, set(leftover)))
    return errs, text

def main():
    gdata = open(os.path.join(ROOT, 'assets/js/glossary-data.js'), encoding='utf-8').read()
    glossary_keys = set(re.findall(r"^\s*'([\w-]+)':\s*\{", gdata, re.M))

    from data_chapters import ALL
    all_errs = []
    made = []
    for ch in sorted(ALL, key=lambda c: c['n']):
        errs, text = validate(ch, glossary_keys)
        all_errs += errs
        if not errs:
            d = os.path.join(ROOT, 'chapters', 'chapter-%02d' % ch['n'])
            os.makedirs(d, exist_ok=True)
            with open(os.path.join(d, 'index.html'), 'w', encoding='utf-8') as f:
                f.write(text)
            made.append(ch['n'])
    if all_errs:
        print('❌ خطاها:')
        for e in all_errs:
            print('  -', e)
        sys.exit(1)
    print('✅ ساخته شد:', len(made), 'فصل →', made)

if __name__ == '__main__':
    main()
