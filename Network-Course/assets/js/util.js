/* util.js — توابع کمکی مشترک */
const CourseUtil = (() => {

  function initTheme() {
    const saved = localStorage.getItem('course-theme') || 'light';
    document.documentElement.setAttribute('data-theme', saved);
  }
  function toggleTheme() {
    const cur = document.documentElement.getAttribute('data-theme');
    const next = cur === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('course-theme', next);
    toast(next === 'dark' ? '🌙 حالت تاریک' : '☀️ حالت روشن');
  }

  function initFont() {
    const saved = localStorage.getItem('course-font') || 'normal';
    document.documentElement.setAttribute('data-font', saved);
  }
  function cycleFont() {
    const order = ['small', 'normal', 'large'];
    const cur = document.documentElement.getAttribute('data-font') || 'normal';
    const next = order[(order.indexOf(cur) + 1) % order.length];
    document.documentElement.setAttribute('data-font', next);
    localStorage.setItem('course-font', next);
    const labels = { small: 'کوچک', normal: 'متوسط', large: 'بزرگ' };
    toast(`🔤 فونت: ${labels[next]}`);
  }

  function toast(msg, type = '') {
    let box = document.querySelector('.toast-container');
    if (!box) {
      box = document.createElement('div');
      box.className = 'toast-container';
      document.body.appendChild(box);
    }
    const el = document.createElement('div');
    el.className = 'toast ' + type;
    el.textContent = msg;
    box.appendChild(el);
    setTimeout(() => {
      el.style.opacity = '0';
      el.style.transform = 'translateY(10px)';
      el.style.transition = 'all .3s';
      setTimeout(() => el.remove(), 300);
    }, 2600);
  }

  function modal(title, html) {
    let back = document.querySelector('.modal-backdrop');
    if (!back) {
      back = document.createElement('div');
      back.className = 'modal-backdrop';
      back.innerHTML = `
        <div class="modal">
          <h3 class="modal-title"></h3>
          <div class="modal-body"></div>
          <div style="text-align:left;margin-top:18px">
            <button class="btn" data-close>بستن</button>
          </div>
        </div>`;
      document.body.appendChild(back);
      back.addEventListener('click', e => {
        if (e.target === back || e.target.dataset.close !== undefined) {
          back.classList.remove('show');
        }
      });
    }
    back.querySelector('.modal-title').textContent = title;
    back.querySelector('.modal-body').innerHTML = html;
    back.classList.add('show');
  }

  function mountSettingsFab() {
    const fab = document.createElement('div');
    fab.className = 'settings-fab';
    fab.innerHTML = `
      <button title="تغییر تم" data-theme-btn>🌓</button>
      <button title="اندازه فونت" data-font-btn>🔤</button>
      <button title="بازگشت به بالا" data-top-btn>⬆️</button>
    `;
    document.body.appendChild(fab);
    fab.querySelector('[data-theme-btn]').onclick = toggleTheme;
    fab.querySelector('[data-font-btn]').onclick  = cycleFont;
    fab.querySelector('[data-top-btn]').onclick   = () =>
      window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function markChapterVisited(id) {
    const set = new Set(JSON.parse(localStorage.getItem('course-visited') || '[]'));
    set.add(id);
    localStorage.setItem('course-visited', JSON.stringify([...set]));
  }
  function markChapterDone(id) {
    const set = new Set(JSON.parse(localStorage.getItem('course-done') || '[]'));
    set.add(id);
    localStorage.setItem('course-done', JSON.stringify([...set]));
  }
  function isChapterDone(id) {
    return JSON.parse(localStorage.getItem('course-done') || '[]').includes(id);
  }

  return {
    initTheme, toggleTheme,
    initFont, cycleFont,
    toast, modal,
    mountSettingsFab,
    markChapterVisited, markChapterDone, isChapterDone
  };
})();

CourseUtil.initTheme();
CourseUtil.initFont();
document.addEventListener('DOMContentLoaded', () => CourseUtil.mountSettingsFab());