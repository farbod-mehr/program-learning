/* ============================================================
   course-config.js — شناسنامه دوره «صفر تا صد پایتون»
   ------------------------------------------------------------
   ⚠️  این فایل به‌طور خودکار از course.json تولید می‌شود.
       ویرایش دستی لازم نیست؛ برای تغییر تنظیمات، course.json
       را ویرایش و اسکریپت build را دوباره اجرا کنید.

   ساختار:
   ۱) شناسه و عنوان
   ۲) مسیرها و لینک‌ها
   ۳) برند و ظاهر
   ۴) سطوح یادگیری (مطابق filter-chip ها)
   ۵) تنظیمات پیش‌فرض (تم، فونت، آزمون)
   ۶) پرچم‌های فعال/غیرفعال ویژگی‌ها
   ۷) محدودیت‌ها و آستانه‌ها
   ۸) سازگاری با نسخه قدیم + API کمکی
   ============================================================ */

window.DJC_CONFIG = (function () {
  'use strict';

  /* ═══════════════════════════════════════════════════════════
     ۰) نسخه و تاریخ ساخت
     ═══════════════════════════════════════════════════════════ */
  var _version = '3.0.0';
  var _buildDate = '1405/01/01';
  var _schemaVersion = 3;   /* برای مایگریشن‌های آینده */

  /* ═══════════════════════════════════════════════════════════
     ۱) شناسه و عنوان
     ═══════════════════════════════════════════════════════════ */

  /* شناسه یکتا — پیشوند همه کلیدهای localStorage
     ⚠️ تغییر این مقدار باعث از دست رفتن پیشرفت کاربران می‌شود. */
  var courseId = 'pyx';

  var courseTitle = 'دوره تخصصی صفر تا صد پایتون';
  var courseShortTitle = 'صفر تا صد پایتون';
  var courseSubtitle = 'از مبتدی تا مهندس نرم‌افزار';
  var courseDescription = 'مسیر پروژه‌محور فارسی از صفر مطلق تا توسعه‌دهنده حرفه‌ای پایتون — با آزمون تعاملی، واژه‌نامه هوشمند و داشبورد یادگیری.';

  /* زبان و جهت (برای پشتیبانی چندزبانه در آینده) */
  var courseLanguage = 'fa';
  var courseDirection = 'rtl';

  /* تعداد کل فصل‌ها — در داشبورد برای محاسبه درصد پیشرفت استفاده می‌شود. */
  var totalChapters = 30;

  /* ═══════════════════════════════════════════════════════════
     ۲) مسیرها و لینک‌ها
     ═══════════════════════════════════════════════════════════ */

  var links = {
    /* مسیرهای داخلی */
    home: 'index.html',
    glossary: 'glossary.html',
    chaptersDir: 'chapters/',
    chapterPattern: 'chapters/chapter-{n}/index.html',

    /* منابع خارجی (در فوتر و راهنما استفاده می‌شوند) */
    pythonDocs: 'https://docs.python.org/3/',
    pep8: 'https://peps.python.org/pep-0008/',
    pypi: 'https://pypi.org/'
  };

  /* مسیر فایل‌های استاتیک (تصاویر، CSS، JS) */
  var assets = {
    images: 'assets/images/',
    css: 'assets/css/',
    js: 'assets/js/'
  };

  /* ═══════════════════════════════════════════════════════════
     ۳) برند و ظاهر
     ═══════════════════════════════════════════════════════════ */

  var brand = {
    emoji: '🐍',
    name: 'دوره تخصصی پایتون',
    tagline: 'از صفر تا حرفه‌ای',
    footerNote: 'دوره فارسی، پروژه‌محور و حرفه‌ای صفر تا صد پایتون.',
    copyright: '© ۱۴۰۵ — دوره تخصصی پایتون'
  };

  /* ═══════════════════════════════════════════════════════════
     ۴) سطوح یادگیری
     مطابق data-cat فیلتر-چیپ‌های صفحه اصلی.
     برای افزودن سطح جدید، chip متناظر را در HTML اضافه کنید.
     ═══════════════════════════════════════════════════════════ */

  var levels = [
    {
      id: 1,
      slug: 'basics',
      title: 'شروع و مبانی',
      shortTitle: 'مبانی',
      icon: '🐣',
      description: 'نصب، سینتکس، متغیر، نوع داده و کنترل جریان.',
      chaptersFrom: 1,
      chaptersTo: 8
    },
    {
      id: 2,
      slug: 'data-structures',
      title: 'ساختمان داده و توابع',
      shortTitle: 'ساختمان داده',
      icon: '🧱',
      description: 'رشته، لیست، دیکشنری، تابع، ماژول و خطا.',
      chaptersFrom: 9,
      chaptersTo: 15
    },
    {
      id: 3,
      slug: 'applied',
      title: 'برنامه‌نویسی کاربردی',
      shortTitle: 'کاربردی',
      icon: '🛠️',
      description: 'فایل، تست، شی‌گرایی، پایگاه داده و وب.',
      chaptersFrom: 16,
      chaptersTo: 23
    },
    {
      id: 4,
      slug: 'professional',
      title: 'حرفه‌ای و پروژه',
      shortTitle: 'حرفه‌ای',
      icon: '🚀',
      description: 'هم‌روندی، API، داده، امنیت، استقرار و پروژه نهایی.',
      chaptersFrom: 24,
      chaptersTo: 30
    }
  ];

  /* ═══════════════════════════════════════════════════════════
     ۵) تنظیمات پیش‌فرض
     مقادیری که برای کاربر تازه (بدون داده ذخیره‌شده) اعمال می‌شوند.
     ═══════════════════════════════════════════════════════════ */

  var defaults = {
    /* تم: 'auto' = تشخیص خودکار سیستم | 'light' | 'dark' */
    theme: 'auto',

    /* سطح فونت: 0 = عادی | 1 = بزرگ | 2 = بزرگ‌تر */
    fontLevel: 0,

    /* آزمون تعاملی */
    quiz: {
      passScore: 60,        /* حد نصاب قبولی (درصد) */
      showTimer: true,
      autoAdvance: true,    /* اسکرول خودکار به پرسش بعدی */
      autoAdvanceDelay: 500 /* میلی‌ثانیه */
    },

    /* داشبورد */
    dashboard: {
      showScores: true,     /* نمایش فهرست بهترین نمره‌ها */
      maxScoresShown: 12    /* حداکثر تعداد رکورد نمایشی */
    }
  };

  /* ═══════════════════════════════════════════════════════════
     ۶) پرچم‌های ویژگی‌ها
     برای خاموش‌کردن سریع یک قابلیت بدون حذف کد.
     ═══════════════════════════════════════════════════════════ */

  var features = {
    /* UI */
    readingBar: true,
    floatingToolbar: true,
    backToTop: true,
    toasts: true,
    shortcutsModal: true,

    /* محتوا */
    syntaxHighlight: true,
    copyButtons: true,
    tocSpy: true,
    smoothScroll: true,
    openAllAnswers: true,

    /* تعامل */
    themeToggle: true,
    fontSizing: true,
    keyboardShortcuts: true,

    /* داده */
    saveProgress: true,
    saveNotes: true,
    saveQuizScores: true,
    dashboard: true,

    /* واژه‌نامه */
    glossaryHover: true,
    glossaryChapter: true,
    glossaryFull: true,

    /* آزمون */
    quiz: true,
    quizFlags: true,
    quizReview: true
  };

  /* ═══════════════════════════════════════════════════════════
     ۷) محدودیت‌ها و آستانه‌ها
     اعداد جادویی متمرکز برای تنظیم سریع.
     ═══════════════════════════════════════════════════════════ */

  var limits = {
    /* ذخیره‌سازی */
    notesMaxChars: 20000,
    noteSaveDebounce: 600,       /* ms */
    searchDebounce: 100,          /* ms */

    /* توست */
    toastDuration: 3200,          /* ms */
    toastMaxCount: 4,

    /* واژه‌نامه */
    tooltipShowDelay: 140,        /* ms */
    tooltipHideDelay: 220,        /* ms */
    tooltipMaxWidth: 420,         /* px */

    /* اسکرول اسپای */
    tocSpyOffset: 140,            /* px از بالا */
    tocSpyThrottle: 100,          /* ms */

    /* نوار پیشرفت */
    readingBarThrottle: 60,       /* ms */
    backToTopThreshold: 400       /* px */
  };

  /* آستانه‌های نمره‌دهی و ستاره‌ها (برای quiz.js) */
  var grading = {
    pass: 60,           /* قبولی */
    good: 70,           /* دو ستاره */
    excellent: 90,      /* سه ستاره */
    mastery: 100        /* کامل */
  };

  /* ═══════════════════════════════════════════════════════════
     ۸) API کمکی (اختیاری)
     توابع کوچک برای دسترسی راحت‌تر به بخش‌های config.
     ═══════════════════════════════════════════════════════════ */

  /* ساخت مسیر فصل شماره n */
  function chapterUrl(n) {
    var num = String(n).padStart(2, '0');
    return links.chapterPattern.replace('{n}', num);
  }

  /* پیدا کردن سطح یک فصل با شماره */
  function levelOf(chapterNumber) {
    for (var i = 0; i < levels.length; i++) {
      var lv = levels[i];
      if (chapterNumber >= lv.chaptersFrom && chapterNumber <= lv.chaptersTo) {
        return lv;
      }
    }
    return null;
  }

  /* بررسی فعال بودن یک ویژگی */
  function isOn(featureName) {
    return !!features[featureName];
  }

  /* ═══════════════════════════════════════════════════════════
     ۹) بازگشت شیء نهایی
     ⚠️ فیلدهای courseId / courseTitle / totalChapters
        برای سازگاری با نسخه‌های قبلی حفظ شده‌اند.
     ═══════════════════════════════════════════════════════════ */

  return {
    /* --- سازگاری کامل با نسخه قبلی (دست نزنید) --- */
    courseId: courseId,
    courseTitle: courseTitle,
    totalChapters: totalChapters,

    /* --- اطلاعات دوره --- */
    courseShortTitle: courseShortTitle,
    courseSubtitle: courseSubtitle,
    courseDescription: courseDescription,
    courseLanguage: courseLanguage,
    courseDirection: courseDirection,

    /* --- نسخه --- */
    version: _version,
    buildDate: _buildDate,
    schemaVersion: _schemaVersion,

    /* --- ساختارها --- */
    links: links,
    assets: assets,
    brand: brand,
    levels: levels,
    defaults: defaults,
    features: features,
    limits: limits,
    grading: grading,

    /* --- توابع کمکی --- */
    chapterUrl: chapterUrl,
    levelOf: levelOf,
    isOn: isOn
  };
})();