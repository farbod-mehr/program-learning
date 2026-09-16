/* ============================================================
   دوره جامع Django — تعاملات اصلی (app.js)
   ------------------------------------------------------------
   تم تاریک/روشن، اندازه فونت، نوار پیشرفت مطالعه، کپی کد،
   رنگ‌آمیزی نحو پایتون/بش، فهرست بخش‌ها، پاسخ‌ها، پیشرفت فصل‌ها،
   جست‌وجو و فیلتر، داشبورد یادگیری، یادداشت‌های من،
   میان‌برهای کیبورد و بازگشت به بالا.
   ============================================================ */
(function () {
  'use strict';
  if (!window.DJC) return;
  var toFa = DJC.toFa;

  /* ============ تم تاریک / روشن ============ */
  var themeBtns = document.querySelectorAll('[data-theme-toggle]');
  function applyThemeIcon() {
    var dark = document.documentElement.getAttribute('data-theme') === 'dark';
    themeBtns.forEach(function (b) {
      b.textContent = dark ? '☀️' : '🌙';
      b.title = dark ? 'حالت روشن' : 'حالت تاریک';
      b.setAttribute('aria-label', b.title);
    });
  }
  function toggleTheme() {
    var cur = document.documentElement.getAttribute('data-theme') === 'dark' ? 'dark' : 'light';
    var next = cur === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    try { localStorage.setItem(DJC.KEYS.theme, next); } catch (e) {}
    applyThemeIcon();
  }
  themeBtns.forEach(function (b) { b.addEventListener('click', toggleTheme); });
  applyThemeIcon();

  /* ============ اندازه فونت (۰=عادی ۱=بزرگ ۲=بزرگ‌تر) ============ */
  function applyFont() {
    var f = 0;
    try { f = parseInt(localStorage.getItem(DJC.KEYS.font) || '0', 10); } catch (e) {}
    document.documentElement.setAttribute('data-font', String(f));
    document.querySelectorAll('[data-font-label]').forEach(function (el) {
      el.textContent = ['عادی', 'بزرگ', 'بزرگ‌تر'][f] || 'عادی';
    });
  }
  function changeFont(delta) {
    var f = 0;
    try { f = parseInt(localStorage.getItem(DJC.KEYS.font) || '0', 10); } catch (e) {}
    f = Math.min(2, Math.max(0, f + delta));
    try { localStorage.setItem(DJC.KEYS.font, String(f)); } catch (e) {}
    applyFont();
  }
  document.querySelectorAll('[data-font-plus]').forEach(function (b) {
    b.addEventListener('click', function () { changeFont(+1); });
  });
  document.querySelectorAll('[data-font-minus]').forEach(function (b) {
    b.addEventListener('click', function () { changeFont(-1); });
  });
  applyFont();

  /* ============ نوار پیشرفت مطالعه ============ */
  var bar = document.getElementById('reading-bar');
  function updateBar() {
    if (!bar) return;
    var h = document.documentElement;
    var max = h.scrollHeight - h.clientHeight;
    bar.style.width = (max > 0 ? (h.scrollTop / max) * 100 : 0) + '%';
  }
  window.addEventListener('scroll', updateBar, { passive: true });
  updateBar();

  /* ============ رنگ‌آمیزی نحو کد (پایتون / بش) ============ */
  function highlightPython(code) {
    var re = /(#[^\n]*)|("""[\s\S]*?"""|'''[\s\S]*?'''|"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*')|(@\w+)|\b(def|class|return|if|elif|else|for|while|import|from|as|in|not|and|or|is|None|True|False|try|except|finally|with|lambda|yield|pass|break|continue|raise|global|assert|del|async|await)\b|\b(\d+(?:\.\d+)?)\b/g;
    return code.replace(re, function (m, cm, st, dec, kw, num) {
      if (cm) return '<span class="c-comment">' + cm + '</span>';
      if (st) return '<span class="c-str">' + st + '</span>';
      if (dec) return '<span class="c-dec">' + dec + '</span>';
      if (kw) return '<span class="c-kw">' + kw + '</span>';
      if (num) return '<span class="c-num">' + num + '</span>';
      return m;
    });
  }
  function highlightBash(code) {
    var re = /(#[^\n]*)|("(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*')|(^|\n|\s)(python|pip|django-admin|cd|mkdir|ls|source|deactivate|git|curl|sudo|apt|brew|manage\.py)(?=\s|$)|(\s--?[\w-]+)/g;
    return code.replace(re, function (m, cm, st, pre, cmd, flag) {
      if (cm) return '<span class="c-comment">' + cm + '</span>';
      if (st) return '<span class="c-str">' + st + '</span>';
      if (cmd) return (pre || '') + '<span class="c-kw">' + cmd + '</span>';
      if (flag) return '<span class="c-num">' + flag + '</span>';
      return m;
    });
  }
  document.querySelectorAll('pre.code').forEach(function (pre) {
    var code = pre.querySelector('code');
    var target = code || pre;
    var lang = (target.getAttribute('data-lang') || '').toLowerCase();
    if (lang !== 'python' && lang !== 'bash' && lang !== 'shell') return;
    var raw = DJC.escapeHtml(target.textContent);
    target.innerHTML = lang === 'python' ? highlightPython(raw) : highlightBash(raw);
  });

  /* ============ دکمه کپی روی بلوک‌های کد ============ */
  document.querySelectorAll('pre.code').forEach(function (pre) {
    var box = pre.closest('.code-box');
    if (!box) return;
    var head = box.querySelector('.code-head');
    if (!head || head.querySelector('.copy-btn')) return;
    var btn = document.createElement('button');
    btn.className = 'copy-btn';
    btn.type = 'button';
    btn.textContent = '📋 کپی کد';
    head.appendChild(btn);
    btn.addEventListener('click', function () {
      var text = pre.innerText;
      function done() {
        btn.textContent = '✅ کپی شد';
        btn.classList.add('ok');
        setTimeout(function () { btn.textContent = '📋 کپی کد'; btn.classList.remove('ok'); }, 2000);
      }
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done, function () { fallbackCopy(text); done(); });
      } else { fallbackCopy(text); done(); }
    });
  });
  function fallbackCopy(text) {
    var ta = document.createElement('textarea');
    ta.value = text;
    ta.style.position = 'fixed'; ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.select();
    try { document.execCommand('copy'); } catch (e) {}
    document.body.removeChild(ta);
  }

  /* ============ فهرست بخش‌ها: هایلایت بخش فعال ============ */
  var tocLinks = Array.prototype.slice.call(document.querySelectorAll('.toc-list a'));
  var partEls = tocLinks.map(function (a) {
    var id = a.getAttribute('href');
    return id && id.charAt(0) === '#' ? document.querySelector(id) : null;
  });
  if (tocLinks.length) {
    var spyTimer = null;
    window.addEventListener('scroll', function () {
      if (spyTimer) return;
      spyTimer = setTimeout(function () {
        spyTimer = null;
        var pos = window.scrollY + 140;
        var current = 0;
        partEls.forEach(function (el, i) { if (el && el.offsetTop <= pos) current = i; });
        tocLinks.forEach(function (a, i) { a.classList.toggle('active', i === current); });
      }, 90);
    }, { passive: true });
  }

  /* ============ باز/بستن همه پاسخ‌ها ============ */
  function toggleAnswers(openAll) {
    document.querySelectorAll('details.answer, details.faq-item').forEach(function (d) { d.open = openAll; });
    DJC.toast(openAll ? 'همه پاسخ‌ها باز شد.' : 'همه پاسخ‌ها بسته شد.');
  }
  var btnOpen = document.getElementById('btn-open-answers');
  var btnClose = document.getElementById('btn-close-answers');
  if (btnOpen) btnOpen.addEventListener('click', function () { toggleAnswers(true); });
  if (btnClose) btnClose.addEventListener('click', function () { toggleAnswers(false); });

  /* ============ «این فصل را تمام کردم» ============ */
  var doneBtn = document.getElementById('mark-done');
  function getFinished() { return DJC.getJSON(DJC.KEYS.finished, {}); }
  function paintDoneBtn(id) {
    if (!doneBtn) return;
    if (getFinished()[id]) {
      doneBtn.classList.add('done');
      doneBtn.innerHTML = '✅ این فصل را تمام کرده‌اید';
    } else {
      doneBtn.classList.remove('done');
      doneBtn.innerHTML = '✔️ این فصل را تمام کردم';
    }
  }
  function paintHomeMarks() {
    var f = getFinished();
    document.querySelectorAll('.card .done-mark').forEach(function (m) {
      var on = !!f[m.getAttribute('data-id')];
      m.textContent = on ? '✔' : '';
      m.closest('.card').classList.toggle('card-done', on);
    });
  }
  if (doneBtn) {
    var chapterId = doneBtn.getAttribute('data-chapter');
    paintDoneBtn(chapterId);
    doneBtn.addEventListener('click', function () {
      if (!DJC.storageOK) { DJC.toast('مرورگر شما اجازه ذخیره پیشرفت را نمی‌دهد.', 'warn'); return; }
      var f = getFinished();
      if (f[chapterId]) { delete f[chapterId]; DJC.toast('علامت «تمام‌شده» برداشته شد.'); }
      else {
        f[chapterId] = Date.now();
        DJC.toast('آفرین! فصل به‌عنوان تمام‌شده ثبت شد. 🎉', 'ok');
      }
      DJC.setJSON(DJC.KEYS.finished, f);
      paintDoneBtn(chapterId);
      paintHomeMarks();
      renderDashboard();
    });
  }
  paintHomeMarks();

  /* ============ نشان نمره آزمون روی کارت فصل‌ها ============ */
  function paintQuizBadges() {
    var store = DJC.getJSON(DJC.KEYS.quiz, {});
    document.querySelectorAll('.quiz-badge[data-quiz-for]').forEach(function (badge) {
      var id = badge.getAttribute('data-quiz-for');
      var rec = store[id];
      if (rec && rec.best > 0) {
        badge.textContent = '🏅 آزمون: ' + toFa(rec.best) + '٪';
        badge.classList.add('has-score', rec.best >= 60 ? 'good' : 'bad');
      } else {
        badge.textContent = '📝 آزمون تعاملی';
      }
    });
  }
  paintQuizBadges();

  /* ============ داشبورد یادگیری (صفحه اصلی) ============ */
  var TOTAL_CHAPTERS = 30;
  function renderDashboard() {
    var wrap = document.getElementById('dashboard');
    if (!wrap) return;
    var finished = getFinished();
    var doneCount = Object.keys(finished).length;
    var quizzes = DJC.getJSON(DJC.KEYS.quiz, {});
    var quizIds = Object.keys(quizzes).filter(function (k) { return quizzes[k].best > 0; });
    var avg = 0;
    if (quizIds.length) {
      var sum = quizIds.reduce(function (s, k) { return s + quizzes[k].best; }, 0);
      avg = Math.round(sum / quizIds.length);
    }
    var termCount = Object.keys(window.DJC_GLOSSARY || {}).length;

    var pct = Math.round((doneCount / TOTAL_CHAPTERS) * 100);
    document.getElementById('dash-done').textContent = toFa(doneCount) + '/' + toFa(TOTAL_CHAPTERS);
    document.getElementById('dash-quizzes').textContent = toFa(quizIds.length);
    document.getElementById('dash-avg').textContent = quizIds.length ? toFa(avg) + '٪' : '—';
    document.getElementById('dash-terms').textContent = toFa(termCount);
    var statTerms = document.getElementById('stat-terms');
    if (statTerms) statTerms.textContent = '+' + toFa(termCount);
    var dashFill = document.getElementById('dash-fill');
    if (dashFill) dashFill.style.width = pct + '%';
    var dashPct = document.getElementById('dash-pct');
    if (dashPct) dashPct.textContent = toFa(pct) + '٪';

    /* فهرست بهترین نمره‌ها */
    var list = document.getElementById('dash-scores');
    if (!list) return;
    if (!quizIds.length) {
      list.innerHTML = '<p class="dash-empty">هنوز آزمونی نداده‌اید! از «آزمون تعاملی» انتهای هر فصل شروع کنید. 📝</p>';
      return;
    }
    list.innerHTML = '<h4>🏅 بهترین نمره‌های شما</h4><div class="dash-score-grid">' +
      quizIds.map(function (k) {
        var r = quizzes[k];
        return '<div class="dash-score">' +
          '<span class="dash-score-id">فصل ' + esc2(k.replace('ch-', '').replace(/^0/, '') || k) + '</span>' +
          '<span class="dash-score-val ' + (r.best >= 60 ? 'good' : 'bad') + '">' + toFa(r.best) + '٪</span>' +
          '<span class="dash-score-tries">' + toFa(r.tries || 1) + ' بار</span>' +
          '</div>';
      }).join('') + '</div>';
  }
  function esc2(s) {
    return DJC.toFa(s);
  }
  renderDashboard();

  /* ============ جست‌وجو و فیلتر فصل‌ها (صفحه اصلی) ============ */
  var searchInput = document.getElementById('chapter-search');
  var chips = Array.prototype.slice.call(document.querySelectorAll('.filter-chip'));
  var cards = Array.prototype.slice.call(document.querySelectorAll('.card[data-search]'));
  var noRes = document.getElementById('no-result');
  if (cards.length) {
    function applyFilter() {
      var q = searchInput ? DJC.toEn(searchInput.value).trim().toLowerCase() : '';
      var activeCat = null;
      chips.forEach(function (c) { if (c.classList.contains('on')) activeCat = c.getAttribute('data-cat'); });
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
      document.querySelectorAll('.cat-wrap').forEach(function (w) {
        var any = false;
        w.querySelectorAll('.card').forEach(function (c) { if (c.style.display !== 'none') any = true; });
        w.style.display = any ? '' : 'none';
      });
    }
    if (searchInput) searchInput.addEventListener('input', applyFilter);
    chips.forEach(function (c) {
      c.addEventListener('click', function () {
        var was = c.classList.contains('on');
        chips.forEach(function (o) { o.classList.remove('on'); });
        if (!was) c.classList.add('on');
        applyFilter();
      });
    });
  }

  /* ============ یادداشت‌های من (ذخیره خودکار هر فصل) ============ */
  var notesBox = document.querySelector('.notes-box');
  if (notesBox) {
    var chId = notesBox.getAttribute('data-chapter') || 'unknown';
    var notes = DJC.getJSON(DJC.KEYS.notes, {});
    if (notes[chId]) notesBox.value = notes[chId];
    var status = document.querySelector('.notes-status');
    var counter = document.querySelector('.notes-count');
    function paintCount() {
      if (counter) counter.textContent = toFa(notesBox.value.length) + ' نویسه';
    }
    var save = DJC.debounce(function () {
      var all = DJC.getJSON(DJC.KEYS.notes, {});
      all[chId] = notesBox.value;
      DJC.setJSON(DJC.KEYS.notes, all);
      if (status) {
        status.textContent = '✔ ذخیره شد — ' + new Date().toLocaleTimeString('fa-IR');
        status.classList.add('saved');
      }
    }, 600);
    notesBox.addEventListener('input', function () {
      paintCount();
      if (status) { status.textContent = '⏳ در حال ذخیره...'; status.classList.remove('saved'); }
      save();
    });
    var clearBtn = document.querySelector('[data-notes-clear]');
    if (clearBtn) clearBtn.addEventListener('click', function () {
      if (!confirm('همه یادداشت‌های این فصل پاک شود؟')) return;
      notesBox.value = '';
      var all = DJC.getJSON(DJC.KEYS.notes, {});
      delete all[chId];
      DJC.setJSON(DJC.KEYS.notes, all);
      paintCount();
      if (status) { status.textContent = '🗑 پاک شد.'; status.classList.remove('saved'); }
    });
    paintCount();
  }

  /* ============ میان‌برهای کیبورد + مودال راهنما ============ */
  var modal = document.getElementById('shortcuts-modal');
  function openModal() { if (modal) { modal.hidden = false; document.body.classList.add('modal-open'); } }
  function closeModal() { if (modal) { modal.hidden = true; document.body.classList.remove('modal-open'); } }
  document.querySelectorAll('[data-shortcuts]').forEach(function (b) { b.addEventListener('click', openModal); });
  if (modal) {
    modal.addEventListener('click', function (ev) {
      if (ev.target === modal || ev.target.closest('[data-close-modal]')) closeModal();
    });
  }
  document.addEventListener('keydown', function (e) {
    var tag = e.target && e.target.tagName;
    if (/^(INPUT|TEXTAREA|SELECT)$/.test(tag)) {
      if (e.key === 'Escape') e.target.blur();
      return;
    }
    if (e.key === 'Escape') { closeModal(); return; }
    if (e.key === '?') { e.preventDefault(); modal && modal.hidden ? openModal() : closeModal(); return; }
    if (e.key === '/') {
      var s = document.getElementById('chapter-search') || document.getElementById('glossary-search');
      if (s) { e.preventDefault(); s.focus(); }
      return;
    }
    if (e.key === 'd' || e.key === 'D') { toggleTheme(); return; }
    /* پیمایش فصل‌ها با جهت‌ها (در صفحه فصل) */
    var prev = document.getElementById('prev-chap');
    var next = document.getElementById('next-chap');
    if (e.key === 'ArrowLeft' && next && !next.classList.contains('disabled')) { next.click(); }
    else if (e.key === 'ArrowRight' && prev && !prev.classList.contains('disabled')) { prev.click(); }
  });

  /* ============ بازگشت به بالا ============ */
  var toTop = document.getElementById('toTop');
  if (toTop) {
    window.addEventListener('scroll', function () {
      toTop.classList.toggle('show', window.scrollY > 400);
    }, { passive: true });
    toTop.addEventListener('click', function () { window.scrollTo({ top: 0, behavior: 'smooth' }); });
  }

  /* ============ پیمایش نرم لینک‌های داخلی ============ */
  document.querySelectorAll('a[href^="#p"]').forEach(function (a) {
    a.addEventListener('click', function (ev) {
      var el = document.querySelector(a.getAttribute('href'));
      if (el) {
        ev.preventDefault();
        el.scrollIntoView({ behavior: 'smooth', block: 'start' });
        history.replaceState(null, '', a.getAttribute('href'));
      }
    });
  });
})();
