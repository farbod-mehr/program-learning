/* quiz.js — موتور آزمون تعاملی */

(function () {

  function initQuiz(quiz) {
    const id       = quiz.dataset.quizId;
    const duration = parseInt(quiz.dataset.duration || '0', 10);
    const timerEl  = quiz.querySelector('.quiz-timer');
    const resultEl = quiz.querySelector('.quiz-result');
    const submitBtn= quiz.querySelector('[data-submit]');
    const retryBtn = quiz.querySelector('[data-retry]');
    const questions= quiz.querySelectorAll('.quiz-question');

    let remaining = duration;
    let intervalId = null;
    let finished = false;

    function renderTimer() {
      const m = String(Math.floor(remaining / 60)).padStart(2, '0');
      const s = String(remaining % 60).padStart(2, '0');
      timerEl.textContent = '⏱ ' + m + ':' + s;
    }

    function startTimer() {
      if (!duration) { timerEl.style.display = 'none'; return; }
      renderTimer();
      intervalId = setInterval(() => {
        remaining--;
        renderTimer();
        if (remaining <= 0) {
          clearInterval(intervalId);
          if (!finished) grade(true);
        }
      }, 1000);
    }

    function grade(timeout = false) {
      finished = true;
      clearInterval(intervalId);

      let correct = 0;
      questions.forEach(q => {
        const ans = q.dataset.answer;
        const opts = q.querySelectorAll('.quiz-option');
        let picked = null;
        opts.forEach(o => {
          const inp = o.querySelector('input');
          inp.disabled = true;
          if (inp.checked) picked = inp.value;
          o.classList.remove('correct', 'wrong');
        });
        opts.forEach(o => {
          const v = o.querySelector('input').value;
          if (v === ans) o.classList.add('correct');
          if (v === picked && picked !== ans) o.classList.add('wrong');
        });
        if (picked === ans) correct++;
      });

      const total = questions.length;
      const pct = Math.round((correct / total) * 100);

      resultEl.style.display = 'block';
      resultEl.innerHTML = timeout
        ? `⏰ زمان تمام شد! نمره: <b>${correct} از ${total}</b> (${pct}٪)`
        : `✅ نمره‌ی شما: <b>${correct} از ${total}</b> (${pct}٪)`;

      const key = 'course-quiz-' + id;
      const prev = JSON.parse(localStorage.getItem(key) || 'null');
      if (!prev || pct > prev.pct) {
        localStorage.setItem(key, JSON.stringify({ correct, total, pct, at: Date.now() }));
      }

      if (pct >= 60) CourseUtil.markChapterDone(id);
      CourseUtil.toast(pct >= 60 ? '🎉 قبول شدی!' : '📚 دوباره تلاش کن', pct >= 60 ? 'success' : 'error');
    }

    function reset() {
      finished = false;
      remaining = duration;
      resultEl.style.display = 'none';
      resultEl.innerHTML = '';
      questions.forEach(q => {
        q.querySelectorAll('.quiz-option').forEach(o => {
          o.classList.remove('correct', 'wrong');
          const inp = o.querySelector('input');
          inp.disabled = false;
          inp.checked = false;
        });
      });
      if (intervalId) clearInterval(intervalId);
      startTimer();
    }

    submitBtn.addEventListener('click', () => {
      if (finished) return;
      const allAnswered = [...questions].every(q =>
        [...q.querySelectorAll('input')].some(i => i.checked)
      );
      if (!allAnswered) {
        CourseUtil.toast('لطفاً به همه‌ی سوالات پاسخ بده', 'error');
        return;
      }
      grade(false);
    });
    retryBtn.addEventListener('click', reset);

    startTimer();
  }

  document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.quiz').forEach(initQuiz);
  });
})();