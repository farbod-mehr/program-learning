/* ============================================================
   دوره جامع Django — ابزارهای مشترک (util.js)
   توابع پایه: ذخیره‌سازی، تبدیل اعداد فارسی، دیبانس
   این فایل باید قبل از همه فایل‌های دیگر بارگذاری شود.
   ============================================================ */
(function () {
  'use strict';

  var storageOK = true;
  try {
    localStorage.setItem('__djc_test__', '1');
    localStorage.removeItem('__djc_test__');
  } catch (e) { storageOK = false; }

  var FA_DIGITS = '۰۱۲۳۴۵۶۷۸۹';

  /* تبدیل رقم‌های لاتین به فارسی */
  function toFa(input) {
    return String(input).replace(/\d/g, function (d) { return FA_DIGITS[+d]; });
  }

  /* تبدیل رقم‌های فارسی/عربی به لاتین (برای پردازش) */
  function toEn(input) {
    return String(input)
      .replace(/[۰-۹]/g, function (d) { return d.charCodeAt(0) - 1776; })
      .replace(/[٠-٩]/g, function (d) { return d.charCodeAt(0) - 1632; });
  }

  /* خواندن JSON از localStorage با کلید مشخص */
  function getJSON(key, fallback) {
    if (!storageOK) return fallback;
    try {
      var raw = localStorage.getItem(key);
      return raw ? JSON.parse(raw) : fallback;
    } catch (e) { return fallback; }
  }

  /* نوشتن JSON در localStorage */
  function setJSON(key, value) {
    if (!storageOK) return false;
    try { localStorage.setItem(key, JSON.stringify(value)); return true; }
    catch (e) { return false; }
  }

  /* اجرای تابع با تأخیر (برای ذخیره خودکار یادداشت و جستجو) */
  function debounce(fn, wait) {
    var t = null;
    return function () {
      var args = arguments, ctx = this;
      clearTimeout(t);
      t = setTimeout(function () { fn.apply(ctx, args); }, wait);
    };
  }

  /* گریز از HTML (برای درج امن متن در قالب) */
  function escapeHtml(s) {
    return String(s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
  }

  /* نمایش پیام شناور (توست) در همه صفحات */
  function toast(message, type) {
    var wrap = document.getElementById('toast-wrap');
    if (!wrap) return;
    var el = document.createElement('div');
    el.className = 'toast' + (type ? ' toast-' + type : '');
    el.setAttribute('role', 'status');
    el.textContent = message;
    wrap.appendChild(el);
    requestAnimationFrame(function () { el.classList.add('show'); });
    setTimeout(function () {
      el.classList.remove('show');
      setTimeout(function () { el.remove(); }, 350);
    }, 3200);
  }

  /* کلیدهای ذخیره‌سازی استاندارد دوره */
  var KEYS = {
    finished: 'djc_finished_v1',   // فصل‌های تمام‌شده (سازگار با نسخه قبل)
    quiz: 'djc_quiz_v1',           // بهترین نمره آزمون‌ها
    notes: 'djc_notes_v1',         // یادداشت‌های شخصی هر فصل
    theme: 'djc_theme_v1',         // حالت روشن/تاریک
    font: 'djc_font_v1',           // اندازه فونت (0/1/2)
    flags: 'djc_quiz_flags_v1'     // پرسش‌های نشان‌شده در آزمون‌ها
  };

  window.DJC = {
    storageOK: storageOK,
    toFa: toFa,
    toEn: toEn,
    getJSON: getJSON,
    setJSON: setJSON,
    debounce: debounce,
    escapeHtml: escapeHtml,
    toast: toast,
    KEYS: KEYS
  };
})();
