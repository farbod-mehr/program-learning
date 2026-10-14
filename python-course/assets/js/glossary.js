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

/* ============================================================
   glossary.js — موتور واژه‌نامه دوره پایتون (نسخه ۳)
   ------------------------------------------------------------
   امکانات:
   ۱) تولتیپ هوشمند روی <span class="term" data-term="key">
      - نمایش: EN + دسته + FA + توضیح + مثال کد + نکته
      - پشتیبانی از هاور (دسکتاپ)، فوکوس (کیبورد)، لمس (موبایل)
   ۲) واژه‌نامه خودکار پایان فصل:
      <div class="chapter-glossary" data-auto="true"></div>
   ۳) صفحه واژه‌نامه جامع:
      <div id="glossary-all"></div>
   ۴) شمارنده واژه‌های فصل در هیرو
   ۵) به‌روزرسانی خودکار شمارنده‌های آماری (در صورت وجود)
   ============================================================ */
(function () {
  'use strict';
  if (!window.DJC) return;

  var G = window.DJC_GLOSSARY || {};
  var esc = DJC.escapeHtml;
  var toFa = DJC.toFa;
  var toEn = DJC.toEn;
  var debounce = DJC.debounce;

  /* ═══════════════════════════════════════════════════════════
     ۱) تولتیپ هاور / لمس
     ═══════════════════════════════════════════════════════════ */

  var tip = null;
  var showTimer = null;
  var hideTimer = null;
  var currentTarget = null;
  var SHOW_DELAY = 140;
  var HIDE_DELAY = 220;

  function ensureTip() {
    if (tip && tip.isConnected) return tip;
    tip = document.createElement('div');
    tip.id = 'djc-tooltip';
    tip.setAttribute('role', 'tooltip');
    tip.setAttribute('aria-hidden', 'true');
    document.body.appendChild(tip);
    return tip;
  }

  /* ساخت HTML تولتیپ از داده واژه */
  function tipHtml(key) {
    var t = G[key];
    if (!t) return '';

    var exampleBlock = t.example
      ? '<div class="tip-example">' +
          '<div class="tip-label">📝 مثال</div>' +
          '<pre dir="ltr">' + esc(t.example) + '</pre>' +
        '</div>'
      : '';

    var tipBlock = t.tip
      ? '<div class="tip-note">' +
          '<span class="tip-note-ico">💡</span>' +
          '<span>' + esc(t.tip) + '</span>' +
        '</div>'
      : '';

    var hasChapterGloss = !!document.getElementById('p15');
    var footBlock = '<div class="tip-foot">' +
      (hasChapterGloss
        ? '<a href="#p15" class="tip-link" data-goto="chapter">📖 واژه‌نامهٔ همین فصل</a>'
        : '') +
      '<a href="' + chapterRelative('glossary.html') + '" class="tip-link">🌐 واژه‌نامهٔ جامع</a>' +
    '</div>';

    return '' +
      '<div class="tip-head">' +
        '<span class="tip-en" dir="ltr">' + esc(t.en) + '</span>' +
        '<span class="tip-cat">' + esc(t.cat) + '</span>' +
      '</div>' +
      '<div class="tip-fa">' + esc(t.fa) + '</div>' +
      '<div class="tip-desc">' + esc(t.desc) + '</div>' +
      exampleBlock +
      tipBlock +
      footBlock;
  }

  /* مسیر نسبی بر اساس نوع صفحه */
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
    /* پس از رندر، موقعیت را محاسبه کن */
    requestAnimationFrame(function () {
      if (currentTarget === target) positionTip(target);
    });
  }

  function positionTip(target) {
    var el = ensureTip();
    if (!el || !target.isConnected) return;

    var r = target.getBoundingClientRect();
    var tw = el.offsetWidth;
    var th = el.offsetHeight;
    var pad = 12;
    var vw = window.innerWidth;
    var vh = window.innerHeight;

    /* جای افقی: وسط واژه، مهار در لبه‌ها */
    var left = r.left + r.width / 2 - tw / 2;
    left = Math.max(pad, Math.min(left, vw - tw - pad));

    /* جای عمودی: زیر واژه یا بالای آن */
    var top;
    if (r.bottom + th + 20 < vh) {
      top = r.bottom + window.scrollY + 12;
    } else if (r.top - th - 12 > 0) {
      top = r.top + window.scrollY - th - 12;
    } else {
      /* نه جا هست نه بالای صفحه — برو پایین */
      top = r.bottom + window.scrollY + 12;
    }

    el.style.left = left + 'px';
    el.style.top = top + 'px';

    /* پیکان زیر خود واژه */
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
    showTimer = setTimeout(function () { showTip(target); }, SHOW_DELAY);
  }

  function scheduleHide() {
    clearTimeout(showTimer);
    hideTimer = setTimeout(hideTip, HIDE_DELAY);
  }

  /* اتصال رویدادها به همه .term ها */
  function bindTerms() {
    var terms = document.querySelectorAll('.term[data-term]');
    var boundCount = 0;

    terms.forEach(function (el) {
      if (el.__djcBound) return;
      el.__djcBound = true;
      boundCount++;

      var key = el.getAttribute('data-term');
      if (!key || !G[key]) {
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
        ev.stopPropagation();
        if (currentTarget === el && tip && tip.classList.contains('show')) {
          hideTip();
        } else {
          showTip(el);
        }
      });

      /* کیبورد: Enter/Space هم کار کنه */
      el.addEventListener('keydown', function (ev) {
        if (ev.key === 'Enter' || ev.key === ' ') {
          ev.preventDefault();
          showTip(el);
        }
      });
    });

    /* فقط یک بار listenerهای سراسری را نصب کن */
    if (!bindTerms._installed) {
      bindTerms._installed = true;

      document.addEventListener('click', function (ev) {
        if (tip && !tip.contains(ev.target) && !ev.target.closest('.term')) {
          hideTip();
        }
      });

      document.addEventListener('keydown', function (ev) {
        if (ev.key === 'Escape') hideTip();
      });

      window.addEventListener('scroll', function () {
        if (currentTarget) positionTip(currentTarget);
      }, { passive: true });

      window.addEventListener('resize', function () { hideTip(); }, { passive: true });

      /* نگه‌داشتن موس روی تولتیپ برای کلیک روی لینک‌ها */
      var el = ensureTip();
      el.addEventListener('mouseenter', function () { clearTimeout(hideTimer); });
      el.addEventListener('mouseleave', scheduleHide);
    }

    return boundCount;
  }

  /* ═══════════════════════════════════════════════════════════
     ۲) واژه‌نامه فصل (خودکار)
     ═══════════════════════════════════════════════════════════ */

  function usedTerms() {
    var seen = {}, order = [];
    document.querySelectorAll('.term[data-term]').forEach(function (el) {
      var k = el.getAttribute('data-term');
      if (k && !seen[k] && G[k]) {
        seen[k] = true;
        order.push(k);
      }
    });
    return order;
  }

  /* ساخت HTML یک کارت واژه */
  function glossCardHtml(key) {
    var t = G[key];
    if (!t) return '';

    var searchText = [t.en, t.fa, t.cat, t.desc, t.example || '', t.tip || '']
      .join(' ').toLowerCase();

    var exampleBlock = t.example
      ? '<div class="gloss-example">' +
          '<span class="gloss-ex-ico">📝</span>' +
          '<pre dir="ltr">' + esc(t.example) + '</pre>' +
        '</div>'
      : '';

    var tipBlock = t.tip
      ? '<div class="gloss-note">' +
          '<span class="gloss-note-ico">💡</span>' +
          '<span>' + esc(t.tip) + '</span>' +
        '</div>'
      : '';

    return '' +
      '<div class="gloss-card" data-key="' + esc(key) + '" data-search="' + esc(searchText) + '">' +
        '<div class="gloss-top">' +
          '<span class="gloss-en" dir="ltr">' + esc(t.en) + '</span>' +
          '<span class="gloss-cat-pill">' + esc(t.cat) + '</span>' +
        '</div>' +
        '<div class="gloss-fa">' + esc(t.fa) + '</div>' +
        '<p class="gloss-desc">' + esc(t.desc) + '</p>' +
        exampleBlock +
        tipBlock +
      '</div>';
  }

  /* فیلتر کردن کارت‌ها بر اساس عبارت جست‌وجو */
  function filterCards(cards, query) {
    var q = query ? toEn(query).trim().toLowerCase() : '';
    var found = 0;
    cards.forEach(function (c) {
      var text = c.getAttribute('data-search') || '';
      var ok = !q || text.indexOf(q) !== -1;
      c.style.display = ok ? '' : 'none';
      if (ok) found++;
    });
    return found;
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
        '<div class="gloss-search">' +
          '<input type="search" placeholder="جست‌وجو در واژه‌نامه این فصل..." aria-label="جست‌وجوی واژه‌نامه فصل">' +
        '</div>' +
        '<span class="gloss-count">' + toFa(keys.length) + ' واژه در این فصل</span>' +
      '</div>' +
      '<div class="gloss-grid">' + keys.map(glossCardHtml).join('') + '</div>' +
      '<p class="gloss-empty" style="display:none">واژه‌ای با این عبارت پیدا نشد. 🔍</p>';

    box.innerHTML = html;

    var input = box.querySelector('input');
    var cards = Array.prototype.slice.call(box.querySelectorAll('.gloss-card'));
    var empty = box.querySelector('.gloss-empty');

    if (input) {
      input.addEventListener('input', debounce(function () {
        var found = filterCards(cards, input.value);
        if (empty) empty.style.display = found ? 'none' : 'block';
      }, 120));
    }

    /* کلیک روی کارت → پرش به اولین کاربرد در متن فصل */
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

  /* ═══════════════════════════════════════════════════════════
     ۳) واژه‌نامه جامع (صفحه مستقل)
     ═══════════════════════════════════════════════════════════ */

  function buildFullGlossary() {
    var box = document.getElementById('glossary-all');
    if (!box) return;

    /* گروه‌بندی بر اساس دسته */
    var cats = {};
    var total = 0;
    Object.keys(G).forEach(function (k) {
      var cat = (G[k].cat || 'سایر');
      if (!cats[cat]) cats[cat] = [];
      cats[cat].push(k);
      total++;
    });

    /* مرتب‌سازی الفبایی درون هر دسته */
    Object.keys(cats).forEach(function (cat) {
      cats[cat].sort(function (a, b) {
        return (G[a].en || '').localeCompare(G[b].en || '');
      });
    });

    var html = '' +
      '<div class="gloss-toolbar">' +
        '<div class="gloss-search">' +
          '<input type="search" id="glossary-search" ' +
            'placeholder="جست‌وجو در همه واژه‌ها... (انگلیسی یا فارسی)" ' +
            'aria-label="جست‌وجوی واژه‌نامه جامع">' +
        '</div>' +
        '<span class="gloss-count" id="glossary-count">' + toFa(total) + ' واژه</span>' +
      '</div>' +
      Object.keys(cats).map(function (cat) {
        return '<section class="gloss-cat" data-cat="' + esc(cat) + '">' +
          '<h3 class="gloss-cat-title">' +
            esc(cat) +
            ' <span class="gloss-cat-n">' + toFa(cats[cat].length) + '</span>' +
          '</h3>' +
          '<div class="gloss-grid">' + cats[cat].map(glossCardHtml).join('') + '</div>' +
        '</section>';
      }).join('') +
      '<p class="gloss-empty" id="glossary-empty" style="display:none">' +
        'واژه‌ای با این عبارت پیدا نشد. 🔍' +
      '</p>';

    box.innerHTML = html;

    var input = document.getElementById('glossary-search');
    var countEl = document.getElementById('glossary-count');
    var emptyEl = document.getElementById('glossary-empty');
    var cards = Array.prototype.slice.call(box.querySelectorAll('.gloss-card'));
    var catSections = Array.prototype.slice.call(box.querySelectorAll('.gloss-cat'));
    var totalWords = Object.keys(G).length;

    if (input) {
      input.addEventListener('input', debounce(function () {
        var q = toEn(input.value).trim().toLowerCase();
        var found = filterCards(cards, input.value);

        /* پنهان‌کردن دسته‌های خالی */
        catSections.forEach(function (s) {
          var any = false;
          var sCards = s.querySelectorAll('.gloss-card');
          for (var i = 0; i < sCards.length; i++) {
            if (sCards[i].style.display !== 'none') { any = true; break; }
          }
          s.style.display = any ? '' : 'none';
        });

        if (countEl) {
          countEl.textContent = q
            ? toFa(found) + ' واژه پیدا شد'
            : toFa(totalWords) + ' واژه';
        }
        if (emptyEl) emptyEl.style.display = found ? 'none' : 'block';
      }, 120));
    }
  }

  /* ═══════════════════════════════════════════════════════════
     ۴) شمارنده‌ها و آمار
     ═══════════════════════════════════════════════════════════ */

  function paintTermStats() {
    var el = document.getElementById('chapter-term-count');
    if (el) el.textContent = toFa(usedTerms().length);

    /* شمارنده واژه‌های صفحه واژه‌نامه جامع */
    var statWords = document.getElementById('gloss-stat-words');
    if (statWords) {
      var total = Object.keys(G).length;
      statWords.textContent = toFa(total);
    }

    /* شمارنده دسته‌ها */
    var statCats = document.getElementById('gloss-stat-cats');
    if (statCats) {
      var cats = {};
      Object.keys(G).forEach(function (k) { cats[G[k].cat] = 1; });
      statCats.textContent = toFa(Object.keys(cats).length);
    }
  }

  /* ═══════════════════════════════════════════════════════════
     ۵) راه‌اندازی اولیه
     ═══════════════════════════════════════════════════════════ */

  function init() {
    try {
      bindTerms();
      buildChapterGlossary();
      buildFullGlossary();
      paintTermStats();
    } catch (err) {
      /* شکست نرم: چیزی نباید صفحه را بشکند */
      if (window.console && console.warn) {
        console.warn('DJC Glossary init error:', err);
      }
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  /* ═══════════════════════════════════════════════════════════
     API عمومی برای استفاده سایر اسکریپت‌ها
     ═══════════════════════════════════════════════════════════ */

  window.DJC_GLOSSARY_ENGINE = {
    rebind: bindTerms,
    usedTerms: usedTerms,
    showTip: showTip,
    hideTip: hideTip
  };
})();