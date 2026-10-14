/* ============================================================
   دوره جامع پایتون — تعاملات اصلی (app.js v3)
   ------------------------------------------------------------
   این فایل باید پس از util.js بارگذاری شود.

   بخش‌ها:
   ۰) راه‌اندازی و بازیابی تنظیمات
   ۱) تم روشن/تاریک (با تشخیص خودکار)
   ۲) اندازه فونت
   ۳) نوار پیشرفت مطالعه
   ۴) رنگ‌آمیزی نحو کد (Python / Bash / HTML)
   ۵) دکمه کپی روی بلوک‌های کد
   ۶) فهرست بخش‌ها: هایلایت بخش فعال
   ۷) باز/بستن همه پاسخ‌ها
   ۸) «این فصل را تمام کردم»
   ۹) نشان نمره آزمون روی کارت فصل‌ها
   ۱۰) داشبورد یادگیری
   ۱۱) جست‌وجو و فیلتر فصل‌ها
   ۱۲) یادداشت‌های من (ذخیره خودکار)
   ۱۳) میان‌برهای کیبورد + مودال راهنما
   ۱۴) بازگشت به بالا
   ۱۵) پیمایش نرم لینک‌های داخلی
   ۱۶) راه‌اندازی نهایی
   ============================================================ */
(function () {
  'use strict';
  if (!window.DJC) return;

  /* ═══════════════════════════════════════════════════════════
     ۰) راه‌اندازی و بازیابی تنظیمات
     ═══════════════════════════════════════════════════════════ */

  var toFa = DJC.toFa;
  var qs = DJC.qs;
  var qsa = DJC.qsa;
  var log = DJC.log;

  /* ویژگی‌های محیط */
  var reduceMotion = DJC.prefersReducedMotion();
  var SCROLL_BEHAVIOR = reduceMotion ? 'auto' : 'smooth';

  /* کلاس کمکی برای انیمیشن اسکرول */
  function scrollTo(el, block) {
    if (!el) return;
    el.scrollIntoView({ behavior: SCROLL_BEHAVIOR, block: block || 'start' });
  }

  /* ═══════════════════════════════════════════════════════════
     ۱) تم روشن/تاریک
     ═══════════════════════════════════════════════════════════ */

  (function initTheme() {
    var themeBtns = qsa('[data-theme-toggle]');

    /* آیکون و tooltip دکمه‌ها را مطابق تم فعلی تنظیم کن */
    function paintIcons() {
      var dark = document.documentElement.getAttribute('data-theme') === 'dark';
      themeBtns.forEach(function (b) {
        b.textContent = dark ? '☀️' : '🌙';
        b.title = dark ? 'حالت روشن' : 'حالت تاریک';
        b.setAttribute('aria-label', b.title);
      });
    }

    /* تغییر تم با محافظت از پرش رنگ */
    function toggle() {
      var cur = document.documentElement.getAttribute('data-theme') === 'dark' ? 'dark' : 'light';
      var next = cur === 'dark' ? 'light' : 'dark';

      /* انیمیشن نرم رنگ‌ها */
      if (!reduceMotion) {
        document.documentElement.style.transition = 'background-color .25s, color .25s';
        setTimeout(function () {
          document.documentElement.style.transition = '';
        }, 300);
      }

      document.documentElement.setAttribute('data-theme', next);
      DJC.setJSON(DJC.KEYS.theme, next);
      paintIcons();
    }

    themeBtns.forEach(function (b) {
      b.addEventListener('click', toggle);
    });

    paintIcons();
  })();

  /* ═══════════════════════════════════════════════════════════
     ۲) اندازه فونت (۰=عادی ۱=بزرگ ۲=بزرگ‌تر)
     ═══════════════════════════════════════════════════════════ */

  (function initFont() {
    function getLevel() {
      var raw = DJC.getJSON(DJC.KEYS.font, 0);
      var f = parseInt(raw, 10);
      return isNaN(f) ? 0 : Math.min(2, Math.max(0, f));
    }

    function apply() {
      var f = getLevel();
      document.documentElement.setAttribute('data-font', String(f));
      qsa('[data-font-label]').forEach(function (el) {
        el.textContent = ['عادی', 'بزرگ', 'بزرگ‌تر'][f] || 'عادی';
      });
    }

    function change(delta) {
      var f = getLevel();
      f = Math.min(2, Math.max(0, f + delta));
      DJC.setJSON(DJC.KEYS.font, f);
      apply();
    }

    qsa('[data-font-plus]').forEach(function (b) {
      b.addEventListener('click', function () { change(+1); });
    });
    qsa('[data-font-minus]').forEach(function (b) {
      b.addEventListener('click', function () { change(-1); });
    });

    apply();
  })();

  /* ═══════════════════════════════════════════════════════════
     ۳) نوار پیشرفت مطالعه
     ═══════════════════════════════════════════════════════════ */

  (function initReadingBar() {
    var bar = document.getElementById('reading-bar');
    if (!bar) return;

    function update() {
      var h = document.documentElement;
      var max = h.scrollHeight - h.clientHeight;
      var pct = max > 0 ? (h.scrollTop / max) * 100 : 0;
      bar.style.width = pct + '%';
      bar.setAttribute('aria-valuenow', String(Math.round(pct)));
    }

    var throttledUpdate = DJC.throttle(update, 60);
    window.addEventListener('scroll', throttledUpdate, { passive: true });
    window.addEventListener('resize', throttledUpdate, { passive: true });
    update();
  })();

  /* ═══════════════════════════════════════════════════════════
     ۴) رنگ‌آمیزی نحو کد
     ═══════════════════════════════════════════════════════════ */

  (function initSyntaxHighlight() {
    /* --- HTML: تگ‌ها، attribute، کامنت --- */
    function highlightHtml(code) {
      return code.replace(
        /(&lt;!--[\s\S]*?--&gt;)|(&lt;\/?)([a-zA-Z][\w:-]*)((?:[^&]|&(?!gt;|lt;))*)(\/?&gt;)/g,
        function (m, cmt, open, name, attrs, close) {
          if (cmt) return '<span class="c-comment">' + cmt + '</span>';
          var a = (attrs || '').replace(
            /([a-zA-Z-:@]+)(=)(&quot;[^]*?&quot;|&#39;[^]*?&#39;|[^\s]*)/g,
            function (mm, k, eq, v) {
              return '<span class="c-num">' + k + '</span>' +
                     eq +
                     '<span class="c-str">' + v + '</span>';
            });
          return '<span class="c-kw">' + open + name + '</span>' +
                 a +
                 '<span class="c-kw">' + close + '</span>';
        }
      );
    }

    /* --- Python: کامنت، رشته، decorator، keyword، number --- */
    var PY_KEYWORDS = [
      'def', 'class', 'return', 'if', 'elif', 'else', 'for', 'while',
      'import', 'from', 'as', 'in', 'not', 'and', 'or', 'is', 'None',
      'True', 'False', 'try', 'except', 'finally', 'with', 'lambda',
      'yield', 'pass', 'break', 'continue', 'raise', 'global', 'nonlocal',
      'assert', 'del', 'async', 'await', 'self', 'cls'
    ];
    var PY_KEYWORD_RE = '\\b(' + PY_KEYWORDS.join('|') + ')\\b';
    var PY_RE = new RegExp(
      '(#[^\\n]*)' +                                    /* کامنت */
      '|("""[\\s\\S]*?"""|\'\'\'[\\s\\S]*?\'\'\'|"(?:\\\\.|[^"\\\\])*"|\'(?:\\\\.|[^\'\\\\])*\')' + /* رشته */
      '|(@\\w+)' +                                       /* decorator */
      '|\\b(' + PY_KEYWORDS.join('|') + ')\\b' +         /* keyword */
      '|\\b(\\d+(?:\\.\\d+)?)\\b',                       /* عدد */
      'g'
    );

    function highlightPython(code) {
      return code.replace(PY_RE, function (m, cm, st, dec, kw, num) {
        if (cm) return '<span class="c-comment">' + cm + '</span>';
        if (st) return '<span class="c-str">' + st + '</span>';
        if (dec) return '<span class="c-dec">' + dec + '</span>';
        if (kw) return '<span class="c-kw">' + kw + '</span>';
        if (num) return '<span class="c-num">' + num + '</span>';
        return m;
      });
    }

    /* --- Bash: کامنت، رشته، دستور، flag --- */
    var BASH_CMDS = [
      'python', 'python3', 'pip', 'pip3', 'django-admin', 'cd', 'mkdir',
      'ls', 'dir', 'source', 'deactivate', 'git', 'curl', 'wget', 'sudo',
      'apt', 'apt-get', 'brew', 'nano', 'vim', 'cat', 'echo', 'touch',
      'rm', 'cp', 'mv', 'docker', 'uvicorn', 'gunicorn', 'pytest',
      'pytest', 'ruff', 'black', 'mypy', 'poetry'
    ];
    var BASH_RE = new RegExp(
      '(#[^\\n]*)' +
      '|("(?:\\\\.|[^"\\\\])*"|\'(?:\\\\.|[^\'\\\\])*\')' +
      '|(^|\\n|\\s)(' + BASH_CMDS.join('|') + '|manage\\.py)(?=\\s|$)' +
      '|(\\s--?[\\w-]+)',
      'g'
    );

    function highlightBash(code) {
      return code.replace(BASH_RE, function (m, cm, st, pre, cmd, flag) {
        if (cm) return '<span class="c-comment">' + cm + '</span>';
        if (st) return '<span class="c-str">' + st + '</span>';
        if (cmd) return (pre || '') + '<span class="c-kw">' + cmd + '</span>';
        if (flag) return '<span class="c-num">' + flag + '</span>';
        return m;
      });
    }

    /* اعمال روی همه بلوک‌های کد */
    qsa('pre.code').forEach(function (pre) {
      var code = pre.querySelector('code');
      var target = code || pre;
      var lang = (target.getAttribute('data-lang') || '').toLowerCase();

      if (lang !== 'python' && lang !== 'bash' && lang !== 'shell' && lang !== 'html') return;

      /* اگر قبلاً رنگ‌آمیزی شده، دوباره انجام نده */
      if (target.__djcHighlighted) return;
      target.__djcHighlighted = true;

      var raw = DJC.escapeHtml(target.textContent);
      target.innerHTML =
        lang === 'python' ? highlightPython(raw) :
        lang === 'html' ? highlightHtml(raw) :
        highlightBash(raw);
    });
  })();

  /* ═══════════════════════════════════════════════════════════
     ۵) دکمه کپی روی بلوک‌های کد
     ═══════════════════════════════════════════════════════════ */

  (function initCopyButtons() {
    qsa('pre.code').forEach(function (pre) {
      var box = pre.closest('.code-box');
      if (!box) return;
      var head = box.querySelector('.code-head');
      if (!head || head.querySelector('.copy-btn')) return;

      var btn = document.createElement('button');
      btn.className = 'copy-btn';
      btn.type = 'button';
      btn.textContent = '📋 کپی کد';
      btn.setAttribute('aria-label', 'کپی کد در کلیپ‌بورد');
      head.appendChild(btn);

      btn.addEventListener('click', function () {
        var text = pre.innerText || pre.textContent;

        DJC.copy(text).then(function () {
          btn.textContent = '✅ کپی شد';
          btn.classList.add('ok');
          setTimeout(function () {
            btn.textContent = '📋 کپی کد';
            btn.classList.remove('ok');
          }, 2000);
        }).catch(function () {
          btn.textContent = '❌ خطا';
          setTimeout(function () {
            btn.textContent = '📋 کپی کد';
          }, 2000);
        });
      });
    });
  })();

  /* ═══════════════════════════════════════════════════════════
     ۶) فهرست بخش‌ها: هایلایت بخش فعال
     ═══════════════════════════════════════════════════════════ */

  (function initTocSpy() {
    var tocLinks = qsa('.toc-list a');
    if (!tocLinks.length) return;

    var partEls = tocLinks.map(function (a) {
      var id = a.getAttribute('href');
      return id && id.charAt(0) === '#' ? document.querySelector(id) : null;
    });

    var lastActive = -1;

    function updateActive() {
      var pos = window.scrollY + 140;
      var current = 0;
      for (var i = 0; i < partEls.length; i++) {
        var el = partEls[i];
        if (el && el.offsetTop <= pos) current = i;
      }
      if (current === lastActive) return;
      lastActive = current;
      tocLinks.forEach(function (a, i) {
        a.classList.toggle('active', i === current);
      });
    }

    var throttled = DJC.throttle(updateActive, 100);
    window.addEventListener('scroll', throttled, { passive: true });
    window.addEventListener('resize', throttled, { passive: true });
    updateActive();
  })();

  /* ═══════════════════════════════════════════════════════════
     ۷) باز/بستن همه پاسخ‌ها
     ═══════════════════════════════════════════════════════════ */

  (function initAnswerToggles() {
    var btnOpen = document.getElementById('btn-open-answers');
    var btnClose = document.getElementById('btn-close-answers');
    if (!btnOpen && !btnClose) return;

    function toggleAll(open) {
      var nodes = qsa('details.answer, details.faq-item');
      if (!nodes.length) return;
      nodes.forEach(function (d) { d.open = open; });
      DJC.toast(open ? 'همه پاسخ‌ها باز شد.' : 'همه پاسخ‌ها بسته شد.', open ? 'ok' : undefined);
    }

    if (btnOpen) btnOpen.addEventListener('click', function () { toggleAll(true); });
    if (btnClose) btnClose.addEventListener('click', function () { toggleAll(false); });
  })();

  /* ═══════════════════════════════════════════════════════════
     ۸) «این فصل را تمام کردم»
     ═══════════════════════════════════════════════════════════ */

  var getFinished = function () {
    return DJC.getJSON(DJC.KEYS.finished, {});
  };

  (function initDoneButton() {
    var doneBtn = document.getElementById('mark-done');

    function paintButton(id) {
      if (!doneBtn) return;
      var isDone = !!getFinished()[id];
      if (isDone) {
        doneBtn.classList.add('done');
        doneBtn.innerHTML = '✅ این فصل را تمام کرده‌اید';
      } else {
        doneBtn.classList.remove('done');
        doneBtn.innerHTML = '✔️ این فصل را تمام کردم';
      }
      doneBtn.setAttribute('aria-pressed', isDone ? 'true' : 'false');
    }

    if (!doneBtn) return;

    var chapterId = doneBtn.getAttribute('data-chapter');
    paintButton(chapterId);

    doneBtn.addEventListener('click', function () {
      if (!DJC.storageOK) {
        DJC.toast('مرورگر شما اجازه ذخیره پیشرفت را نمی‌دهد.', 'warn');
        return;
      }
      var f = getFinished();
      if (f[chapterId]) {
        delete f[chapterId];
        DJC.toast('علامت «تمام‌شده» برداشته شد.');
      } else {
        f[chapterId] = Date.now();
        DJC.toast('آفرین! فصل به‌عنوان تمام‌شده ثبت شد. 🎉', 'ok');
      }
      DJC.setJSON(DJC.KEYS.finished, f);
      paintButton(chapterId);
      paintHomeMarks();
      renderDashboard();
    });
  })();

  /* نشان‌گذاری کارت‌های فصل تمام‌شده در صفحه اصلی */
  function paintHomeMarks() {
    var marks = qsa('.card .done-mark');
    if (!marks.length) return;
    var f = getFinished();
    marks.forEach(function (m) {
      var id = m.getAttribute('data-id');
      var on = !!f[id];
      m.textContent = on ? '✔' : '';
      var card = m.closest('.card');
      if (card) card.classList.toggle('card-done', on);
    });
  }

  /* ═══════════════════════════════════════════════════════════
     ۹) نشان نمره آزمون روی کارت فصل‌ها
     ═══════════════════════════════════════════════════════════ */

  (function initQuizBadges() {
    var badges = qsa('.quiz-badge[data-quiz-for]');
    if (!badges.length) return;

    var store = DJC.getJSON(DJC.KEYS.quiz, {});
    badges.forEach(function (badge) {
      var id = badge.getAttribute('data-quiz-for');
      var rec = store[id];
      if (rec && rec.best > 0) {
        badge.textContent = '🏅 آزمون: ' + toFa(rec.best) + '٪';
        badge.classList.add('has-score', rec.best >= 60 ? 'good' : 'bad');
      } else {
        badge.textContent = '📝 آزمون تعاملی';
      }
    });
  })();

  /* ═══════════════════════════════════════════════════════════
     ۱۰) داشبورد یادگیری (صفحه اصلی)
     ═══════════════════════════════════════════════════════════ */

  function renderDashboard() {
    var wrap = document.getElementById('dashboard');
    if (!wrap) return;

    var TOTAL = (window.DJC_CONFIG && window.DJC_CONFIG.totalChapters) || 30;

    var finished = getFinished();
    var doneCount = Object.keys(finished).length;

    var quizzes = DJC.getJSON(DJC.KEYS.quiz, {});
    var quizIds = Object.keys(quizzes).filter(function (k) {
      return quizzes[k] && quizzes[k].best > 0;
    });

    var avg = 0;
    if (quizIds.length) {
      var sum = quizIds.reduce(function (s, k) { return s + quizzes[k].best; }, 0);
      avg = Math.round(sum / quizIds.length);
    }

    var termCount = Object.keys(window.DJC_GLOSSARY || {}).length;
    var pct = Math.round((doneCount / TOTAL) * 100);

    /* اعداد داشبورد */
    setText('dash-done', toFa(doneCount) + '/' + toFa(TOTAL));
    setText('dash-quizzes', toFa(quizIds.length));
    setText('dash-avg', quizIds.length ? toFa(avg) + '٪' : '—');
    setText('dash-terms', toFa(termCount));
    setText('stat-terms', '+' + toFa(termCount));
    setText('dash-pct', toFa(pct) + '٪');

    /* نوار پیشرفت */
    var fill = document.getElementById('dash-fill');
    if (fill) fill.style.width = pct + '%';

    /* فهرست بهترین نمره‌ها */
    var list = document.getElementById('dash-scores');
    if (!list) return;

    if (!quizIds.length) {
      list.innerHTML = '<p class="dash-empty">هنوز آزمونی نداده‌اید! از «آزمون تعاملی» انتهای هر فصل شروع کنید. 📝</p>';
      return;
    }

    list.innerHTML =
      '<h4>🏅 بهترین نمره‌های شما</h4>' +
      '<div class="dash-score-grid">' +
      quizIds.map(function (k) {
        var r = quizzes[k];
        var num = k.replace('ch-', '').replace(/^0+/, '') || k;
        var cls = r.best >= 60 ? 'good' : 'bad';
        return '<div class="dash-score">' +
          '<span class="dash-score-id">فصل ' + toFa(num) + '</span>' +
          '<span class="dash-score-val ' + cls + '">' + toFa(r.best) + '٪</span>' +
          '<span class="dash-score-tries">' + toFa(r.tries || 1) + ' بار</span>' +
          '</div>';
      }).join('') +
      '</div>';
  }

  /* کمکی: تنظیم متن با بررسی وجود */
  function setText(id, text) {
    var el = document.getElementById(id);
    if (el) el.textContent = text;
  }

  /* ═══════════════════════════════════════════════════════════
     ۱۱) جست‌وجو و فیلتر فصل‌ها (صفحه اصلی)
     ═══════════════════════════════════════════════════════════ */

  (function initSearchFilter() {
    var searchInput = document.getElementById('chapter-search');
    var chips = qsa('.filter-chip');
    var cards = qsa('.card[data-search]');
    var noRes = document.getElementById('no-result');

    if (!cards.length) return;

    function getActiveCat() {
      var cat = null;
      chips.forEach(function (c) {
        if (c.classList.contains('on')) cat = c.getAttribute('data-cat');
      });
      return cat;
    }

    function apply() {
      var q = searchInput ? DJC.toEn(searchInput.value).trim().toLowerCase() : '';
      var activeCat = getActiveCat();
      var visible = 0;

      cards.forEach(function (card) {
        var text = (card.getAttribute('data-search') || '').toLowerCase();
        var ok = true;
        if (q && text.indexOf(q) === -1) ok = false;
        if (ok && activeCat && card.getAttribute('data-cat') !== activeCat) ok = false;
        card.style.display = ok ? '' : 'none';
        if (ok) visible++;
      });

      if (noRes) noRes.style.display = visible ? 'none' : 'block';

      /* پنهان‌کردن دسته‌های خالی */
      qsa('.cat-wrap').forEach(function (w) {
        var any = false;
        var inner = w.querySelectorAll('.card');
        for (var i = 0; i < inner.length; i++) {
          if (inner[i].style.display !== 'none') { any = true; break; }
        }
        w.style.display = any ? '' : 'none';
      });
    }

    var debouncedApply = DJC.debounce(apply, 100);

    if (searchInput) {
      searchInput.addEventListener('input', debouncedApply);
    }

    chips.forEach(function (c) {
      c.addEventListener('click', function () {
        var was = c.classList.contains('on');
        chips.forEach(function (o) {
          o.classList.remove('on');
          o.setAttribute('aria-pressed', 'false');
        });
        if (!was) {
          c.classList.add('on');
          c.setAttribute('aria-pressed', 'true');
        }
        apply();
      });
      c.setAttribute('aria-pressed', c.classList.contains('on') ? 'true' : 'false');
    });
  })();

  /* ═══════════════════════════════════════════════════════════
     ۱۲) یادداشت‌های من (ذخیره خودکار)
     ═══════════════════════════════════════════════════════════ */

  (function initNotes() {
    var notesBox = document.querySelector('.notes-box');
    if (!notesBox) return;

    var chId = notesBox.getAttribute('data-chapter') || 'unknown';
    var notes = DJC.getJSON(DJC.KEYS.notes, {});
    if (notes[chId]) notesBox.value = notes[chId];

    var status = document.querySelector('.notes-status');
    var counter = document.querySelector('.notes-count');

    /* حد نویسه (برای جلوگیری از پر شدن حافظه) */
    var MAX_CHARS = 20000;

    function paintCount() {
      if (!counter) return;
      var len = notesBox.value.length;
      counter.textContent = toFa(len) + ' نویسه';
      if (len > MAX_CHARS) {
        counter.textContent += ' ⚠️';
      }
    }

    function showStatus(text, saved) {
      if (!status) return;
      status.textContent = text;
      status.classList.toggle('saved', !!saved);
    }

    var save = DJC.debounce(function () {
      var all = DJC.getJSON(DJC.KEYS.notes, {});
      all[chId] = notesBox.value.slice(0, MAX_CHARS);
      var ok = DJC.setJSON(DJC.KEYS.notes, all);
      if (ok) {
        var t = new Date().toLocaleTimeString('fa-IR');
        showStatus('✔ ذخیره شد — ' + t, true);
      } else {
        showStatus('❌ ذخیره نشد', false);
      }
    }, 600);

    notesBox.addEventListener('input', function () {
      paintCount();
      showStatus('⏳ در حال ذخیره...', false);
      save();
    });

    var clearBtn = document.querySelector('[data-notes-clear]');
    if (clearBtn) {
      clearBtn.addEventListener('click', function () {
        if (!confirm('همه یادداشت‌های این فصل پاک شود؟')) return;
        notesBox.value = '';
        var all = DJC.getJSON(DJC.KEYS.notes, {});
        delete all[chId];
        DJC.setJSON(DJC.KEYS.notes, all);
        paintCount();
        showStatus('🗑 پاک شد.', false);
      });
    }

    paintCount();
  })();

  /* ═══════════════════════════════════════════════════════════
     ۱۳) میان‌برهای کیبورد + مودال راهنما
     ═══════════════════════════════════════════════════════════ */

  (function initKeyboardShortcuts() {
    var modal = document.getElementById('shortcuts-modal');
    var lastFocused = null;

    function openModal() {
      if (!modal) return;
      modal.hidden = false;
      document.body.classList.add('modal-open');
      lastFocused = document.activeElement;

      /* فوکوس روی اولین عنصر قابل فوکوس */
      var first = modal.querySelector('button, [href], input, [tabindex]:not([tabindex="-1"])');
      if (first) setTimeout(function () { first.focus(); }, 50);
    }

    function closeModal() {
      if (!modal || modal.hidden) return;
      modal.hidden = true;
      document.body.classList.remove('modal-open');
      if (lastFocused && lastFocused.focus) lastFocused.focus();
    }

    /* باز کردن با دکمه‌ها */
    qsa('[data-shortcuts]').forEach(function (b) {
      b.addEventListener('click', openModal);
    });

    /* بستن با کلیک روی پس‌زمینه یا دکمه بستن */
    if (modal) {
      modal.addEventListener('click', function (ev) {
        if (ev.target === modal || ev.target.closest('[data-close-modal]')) {
          closeModal();
        }
      });

      /* Focus trap */
      modal.addEventListener('keydown', function (ev) {
        if (ev.key !== 'Tab') return;
        var focusable = qsa(
          'button, [href], input, [tabindex]:not([tabindex="-1"])',
          modal
        );
        if (!focusable.length) return;
        var first = focusable[0];
        var last = focusable[focusable.length - 1];
        if (ev.shiftKey && document.activeElement === first) {
          ev.preventDefault();
          last.focus();
        } else if (!ev.shiftKey && document.activeElement === last) {
          ev.preventDefault();
          first.focus();
        }
      });
    }

    /* میان‌برهای سراسری */
    document.addEventListener('keydown', function (ev) {
      var tag = ev.target && ev.target.tagName;
      var inField = /^(INPUT|TEXTAREA|SELECT)$/.test(tag);

      /* در فیلدهای متنی فقط Escape */
      if (inField) {
        if (ev.key === 'Escape' && ev.target.blur) ev.target.blur();
        return;
      }

      /* Escape → بستن مودال */
      if (ev.key === 'Escape') {
        closeModal();
        return;
      }

      /* ? → نمایش/بستن راهنما */
      if (ev.key === '?' || (ev.key === '/' && ev.shiftKey)) {
        ev.preventDefault();
        if (modal && modal.hidden) openModal();
        else closeModal();
        return;
      }

      /* / → فوکوس روی جست‌وجو */
      if (ev.key === '/') {
        var s = document.getElementById('chapter-search') ||
                document.getElementById('glossary-search');
        if (s) {
          ev.preventDefault();
          s.focus();
          if (s.select) s.select();
        }
        return;
      }

      /* d → تغییر تم */
      if (ev.key === 'd' || ev.key === 'D') {
        var tb = document.querySelector('[data-theme-toggle]');
        if (tb) tb.click();
        return;
      }

      /* = / + → افزایش فونت */
      if (ev.key === '=' || ev.key === '+') {
        var fp = document.querySelector('[data-font-plus]');
        if (fp) fp.click();
        return;
      }

      /* - → کاهش فونت */
      if (ev.key === '-' || ev.key === '_') {
        var fm = document.querySelector('[data-font-minus]');
        if (fm) fm.click();
        return;
      }

      /* ← → پیمایش فصل بعدی/قبلی */
      var prev = document.getElementById('prev-chap');
      var next = document.getElementById('next-chap');

      if (ev.key === 'ArrowLeft' && next && !next.classList.contains('disabled')) {
        next.click();
      } else if (ev.key === 'ArrowRight' && prev && !prev.classList.contains('disabled')) {
        prev.click();
      }
    });
  })();

  /* ═══════════════════════════════════════════════════════════
     ۱۴) بازگشت به بالا
     ═══════════════════════════════════════════════════════════ */

  (function initBackToTop() {
    var toTop = document.getElementById('toTop');
    if (!toTop) return;

    var throttledToggle = DJC.throttle(function () {
      toTop.classList.toggle('show', window.scrollY > 400);
    }, 100);

    window.addEventListener('scroll', throttledToggle, { passive: true });

    toTop.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: SCROLL_BEHAVIOR });
    });

    /* وضعیت اولیه */
    throttledToggle();
  })();

  /* ═══════════════════════════════════════════════════════════
     ۱۵) پیمایش نرم لینک‌های داخلی
     ═══════════════════════════════════════════════════════════ */

  (function initSmoothScroll() {
    /* لینک‌های #p (بخش‌های فصل) */
    document.addEventListener('click', function (ev) {
      var a = ev.target.closest('a[href^="#p"]');
      if (!a) return;
      var href = a.getAttribute('href');
      if (href.length < 2) return;

      var el = document.querySelector(href);
      if (!el) return;

      ev.preventDefault();
      scrollTo(el, 'start');

      /* به‌روزرسانی URL بدون پرش */
      try {
        history.replaceState(null, '', href);
      } catch (e) { /* ignore */ }
    });
  })();

  /* ═══════════════════════════════════════════════════════════
     ۱۶) راه‌اندازی نهایی
     ═══════════════════════════════════════════════════════════ */

  function init() {
    try {
      paintHomeMarks();
      renderDashboard();
      log.info('DJC app initialized');
    } catch (e) {
      log.error('DJC app init error:', e);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();