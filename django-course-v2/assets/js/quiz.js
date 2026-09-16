/* ============================================================
   دوره جامع Django — موتور آزمون تعاملی (quiz.js)
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

   امکانات موتور:
   ✔ انتخاب گزینه با بازخورد فوری (سبز/قرمز + نمایان‌شدن پاسخ درست)
   ✔ توضیح آموزشی هر پرسش بعد از پاسخ
   ✔ نوار پیشرفت + شمارنده پاسخ + زمان‌سنج زنده
   ✔ کارت نتیجه: درصد، قبولی/ردی، ستاره، بهترین رکورد
   ✔ شروع دوباره، مرور پاسخ‌های نادرست، نشان‌کردن پرسش‌ها (🚩)
   ✔ ذخیره بهترین نمره در localStorage (نمایش در داشبورد صفحه اصلی)
   ============================================================ */
(function () {
  'use strict';
  if (!window.DJC) return;
  var toFa = DJC.toFa, esc = DJC.escapeHtml;
  var QUIZ_KEY = DJC.KEYS.quiz, FLAG_KEY = DJC.KEYS.flags;

  function buildQuiz(root) {
    var id = root.getAttribute('data-id') || 'quiz';
    var passScore = parseInt(root.getAttribute('data-pass') || '60', 10);
    var questions = Array.prototype.slice.call(root.querySelectorAll('.quiz-q'));
    if (!questions.length) return;

    var state = {
      answered: 0,
      correct: 0,
      wrongQs: [],
      startedAt: Date.now(),
      finished: false
    };
    var flags = getFlags(id);

    /* ---------- سربرگ آزمون ---------- */
    var head = document.createElement('div');
    head.className = 'quiz-head';
    head.innerHTML = '' +
      '<div class="quiz-head-row">' +
        '<span class="quiz-title">📝 ' + esc(root.getAttribute('data-title') || 'آزمون تعاملی') + '</span>' +
        '<span class="quiz-timer" title="زمان صرف‌شده">⏱ <b>۰۰:۰۰</b></span>' +
      '</div>' +
      '<div class="quiz-progress"><div class="quiz-progress-fill"></div></div>' +
      '<div class="quiz-head-row quiz-meta-row">' +
        '<span class="quiz-counter">پاسخ داده‌شده: <b>۰</b>/' + toFa(questions.length) + '</span>' +
        '<span class="quiz-pass-hint">حد نصاب قبولی: ' + toFa(passScore) + '٪</span>' +
      '</div>';
    root.insertBefore(head, root.firstChild);
    var fill = head.querySelector('.quiz-progress-fill');
    var counter = head.querySelector('.quiz-counter b');
    var timerEl = head.querySelector('.quiz-timer b');

    /* زمان‌سنج زنده */
    var timer = setInterval(function () {
      if (state.finished) return;
      var s = Math.floor((Date.now() - state.startedAt) / 1000);
      var mm = String(Math.floor(s / 60)).padStart(2, '0');
      var ss = String(s % 60).padStart(2, '0');
      timerEl.textContent = toFa(mm + ':' + ss);
    }, 1000);

    /* ---------- آماده‌سازی هر پرسش ---------- */
    questions.forEach(function (q, qi) {
      var qid = 'q' + qi;
      q.setAttribute('data-qid', qid);
      var answer = (q.getAttribute('data-answer') || '').trim().toLowerCase();
      var opts = Array.prototype.slice.call(q.querySelectorAll('.quiz-opt'));

      /* شماره پرسش و دکمه نشان‌کردن */
      var text = q.querySelector('.quiz-q-text');
      if (text && !text.querySelector('.quiz-flag')) {
        var flag = document.createElement('button');
        flag.type = 'button';
        flag.className = 'quiz-flag' + (flags.indexOf(qid) !== -1 ? ' on' : '');
        flag.setAttribute('aria-label', 'نشان‌کردن پرسش برای مرور');
        flag.title = 'نشان‌کردن برای مرور بعدی 🚩';
        flag.textContent = '🚩';
        text.appendChild(flag);
        flag.addEventListener('click', function (ev) {
          ev.stopPropagation();
          var i = flags.indexOf(qid);
          if (i === -1) { flags.push(qid); flag.classList.add('on'); }
          else { flags.splice(i, 1); flag.classList.remove('on'); }
          saveFlags(id, flags);
        });
      }

      /* توضیح پاسخ */
      var explain = q.querySelector('.quiz-explain');
      var inlineExplain = q.getAttribute('data-explain');
      if (!explain && inlineExplain) {
        explain = document.createElement('div');
        explain.className = 'quiz-explain';
        explain.innerHTML = '💡 ' + esc(inlineExplain);
        q.appendChild(explain);
      }

      opts.forEach(function (opt) {
        /* حرف فارسی گزینه (الف/ب/ج/د) اگر نویسنده مشخص نکرده باشد */
        var faMap = { a: 'الف', b: 'ب', c: 'ج', d: 'د', e: 'ه', f: 'و' };
        if (!opt.getAttribute('data-key-fa')) {
          opt.setAttribute('data-key-fa', faMap[(opt.getAttribute('data-key') || '').toLowerCase()] || '');
        }
        opt.addEventListener('click', function () {
          if (q.classList.contains('answered')) return;
          q.classList.add('answered');
          var key = (opt.getAttribute('data-key') || '').toLowerCase();
          var isRight = key === answer;
          if (isRight) {
            opt.classList.add('correct');
            state.correct++;
          } else {
            opt.classList.add('wrong');
            q.querySelector('.quiz-opt[data-key="' + answer + '"]') &&
              q.querySelector('.quiz-opt[data-key="' + answer + '"]').classList.add('correct');
            state.wrongQs.push(q);
          }
          opts.forEach(function (o) { o.disabled = true; });
          q.classList.add(isRight ? 'is-right' : 'is-wrong');
          if (explain) explain.classList.add('show');
          state.answered++;
          updateHead();
          if (state.answered === questions.length) finish();
        });
      });
    });

    /* ---------- نوار ابزار آزمون ---------- */
    var actions = document.createElement('div');
    actions.className = 'quiz-actions';
    actions.innerHTML = '' +
      '<button type="button" class="btn small" data-act="reset">↺ شروع دوباره</button>' +
      '<button type="button" class="btn small ghost" data-act="wrong" disabled>🔍 مرور پاسخ‌های نادرست</button>' +
      '<button type="button" class="btn small ghost" data-act="flagged">🚩 پرسش‌های نشان‌شده</button>';
    root.appendChild(actions);

    /* ---------- کارت نتیجه ---------- */
    var result = document.createElement('div');
    result.className = 'quiz-result';
    result.hidden = true;
    root.appendChild(result);

    function updateHead() {
      var pct = Math.round((state.answered / questions.length) * 100);
      fill.style.width = pct + '%';
      counter.textContent = toFa(state.answered);
    }

    function finish() {
      state.finished = true;
      clearInterval(timer);
      var pct = Math.round((state.correct / questions.length) * 100);
      var passed = pct >= passScore;
      var stars = pct >= 90 ? '⭐⭐⭐' : pct >= 70 ? '⭐⭐' : passed ? '⭐' : '';
      var secs = Math.floor((Date.now() - state.startedAt) / 1000);
      var mm = String(Math.floor(secs / 60)).padStart(2, '0');
      var ss = String(secs % 60).padStart(2, '0');

      /* ذخیره و مقایسه با بهترین رکورد */
      var store = DJC.getJSON(QUIZ_KEY, {});
      var rec = store[id] || { best: 0, tries: 0 };
      var isRecord = pct > rec.best;
      rec.best = Math.max(rec.best, pct);
      rec.last = pct;
      rec.tries = (rec.tries || 0) + 1;
      rec.ts = Date.now();
      store[id] = rec;
      DJC.setJSON(QUIZ_KEY, store);

      result.innerHTML = '' +
        '<div class="quiz-result-icon">' + (passed ? '🎉' : '💪') + '</div>' +
        '<h4>' + (passed ? 'آزمون را با موفقیت پشت سر گذاشتید!' : 'این بار نشد؛ دوباره تلاش کنید!') + '</h4>' +
        '<div class="quiz-score-row">' +
          '<div class="quiz-score ' + (passed ? 'pass' : 'fail') + '">' +
            '<span class="quiz-score-num">' + toFa(pct) + '٪</span>' +
            '<span class="quiz-score-lbl">' + toFa(state.correct) + ' پاسخ درست از ' + toFa(questions.length) + '</span>' +
          '</div>' +
          '<ul class="quiz-result-meta">' +
            '<li>⏱ زمان: ' + toFa(mm + ':' + ss) + '</li>' +
            '<li>🏅 بهترین رکورد شما: ' + toFa(rec.best) + '٪' + (isRecord ? ' <b class="new-record">رکورد جدید!</b>' : '') + '</li>' +
            '<li>🔁 تعداد دفعات: ' + toFa(rec.tries) + '</li>' +
            (stars ? '<li>' + stars + '</li>' : '') +
          '</ul>' +
        '</div>';
      result.hidden = false;
      result.classList.add('show');
      actions.querySelector('[data-act="wrong"]').disabled = state.wrongQs.length === 0;
      DJC.toast(passed ? 'آفرین! نمره شما ' + toFa(pct) + '٪ شد.' : 'نمره شما ' + toFa(pct) + '٪ شد؛ پاسخ‌های نادرست را مرور کنید.', passed ? 'ok' : 'warn');
    }

    /* ---------- عملیات ---------- */
    actions.addEventListener('click', function (ev) {
      var btn = ev.target.closest('button[data-act]');
      if (!btn) return;
      var act = btn.getAttribute('data-act');

      if (act === 'reset') {
        state = { answered: 0, correct: 0, wrongQs: [], startedAt: Date.now(), finished: false };
        questions.forEach(function (q) {
          q.classList.remove('answered', 'is-right', 'is-wrong');
          q.querySelectorAll('.quiz-opt').forEach(function (o) {
            o.disabled = false;
            o.classList.remove('correct', 'wrong');
          });
          var ex = q.querySelector('.quiz-explain');
          if (ex) ex.classList.remove('show');
        });
        result.hidden = true;
        result.classList.remove('show');
        actions.querySelector('[data-act="wrong"]').disabled = true;
        updateHead();
        clearInterval(timer);
        timer = setInterval(function () {
          if (state.finished) return;
          var s = Math.floor((Date.now() - state.startedAt) / 1000);
          timerEl.textContent = toFa(String(Math.floor(s / 60)).padStart(2, '0') + ':' + String(s % 60).padStart(2, '0'));
        }, 1000);
        timerEl.textContent = toFa('00:00');
        root.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }

      if (act === 'wrong' && state.wrongQs.length) {
        var first = state.wrongQs[0];
        first.scrollIntoView({ behavior: 'smooth', block: 'center' });
        state.wrongQs.forEach(function (q) {
          q.classList.add('review-flash');
          setTimeout(function () { q.classList.remove('review-flash'); }, 2500);
        });
      }

      if (act === 'flagged') {
        var on = btn.classList.toggle('filter-on');
        questions.forEach(function (q) {
          var qid = q.getAttribute('data-qid');
          var show = !on || flags.indexOf(qid) !== -1;
          q.style.display = show ? '' : 'none';
        });
        if (on && !flags.length) DJC.toast('هنوز پرسشی را نشان نکرده‌اید؛ روی 🚩 کنار هر پرسش بزنید.');
      }
    });

    updateHead();
  }

  function getFlags(id) {
    var all = DJC.getJSON(FLAG_KEY, {});
    return all[id] || [];
  }
  function saveFlags(id, list) {
    var all = DJC.getJSON(FLAG_KEY, {});
    all[id] = list;
    DJC.setJSON(FLAG_KEY, all);
  }

  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.quiz').forEach(buildQuiz);
  });

  window.DJC_QUIZ = { getFlags: getFlags };
})();
