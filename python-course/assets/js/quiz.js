/* ============================================================
   دوره جامع پایتون — موتور آزمون تعاملی (quiz.js v3)
   ------------------------------------------------------------
   قالب نشانه‌گذاری هر آزمون در فصل‌ها:

   <div class="quiz" data-id="ch-01" data-title="آزمون تعاملی فصل ۱" data-pass="60">
     <div class="quiz-q" data-answer="b">
       <h4 class="quiz-q-text">۱) متن پرسش؟</h4>
       <div class="quiz-opts">
         <button type="button" class="quiz-opt" data-key="a">گزینه الف</button>
         <button type="button" class="quiz-opt" data-key="b">گزینه ب</button>
         <button type="button" class="quiz-opt" data-key="c">گزینه ج</button>
         <button type="button" class="quiz-opt" data-key="d">گزینه د</button>
       </div>
       <div class="quiz-explain">💡 توضیح پاسخ صحیح...</div>
     </div>
     ... (پرسش‌های بعدی)
   </div>

   ویژگی‌های نسخه ۳:
   ✔ انتخاب گزینه با بازخورد فوری (سبز/قرمز)
   ✔ توضیح آموزشی هر پرسش بعد از پاسخ
   ✔ نوار پیشرفت + شمارنده + زمان‌سنج زنده
   ✔ کارت نتیجه: درصد، قبولی، ستاره، بهترین رکورد
   ✔ شروع دوباره، مرور پاسخ‌های نادرست، نشان‌کردن پرسش‌ها
   ✔ ذخیره بهترین نمره در localStorage
   ✔ پشتیبانی کامل از کیبورد (۱-۴ برای انتخاب، R/B/J/F)
   ✔ بهبود دسترسی‌پذیری با ARIA
   ✔ مدیریت چند آزمون در یک صفحه
   ✔ ذخیره پیشرفت هر آزمون به‌صورت جداگانه
   ✔ تاریخچه آخرین اجراها
   ============================================================ */
