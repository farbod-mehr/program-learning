/* ============================================================
   دوره جامع پایتون — ابزارهای مشترک (util.js v3)
   ------------------------------------------------------------
   این فایل باید قبل از همه فایل‌های دیگر بارگذاری شود.

   بخش‌ها:
   ۰) تشخیص ذخیره‌سازی + fallback حافظه
   ۱) ارقام فارسی/لاتین
   ۲) قالب‌بندی اعداد و حجم
   ۳) JSON در localStorage (نسخه ارتقاءیافته)
   ۴) توابع زمان‌بندی: debounce، throttle، once
   ۵) ابزار اشیاء و آرایه‌ها
   ۶) ابزار DOM: qs، qsa، on (delegation)
   ۷) ابزار رشته: escapeHtml، escapeAttr، sanitize
   ۸) کلیپ‌بورد
   ۹) تشخیص محیط: موبایل، تاچ، reduced-motion
   ۱۰) لاگر خاموش‌شدنی
   ۱۱) توست (Toast) پیشرفته
   ۱۲) کلیدهای استاندارد + ابزارهای مدیریت داده
   ۱۳) API عمومی (window.DJC)
   ============================================================ */
(function () {
  'use strict';

  /* ═══════════════════════════════════════════════════════════
     ۰) تشخیص ذخیره‌سازی + fallback حافظه
     ═══════════════════════════════════════════════════════════ */

  var storageOK = false;
  var memoryStore = {};   /* fallback وقتی localStorage در دسترس نیست */

  try {
    var testKey = '__djc_test__';
    localStorage.setItem(testKey, '1');
    if (localStorage.getItem(testKey) === '1') {
      localStorage.removeItem(testKey);
      storageOK = true;
    }
  } catch (e) {
    storageOK = false;
  }

  /* ═══════════════════════════════════════════════════════════
     ۱) ارقام فارسی/لاتین
     ═══════════════════════════════════════════════════════════ */

  var FA_DIGITS = '۰۱۲۳۴۵۶۷۸۹';

  /* تبدیل ارقام لاتین به فارسی */
  function toFa(input) {
    if (input === null || input === undefined) return '';
    return String(input).replace(/\d/g, function (d) { return FA_DIGITS[+d]; });
  }

  /* تبدیل ارقام فارسی/عربی به لاتین */
  function toEn(input) {
    if (input === null || input === undefined) return '';
    return String(input)
      .replace(/[۰-۹]/g, function (d) { return d.charCodeAt(0) - 1776; })
      .replace(/[٠-٩]/g, function (d) { return d.charCodeAt(0) - 1632; });
  }

  /* ═══════════════════════════════════════════════════════════
     ۲) قالب‌بندی اعداد و حجم
     ═══════════════════════════════════════════════════════════ */

  /* قالب‌بندی عدد با جداکننده هزارگان
     مثال: formatNumber(1234567)      → '۱,۲۳۴,۵۶۷'
           formatNumber(1234567, false) → '1,234,567'
           formatNumber(1234.5)        → '۱,۲۳۴.۵'
  */
  function formatNumber(num, persian) {
    if (num === null || num === undefined || isNaN(num)) return '';
    persian = persian !== false;   /* پیش‌فرض: فارسی */
    var n = Number(num);
    var parts = n.toString().split('.');
    var intPart = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    var result = parts[1] !== undefined ? intPart + '.' + parts[1] : intPart;
    return persian ? toFa(result) : result;
  }

  /* قالب‌بندی حجم فایل
     مثال: formatBytes(1024) → '۱ کیلوبایت'
  */
  function formatBytes(bytes, decimals) {
    if (!bytes || bytes < 0) return '۰ بایت';
    decimals = decimals === undefined ? 1 : decimals;
    var units = ['بایت', 'کیلوبایت', 'مگابایت', 'گیگابایت', 'ترابایت'];
    var i = 0;
    var val = bytes;
    while (val >= 1024 && i < units.length - 1) {
      val /= 1024;
      i++;
    }
    var rounded = i === 0 ? Math.round(val) : Number(val.toFixed(decimals));
    return toFa(formatNumber(rounded, false)) + ' ' + units[i];
  }

  /* ═══════════════════════════════════════════════════════════
     ۳) JSON در localStorage (نسخه ارتقاءیافته)
     ═══════════════════════════════════════════════════════════ */

  /* خواندن JSON از localStorage (یا حافظه موقت) */
  function getJSON(key, fallback) {
    if (!key) return fallback;
    try {
      var raw;
      if (storageOK) {
        raw = localStorage.getItem(key);
      } else {
        raw = memoryStore[key];
      }
      if (raw === null || raw === undefined) return fallback;
      return JSON.parse(raw);
    } catch (e) {
      return fallback;
    }
  }

  /* نوشتن JSON در localStorage */
  function setJSON(key, value) {
    if (!key) return false;
    var str;
    try {
      str = JSON.stringify(value);
    } catch (e) {
      return false;
    }
    try {
      if (storageOK) {
        localStorage.setItem(key, str);
      } else {
        memoryStore[key] = str;
      }
      return true;
    } catch (e) {
      /* در صورت پر بودن حافظه، به حافظه موقت سوئیچ کن */
      memoryStore[key] = str;
      return false;
    }
  }

  /* حذف کلید از حافظه */
  function removeKey(key) {
    if (!key) return false;
    try {
      if (storageOK) localStorage.removeItem(key);
      delete memoryStore[key];
      return true;
    } catch (e) {
      return false;
    }
  }

  /* آیا کلید وجود دارد؟ */
  function hasKey(key) {
    if (!key) return false;
    try {
      if (storageOK) return localStorage.getItem(key) !== null;
      return memoryStore[key] !== undefined;
    } catch (e) {
      return false;
    }
  }

  /* ═══════════════════════════════════════════════════════════
     ۴) توابع زمان‌بندی
     ═══════════════════════════════════════════════════════════ */

  /* تابع debounce — اجرا با تأخیر پس از توقف فراخوانی */
  function debounce(fn, wait) {
    wait = wait || 200;
    var timer = null;
    var debounced = function () {
      var args = arguments;
      var ctx = this;
      clearTimeout(timer);
      timer = setTimeout(function () {
        fn.apply(ctx, args);
        timer = null;
      }, wait);
    };
    /* امکان لغو دستی */
    debounced.cancel = function () {
      if (timer) { clearTimeout(timer); timer = null; }
    };
    return debounced;
  }

  /* تابع throttle — حداکثر یک اجرا در بازه زمانی مشخص */
  function throttle(fn, wait) {
    wait = wait || 100;
    var last = 0;
    var timer = null;
    var throttled = function () {
      var args = arguments;
      var ctx = this;
      var now = Date.now();
      var remaining = wait - (now - last);
      if (remaining <= 0) {
        if (timer) { clearTimeout(timer); timer = null; }
        last = now;
        fn.apply(ctx, args);
      } else if (!timer) {
        timer = setTimeout(function () {
          last = Date.now();
          timer = null;
          fn.apply(ctx, args);
        }, remaining);
      }
    };
    throttled.cancel = function () {
      if (timer) { clearTimeout(timer); timer = null; }
      last = 0;
    };
    return throttled;
  }

  /* once — فقط یک بار اجرا می‌شود */
  function once(fn) {
    var called = false;
    var result;
    return function () {
      if (called) return result;
      called = true;
      result = fn.apply(this, arguments);
      return result;
    };
  }

  /* ═══════════════════════════════════════════════════════════
     ۵) ابزار اشیاء و آرایه‌ها
     ═══════════════════════════════════════════════════════════ */

  function isObject(v) {
    return v !== null && typeof v === 'object' && !Array.isArray(v);
  }
  function isArray(v) { return Array.isArray(v); }
  function isFunction(v) { return typeof v === 'function'; }
  function isString(v) { return typeof v === 'string'; }
  function isNumber(v) { return typeof v === 'number' && !isNaN(v); }

  /* آیا مقدار خالی است؟ */
  function isEmpty(v) {
    if (v === null || v === undefined) return true;
    if (isString(v)) return v.trim() === '';
    if (isArray(v)) return v.length === 0;
    if (isObject(v)) return Object.keys(v).length === 0;
    return false;
  }

  /* کپی عمیق امن */
  function deepClone(v) {
    if (v === null || typeof v !== 'object') return v;
    if (isArray(v)) return v.map(deepClone);
    if (isObject(v)) {
      var out = {};
      Object.keys(v).forEach(function (k) { out[k] = deepClone(v[k]); });
      return out;
    }
    return v;
  }

  /* ادغام سطحی چند شیء */
  function extend(target) {
    var args = Array.prototype.slice.call(arguments, 1);
    args.forEach(function (src) {
      if (!isObject(src)) return;
      Object.keys(src).forEach(function (k) { target[k] = src[k]; });
    });
    return target;
  }

  /* محدود کردن عدد در بازه */
  function clamp(num, min, max) {
    return Math.max(min, Math.min(max, num));
  }

  /* شناسه یکتا */
  var uidCounter = 0;
  function uid(prefix) {
    uidCounter++;
    return (prefix || 'djc') + '-' +
           Date.now().toString(36) + '-' +
           uidCounter.toString(36) +
           Math.random().toString(36).slice(2, 6);
  }

  /* ═══════════════════════════════════════════════════════════
     ۶) ابزار DOM
     ═══════════════════════════════════════════════════════════ */

  /* querySelector کوتاه */
  function qs(selector, ctx) {
    return (ctx || document).querySelector(selector);
  }

  /* querySelectorAll با خروجی آرایه */
  function qsa(selector, ctx) {
    return Array.prototype.slice.call((ctx || document).querySelectorAll(selector));
  }

  /* event delegation — اتصال رویداد به والد با فیلتر فرزند
     مثال: on(document, 'click', '.btn', handler)
  */
  function on(root, event, selector, handler) {
    if (isFunction(selector)) {
      handler = selector;
      selector = null;
    }
    root = root || document;
    root.addEventListener(event, function (ev) {
      if (!selector) {
        handler.call(root, ev);
        return;
      }
      var target = ev.target.closest(selector);
      if (target && root.contains(target)) {
        handler.call(target, ev, target);
      }
    });
  }

  /* ═══════════════════════════════════════════════════════════
     ۷) ابزار رشته
     ═══════════════════════════════════════════════════════════ */

  /* گریز از HTML برای درج ایمن در متن */
  function escapeHtml(s) {
    if (s === null || s === undefined) return '';
    return String(s)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  /* گریز برای مقادیر attribute (سخت‌گیرانه‌تر) */
  function escapeAttr(s) {
    if (s === null || s === undefined) return '';
    return String(s)
      .replace(/&/g, '&amp;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/`/g, '&#96;');
  }

  /* پاک‌سازی نام فایل */
  function sanitizeFileName(name) {
    if (!name) return '';
    return String(name)
      .replace(/[\\/:*?"<>|]/g, '-')
      .replace(/\s+/g, '-')
      .replace(/-+/g, '-')
      .replace(/^-|-$/g, '')
      .slice(0, 100);
  }

  /* کوتاه کردن متن بلند */
  function truncate(str, max) {
    max = max || 100;
    if (!str || str.length <= max) return str || '';
    return str.slice(0, max - 1) + '…';
  }

  /* ═══════════════════════════════════════════════════════════
     ۸) کلیپ‌بورد
     ═══════════════════════════════════════════════════════════ */

  function copyToClipboard(text) {
    /* روش مدرن */
    if (navigator.clipboard && navigator.clipboard.writeText) {
      return navigator.clipboard.writeText(text);
    }
    /* fallback: textarea موقت */
    return new Promise(function (resolve, reject) {
      try {
        var ta = document.createElement('textarea');
        ta.value = text;
        ta.style.position = 'fixed';
        ta.style.top = '-1000px';
        ta.style.opacity = '0';
        document.body.appendChild(ta);
        ta.select();
        var ok = document.execCommand('copy');
        document.body.removeChild(ta);
        ok ? resolve() : reject(new Error('copy failed'));
      } catch (e) {
        reject(e);
      }
    });
  }

  /* ═══════════════════════════════════════════════════════════
     ۹) تشخیص محیط
     ═══════════════════════════════════════════════════════════ */

  var isTouch = (function () {
    try {
      return 'ontouchstart' in window ||
             (navigator.maxTouchPoints && navigator.maxTouchPoints > 0);
    } catch (e) { return false; }
  })();

  var isMobile = (function () {
    try {
      return /Android|iPhone|iPad|iPod|Mobile|webOS|BlackBerry/i.test(navigator.userAgent) ||
             window.innerWidth < 768;
    } catch (e) { return false; }
  })();

  function prefersReducedMotion() {
    try {
      return window.matchMedia &&
             window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    } catch (e) { return false; }
  }

  function prefersDarkMode() {
    try {
      return window.matchMedia &&
             window.matchMedia('(prefers-color-scheme: dark)').matches;
    } catch (e) { return false; }
  }

  /* ═══════════════════════════════════════════════════════════
     ۱۰) لاگر خاموش‌شدنی
     ═══════════════════════════════════════════════════════════ */

  function isDebug() {
    return !!window.DJC_DEBUG;
  }

  var log = {
    debug: function () {
      if (isDebug() && console.debug) console.debug.apply(console, arguments);
    },
    info: function () {
      if (isDebug() && console.info) console.info.apply(console, arguments);
    },
    warn: function () {
      if (console.warn) console.warn.apply(console, arguments);
    },
    error: function () {
      if (console.error) console.error.apply(console, arguments);
    }
  };

  /* ═══════════════════════════════════════════════════════════
     ۱۱) توست پیشرفته
     ═══════════════════════════════════════════════════════════ */

  var TOAST_MAX = 4;              /* حداکثر توست همزمان */
  var TOAST_DURATION = 3200;      /* مدت پیش‌فرض نمایش */

  var TYPE_ICONS = {
    ok:    '✅',
    warn:  '⚠️',
    error: '❌',
    info:  'ℹ️'
  };

  /* حذف یک توست با انیمیشن */
  function dismissToast(el) {
    if (!el || el.__dismissing) return;
    el.__dismissing = true;
    el.classList.remove('show');
    setTimeout(function () {
      if (el.parentNode) el.parentNode.removeChild(el);
    }, 350);
  }

  /* نمایش پیام شناور
     امضا:
       toast(message)
       toast(message, 'ok'|'warn'|'error'|'info')
       toast(message, 'ok', { duration: 5000, dismissible: true })
  */
  function toast(message, type, options) {
    var wrap = document.getElementById('toast-wrap');
    if (!wrap) {
      log.warn('toast-wrap not found; message:', message);
      return null;
    }

    options = options || {};
    var duration = typeof options.duration === 'number'
      ? options.duration
      : TOAST_DURATION;

    /* محدودسازی تعداد */
    var existing = wrap.querySelectorAll('.toast');
    if (existing.length >= TOAST_MAX) {
      dismissToast(existing[0]);
    }

    var el = document.createElement('div');
    el.className = 'toast' + (type ? ' toast-' + type : '');
    el.setAttribute('role', type === 'error' ? 'alert' : 'status');
    el.setAttribute('aria-live', type === 'error' ? 'assertive' : 'polite');

    /* آیکون + متن */
    var ico = document.createElement('span');
    ico.className = 'toast-ico';
    ico.textContent = TYPE_ICONS[type] || '';
    ico.setAttribute('aria-hidden', 'true');

    var msg = document.createElement('span');
    msg.className = 'toast-msg';
    msg.textContent = message;

    el.appendChild(ico);
    el.appendChild(msg);

    /* زمان‌بند خودکار */
    var timer = null;
    function scheduleDismiss() {
      if (duration > 0) {
        timer = setTimeout(function () { dismissToast(el); }, duration);
      }
    }
    function pause() {
      if (timer) { clearTimeout(timer); timer = null; }
    }
    function resume() {
      pause();
      scheduleDismiss();
    }

    /* برهم‌کنش کاربر */
    el.addEventListener('click', function () { dismissToast(el); });
    el.addEventListener('mouseenter', pause);
    el.addEventListener('mouseleave', resume);

    wrap.appendChild(el);

    /* انیمیشن ورود */
    requestAnimationFrame(function () {
      requestAnimationFrame(function () { el.classList.add('show'); });
    });

    scheduleDismiss();
    return el;
  }

  /* پاک‌سازی همه توست‌ها */
  toast.clear = function () {
    var wrap = document.getElementById('toast-wrap');
    if (!wrap) return;
    qsa('.toast', wrap).forEach(dismissToast);
  };

  /* ═══════════════════════════════════════════════════════════
     ۱۲) کلیدهای استاندارد + ابزارهای مدیریت داده
     ═══════════════════════════════════════════════════════════ */

  var CFG = window.DJC_CONFIG || {};
  var P = (CFG.courseId || 'djc') + '_';

  var KEYS = {
    finished: P + 'finished_v1',   /* فصل‌های تمام‌شده */
    quiz:     P + 'quiz_v1',       /* بهترین نمره آزمون‌ها */
    notes:    P + 'notes_v1',      /* یادداشت‌های شخصی هر فصل */
    theme:    'djc_theme_v1',      /* حالت روشن/تاریک (سراسری) */
    font:     'djc_font_v1',       /* اندازه فونت (سراسری) */
    flags:    P + 'quiz_flags_v1'  /* پرسش‌های نشان‌شده در آزمون‌ها */
  };

  /* پاک کردن همه داده‌های این دوره (نه تم و فونت سراسری) */
  function clearCourse() {
    [KEYS.finished, KEYS.quiz, KEYS.notes, KEYS.flags].forEach(removeKey);
  }

  /* لیست همه کلیدهای این دوره */
  function courseKeys() {
    return [KEYS.finished, KEYS.quiz, KEYS.notes, KEYS.flags].slice();
  }

  /* تخمین حجم داده‌های دوره (بایت) */
  function courseSize() {
    var total = 0;
    courseKeys().forEach(function (k) {
      try {
        var v = storageOK ? localStorage.getItem(k) : memoryStore[k];
        if (v) total += v.length * 2;  /* تخمین UTF-16 */
      } catch (e) {}
    });
    return total;
  }

  /* ═══════════════════════════════════════════════════════════
     ۱۳) API عمومی
     ═══════════════════════════════════════════════════════════ */

  window.DJC = {
    /* وضعیت */
    storageOK: storageOK,

    /* ارقام */
    toFa: toFa,
    toEn: toEn,

    /* قالب‌بندی */
    formatNumber: formatNumber,
    formatBytes: formatBytes,

    /* ذخیره‌سازی */
    getJSON: getJSON,
    setJSON: setJSON,
    removeKey: removeKey,
    hasKey: hasKey,

    /* زمان‌بندی */
    debounce: debounce,
    throttle: throttle,
    once: once,

    /* اشیاء و آرایه */
    isObject: isObject,
    isArray: isArray,
    isFunction: isFunction,
    isString: isString,
    isNumber: isNumber,
    isEmpty: isEmpty,
    deepClone: deepClone,
    extend: extend,
    clamp: clamp,
    uid: uid,

    /* DOM */
    qs: qs,
    qsa: qsa,
    on: on,

    /* رشته */
    escapeHtml: escapeHtml,
    escapeAttr: escapeAttr,
    sanitizeFileName: sanitizeFileName,
    truncate: truncate,

    /* کلیپ‌بورد */
    copy: copyToClipboard,

    /* محیط */
    isTouch: isTouch,
    isMobile: isMobile,
    prefersReducedMotion: prefersReducedMotion,
    prefersDarkMode: prefersDarkMode,

    /* لاگ */
    log: log,

    /* توست */
    toast: toast,

    /* کلیدها */
    KEYS: KEYS,

    /* مدیریت داده دوره */
    clearCourse: clearCourse,
    courseKeys: courseKeys,
    courseSize: courseSize
  };
})();