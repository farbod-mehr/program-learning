/* ============================================================
   دوره جامع Django — موتور واژه‌نامه (glossary.js)
   ------------------------------------------------------------
   سه وظیفه:
   ۱) نشانه‌گذاری خودکار: هر <span class="term" data-term="..."> در متن
      با هاور (دسکتاپ) یا لمس/کلیک (موبایل) یک تولتیپ فارسی نشان می‌دهد:
      واژه انگلیسی + ترجمه + توضیح + لینک به واژه‌نامه.
   ۲) ساخت خودکار «واژه‌نامه فصل» در انتهای هر فصل:
      <div class="chapter-glossary" data-auto="true"></div>
      → همه واژه‌های به‌کاررفته در همان فصل را کارت‌کارتی فهرست می‌کند
        همراه با جست‌وجوی زنده.
   ۳) پر کردن صفحه «واژه‌نامه جامع»:
      <div id="glossary-all"></div> → همه واژه‌ها بر اساس دسته‌بندی + جست‌وجو.
   ============================================================ */
(function () {
  'use strict';
  if (!window.DJC) return;
  var G = window.DJC_GLOSSARY || {};
  var esc = DJC.escapeHtml, toFa = DJC.toFa;

  /* ---------- ۱) تولتیپ هاور/لمس ---------- */
  var tip = null, hideTimer = null, showTimer = null, currentTarget = null;

  function ensureTip() {
    if (tip) return tip;
    tip = document.createElement('div');
    tip.id = 'djc-tooltip';
    tip.setAttribute('role', 'tooltip');
    tip.setAttribute('aria-hidden', 'true');
    document.body.appendChild(tip);
    return tip;
  }

  function tipHtml(key) {
    var t = G[key];
    if (!t) return '';
    return '' +
      '<div class="tip-head">' +
        '<span class="tip-en" dir="ltr">' + esc(t.en) + '</span>' +
        '<span class="tip-cat">' + esc(t.cat) + '</span>' +
      '</div>' +
      '<div class="tip-fa">' + esc(t.fa) + '</div>' +
      '<div class="tip-desc">' + esc(t.desc) + '</div>' +
      '<div class="tip-foot">' +
        '<a href="#p15" class="tip-link" data-goto="chapter">📖 واژه‌نامهٔ همین فصل</a>' +
        '<a href="' + chapterRelative('glossary.html') + '" class="tip-link" data-goto="full">🌐 واژه‌نامهٔ جامع دوره</a>' +
      '</div>';
  }

  /* مسیر نسبی بسته به اینکه در صفحه اصلی هستیم یا داخل فصل */
  function chapterRelative(path) {
    var inChapter = document.body.getAttribute('data-page') === 'chapter';
    return inChapter ? '../../' + path : path;
  }

  function showTip(target) {
    var key = target.getAttribute('data-term');
    if (!key || !G[key]) return;
    var el = ensureTip();
    el.innerHTML = tipHtml(key);
    el.classList.add('show');
    el.setAttribute('aria-hidden', 'false');
    currentTarget = target;
    positionTip(target);
  }

  function positionTip(target) {
    var el = ensureTip();
    var r = target.getBoundingClientRect();
    var tw = el.offsetWidth, th = el.offsetHeight;
    var pad = 10;
    /* جای افقی: وسط واژه، با مهار در لبه‌های صفحه */
    var left = r.left + r.width / 2 - tw / 2;
    left = Math.max(pad, Math.min(left, window.innerWidth - tw - pad));
    /* جای عمودی: ترجیحاً زیر واژه، وگرنه بالای آن */
    var top = r.bottom + window.scrollY + 10;
    if (r.bottom + th + 20 > window.innerHeight) {
      top = r.top + window.scrollY - th - 10;
    }
    el.style.left = left + 'px';
    el.style.top = top + 'px';
    /* پیکان تولتیپ را زیر خودِ واژه نگه می‌دارد */
    var arrowX = r.left + r.width / 2 - left;
    el.style.setProperty('--arrow-x', arrowX + 'px');
  }

  function hideTip() {
    if (!tip) return;
    tip.classList.remove('show');
    tip.setAttribute('aria-hidden', 'true');
    currentTarget = null;
  }

  function scheduleShow(target) {
    clearTimeout(hideTimer);
    clearTimeout(showTimer);
    showTimer = setTimeout(function () { showTip(target); }, 140);
  }

  function scheduleHide() {
    clearTimeout(showTimer);
    hideTimer = setTimeout(hideTip, 220);
  }

  function bindTerms() {
    var terms = document.querySelectorAll('.term[data-term]');
    terms.forEach(function (el, i) {
      if (el.__djcBound) return;
      el.__djcBound = true;
      if (!G[el.getAttribute('data-term')]) {
        el.classList.add('term-unknown');
        return;
      }
      el.classList.add('term-ready');
      el.setAttribute('tabindex', '0');
      el.setAttribute('aria-describedby', 'djc-tooltip');
      /* دسکتاپ: هاور */
      el.addEventListener('mouseenter', function () { scheduleShow(el); });
      el.addEventListener('mouseleave', scheduleHide);
      /* دسترسی‌پذیری: فوکوس با کیبورد */
      el.addEventListener('focus', function () { scheduleShow(el); });
      el.addEventListener('blur', scheduleHide);
      /* موبایل: لمس/کلیک → نمایش/پنهان */
      el.addEventListener('click', function (ev) {
        ev.preventDefault();
        if (currentTarget === el && tip && tip.classList.contains('show')) hideTip();
        else showTip(el);
      });
    });
    /* با کلیک بیرون یا Esc تولتیپ بسته شود */
    document.addEventListener('click', function (ev) {
      if (tip && !tip.contains(ev.target) && !ev.target.closest('.term')) hideTip();
    });
    document.addEventListener('keydown', function (ev) {
      if (ev.key === 'Escape') hideTip();
    });
    window.addEventListener('scroll', function () { if (currentTarget) positionTip(currentTarget); }, { passive: true });
    window.addEventListener('resize', function () { hideTip(); }, { passive: true });
    /* نگه‌داشتن موس روی خود تولتیپ (برای کلیک روی لینک‌هایش) */
    ensureTip().addEventListener('mouseenter', function () { clearTimeout(hideTimer); });
    ensureTip().addEventListener('mouseleave', scheduleHide);
    /* لینک واژه‌نامه فصل فقط وقتی کار می‌کند که آن بخش وجود داشته باشد */
    ensureTip().addEventListener('click', function (ev) {
      var a = ev.target.closest('a[data-goto="chapter"]');
      if (a && !document.getElementById('p15')) {
        ev.preventDefault();
        DJC.toast('این صفحه بخش واژه‌نامه فصل ندارد.');
      }
    });
    return terms.length;
  }

  /* ---------- ۲) واژه‌نامه فصل (خودکار) ---------- */
  function usedTerms() {
    var seen = {}, order = [];
    document.querySelectorAll('.term[data-term]').forEach(function (el) {
      var k = el.getAttribute('data-term');
      if (!seen[k] && G[k]) { seen[k] = true; order.push(k); }
    });
    return order;
  }

  function glossCardHtml(key) {
    var t = G[key];
    return '' +
      '<div class="gloss-card" data-key="' + esc(key) + '" data-search="' +
        esc((t.en + ' ' + t.fa + ' ' + t.cat + ' ' + t.desc).toLowerCase()) + '">' +
        '<div class="gloss-top">' +
          '<span class="gloss-en" dir="ltr">' + esc(t.en) + '</span>' +
          '<span class="gloss-cat-pill">' + esc(t.cat) + '</span>' +
        '</div>' +
        '<div class="gloss-fa">' + esc(t.fa) + '</div>' +
        '<p class="gloss-desc">' + esc(t.desc) + '</p>' +
      '</div>';
  }

  function buildChapterGlossary() {
    var box = document.querySelector('.chapter-glossary[data-auto]');
    if (!box) return;
    var keys = usedTerms();
    if (!keys.length) {
      box.innerHTML = '<p class="gloss-empty">در این فصل واژه تخصصی نشانه‌گذاری نشده است.</p>';
      return;
    }
    var html = '' +
      '<div class="gloss-toolbar">' +
        '<div class="gloss-search"><input type="search" placeholder="جست‌وجو در واژه‌نامه این فصل..." aria-label="جست‌وجوی واژه‌نامه فصل"></div>' +
        '<span class="gloss-count">' + toFa(keys.length) + ' واژه در این فصل</span>' +
      '</div>' +
      '<div class="gloss-grid">' + keys.map(glossCardHtml).join('') + '</div>' +
      '<p class="gloss-empty" style="display:none">واژه‌ای با این عبارت پیدا نشد.</p>';
    box.innerHTML = html;

    var input = box.querySelector('input');
    var cards = box.querySelectorAll('.gloss-card');
    var empty = box.querySelector('.gloss-empty');
    input.addEventListener('input', DJC.debounce(function () {
      var q = DJC.toEn(input.value).trim().toLowerCase();
      var found = 0;
      cards.forEach(function (c) {
        var ok = !q || c.getAttribute('data-search').indexOf(q) !== -1;
        c.style.display = ok ? '' : 'none';
        if (ok) found++;
      });
      empty.style.display = found ? 'none' : 'block';
    }, 120));
    /* با کلیک روی هر کارت، اولین کاربرد همان واژه در فصل پیدا و برجسته شود */
    cards.forEach(function (c) {
      c.addEventListener('click', function () {
        var k = c.getAttribute('data-key');
        var first = document.querySelector('.term[data-term="' + k + '"]');
        if (!first) return;
        first.scrollIntoView({ behavior: 'smooth', block: 'center' });
        first.classList.add('term-flash');
        setTimeout(function () { first.classList.remove('term-flash'); }, 1600);
      });
    });
  }

  /* ---------- ۳) صفحه واژه‌نامه جامع ---------- */
  function buildFullGlossary() {
    var box = document.getElementById('glossary-all');
    if (!box) return;
    var cats = {}, total = 0;
    Object.keys(G).forEach(function (k) {
      var c = G[k].cat;
      (cats[c] = cats[c] || []).push(k);
      total++;
    });
    var html = '' +
      '<div class="gloss-toolbar">' +
        '<div class="gloss-search"><input type="search" id="glossary-search" placeholder="جست‌وجو در همه واژه‌ها... (انگلیسی یا فارسی)" aria-label="جست‌وجوی واژه‌نامه جامع"></div>' +
        '<span class="gloss-count" id="glossary-count">' + toFa(total) + ' واژه</span>' +
      '</div>' +
      Object.keys(cats).map(function (cat) {
        return '<section class="gloss-cat" data-cat="' + esc(cat) + '">' +
          '<h3 class="gloss-cat-title">' + esc(cat) + ' <span class="gloss-cat-n">' + toFa(cats[cat].length) + '</span></h3>' +
          '<div class="gloss-grid">' + cats[cat].map(glossCardHtml).join('') + '</div>' +
        '</section>';
      }).join('') +
      '<p class="gloss-empty" id="glossary-empty" style="display:none">واژه‌ای با این عبارت پیدا نشد. 🔍</p>';
    box.innerHTML = html;

    var input = document.getElementById('glossary-search');
    var cards = box.querySelectorAll('.gloss-card');
    var catSections = box.querySelectorAll('.gloss-cat');
    input.addEventListener('input', DJC.debounce(function () {
      var q = DJC.toEn(input.value).trim().toLowerCase();
      var found = 0;
      cards.forEach(function (c) {
        var ok = !q || c.getAttribute('data-search').indexOf(q) !== -1;
        c.style.display = ok ? '' : 'none';
        if (ok) found++;
      });
      catSections.forEach(function (s) {
        var any = false;
        s.querySelectorAll('.gloss-card').forEach(function (c) { if (c.style.display !== 'none') any = true; });
        s.style.display = any ? '' : 'none';
      });
      document.getElementById('glossary-count').textContent =
        q ? (toFa(found) + ' واژه پیدا شد') : (toFa(Object.keys(G).length) + ' واژه');
      document.getElementById('glossary-empty').style.display = found ? 'none' : 'block';
    }, 120));
  }

  /* ---------- شمارنده واژه‌های صفحه (برای هیروی فصل) ---------- */
  function paintTermStats() {
    var el = document.getElementById('chapter-term-count');
    if (el) el.textContent = toFa(usedTerms().length);
  }

  document.addEventListener('DOMContentLoaded', function () {
    bindTerms();
    buildChapterGlossary();
    buildFullGlossary();
    paintTermStats();
  });

  window.DJC_GLOSSARY_ENGINE = { rebind: bindTerms, usedTerms: usedTerms };
})();