(function () {
  'use strict';
  if (!window.DJC) return;

  var toFa = DJC.toFa;
  var esc = DJC.escapeHtml;
  var QUIZ_KEY = DJC.KEYS.quiz;
  var FLAG_KEY = DJC.KEYS.flags;

  /* نگاشت حرف به فارسی برای گزینه‌ها */
  var FA_KEY = { a: 'الف', b: 'ب', c: 'ج', d: 'د', e: 'ه', f: 'و' };

  /* تنظیمات پیش‌فرض */
  var DEFAULTS = {
    passScore: 60,
    showTimer: true,
    showStars: true,
    shuffleOptions: false
  };

  /* ═══════════════════════════════════════════════════════════
     توابع کمکی
     ═══════════════════════════════════════════════════════════ */

  /* تبدیل ثانیه به قالب mm:ss */
  function formatTime(seconds) {
    var mm = String(Math.floor(seconds / 60)).padStart(2, '0');
    var ss = String(seconds % 60).padStart(2, '0');
    return mm + ':' + ss;
  }

  /* محاسبه ستاره‌ها بر اساس درصد */
  function getStars(pct, passed) {
    if (pct >= 90) return '⭐⭐⭐';
    if (pct >= 70) return '⭐⭐';
    if (passed) return '⭐';
    return '';
  }

  /* خواندن آرایه پرچم‌های یک آزمون */
  function getFlags(id) {
    var all = DJC.getJSON(FLAG_KEY, {});
    return Array.isArray(all[id]) ? all[id].slice() : [];
  }

  /* ذخیره آرایه پرچم‌های یک آزمون */
  function saveFlags(id, list) {
    var all = DJC.getJSON(FLAG_KEY, {});
    all[id] = list;
    DJC.setJSON(FLAG_KEY, all);
  }

  /* بارگذاری رکورد ذخیره‌شده */
  function loadRecord(id) {
    var store = DJC.getJSON(QUIZ_KEY, {});
    return store[id] || { best: 0, tries: 0, history: [] };
  }

  /* ذخیره رکورد جدید */
  function saveRecord(id, record) {
    var store = DJC.getJSON(QUIZ_KEY, {});
    store[id] = record;
    DJC.setJSON(QUIZ_KEY, store);
  }

  /* نمایش نرم اسکرول */
  function scrollTo(el, position) {
    if (!el) return;
    try {
      el.scrollIntoView({ behavior: 'smooth', block: position || 'start' });
    } catch (e) {
      el.scrollIntoView();
    }
  }

  /* ═══════════════════════════════════════════════════════════
     سازنده اصلی آزمون
     ═══════════════════════════════════════════════════════════ */

  function buildQuiz(root) {
    if (!root || root.__djcQuizBuilt) return;
    root.__djcQuizBuilt = true;

    /* ---------- خواندن داده‌ها ---------- */
    var id = root.getAttribute('data-id') || ('quiz-' + Date.now());
    var title = root.getAttribute('data-title') || 'آزمون تعاملی';
    var passScore = parseInt(root.getAttribute('data-pass'), 10) || DEFAULTS.passScore;
    var questions = Array.prototype.slice.call(root.querySelectorAll('.quiz-q'));

    if (!questions.length) return;

    var totalQ = questions.length;
    var flags = getFlags(id);
    var record = loadRecord(id);

    /* ---------- State مرکزی ---------- */
    var state = {
      answered: 0,
      correct: 0,
      wrongQs: [],
      startedAt: Date.now(),
      finished: false,
      timerId: null,
      filterMode: false   /* آیا فیلتر «نشان‌شده‌ها» فعال است */
    };

    /* ---------- ساخت سربرگ ---------- */
    var head = document.createElement('div');
    head.className = 'quiz-head';
    head.innerHTML =
      '<div class="quiz-head-row">' +
        '<span class="quiz-title">📝 ' + esc(title) + '</span>' +
        '<span class="quiz-timer" title="زمان صرف‌شده" aria-live="off">' +
          '⏱ <b>۰۰:۰۰</b>' +
        '</span>' +
      '</div>' +
      '<div class="quiz-progress" role="progressbar" aria-valuemin="0" aria-valuemax="' + totalQ + '" aria-valuenow="0">' +
        '<div class="quiz-progress-fill"></div>' +
      '</div>' +
      '<div class="quiz-head-row quiz-meta-row">' +
        '<span class="quiz-counter">پاسخ داده‌شده: <b>۰</b>/' + toFa(totalQ) + '</span>' +
        '<span class="quiz-pass-hint">حد نصاب قبولی: ' + toFa(passScore) + '٪</span>' +
      '</div>';

    root.insertBefore(head, root.firstChild);

    var fill = head.querySelector('.quiz-progress-fill');
    var progressBar = head.querySelector('.quiz-progress');
    var counter = head.querySelector('.quiz-counter b');
    var timerEl = head.querySelector('.quiz-timer b');

    /* ---------- زمان‌سنج زنده ---------- */
    function startTimer() {
      if (state.timerId) clearInterval(state.timerId);
      state.timerId = setInterval(function () {
        if (state.finished) return;
        var s = Math.floor((Date.now() - state.startedAt) / 1000);
        timerEl.textContent = toFa(formatTime(s));
      }, 1000);
    }

    function stopTimer() {
      if (state.timerId) clearInterval(state.timerId);
      state.timerId = null;
    }

    startTimer();

    /* ---------- آماده‌سازی هر پرسش ---------- */
    questions.forEach(function (q, qi) {
      var qid = 'q' + qi;
      q.setAttribute('data-qid', qid);
      q.setAttribute('data-index', String(qi + 1));

      var correctKey = (q.getAttribute('data-answer') || '').trim().toLowerCase();
      q.setAttribute('data-correct', correctKey);

      var opts = Array.prototype.slice.call(q.querySelectorAll('.quiz-opt'));

      /* شماره‌گذاری و دکمه نشان‌کردن */
      var textEl = q.querySelector('.quiz-q-text');
      if (textEl && !textEl.querySelector('.quiz-flag')) {
        var flagBtn = createFlagButton(qid, textEl);
        textEl.appendChild(flagBtn);
      }

      /* توضیح پاسخ (اگر HTML نبود، از data-explain بساز) */
      var explain = q.querySelector('.quiz-explain');
      var inlineExplain = q.getAttribute('data-explain');
      if (!explain && inlineExplain) {
        explain = document.createElement('div');
        explain.className = 'quiz-explain';
        explain.setAttribute('role', 'status');
        explain.innerHTML = '💡 ' + esc(inlineExplain);
        q.appendChild(explain);
      } else if (explain) {
        explain.setAttribute('role', 'status');
      }

      /* اتصال هر گزینه */
      opts.forEach(function (opt, oi) {
        var key = (opt.getAttribute('data-key') || '').toLowerCase();

        /* اگر نویسنده حرف فارسی نداده، خودمان اضافه کنیم */
        if (!opt.getAttribute('data-key-fa')) {
          opt.setAttribute('data-key-fa', FA_KEY[key] || '');
        }

        /* ARIA */
        opt.setAttribute('aria-pressed', 'false');
        opt.setAttribute('tabindex', '0');

        opt.addEventListener('click', function () {
          handleAnswer(q, opt, key, correctKey, opts, explain, qi);
        });

        /* پشتیبانی از Enter و Space */
        opt.addEventListener('keydown', function (ev) {
          if (ev.key === 'Enter' || ev.key === ' ') {
            ev.preventDefault();
            opt.click();
          }
        });
      });
    });

    /* ---------- دکمه نشان‌کردن ---------- */
    function createFlagButton(qid, textEl) {
      var flag = document.createElement('button');
      flag.type = 'button';
      flag.className = 'quiz-flag' + (flags.indexOf(qid) !== -1 ? ' on' : '');
      flag.setAttribute('aria-label', 'نشان‌کردن پرسش برای مرور بعدی');
      flag.setAttribute('aria-pressed', flags.indexOf(qid) !== -1 ? 'true' : 'false');
      flag.title = 'نشان‌کردن برای مرور بعدی 🚩';
      flag.textContent = '🚩';
      flag.addEventListener('click', function (ev) {
        ev.stopPropagation();
        var idx = flags.indexOf(qid);
        if (idx === -1) {
          flags.push(qid);
          flag.classList.add('on');
          flag.setAttribute('aria-pressed', 'true');
          DJC.toast('پرسش نشان‌گذاری شد 🚩');
        } else {
          flags.splice(idx, 1);
          flag.classList.remove('on');
          flag.setAttribute('aria-pressed', 'false');
          DJC.toast('نشانه برداشته شد');
        }
        saveFlags(id, flags);
      });
      return flag;
    }

    /* ---------- پردازش پاسخ یک پرسش ---------- */
    function handleAnswer(q, opt, key, correctKey, opts, explain, qi) {
      if (q.classList.contains('answered')) return;

      q.classList.add('answered');
      var isRight = key === correctKey;

      if (isRight) {
        opt.classList.add('correct');
        opt.setAttribute('aria-pressed', 'true');
        state.correct++;
      } else {
        opt.classList.add('wrong');
        opt.setAttribute('aria-pressed', 'false');
        var correctOpt = q.querySelector('.quiz-opt[data-key="' + correctKey + '"]');
        if (correctOpt) {
          correctOpt.classList.add('correct');
          correctOpt.setAttribute('aria-pressed', 'true');
        }
        state.wrongQs.push(q);
      }

      /* غیرفعال‌سازی گزینه‌ها */
      opts.forEach(function (o) {
        o.disabled = true;
        o.setAttribute('tabindex', '-1');
      });

      q.classList.add(isRight ? 'is-right' : 'is-wrong');
      if (explain) explain.classList.add('show');

      state.answered++;
      updateHead();

      /* اگه همه پاسخ داده شدن، تمومش کن */
      if (state.answered === totalQ) {
        finish();
      } else if (isRight) {
        /* بعد از پاسخ درست، نرم اسکرول به پرسش بعدی */
        var nextQ = questions.find(function (qq) {
          return !qq.classList.contains('answered') && qq.style.display !== 'none';
        });
        if (nextQ) {
          setTimeout(function () {
            /* فقط اگر کاربر جای دیگه نرفته باشد */
            if (!state.finished) scrollTo(nextQ, 'center');
          }, 500);
        }
      }
    }

    /* ---------- به‌روزرسانی سربرگ ---------- */
    function updateHead() {
      var pct = Math.round((state.answered / totalQ) * 100);
      fill.style.width = pct + '%';
      counter.textContent = toFa(state.answered);
      if (progressBar) progressBar.setAttribute('aria-valuenow', String(state.answered));
    }

    /* ---------- پایان آزمون ---------- */
    function finish() {
      state.finished = true;
      stopTimer();

      var pct = Math.round((state.correct / totalQ) * 100);
      var passed = pct >= passScore;
      var stars = getStars(pct, passed);
      var seconds = Math.floor((Date.now() - state.startedAt) / 1000);
      var isRecord = pct > record.best;

      /* به‌روزرسانی رکورد */
      record.best = Math.max(record.best, pct);
      record.last = pct;
      record.tries = (record.tries || 0) + 1;
      record.ts = Date.now();
      record.lastTime = seconds;
      if (!Array.isArray(record.history)) record.history = [];
      record.history.push({ pct: pct, time: seconds, at: Date.now() });
      /* فقط ۱۰ تای آخر */
      if (record.history.length > 10) record.history = record.history.slice(-10);
      saveRecord(id, record);

      /* ساخت کارت نتیجه */
      result.innerHTML =
        '<div class="quiz-result-icon">' + (passed ? '🎉' : '💪') + '</div>' +
        '<h4>' + (passed
          ? 'آفرین! آزمون را با موفقیت پشت سر گذاشتید.'
          : 'این بار نشد؛ با مرور پاسخ‌های نادرست دوباره تلاش کنید.') +
        '</h4>' +
        '<div class="quiz-score-row">' +
          '<div class="quiz-score ' + (passed ? 'pass' : 'fail') + '">' +
            '<span class="quiz-score-num">' + toFa(pct) + '٪</span>' +
            '<span class="quiz-score-lbl">' + toFa(state.correct) + ' از ' + toFa(totalQ) + ' پاسخ درست</span>' +
          '</div>' +
          '<ul class="quiz-result-meta">' +
            '<li>⏱ زمان: ' + toFa(formatTime(seconds)) + '</li>' +
            '<li>🏅 بهترین رکورد شما: ' + toFa(record.best) + '٪' +
              (isRecord ? ' <b class="new-record">رکورد جدید!</b>' : '') + '</li>' +
            '<li>🔁 تعداد دفعات: ' + toFa(record.tries) + '</li>' +
            (state.wrongQs.length
              ? '<li>❌ پاسخ‌های نادرست: ' + toFa(state.wrongQs.length) + '</li>'
              : '<li>✨ همه پاسخ‌ها درست بود!</li>') +
            (stars ? '<li>' + stars + '</li>' : '') +
          '</ul>' +
        '</div>';

      result.hidden = false;
      result.classList.add('show');

      /* فعال/غیرفعال دکمه مرور اشتباهات */
      var wrongBtn = actions.querySelector('[data-act="wrong"]');
      if (wrongBtn) wrongBtn.disabled = state.wrongQs.length === 0;

      /* نرم اسکرول به کارت نتیجه */
      setTimeout(function () { scrollTo(result, 'center'); }, 100);

      /* توست */
      DJC.toast(
        passed
          ? 'آفرین! نمره شما ' + toFa(pct) + '٪ شد. 🎉'
          : 'نمره شما ' + toFa(pct) + '٪ شد؛ پاسخ‌های نادرست را مرور کنید.',
        passed ? 'ok' : 'warn'
      );
    }

    /* ---------- نوار ابزار ---------- */
    var actions = document.createElement('div');
    actions.className = 'quiz-actions';
    actions.innerHTML =
      '<button type="button" class="btn small" data-act="reset">↺ شروع دوباره</button>' +
      '<button type="button" class="btn small ghost" data-act="wrong" disabled>🔍 مرور پاسخ‌های نادرست</button>' +
      '<button type="button" class="btn small ghost" data-act="flagged">🚩 پرسش‌های نشان‌شده</button>';
    root.appendChild(actions);

    /* ---------- کارت نتیجه (خالی، پس از پایان پر می‌شود) ---------- */
    var result = document.createElement('div');
    result.className = 'quiz-result';
    result.hidden = true;
    result.setAttribute('role', 'status');
    result.setAttribute('aria-live', 'polite');
    root.appendChild(result);

    /* ---------- عملیات نوار ابزار ---------- */
    actions.addEventListener('click', function (ev) {
      var btn = ev.target.closest('button[data-act]');
      if (!btn) return;
      var act = btn.getAttribute('data-act');
      if (act === 'reset') resetQuiz(btn);
      else if (act === 'wrong') reviewWrong(btn);
      else if (act === 'flagged') toggleFlagged(btn);
    });

    /* شروع دوباره */
    function resetQuiz(btn) {
      if (state.answered > 0 && !state.finished) {
        if (!confirm('آزمون در حال اجرا است؛ مطمئنید می‌خواهید دوباره شروع کنید؟')) return;
      }

      /* اگر فیلتر نشان‌شده‌ها فعال است، خاموشش کن */
      if (state.filterMode) {
        btn.classList.remove('filter-on');
        state.filterMode = false;
        questions.forEach(function (q) { q.style.display = ''; });
      }

      state.answered = 0;
      state.correct = 0;
      state.wrongQs = [];
      state.startedAt = Date.now();
      state.finished = false;

      questions.forEach(function (q) {
        q.classList.remove('answered', 'is-right', 'is-wrong', 'review-flash');
        q.style.display = '';
        q.querySelectorAll('.quiz-opt').forEach(function (o) {
          o.disabled = false;
          o.classList.remove('correct', 'wrong');
          o.setAttribute('aria-pressed', 'false');
          o.setAttribute('tabindex', '0');
        });
        var ex = q.querySelector('.quiz-explain');
        if (ex) ex.classList.remove('show');
      });

      result.hidden = true;
      result.classList.remove('show');
      actions.querySelector('[data-act="wrong"]').disabled = true;

      updateHead();
      timerEl.textContent = toFa('00:00');
      startTimer();

      scrollTo(root, 'start');
      DJC.toast('آزمون دوباره شروع شد');
    }

    /* مرور پاسخ‌های نادرست */
    function reviewWrong(btn) {
      if (!state.wrongQs.length) return;
      var first = state.wrongQs[0];
      scrollTo(first, 'center');
      state.wrongQs.forEach(function (q) {
        q.classList.add('review-flash');
        setTimeout(function () { q.classList.remove('review-flash'); }, 2500);
      });
      DJC.toast(toFa(state.wrongQs.length) + ' پاسخ نادرست برجسته شد');
    }

    /* نمایش/پنهان پرسش‌های نشان‌شده */
    function toggleFlagged(btn) {
      state.filterMode = btn.classList.toggle('filter-on');

      if (state.filterMode && !flags.length) {
        DJC.toast('هنوز پرسشی را نشان نکرده‌اید؛ روی 🚩 کنار هر پرسش بزنید.', 'warn');
        btn.classList.remove('filter-on');
        state.filterMode = false;
        return;
      }

      questions.forEach(function (q) {
        var qid = q.getAttribute('data-qid');
        var show = !state.filterMode || flags.indexOf(qid) !== -1;
        q.style.display = show ? '' : 'none';
      });

      if (state.filterMode) {
        DJC.toast('فقط ' + toFa(flags.length) + ' پرسش نشان‌شده نمایش داده می‌شود');
      } else {
        DJC.toast('نمایش همه پرسش‌ها');
      }
    }

    /* ---------- میان‌برهای کیبورد (مخصوص همین آزمون) ---------- */
    root.addEventListener('keydown', function (ev) {
      /* از تایپ در ورودی‌ها جلوگیری نکن */
      var tag = ev.target && ev.target.tagName;
      if (/^(INPUT|TEXTAREA|SELECT)$/.test(tag)) return;

      /* فقط اگر آزمون در viewport کاربر باشد */
      var rect = root.getBoundingClientRect();
      if (rect.bottom < 0 || rect.top > window.innerHeight) return;

      /* 1-4 → انتخاب گزینه الف-د در پرسش در حال نمایش */
      if (/^[1-6]$/.test(ev.key)) {
        var idx = parseInt(ev.key, 10) - 1;
        var visibleQ = questions.find(function (q) {
          return !q.classList.contains('answered') && q.style.display !== 'none';
        });
        if (visibleQ) {
          var opts = visibleQ.querySelectorAll('.quiz-opt');
          if (opts[idx] && !opts[idx].disabled) {
            ev.preventDefault();
            opts[idx].click();
          }
        }
        return;
      }

      /* R → ریست */
      if (ev.key === 'r' || ev.key === 'R') {
        var resetBtn = actions.querySelector('[data-act="reset"]');
        if (resetBtn) { ev.preventDefault(); resetBtn.click(); }
      }
      /* F → فیلتر نشان‌شده‌ها */
      if (ev.key === 'f' || ev.key === 'F') {
        var flagBtn = actions.querySelector('[data-act="flagged"]');
        if (flagBtn) { ev.preventDefault(); flagBtn.click(); }
      }
      /* W → مرور نادرست‌ها */
      if (ev.key === 'w' || ev.key === 'W') {
        var wrongBtn = actions.querySelector('[data-act="wrong"]');
        if (wrongBtn && !wrongBtn.disabled) { ev.preventDefault(); wrongBtn.click(); }
      }
    });

    /* ---------- مقدار اولیه ---------- */
    updateHead();

    /* ---------- پاک‌سازی هنگام خروج ---------- */
    window.addEventListener('beforeunload', stopTimer);
  }

  /* ═══════════════════════════════════════════════════════════
     راه‌اندازی
     ═══════════════════════════════════════════════════════════ */

  function initAll() {
    document.querySelectorAll('.quiz').forEach(buildQuiz);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAll);
  } else {
    initAll();
  }

  /* ═══════════════════════════════════════════════════════════
     API عمومی
     ═══════════════════════════════════════════════════════════ */

  window.DJC_QUIZ = {
    getFlags: getFlags,
    saveFlags: saveFlags,
    loadRecord: loadRecord,
    /** اجرای مجدد روی یک آزمون (مثلاً بعد از افزودن پرسش جدید به DOM) */
    rebuild: function (selector) {
      var el = typeof selector === 'string' ? document.querySelector(selector) : selector;
      if (el) buildQuiz(el);
    },
    /** بازسازی همه آزمون‌های صفحه */
    rebuildAll: function () {
      document.querySelectorAll('.quiz').forEach(function (q) {
        q.__djcQuizBuilt = false;
        buildQuiz(q);
      });
    }
  };
})();