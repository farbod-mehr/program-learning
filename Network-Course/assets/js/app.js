/* app.js — رفتارهای عمومی صفحه */

(function () {

  function initScrollProgress() {
    const fill = document.querySelector('.progress-bar .fill');
    if (!fill) return;
    function update() {
      const h = document.documentElement;
      const max = h.scrollHeight - h.clientHeight;
      const pct = max > 0 ? (h.scrollTop / max) * 100 : 0;
      fill.style.width = pct + '%';
    }
    window.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update);
    update();
  }

  function initChapterVisit() {
    const chap = document.body.dataset.chapter;
    if (chap) CourseUtil.markChapterVisited(chap);
  }

  function initFinishBtn() {
    const btn = document.querySelector('[data-finish-chapter]');
    if (!btn) return;
    const id = btn.dataset.finishChapter;
    if (CourseUtil.isChapterDone(id)) {
      btn.textContent = '✅ این فصل را تمام کردی';
      btn.classList.add('ghost');
    }
    btn.addEventListener('click', () => {
      CourseUtil.markChapterDone(id);
      btn.textContent = '✅ این فصل را تمام کردی';
      btn.classList.add('ghost');
      CourseUtil.toast('🎉 فصل با موفقیت علامت‌گذاری شد', 'success');
    });
  }

  function initKeyboardNav() {
    document.addEventListener('keydown', e => {
      if (e.target.matches('input, textarea')) return;
      const prev = document.querySelector('[data-nav-prev]');
      const next = document.querySelector('[data-nav-next]');
      if (e.key === 'ArrowRight' && prev && !prev.disabled) prev.click();
      if (e.key === 'ArrowLeft'  && next && !next.disabled) next.click();
    });
  }

  function initNotes() {
    const ta = document.querySelector('[data-notes]');
    if (!ta) return;
    const key = 'course-notes-' + (document.body.dataset.chapter || 'misc');
    ta.value = localStorage.getItem(key) || '';
    const hint = document.querySelector('.saved-hint');
    let timer;
    ta.addEventListener('input', () => {
      clearTimeout(timer);
      hint.textContent = 'در حال ذخیره…';
      timer = setTimeout(() => {
        localStorage.setItem(key, ta.value);
        hint.textContent = '✔ ذخیره شد (' + new Date().toLocaleTimeString('fa-IR') + ')';
      }, 500);
    });
  }

  document.addEventListener('DOMContentLoaded', () => {
    initScrollProgress();
    initChapterVisit();
    initFinishBtn();
    initKeyboardNav();
    initNotes();
  });
})();