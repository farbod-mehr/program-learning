/* glossary.js — موتور تولتیپ هاور روی اصطلاحات */

(function () {
  let tip = null;

  function ensureTip() {
    if (!tip) {
      tip = document.createElement('div');
      tip.className = 'term-tooltip';
      document.body.appendChild(tip);
    }
    return tip;
  }

  function showTip(target) {
    const key = target.dataset.term;
    const data = GLOSSARY[key];
    if (!data) return;
    const t = ensureTip();
    t.innerHTML = `<strong>${data.title}</strong><br>${data.body}`;
    const r = target.getBoundingClientRect();
    t.classList.add('show');
    const tw = t.offsetWidth;
    let left = r.left + window.scrollX + r.width / 2 - tw / 2;
    left = Math.max(10, Math.min(left, window.innerWidth - tw - 10));
    t.style.left = left + 'px';
    t.style.top  = (r.top + window.scrollY - t.offsetHeight - 10) + 'px';
  }

  function hideTip() {
    if (tip) tip.classList.remove('show');
  }

  function bind() {
    document.querySelectorAll('.term[data-term]').forEach(el => {
      el.addEventListener('mouseenter', () => showTip(el));
      el.addEventListener('mouseleave', hideTip);
      el.addEventListener('focus', () => showTip(el));
      el.addEventListener('blur', hideTip);
    });
  }

  document.addEventListener('DOMContentLoaded', bind);
  window.CourseGlossary = { bind };
})();