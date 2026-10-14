# 🛡️ دوره تخصصی امنیت وب (حملات و مقابله)

دوره‌ای جامع و کاملاً عملی برای یادگیری **تست نفوذ وب‌اپلیکیشن** — از مبانی تا سطح حرفه‌ای.
این دوره با الهام از سرفصل‌های **CEH V13** و **OWASP** طراحی شده و بر پایه آزمایشگاه عملی با
**Kali Linux** (مهاجم) و **Windows + Django** (هدف) کار می‌کند.

## 📚 سرفصل‌های دوره (21 فصل)

1. **مبانی امنیت وب و نقشه راه CEH** — CIA Triad, OWASP, Kill Chain, انواع مهاجم، اخلاق حرفه‌ای
2. **راه‌اندازی آزمایشگاه امن (Kali + Windows + Django)** — VMware, شبکه ایزوله، نصب ابزارها، قوانین آزمایشگاه
3. **جمع‌آوری اطلاعات (Reconnaissance)** — Passive/Active Recon, OSINT, DNS Enum, Nmap, Gobuster
4. **شناسایی و اسکن وب (Scanning & Enumeration)** — Nikto, Wappalyzer, Burp Spider, OWASP ZAP, شناسایی Stack
5. **حمله به احراز هویت (Authentication Attacks)** — Brute Force, Credential Stuffing, Session Hijacking, MFA Bypass
6. **SQL Injection — نفوذ در قلب دیتابیس** — Union, Boolean, Blind, Time-based, sqlmap, Out-of-Band
7. **XSS — تزریق اسکریپت سمت کلاینت** — Reflected, Stored, DOM-based, BeEF, CSP Bypass
8. **CSRF — جعل درخواست بین‌سایتی** — SameSite, Token, Referer, تغییر رمز و ایمیل قربانی
9. **IDOR و شکست کنترل دسترسی** — Horizontal/Vertical Privilege, BOLA, Mass Assignment
10. **آپلود فایل ناامن و Web Shell** — Bypass Extension/MIME, Polyglot, Reverse Shell, RCE
11. **Command Injection و اجرای کد از راه دور** — OS Command Injection, Blind Injection, Reverse Shell
12. **SSRF — جعل درخواست سمت سرور** — Internal Network, Cloud Metadata (169.254.169.254), Bypass Filters
13. **XXE و حمله به پردازش XML** — File Disclosure, SSRF via XXE, Billion Laughs, Blind XXE
14. **نقشه کامل OWASP Top 10 (2021)** — مرور یکپارچه ده آسیب‌پذیری + آسیب‌پذیری‌های نوظهور
15. **Django و آسیب‌پذیری‌های رایج در بک‌اند** — کدهای ناامن، تنظیمات غلط، DEBUG, ALLOWED_HOSTS, Secret
16. **دیوار آتش وب (WAF) و ModSecurity** — OWASP CRS, Rules, Rate Limiting, Bypass تکنیک‌ها
17. **کدنویسی امن و بازبینی کد (Secure Coding)** — Parameterized Queries, Output Encoding, Input Validation
18. **هدرهای امنیتی و سخت‌سازی سرور** — CSP, HSTS, X-Frame-Options, Hardening, OWASP Secure Headers
19. **مانیتورینگ، لاگ‌گیری و پاسخ به حادثه** — SIEM, Log Analysis, IDS/IPS, Incident Response, Forensics
20. **متدولوژی تست نفوذ و گزارش‌نویسی حرفه‌ای** — PTES, NIST, OWASP WSTG, ساختار گزارش، Severity Rating
21. **پروژه جامع و آزمون عملی نهایی (فصل ویژه)** — سناریوی کامل End-to-End: از Recon تا گزارش + مسیر شغلی

## 🧩 ساختار هر فصل (۱۴ بخش)

1. جعبه عنوان و هویت
2. پیش‌نیازها و راه‌اندازی محیط
3. اهداف یادگیری
4. مقدمه و اهمیت موضوع
5. مفاهیم کلیدی و واژگان تخصصی
6. آموزش گام‌به‌گام حمله (Attack Walkthrough)
7. کارگاه عملی (اجرا در آزمایشگاه)
8. تحلیل دفاعی و راهکارهای مقابله
9. نکات حرفه‌ای و اشتباهات رایج
10. پرسش و پاسخ و رفع اشکال
11. جمع‌بندی و نکات طلایی
12. خودارزیابی و آزمونک
13. پروژه هفتگی (تمرین مستقل)
14. منابع تکمیلی و گام بعدی

## 🚀 شروع کار

1. پوشه پروژه را دانلود و از حالت فشرده خارج کنید.
2. فایل `index.html` را در مرورگر باز کنید.
3. از فصل ۱ شروع کنید و به ترتیب پیش بروید.
4. هر کارگاه را در آزمایشگاه VMware خودتان اجرا کنید.
5. برای هر فصل، پروژه هفتگی و آزمونک را انجام دهید.

## ⚙️ نیازمندی‌های آزمایشگاه

| نقش | سیستم‌عامل | IP پیشنهادی |
| --- | --- | --- |
| مهاجم | Kali Linux | 192.168.56.10 |
| هدف | Windows 10/11 + Django | 192.168.56.20 |
| شبکه | VMware Host-Only (VMnet1) | — |

ابزارها: Burp Suite, OWASP ZAP, sqlmap, Nmap, Nikto, Gobuster, Hydra, BeEF, ModSecurity

## 📁 ساختار پوشه‌ها
web-security-course/
├── index.html
├── README.md
├── assets/
│ ├── css/style.css
│ └── js/script.js
└── chapters/
├── chapter-01/ ... chapter-21/
│ └── index.html

## 🔧 پر کردن محتوای خالی

فایل‌های HTML فعلی، **placeholder** (متن داخل `[ ]`) دارند تا اسکلت آماده باشد.
شما باید آن‌ها را با محتوای واقعی آموزشی پر کنید. برای هر فصل:
- کد حمله/دفاع واقعی بنویسید
- اسکرین‌شات از Kali و سرور هدف اضافه کنید
- منابع معتبر را ذکر کنید

## ⚠️ هشدار اخلاقی و قانونی

تمام مطالب این دوره **فقط برای آموزش در محیط آزمایشگاه ایزوله** است. اجرای این حملات
روی سیستم‌های واقعی بدون اجازه کتبی، **جرم کیفری** محسوب می‌شود. مسئولیت استفاده نادرست
بر عهده کاربر است.

---

**نویسنده:** تیم امنیت  
**سال انتشار:** ۱۴۰۵
