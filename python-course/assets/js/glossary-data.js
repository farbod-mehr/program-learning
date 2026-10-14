/* glossary-data.js — واژه‌نامه دوره (تولید خودکار از glossary.json) */
/* ============================================================
   glossary-data.js — واژه‌نامه دوره پایتون
   ساختار هر واژه:
     en      → واژه انگلیسی (نمایش LTR)
     fa      → ترجمه فارسی
     cat     → دسته موضوعی
     desc    → توضیح ساده به فارسی (طوری که همه بفهمند)
     example → مثال کد واقعی
     tip     → نکته کاربردی طلایی
   ============================================================ */
window.DJC_GLOSSARY = {

  /* ═══════════════ دسته: مبانی ═══════════════ */

  'adapter': {
    en: 'ADAPTER', fa: 'آداپتور', cat: 'مبانی',
    desc: 'مثل پریز تبدیل برق می‌مونه! وقتی دو چیز ساخته‌شده که به هم نمی‌خورن، یه آداپتور بینشون می‌ذاریم تا بتونن با هم کار کنن. در برنامه‌نویسی یعنی یه کلاس که رابط یه کتابخانه قدیمی رو به شکل جدید درمیاره.',
    example: 'class OldPrinter:\n    def print_old(self):\n        return "print from old"\n\nclass PrinterAdapter:\n    def __init__(self, old):\n        self.old = old\n    def print(self):\n        return self.old.print_old()\n\np = PrinterAdapter(OldPrinter())\nprint(p.print())',
    tip: 'وقتی کتابخانه‌ای رو عوض می‌کنی ولی نمی‌خوای کل کدت رو دست بزنی، آداپتور نجاتت می‌ده.'
  },

  'api': {
    en: 'API', fa: 'رابط برنامه‌نویسی', cat: 'ساختمان داده',
    desc: 'مثل منوی رستورانه! تو به گارسون می‌گی چی می‌خوای، اون می‌ره آشپزخانه و غذا رو می‌یاره. تو نمی‌دونی آشپز چطور آشپزی می‌کنه، فقط از طریق گارسون سفارش می‌دی و غذا می‌گیری. API هم همینطوره: یه راه رسمی برای اینکه برنامه‌ات با یه سرویس دیگه حرف بزنه.',
    example: 'import requests\nr = requests.get("https://api.github.com/users/torvalds")\ndata = r.json()\nprint(data["name"])  # Linus Torvalds',
    tip: 'همیشه قبل از استفاده از API مستنداتش رو بخون و توکن/کلید لازم رو با احتیاط نگه‌دار.'
  },

  'architecture': {
    en: 'ARCHITECTURE', fa: 'معماری', cat: 'برنامه‌نویسی کاربردی',
    desc: 'مثل نقشه‌ی یه ساختمونه! کجا آشپزخانه باشه، کجا اتاق خواب، راهروها کجا وصل شن. در برنامه‌نویسی معماری یعنی تصمیم می‌گیری بخش‌های برنامه‌ات (دیتابیس، منطق، رابط کاربری) چطور کنار هم قرار بگیرن و با هم حرف بزنن.',
    example: '# معماری لایه‌ای\n# UI → Service → Repository → Database\n\nclass UserService:            # لایه منطق\n    def __init__(self, repo):\n        self.repo = repo\n    def register(self, name):\n        return self.repo.save({"name": name})',
    tip: 'معماری رو از اول درست بچین، بعداً عوض کردنش مثل خراب کردن دیوارهای خونست!'
  },

  'arithmetic': {
    en: 'ARITHMETIC', fa: 'حسابی', cat: 'حرفه‌ای',
    desc: 'همون چهار عمل اصلی ریاضی به‌علاوه دو تای دیگه: جمع (+)، تفریق (-)، ضرب (*)، تقسیم (/) و باقیمانده (%) و توان (**).',
    example: 'print(10 + 3)   # 13\nprint(10 - 3)   # 7\nprint(10 * 3)   # 30\nprint(10 / 3)   # 3.333...\nprint(10 // 3)  # 3 (تقسیم صحیح)\nprint(10 % 3)   # 1 (باقیمانده)\nprint(10 ** 3)  # 1000 (توان)',
    tip: 'عملگر // (تقسیم صحیح) اعشار رو دور می‌ریزه، ولی int() به سمت صفر می‌بره. برای اعداد منفی فرق دارن!'
  },

  'asyncio': {
    en: 'ASYNCIO', fa: 'همگام‌سازی غیرهم‌زمان', cat: 'مبانی',
    desc: 'فرض کن آشپزی می‌کنی و آب قابلمه رو گذاشتی بجوشه. بجای اینکه وایسی تا آب جوش بیاد، می‌ری پیاز خرد می‌کنی! asyncio هم همین کار رو با کد می‌کنه: وقتی یه کار منتظر جواب یه سرور شبکه‌ایه، می‌ره سراغ کارهای دیگه.',
    example: 'import asyncio\n\nasync def boil_water():\n    print("آب رو گذاشتم")\n    await asyncio.sleep(2)  # منتظر می‌مونه ولی برنامه قفل نمی‌شه\n    print("آب جوشید")\n\nasync def chop_onion():\n    print("پیاز خرد می‌کنم")\n\nasyncio.run(boil_water())',
    tip: 'asyncio برای کارهای شبکه‌ای و I/O عالیه، ولی برای محاسبات سنگین CPU اصلاً کمک نمی‌کنه!'
  },

  'attribute': {
    en: 'ATTRIBUTE', fa: 'صفت / ویژگی', cat: 'ساختمان داده',
    desc: 'مثل ویژگی‌های یه شخص: اسمش، سنش، قدش. در پایتون attribute یعنی داده‌ای که به یه شیء چسبیده و با نقطه بهش دسترسی پیدا می‌کنی.',
    example: 'class User:\n    def __init__(self, name, age):\n        self.name = name      # attribute\n        self.age = age        # attribute\n\nu = User("علی", 30)\nprint(u.name)   # علی\nprint(u.age)    # 30',
    tip: 'برای دسترسی ایمن وقتی مطمئن نیستی attribute وجود داره از getattr(obj, "name", "پیش‌فرض") استفاده کن.'
  },

  'await': {
    en: 'AWAIT', fa: 'منتظر بمان', cat: 'برنامه‌نویسی کاربردی',
    desc: 'کلمه‌ای که وقتی یه کار async وقت‌گیر رو صدا می‌زنی، به پایتون می‌گی: «تو برو کارهای دیگه رو انجام بده، من اینجا منتظر می‌مونم تا این تموم بشه».',
    example: 'async def get_data():\n    result = await fetch_from_api()   # صبر می‌کنه\n    return result',
    tip: 'فقط داخل تابعی که با async تعریف شده می‌تونی از await استفاده کنی.'
  },

  'axis': {
    en: 'AXIS', fa: 'محور', cat: 'حرفه‌ای',
    desc: 'همون محورهای X و Y در نمودار. محور افقی معمولاً X و عمودی Y. در نام‌پای وقتی می‌گی axis=0 یعنی «ستون‌ها»، axis=1 یعنی «سطرها».',
    example: 'import matplotlib.pyplot as plt\nfig, ax = plt.subplots()\nax.plot([1,2,3], [4,5,6])\nax.set_xlabel("زمان")\nax.set_ylabel("دما")\nplt.show()',
    tip: 'در Pandas وقتی axis=0 می‌دی، عملیات روی سطرها انجام می‌شه (یعنی از بالا به پایین).'
  },

  'boolean': {
    en: 'BOOLEAN', fa: 'منطقی (بولین)', cat: 'مبانی',
    desc: 'نوعی داده که فقط دو مقدار داره: True (درست) یا False (غلط). مثل کلید برق که یا روشنه یا خاموشه، حالت سوم نداره.',
    example: 'is_raining = True\nis_sunny = False\nprint(10 > 5)      # True\nprint(3 == 4)      # False\nprint(not is_raining)  # False',
    tip: 'در پایتون این‌ها همه False حساب می‌شن: عدد صفر، رشته خالی، لیست خالی، None، و False.'
  },

  'break': {
    en: 'BREAK', fa: 'شکستن', cat: 'ساختمان داده',
    desc: 'دستوری که وسط حلقه، حلقه رو کامل می‌شکنه و می‌زنه بیرون. مثل وقتی وسط فیلم پاشی، دیگه ادامه نمی‌دی، کامل از سینما میای بیرون.',
    example: 'for i in range(10):\n    if i == 3:\n        break\n    print(i)\n# خروجی: 0, 1, 2',
    tip: 'break فقط از یک سطح حلقه بیرون میاد. برای دو حلقه تودرتو، باید حلقه بیرونی رو با یه flag کنترل کنی.'
  },

  'caching': {
    en: 'CACHING', fa: 'کش کردن', cat: 'برنامه‌نویسی کاربردی',
    desc: 'مثل اینکه نتیجه یه محاسبه سنگین رو یه جایی نگه داری، دفعه بعد اگه همون ورودی اومد، سریع جوابش رو بدی بدون دوباره حساب کردن. مثل وقتی جواب یه سؤال رو تو دفترت نوشتی که دفعه بعد سریع پیداش کنی.',
    example: 'from functools import lru_cache\n\n@lru_cache(maxsize=128)\ndef fib(n):\n    if n < 2: return n\n    return fib(n-1) + fib(n-2)\n\nprint(fib(50))  # بدون کش ساعت‌ها طول می‌کشید!',
    tip: 'برای داده‌های شبکه‌ای از Redis یا حافظه موقت (TTL) استفاده کن تا اطلاعات قدیمی نشه.'
  },

  'chart': {
    en: 'CHART', fa: 'نمودار', cat: 'حرفه‌ای',
    desc: 'نمایش گرافیکی داده. مثل نمودار فروش ماهانه که به‌جای لیست اعداد، یه تصویر می‌بینی و سریع می‌فهمی روند چطوریه.',
    example: 'import matplotlib.pyplot as plt\nmonths = ["فروردین", "اردیبهشت", "خرداد"]\nsales = [100, 150, 200]\nplt.bar(months, sales)\nplt.title("فروش ماهانه")\nplt.show()',
    tip: 'برای هر نوع داده، نمودار مناسب انتخاب کن: روند → خطی، مقایسه → میله‌ای، سهم → دایره‌ای.'
  },

  'class': {
    en: 'CLASS', fa: 'کلاس', cat: 'مبانی',
    desc: 'مثل قالب شیرینی‌پزیه! قالب به تنهایی شیرینی نیست، ولی می‌تونی با اون هزار تا شیرینی درست کنی. کلاس هم قالب ساخت شیءهاست: ویژگی‌ها و رفتارهای مشترک رو تعریف می‌کنه.',
    example: 'class Dog:\n    def __init__(self, name):\n        self.name = name\n    def bark(self):\n        return f"{self.name} می‌گه: واق واق!"\n\nrex = Dog("رکس")   # ساخت شیء\nprint(rex.bark())',
    tip: 'اسم کلاس‌ها رو با حرف بزرگ شروع کن (PascalCase): UserProfile نه user_profile.'
  },

  'code': {
    en: 'CODE', fa: 'کد', cat: 'ساختمان داده',
    desc: 'دستوراتی که به کامپیوتر می‌دی تا کاری انجام بده. مثل دستور پخت غذا که مراحل رو یکی‌یکی می‌نویسی تا آشپز (کامپیوتر) اجرا کنه.',
    example: '# این یک خط کد است\ndef greet(name):\n    return f"سلام {name}"\n\nprint(greet("دنیا"))',
    tip: 'کد خوانا بنویس که یک آدم دیگه هم بتونه راحت بفهمه چی نوشتی. کامنت بذار!'
  },

  'comment': {
    en: 'COMMENT', fa: 'کامنت', cat: 'برنامه‌نویسی کاربردی',
    desc: 'توضیحی که برای خودت یا برنامه‌نویس‌های دیگه می‌نویسی و پایتون کاملاً نادیده می‌گیره. مثل یادداشت چسبونکی روی یخچال: کامپیوتر نمی‌خونتش، فقط انسان‌ها می‌خونن.',
    example: '# این تابع مساحت دایره رو حساب می‌کنه\ndef circle_area(r):\n    import math\n    return math.pi * r ** 2  # فرمول اصلی\n\n# کامنت چندخطی:\n"""\nاین هم docstring هست\nبرای توضیح طولانی\n"""',
    tip: 'کامنت رو توضیح بده «چرا» این کار رو کردی، نه «چی» کار می‌کنه (چی رو از خود کد می‌شه فهمید).'
  },

  'comparison': {
    en: 'COMPARISON', fa: 'مقایسه', cat: 'حرفه‌ای',
    desc: 'عملگرهایی که دو چیز رو با هم مقایسه می‌کنن و جواب True یا False می‌دن: برابر (==)، نابرابر (!=)، بزرگ‌تر (>), کوچک‌تر (<), بزرگ‌تر مساوی (>=), کوچک‌تر مساوی (<=).',
    example: 'print(5 == 5)     # True\nprint(5 != 3)     # True\nprint(10 > 3)     # True\nprint("a" < "b")  # True (ترتیب الفبا)\nprint(1 == 1.0)   # True',
    tip: 'برای چک کردن «همون شیء بودن» از is استفاده کن، نه ==. مثلاً None رو با "is None" مقایسه کن.'
  },

  'complexity': {
    en: 'COMPLEXITY', fa: 'پیچیدگی', cat: 'مبانی',
    desc: 'معیار اینکه کدت با بزرگ‌شدن ورودی، چقدر کندتر می‌شه. مثل صف نانوایی: ۱۰ نفر طول نمی‌کشه، ولی ۱۰۰۰ نفر (O(n)) خیلی طول می‌کشه. بعضی الگوریتم‌ها با هر برابر شدن ورودی، دو برابر کندتر می‌شن (O(n²)).',
    example: '# O(1) - ثابت، همیشه سریع\nvalue = my_dict["key"]\n\n# O(n) - خطی، با ورودی کندتر می‌شه\nfor item in my_list:\n    print(item)\n\n# O(n²) - درجه دوم، خیلی سریع کند می‌شه\nfor i in items:\n    for j in items:\n        print(i, j)',
    tip: 'قبل از بهینه‌سازی، اول با timeit اندازه بگیر. اینشتین می‌گفت: «زودهنگام بهینه‌کردن ریشه همه شره»!'
  },

  'composition': {
    en: 'COMPOSITION', fa: 'ترکیب', cat: 'ساختمان داده',
    desc: 'مثل اینکه یه ماشین از چرخ، موتور و صندلی ساخته شده. ماشین «شامل» این قطعه‌هاست. در برنامه‌نویسی یعنی یه کلاس داخل خودش نمونه‌های کلاس‌های دیگه رو نگه داره.',
    example: 'class Engine:\n    def start(self): return "موتور روشن شد"\n\nclass Car:\n    def __init__(self):\n        self.engine = Engine()   # ترکیب\n    def drive(self):\n        return self.engine.start()\n\nCar().drive()',
    tip: 'معمولاً «ترکیب» از «وراثت» بهتره، چون انعطاف بیشتری می‌ده و وابستگی‌ها رو کمتر می‌کنه.'
  },

  'comprehension': {
    en: 'COMPREHENSION', fa: 'فهم فشرده / درک لیستی', cat: 'برنامه‌نویسی کاربردی',
    desc: 'یه روش کوتاه و شیک که با یه خط، لیست یا دیکشنری از روی یه چیز دیگه بسازی. جای اینکه حلقه بنویسی و یکی‌یکی append کنی، همه‌چیز رو تو یه خط می‌نویسی.',
    example: '# حالت طولانی:\nsquares = []\nfor x in range(5):\n    squares.append(x ** 2)\n\n# با comprehension (همون کار، یک خط):\nsquares = [x ** 2 for x in range(5)]\n\n# با شرط:\nevens = [x for x in range(10) if x % 2 == 0]\n\n# دیکشنری:\nsq_dict = {x: x**2 for x in range(5)}',
    tip: 'اگه comprehension بیشتر از یه خط و یه شرط می‌شه، بهتره همون حلقه معمولی رو بنویسی تا خوانا بمونه.'
  },

  'condition': {
    en: 'CONDITION', fa: 'شرط', cat: 'حرفه‌ای',
    desc: 'یه جمله که جوابش بله/خیر (True/False) هست و تصمیم می‌گیره کدت کدوم مسیر رو بره. مثل چراغ راهنما: اگه سبز باشه برو، قرمز باشه بایست.',
    example: 'age = 18\nif age >= 18:\n    print("می‌تونی رانندگی کنی")\nelse:\n    print("هنوز کوچیک‌تری")\n\n# شرط ترکیبی\nif age >= 18 and has_license:\n    print("می‌تونی ماشین برونی")',
    tip: 'در پایتون این‌ها همه falsy هستن (یعنی مثل False رفتار می‌کنن): 0, "", [], {}, None, False.'
  },

  'config': {
    en: 'CONFIG', fa: 'تنظیمات', cat: 'مبانی',
    desc: 'اطلاعاتی که رفتار برنامه رو کنترل می‌کنن: آدرس دیتابیس، کلید API، حالت دیباگ. مثل تنظیمات یه دستگاه که می‌تونی عوضشون کنی بدون دست زدن به خود دستگاه.',
    example: 'import os\nfrom pathlib import Path\n\nDEBUG = os.getenv("DEBUG", "0") == "1"\nDB_URL = os.getenv("DATABASE_URL", "sqlite:///app.db")\nAPI_KEY = os.getenv("API_KEY")',
    tip: 'تنظیمات حساس (رمز، کلید) رو هرگز مستقیم تو کد ننویس. از فایل .env و os.getenv استفاده کن و .env رو تو .gitignore بذار.'
  },

  'continue': {
    en: 'CONTINUE', fa: 'ادامه بده', cat: 'ساختمان داده',
    desc: 'دستوری که وسط حلقه، از ادامه کد می‌پره و می‌ره سراغ تکرار بعدی. مثل وقتی تو صف نانوایی هستی و نوبتت می‌شه ولی می‌گی «من نمی‌خوام» و می‌ذاری نفر بعدی بره جلو.',
    example: 'for i in range(5):\n    if i % 2 == 0:\n        continue  # اعداد زوج رو رد کن\n    print(i)\n# خروجی: 1, 3',
    tip: 'continue رو بذار اول حلقه با یه شرط if تا کدت تمیزتر بشه (الگوی guard clause).'
  },

  'coroutine': {
    en: 'COROUTINE', fa: 'کوروتین', cat: 'برنامه‌نویسی کاربردی',
    desc: 'یه تابع مخصوص که می‌تونه وسط کارش «توقف» کنه و بعداً از همون‌جا ادامه بده. با async def ساخته می‌شه. مثل فیلم دیدن که وسطش وقفه می‌ندازی و فردا از همون‌جا ادامه می‌دی.',
    example: 'async def fetch_user(user_id):\n    print(f"در حال گرفتن کاربر {user_id}")\n    await asyncio.sleep(1)   # مکث می‌کنه\n    return {"id": user_id, "name": "Ali"}\n\n# اجرا:\nasyncio.run(fetch_user(1))',
    tip: 'کوروتین رو با await صدا بزن، وگرنه اجرا نمی‌شه و فقط یه warning می‌گیری.'
  },

  'coverage': {
    en: 'COVERAGE', fa: 'پوشش تست', cat: 'حرفه‌ای',
    desc: 'یه معیار که نشون می‌ده چقدر از خطوط کدت توسط تست‌ها اجرا شده. مثل اینکه معلم چک کنه تو امتحان چند تا سؤال رو جواب دادی.',
    example: '# نصب:\n# pip install coverage\n\n# اجرا:\n# coverage run -m pytest\n# coverage report\n\n# خروجی:\n# Name         Stmts   Miss  Cover\n# main.py         50      5    90%',
    tip: 'پوشش ۱۰۰٪ هدف نهایی نیست! پوشش منطق کد مهم‌تر از درصد خامه. یه تست پوشش‌داده‌شده ولی بی‌ارزش، فایده نداره.'
  },

  'crud': {
    en: 'CRUD', fa: 'چهار عمل پایه', cat: 'مبانی',
    desc: 'مخفف چهار عمل اصلی روی داده‌هاست: Create (ساختن)، Read (خوندن)، Update (ویرایش)، Delete (حذف). هر برنامه‌ای که با داده کار می‌کنه، این چهارتا رو داره.',
    example: '# Create\nINSERT INTO users (name) VALUES ("علی")\n\n# Read\nSELECT * FROM users WHERE id = 1\n\n# Update\nUPDATE users SET name = "رضا" WHERE id = 1\n\n# Delete\nDELETE FROM users WHERE id = 1',
    tip: 'در API این چهارتا معمولاً با POST, GET, PUT, DELETE انجام می‌شن.'
  },

  'csv': {
    en: 'CSV', fa: 'فایل متنی جدولی', cat: 'ساختمان داده',
    desc: 'یه فایل ساده که داده‌ها رو با کاما (,) از هم جدا می‌کنه. مثل یه جدول ساده در نوت‌پد. با اکسل می‌تونی بازش کنی، با پایتون هم.',
    example: 'import csv\n\n# نوشتن\nwith open("users.csv", "w", encoding="utf-8", newline="") as f:\n    w = csv.writer(f)\n    w.writerow(["نام", "سن"])\n    w.writerow(["علی", 30])\n\n# خوندن\nwith open("users.csv", encoding="utf-8") as f:\n    for row in csv.DictReader(f):\n        print(row)',
    tip: 'همیشه encoding="utf-8" و newline="" بذار تا تو ویندوز خط‌های اضافه نگیری.'
  },

  'dataclass': {
    en: 'DATACLASS', fa: 'کلاس داده', cat: 'برنامه‌نویسی کاربردی',
    desc: 'یه دکوراتور که خودکار برات __init__, __repr__, __eq__ می‌سازه. یعنی بجای اینکه ۲۰ خط کلاس بنویسی، تو ۳ خط خلاصه می‌شه.',
    example: 'from dataclasses import dataclass\n\n@dataclass\nclass Point:\n    x: int\n    y: int\n\np = Point(1, 2)\nprint(p)              # Point(x=1, y=2)\nprint(p == Point(1,2))  # True',
    tip: 'برای مدل‌های داده ساده (نه کلاس با رفتار پیچیده) از dataclass استفاده کن، کلی وقت صرفه‌جویی می‌کنی.'
  },

  'dataframe': {
    en: 'DATAFRAME', fa: 'دیتافریم', cat: 'حرفه‌ای',
    desc: 'جدول دو بعدی پانداس که مثل یه فایل اکسل تو پایتون کار می‌کنه. سطرها و ستون‌ها داره، می‌تونی فیلتر کنی، گروه‌بندی کنی، خیلی سریع.',
    example: 'import pandas as pd\n\ndf = pd.DataFrame({\n    "نام": ["علی", "رضا", "سارا"],\n    "سن": [30, 25, 28],\n})\nprint(df[df["سن"] > 26])\nprint(df.groupby("سن").size())',
    tip: 'برای داده‌های حجیم از dtype مناسب (int32 به‌جای int64) استفاده کن تا حافظه کم مصرف بشه.'
  },

  'datetime': {
    en: 'DATETIME', fa: 'تاریخ و زمان', cat: 'مبانی',
    desc: 'ماژول استاندارد پایتون برای کار با تاریخ و ساعت. می‌تونی زمان الان رو بگیری، به گذشته یا آینده بری، فرمت عوض کنی.',
    example: 'from datetime import datetime, timedelta\n\nnow = datetime.now()\nprint(now.strftime("%Y-%m-%d %H:%M"))\n\nnext_week = now + timedelta(days=7)\nprint(next_week.date())',
    tip: 'برای کارهای بین‌المللی همیشه از datetime همراه با timezone استفاده کن تا Daylight Saving مشکلی نسازه.'
  },

  'debug': {
    en: 'DEBUG', fa: 'اشکال‌زدایی', cat: 'ساختمان داده',
    desc: 'پیدا کردن و درست کردن باگ (خطا) در کد. مثل اینکه دنبال سوراخ لاستیک ماشین می‌گردی و پیداش می‌کنی و پنچرش می‌کنی.',
    example: 'def divide(a, b):\n    breakpoint()   # اینجا pdb باز می‌شه\n    return a / b\n\n# در pdb: print(b), n (next), c (continue), q (quit)\n\n# یا با logging:\nimport logging\nlogging.basicConfig(level=logging.DEBUG)\nlogging.debug("مقدار a: %s", 10)',
    tip: 'در VS Code روی حاشیه کنار خط کلیک کن تا breakpoint بذاری. بعد با F5 برنامه رو اجرا کن و خط‌به‌خط جلو برو.'
  },

  'dependency': {
    en: 'DEPENDENCY', fa: 'وابستگی', cat: 'برنامه‌نویسی کاربردی',
    desc: 'کتابخانه یا پکیجی که پروژه‌ات بهش نیاز داره. مثل اینکه برای پختن کیک به آرد و شکر نیاز داری. اگه نباشن، کیک درست نمی‌شه.',
    example: '# requirements.txt\nrequests==2.31.0\npandas>=2.0,<3\nfastapi[all]\n\n# نصب همه:\n# pip install -r requirements.txt',
    tip: 'همیشه نسخه‌ها رو قفل کن (pin) تا در سیستم‌های مختلف رفتار یکسان داشته باشه. از pip-tools یا poetry استفاده کن.'
  },

  'deployment': {
    en: 'DEPLOYMENT', fa: 'استقرار', cat: 'حرفه‌ای',
    desc: 'انتشار برنامه‌ات رو سروری که بقیه بتونن استفاده کنن. مثل وقتی غذا رو تو آشپزخونه درست کردی، حالا میاری جلو مشتری بذاری.',
    example: '# ساخت image داکر\nFROM python:3.12-slim\nWORKDIR /app\nCOPY requirements.txt .\nRUN pip install -r requirements.txt\nCOPY . .\nCMD ["python", "main.py"]\n\n# اجرا:\n# docker build -t myapp .\n# docker run -p 8000:8000 myapp',
    tip: 'قبل از deploy حتماً: تست‌ها رو اجرا کن، مهاجرت‌های دیتابیس رو انجام بده، متغیرهای محیطی رو چک کن.'
  },

  'design-pattern': {
    en: 'DESIGN-PATTERN', fa: 'الگوی طراحی', cat: 'مبانی',
    desc: 'راه‌حل‌های آماده و آزموده‌شده برای مسائل تکرارشونده. مثل دستور پخت‌های استاندارد که هر آشپز حرفه‌ای بلده. مثل Singleton، Factory، Observer.',
    example: '# الگوی Singleton\nclass Database:\n    _instance = None\n    def __new__(cls):\n        if cls._instance is None:\n            cls._instance = super().__new__(cls)\n        return cls._instance\n\nd1, d2 = Database(), Database()\nprint(d1 is d2)  # True',
    tip: 'الگو فقط وقتی به‌کار ببر که مشکل واقعاً اون الگو رو می‌طلبه. زیاده‌روی = پیچیدگی بی‌دلیل.'
  },

  'dictionary': {
    en: 'DICTIONARY', fa: 'دیکشنری', cat: 'ساختمان داده',
    desc: 'یه مجموعه از جفت‌های کلید-مقدار. مثل دفترچه تلفن: با گرفتن اسم (کلید)، شماره تلفن (مقدار) رو پیدا می‌کنی. جست‌وجو توش خیلی سریعه.',
    example: 'person = {"name": "علی", "age": 30, "city": "تهران"}\nprint(person["name"])              # علی\nprint(person.get("email", "نداره"))  # نداره\nperson["email"] = "ali@example.com"  # اضافه کردن\nfor k, v in person.items():\n    print(k, ":", v)',
    tip: 'از پایتون 3.7 به بعد، ترتیب درج اعضا حفظ می‌شه. برای مقادیر پیش‌فرض از .get() استفاده کن نه []'
  },

  'docker': {
    en: 'DOCKER', fa: 'داکر', cat: 'برنامه‌نویسی کاربردی',
    desc: 'یه ابزار که برنامه‌ات رو همراه با همه وابستگی‌هاش تو یه بسته (کنتینر) می‌ذاره. مثل اینکه کل آشپزخونه رو با خودت ببری هرجا، دیگه تو هر خونه‌ای بتونی همون غذا رو درست کنی.',
    example: '# Dockerfile\nFROM python:3.12-slim\nWORKDIR /app\nCOPY requirements.txt .\nRUN pip install --no-cache-dir -r requirements.txt\nCOPY . .\nEXPOSE 8000\nCMD ["uvicorn", "main:app", "--host", "0.0.0.0"]',
    tip: 'لایه‌ها رو طوری بچین که کش مؤثر باشه: اول requirements (کم تغییر می‌کنه)، بعد کد پروژه.'
  },

  'docstring': {
    en: 'DOCSTRING', fa: 'مستند کد', cat: 'حرفه‌ای',
    desc: 'توضیحاتی که با """ (سه تا کوتیشن) داخل تابع یا کلاس می‌نویسی و پایتون ازش برای راهنما (help) استفاده می‌کنه. مثل برچسب پشت جعبه که می‌گه داخلش چیه.',
    example: 'def divide(a: float, b: float) -> float:\n    """تقسیم دو عدد.\n\n    Args:\n        a: صورت کسر\n        b: مخرج (نباید صفر باشه)\n\n    Returns:\n        حاصل تقسیم\n\n    Raises:\n        ZeroDivisionError: اگه b صفر باشه\n    """\n    return a / b\n\nhelp(divide)  # توضیحات نمایش داده می‌شه',
    tip: 'از سبک Google یا NumPy برای docstring استفاده کن — ابزارهای مستندسازی این سبک‌ها رو می‌شناسن.'
  },

  'elif': {
    en: 'ELIF', fa: 'وگرنه اگر', cat: 'مبانی',
    desc: 'میان‌بری «else if». وقتی می‌خوای چند تا شرط پشت سر هم چک کنی: اگه شرط اول درست نبود، شرط دوم رو چک کن، اگه اونم نبود، شرط سوم و... .',
    example: 'score = 85\nif score >= 90:\n    grade = "A"\nelif score >= 80:\n    grade = "B"\nelif score >= 70:\n    grade = "C"\nelse:\n    grade = "F"\nprint(grade)  # B',
    tip: 'ترتیب شرط‌ها مهمه! شرط سخت‌گیرانه‌تر رو اول بذار: if x > 100 قبل از if x > 50.'
  },

  'else': {
    en: 'ELSE', fa: 'وگرنه', cat: 'ساختمان داده',
    desc: 'شاخه‌ای که وقتی هیچ‌کدوم از شرط‌های قبلی درست نبودن اجرا می‌شه. مثل «اگه بارون اومد چتر ببر، وگرنه کلاه بذار».',
    example: 'x = 5\nif x > 10:\n    print("بزرگ")\nelse:\n    print("کوچیک")\n\n# else روی حلقه for: وقتی break نخورده باشه\nfor n in [2, 4, 6]:\n    if n % 2: break\nelse:\n    print("همه زوج بودن")',
    tip: 'else روی حلقه (for/while) فقط وقتی اجرا می‌شه که break رخ نداده باشه. یه ویژگی خاص و مفید پایتونه!'
  },

  'encoding': {
    en: 'ENCODING', fa: 'رمزگذاری', cat: 'برنامه‌نویسی کاربردی',
    desc: 'روشی که کاراکترها (مثل ا، ب، پ) به بایت‌ها (۰ و ۱) تبدیل می‌شن و برعکس. UTF-8 استانداردی که همه‌جا کار می‌کنه.',
    example: 'with open("file.txt", "r", encoding="utf-8") as f:\n    text = f.read()\n\nwith open("out.txt", "w", encoding="utf-8") as f:\n    f.write("سلام دنیا 🌍")',
    tip: 'همیشه encoding="utf-8" بذار. اگه نذاری، تو ویندوز ممکنه حروف فارسی به هم بریزه.'
  },

  'environment': {
    en: 'ENVIRONMENT', fa: 'محیط', cat: 'حرفه‌ای',
    desc: 'دو معنی داره: ۱) جایی که برنامه اجرا می‌شه (development, testing, production). ۲) متغیرهای محیطی که تنظیمات رو از کد جدا می‌کنن.',
    example: 'import os\n\n# حالت اجرا\nENV = os.getenv("ENV", "development")\n\n# تنظیمات خاص هر محیط\nif ENV == "production":\n    DEBUG = False\n    DB_URL = os.getenv("PROD_DB_URL")\nelse:\n    DEBUG = True\n    DB_URL = "sqlite:///dev.db"',
    tip: 'فایل .env رو تو گیت نذار. یه .env.example بساز که قالب رو نشون بده بدون اطلاعات حساس.'
  },

  'error': {
    en: 'ERROR', fa: 'خطا', cat: 'مبانی',
    desc: 'وقتی کد یه مشکلی داره و نمی‌تونه درست اجرا شه. انواع مختلف داره: خطای نحوی (SyntaxError)، خطای نوع (TypeError)، خطای مقدار (ValueError) و... .',
    example: 'try:\n    x = int("abc")   # ValueError\nexcept ValueError as e:\n    print(f"خطا: {e}")\n\ntry:\n    result = 10 / 0   # ZeroDivisionError\nexcept ZeroDivisionError:\n    print("تقسیم بر صفر مجاز نیست")',
    tip: 'پیام خطا رو کامل و با دقت بخون! شماره خط و نوع خطا نصف راه‌حل هستن.'
  },

  'except': {
    en: 'EXCEPT', fa: 'به‌جز / مگر', cat: 'ساختمان داده',
    desc: 'بخشی از try/except که خطاها رو می‌گیره و مدیریت می‌کنه. مثل تور نجات آتش‌نشانی که وقتی کسی پرید، نجاتش می‌ده.',
    example: 'try:\n    data = fetch_data()\nexcept TimeoutError:\n    print("اتصال قطع شد")\nexcept (ValueError, KeyError) as e:\n    print(f"خطای داده: {e}")\nexcept Exception as e:\n    print(f"خطای غیرمنتظره: {e}")',
    tip: 'همیشه خطای مشخص بگیر. except خالی تمام خطاها رو قایم می‌کنه و دیباگ رو جهنم می‌کنه!'
  },

  'exception': {
    en: 'EXCEPTION', fa: 'استثنا', cat: 'برنامه‌نویسی کاربردی',
    desc: 'رخدادی که وسط اجرای برنامه پیش میاد و اگه مدیریت نشه، برنامه کرش می‌کنه. مثل اینکه وسط رانندگی لاستیک پنچر بشه — یا مدیریتش می‌کنی یا ماشین می‌ایسته.',
    example: 'class InsufficientBalance(Exception):\n    pass\n\ndef withdraw(balance, amount):\n    if amount > balance:\n        raise InsufficientBalance(f"موجودی {balance} کمتر از {amount} است")\n    return balance - amount',
    tip: 'برای خطاهای خاص برنامه‌ات، exception اختصاصی بساز که از Exception ارث‌بری کنه.'
  },

  'expression': {
    en: 'EXPRESSION', fa: 'عبارت', cat: 'حرفه‌ای',
    desc: 'ترکیبی از مقادیر، متغیرها و عملگرها که یه مقدار تولید می‌کنه. مثل «۲ + ۳» که می‌شه ۵. هر چیزی که بشه مقدارش رو حساب کرد، عبارت هست.',
    example: 'x = 5                     # این یه statement هست\nresult = x * 2 + 3        # این یه expression هست\ntext = "سلام" + " دنیا"   # اینم expression\nflag = x > 3 and x < 10   # اینم expression',
    tip: 'عبارت (expression) همیشه یه مقدار داره. دستور (statement) یه کار انجام می‌ده (مثل print یا if).'
  },

  'f-string': {
    en: 'F-STRING', fa: 'اف‌استرینگ', cat: 'مبانی',
    desc: 'روش مدرن و راحت برای اینکه متغیرها رو داخل رشته بذاری. فقط یه f قبل از رشته می‌ذاری و متغیرها رو داخل {} می‌نویسی.',
    example: 'name = "علی"\nage = 30\nprint(f"سلام {name}! سن شما {age} ساله")\n\n# محاسبه مستقیم:\nprint(f"سال بعد: {age + 1}")\n\n# فرمت اعداد:\nprice = 1234.5678\nprint(f"قیمت: {price:,.2f} تومان")  # 1,234.57',
    tip: 'اف‌استرینگ از format() و % سریع‌تر و خواناتره. همیشه ازش استفاده کن.'
  },

  'fastapi': {
    en: 'FASTAPI', fa: 'فست‌ای‌پی‌آی', cat: 'ساختمان داده',
    desc: 'یه فریم‌ورک مدرن پایتون برای ساخت API (سرویس‌های وب). چون از type hint استفاده می‌کنه، سریع و امنه و مستندات خودکار می‌سازه.',
    example: 'from fastapi import FastAPI\n\napp = FastAPI()\n\n@app.get("/users/{user_id}")\ndef get_user(user_id: int):\n    return {"id": user_id, "name": "Ali"}\n\n# اجرا: uvicorn main:app --reload\n# مستندات خودکار در: http://localhost:8000/docs',
    tip: 'مستندات خودکار در /docs ساخته می‌شه — برای تست API معرکه‌ست!'
  },

  'file': {
    en: 'FILE', fa: 'فایل', cat: 'برنامه‌نویسی کاربردی',
    desc: 'یه منبع داده روی دیسک که می‌تونی بخونی یا توش بنویسی. مثل دفتر یادداشتی که بازش می‌کنی، چیزی می‌نویسی یا می‌خونی، بعد می‌بندیش.',
    example: '# نوشتن\nwith open("data.txt", "w", encoding="utf-8") as f:\n    f.write("سلام دنیا")\n\n# خوندن\nwith open("data.txt", "r", encoding="utf-8") as f:\n    content = f.read()\n    print(content)\n\n# خوندن خط‌به‌خط\nwith open("data.txt") as f:\n    for line in f:\n        print(line.strip())',
    tip: 'همیشه از with استفاده کن — خودش فایل رو می‌بنده حتی اگه خطا پیش بیاد.'
  },

  'finally': {
    en: 'FINALLY', fa: 'در نهایت', cat: 'حرفه‌ای',
    desc: 'بلوکی که بعد از try/except، در هر شرایطی اجرا می‌شه: چه خطا بده، چه نده. برای کارهای پاک‌سازی عالیه.',
    example: 'f = open("data.txt")\ntry:\n    data = f.read()\n    process(data)\nexcept IOError:\n    print("خطای خوندن")\nfinally:\n    f.close()   # این همیشه اجرا می‌شه',
    tip: 'با دستور with خیلی از کارهای finally خودکار انجام می‌شه، ولی finally برای کارهای خاص مثل بستن کانکشن مفیده.'
  },

  'fixture': {
    en: 'FIXTURE', fa: 'تدارکات تست', cat: 'مبانی',
    desc: 'یه تابع که آماده‌سازی‌های لازم برای تست رو انجام می‌ده: نمونه داده می‌سازه، دیتابیس تست رو بالا می‌آره، فایل موقت درست می‌کنه.',
    example: 'import pytest\n\n@pytest.fixture\ndef sample_user():\n    return {"name": "Ali", "age": 30}\n\n@pytest.fixture\ndef db():\n    conn = create_test_db()\n    yield conn          # تست‌ها اینجا اجرا می‌شن\n    conn.close()        # تمیزکاری\n\ndef test_greet(sample_user, db):\n    assert sample_user["name"] == "Ali"',
    tip: 'fixture باعث می‌شه کد آماده‌سازی رو یه بار بنویسی و تو همه تست‌ها استفاده کنی.'
  },

  'float': {
    en: 'FLOAT', fa: 'عدد اعشاری', cat: 'ساختمان داده',
    desc: 'عددی با اعشار: 3.14، 0.5، 1.5e10. مثل خط‌کشی که بین واحدها رو هم نشون می‌ده، نه فقط ۱ و ۲ و ۳.',
    example: 'pi = 3.14159\nprice = 19.99\nvery_small = 1.5e-10\n\nprint(pi, price)\nprint(round(pi, 2))    # 3.14\n\n# مقایسه‌ها:\nprint(0.1 + 0.2)       # 0.30000000000000004 (نه 0.3!)',
    tip: 'برای اعداد مالی از float استفاده نکن! از decimal.Decimal یا int (سنت) استفاده کن، چون float خطای گرد کردن داره.'
  },

  'formatter': {
    en: 'FORMATTER', fa: 'قالب‌بند', cat: 'برنامه‌نویسی کاربردی',
    desc: 'یه ابزار که کدت رو یه‌دست و مرتب می‌کنه: فاصله‌ها، خطوط بلند، ترتیب importها و... . مثل یه تایپیست که دفترت رو تمیز می‌نویسه.',
    example: '# نصب:\n# pip install black ruff\n\n# استفاده:\n# black .\n# ruff format .\n\n# قبل:           بعد از black:\ndef add(a,b):   def add(a, b):\n  return a+b        return a + b',
    tip: 'black رو در pre-commit hook بذار تا هر کامیت خودکار فرمت بشه. دیگه نگران سبک کد نباش!'
  },

  'function': {
    en: 'FUNCTION', fa: 'تابع', cat: 'حرفه‌ای',
    desc: 'یه بلوک کد که یه کار مشخص انجام می‌ده و می‌تونی چند بار صداش بزنی. مثل دکمه‌ای که هر بار بزنی، یه کار انجام می‌شه بدون اینکه دوباره کد بنویسی.',
    example: 'def greet(name="دنیا"):\n    """احوال‌پرسی ساده"""\n    return f"سلام {name}!"\n\nprint(greet())          # سلام دنیا!\nprint(greet("علی"))     # سلام علی!\n\n# با نوع و پارامتر پیش‌فرض\ndef power(base: int, exp: int = 2) -> int:\n    return base ** exp',
    tip: 'هر تابع فقط یه کار بکنه (Single Responsibility). اگه تابعی اسمش «and» داشت، دو تا تابع بشه!'
  },

  'generator': {
    en: 'GENERATOR', fa: 'مولد', cat: 'مبانی',
    desc: 'تابعی که به‌جای return از yield استفاده می‌کنه. مقادیر رو یکی‌یکی و تنبل (lazy) تولید می‌کنه، نه همه رو یه جا. برای داده‌های حجیم عالیه چون حافظه کم مصرف می‌کنه.',
    example: 'def countdown(n):\n    while n > 0:\n        yield n      # یک مقدار بده و توقف کن\n        n -= 1\n\nfor x in countdown(3):\n    print(x)         # 3, 2, 1\n\n# مزیت: میلیون‌ها عدد رو با حافظه کم\nbig = (x**2 for x in range(10_000_000))',
    tip: 'اگه داده‌ای خیلی بزرگه یا از فایل/شبکه می‌خونی، generator بجای list خیلی حافظه صرفه‌جویی می‌کنه.'
  },

  'groupby': {
    en: 'GROUPBY', fa: 'گروه‌بندی', cat: 'ساختمان داده',
    desc: 'عملیات پانداس که سطرها رو بر اساس یه ستون گروه می‌کنه و روشون محاسبه انجام می‌ده. مثل اینکه تو اکسل جدول بزنی و بر اساس شهر، میانگین سن رو دربیاری.',
    example: 'df.groupby("dept")["salary"].mean()\n\n# چند سطحی:\ndf.groupby(["dept", "city"]).agg({\n    "salary": "sum",\n    "age": "mean",\n    "name": "count",\n})',
    tip: 'برای سرعت بیشتر، قبل از groupby داده رو با فیلتر کوچک‌تر کن. الکی همه رو گروه‌بندی نکن!'
  },

  'hash': {
    en: 'HASH', fa: 'درهم‌سازی', cat: 'برنامه‌نویسی کاربردی',
    desc: 'یه تابع که هر ورودی رو به یه عدد با طول ثابت تبدیل می‌کنه. مهمه که برگشت‌پذیر نباشه: از hash می‌تونی مقدار اصلی رو دربیاری. برای ذخیره رمز عبور عالیه.',
    example: 'h = hash("hello")\nprint(h)   # مثلاً 1234567890123456789\n\n# برای رمز عبور:\nimport hashlib\nprint(hashlib.sha256(b"password").hexdigest())\n\n# بهتر: bcrypt یا argon2\n# from passlib.hash import bcrypt\n# bcrypt.hash("password")',
    tip: 'برای رمز عبور هرگز از SHA ساده استفاده نکن! از bcrypt یا argon2 استفاده کن که کندن و مقاوم در برابر brute-force.'
  },

  'http': {
    en: 'HTTP', fa: 'پروتکل وب', cat: 'حرفه‌ای',
    desc: 'قانونِ حرف زدنِ مرورگر با سرورها. یه درخواست می‌فرستی (مثل «صفحه اصلی رو بده») و سرور یه پاسخ می‌ده (صفحه اصلی با یه کد وضعیت).',
    example: '# درخواست\nGET /users?limit=10 HTTP/1.1\nHost: api.example.com\nAccept: application/json\nAuthorization: Bearer TOKEN\n\n# پاسخ\nHTTP/1.1 200 OK\nContent-Type: application/json\n\n{"users": [...]}',
    tip: 'همیشه از HTTPS (نه HTTP ساده) استفاده کن، چون HTTP ساده اطلاعات رو متن‌باز می‌فرسته.'
  },

  'indentation': {
    en: 'INDENTATION', fa: 'تورفتگی', cat: 'مبانی',
    desc: 'فاصله‌گذاری ابتدای خط. تو پایتون برخلاف خیلی از زبان‌ها که از { } استفاده می‌کنن، تورفتگی مشخص می‌کنه کد داخل کدوم بلوکه. مثل پله‌های یه ساختمون که مشخص می‌کنن هر طبقه کجاست.',
    example: 'if True:\n    print("این توئه")       # ۴ فاصله\n    if True:\n        print("اینم توئه")   # ۸ فاصله\nprint("این بیرونه")           # ۰ فاصله',
    tip: 'PEP 8 می‌گه ۴ تا فاصله (space) برای هر سطح تورفتگی. هرگز با Tab و Space قاطی نکن!'
  },

  'indexing': {
    en: 'INDEXING', fa: 'اندیس‌گذاری', cat: 'ساختمان داده',
    desc: 'دسترسی به یه عنصر خاص از دنباله با شماره‌اش. از صفر شروع می‌شه، و اندیس منفی از آخر می‌شماره. مثل اینکه تو صف بگی «نفر سوم» یا «نفر آخر».',
    example: 'xs = [10, 20, 30, 40, 50]\nprint(xs[0])     # 10 (اولین)\nprint(xs[2])     # 30 (سومین)\nprint(xs[-1])    # 50 (آخرین)\nprint(xs[-2])    # 40 (یکی به آخر)\n\ns = "پایتون"\nprint(s[0])      # پ\nprint(s[-1])     # ن',
    tip: 'اگه اندیسی خارج از محدوده بدی، IndexError می‌گیری. همیشه طول رو چک کن یا از try/except استفاده کن.'
  },

  'inheritance': {
    en: 'INHERITANCE', fa: 'وراثت', cat: 'برنامه‌نویسی کاربردی',
    desc: 'یکی از مفاهیم شیءگرایی. کلاس فرزند همه ویژگی‌ها و رفتارهای کلاس پدر رو به ارث می‌بره و می‌تونه اون‌ها رو تغییر بده یا چیز جدید اضافه کنه. مثل ارث بردن چشم و ابرو از پدر و مادر!',
    example: 'class Animal:\n    def __init__(self, name):\n        self.name = name\n    def speak(self):\n        return "... (صدای نامعلوم)"\n\nclass Dog(Animal):              # ارث‌بری\n    def speak(self):            # بازنویسی\n        return f"{self.name}: واق واق"\n\nrex = Dog("رکس")\nprint(rex.speak())',
    tip: 'برای صدا زدن پدر از super() استفاده کن: super().__init__(name). اینطوری تغییرات پدر به فرزند ارث می‌رسه.'
  },

  'injection': {
    en: 'INJECTION', fa: 'تزریق', cat: 'حرفه‌ای',
    desc: 'یه نوع حمله که هکر کد مخرب رو بجای داده وارد سیستم می‌کنه. معروف‌ترینش SQL Injection هست: کاربر بجای اسم، یه دستور SQL وارد می‌کنه که دیتابیست رو نابود می‌کنه.',
    example: '# ❌ نادرست - آسیب‌پذیر\nname = request.form["name"]\nquery = f"SELECT * FROM users WHERE name = \'{name}\'"\n# اگه name = "x\' OR \'1\'=\'1" باشه → همه رکوردها لو می‌ره!\n\n# ✅ درست - parameterized\nquery = "SELECT * FROM users WHERE name = ?"\ncur.execute(query, (name,))',
    tip: 'هرگز رشته رو مستقیم تو SQL نذار. همیشه از placeholder (?) یا پارامتر bind‌شده استفاده کن.'
  },

  'install': {
    en: 'INSTALL', fa: 'نصب', cat: 'مبانی',
    desc: 'قرار دادن پایتون یا یه کتابخانه روی سیستم. مثل نصب یه اپلیکیشن روی گوشی: یه فایل رو دانلود می‌کنی و روی سیستم می‌نشونی.',
    example: '# نصب پایتون: از python.org دانلود کن\n# یا:\n# Windows: winget install Python.Python.3.12\n# Mac: brew install python@3.12\n# Linux: sudo apt install python3.12\n\n# نصب کتابخانه:\npip install requests pandas django\npip install "django>=4.2,<5"',
    tip: 'در ویندوز هنگام نصب پایتون، گزینه «Add Python to PATH» رو تیک بزن، وگرنه دستور python تو ترمینال کار نمی‌کنه.'
  },

  'int': {
    en: 'INT', fa: 'عدد صحیح', cat: 'ساختمان داده',
    desc: 'عدد بدون اعشار: -3، 0، 42، 1000. تو پایتون 3 محدودیت اندازه نداره و می‌تونی میلیون‌ها رقم رو ذخیره کنی.',
    example: 'x = 42\ny = -7\nz = 10 ** 100       # عدد خیلی بزرگ، مشکلی نیست\n\nprint(type(x))       # <class "int">\nprint(int("123"))    # 123\nprint(int(3.9))      # 3 (برش به سمت صفر)\nprint(10 // 3)       # 3 (تقسیم صحیح)',
    tip: 'تبدیل float به int همیشه به سمت صفر برش می‌ده: int(3.9) = 3 و int(-3.9) = -3.'
  },

  'interpreter': {
    en: 'INTERPRETER', fa: 'مفسر', cat: 'برنامه‌نویسی کاربردی',
    desc: 'برنامه‌ای که کد پایتون رو خط‌به‌خط می‌خونه و اجرا می‌کنه. برخلاف C که کد رو اول کامپایل می‌کنه، پایتون هر خط رو همون‌جا اجرا می‌کنه. مثل مترجم همزمان که حرف‌ها رو لحظه‌ای ترجمه می‌کنه.',
    example: '# اجرای فایل:\npython my_script.py\n\n# حالت تعاملی (REPL):\npython\n>>> 2 + 3\n5\n>>> exit()\n\n# بررسی نسخه:\npython --version',
    tip: 'حالت تعاملی (REPL) برای آزمایش سریع یه قطعه کد کوتاه فوق‌العاده‌ست.'
  },

  'iterable': {
    en: 'ITERABLE', fa: 'پیمایش‌پذیر', cat: 'حرفه‌ای',
    desc: 'هر چیزی که بشه باهاش حلقه for زد. لیست، تاپل، رشته، دیکشنری، set، generator همه iterable هستن. مثل یه کیف که می‌تونی اشیاء داخلش رو یکی‌یکی دربیاری.',
    example: 'for c in "abc":\n    print(c)\n\nfor k in {"a": 1, "b": 2}:\n    print(k)\n\nfor x in [10, 20]:\n    print(x)\n\nfor i in range(3):\n    print(i)',
    tip: 'اگه می‌خوای چک کنی یه شیء iterable هست یا نه، از iter() استفاده کن. اگه خطا نده، iterable هست.'
  },

  'iterator': {
    en: 'ITERATOR', fa: 'پیمایشگر', cat: 'مبانی',
    desc: 'یه شیء که یه‌یکی اعضای یه مجموعه رو بهت می‌ده. با next() عنصر بعدی رو می‌گیری. وقتی تموم بشه، StopIteration خطا می‌ده. مثل کشیدن کارت از یه دسته کارت: هر بار یه کارت.',
    example: 'it = iter([1, 2, 3])\nprint(next(it))   # 1\nprint(next(it))   # 2\nprint(next(it))   # 3\nprint(next(it))   # StopIteration\n\n# iterator یه‌بارمصرفه:\nxs = [1, 2, 3]\nit = iter(xs)\nlist(it)  # [1, 2, 3]\nlist(it)  # [] ← خالی!',
    tip: 'iterator یه‌بارمصرفه. اگه دو بار لازمش داری، از لیست کامل استفاده کن یا دوباره iter() رو صدا بزن.'
  },

  'json': {
    en: 'JSON', fa: 'جیسون', cat: 'ساختمان داده',
    desc: 'یه قالب متنی ساده برای تبادل داده بین برنامه‌ها. شبیه دیکشنری پایتون می‌مونه: کلید-مقدار. تمام APIهای مدرن ازش استفاده می‌کنن.',
    example: 'import json\n\n# تبدیل دیکشنری به رشته JSON\nuser = {"name": "علی", "age": 30}\ns = json.dumps(user, ensure_ascii=False)\nprint(s)  # {"name": "علی", "age": 30}\n\n# برعکس\ndata = json.loads(\'{"x": 1, "y": 2}\')\nprint(data["x"])\n\n# با فایل\nwith open("user.json", "w", encoding="utf-8") as f:\n    json.dump(user, f, ensure_ascii=False, indent=2)',
    tip: 'ensure_ascii=False بذار تا حروف فارسی راحت خونده بشن، نه کدهای \u0600.'
  },

  'key': {
    en: 'KEY', fa: 'کلید', cat: 'برنامه‌نویسی کاربردی',
    desc: 'شناسه‌ای که در دیکشنری به یه مقدار اشاره می‌کنه. مثل برچسب رو شیشه مربا: با دیدن برچسب، می‌دونی داخلش چیه.',
    example: 'd = {"name": "علی", "age": 30}\nprint(d["name"])       # علی\n\n# کلیدهای پیچیده:\nd2 = {(1, 2): "نقطه", "x": 1}\n\n# کلیدها باید hashable باشن (تغییرناپذیر)\n# d3 = {[1, 2]: "invalid"}  ← TypeError',
    tip: 'کلید می‌تونه رشته، عدد، tuple، bool یا None باشه. لیست و دیکشنری نمی‌تونن کلید باشن!'
  },

  'lint': {
    en: 'LINT', fa: 'لینت / بازرسی کد', cat: 'حرفه‌ای',
    desc: 'ابزاری که کدت رو بررسی می‌کنه و خطاها، کد مرده، سبک نادرست و باگ‌های احتمالی رو نشون می‌ده. مثل یه ویراستار که قبل از چاپ کتاب، غلط‌ها رو پیدا می‌کنه.',
    example: '# نصب:\n# pip install ruff\n\n# بررسی:\n# ruff check .\n\n# رفع خودکار:\n# ruff check --fix .\n\n# نمونه خروجی:\n# main.py:5:1: F401 "os" imported but unused\n# main.py:10:9: E501 Line too long (95 > 88)',
    tip: 'ruff سریع‌ترین و جامع‌ترین گزینه امروز است. جای flake8، isort و خیلی ابزارهای دیگه رو می‌گیره.'
  },

  'list': {
    en: 'LIST', fa: 'لیست', cat: 'مبانی',
    desc: 'دنباله‌ای از اشیاء که ترتیب داره و می‌تونی تغییرش بدی. مثل یه لیست خرید: می‌تونی چیز جدید اضافه کنی، حذف کنی، یا وسطش چیزی بذاری.',
    example: 'fruits = ["سیب", "موز", "پرتقال"]\nfruits.append("انگور")           # اضافه به آخر\nfruits.insert(1, "گیلاس")        # اضافه به وسط\nfruits.remove("موز")             # حذف\nfruits[0] = "هلو"                # تغییر\n\nprint(fruits[0])                 # هلو\nprint(fruits[-1])                # انگور\nprint(len(fruits))               # تعداد',
    tip: 'برای کپی مستقل: xs.copy() یا xs[:] — نه "ys = xs" که هر دو به یه لیست اشاره می‌کنن.'
  },

  'logging': {
    en: 'LOGGING', fa: 'ثبت رویداد / لاگ', cat: 'ساختمان داده',
    desc: 'به‌جای print، از logging استفاده می‌کنی تا پیام‌ها رو با سطح اهمیت (info، warning، error) و زمان، در فایل یا کنسول ثبت کنی. حرفه‌ای‌تر از پرینت‌های معمولیه.',
    example: 'import logging\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format="%(asctime)s [%(levelname)s] %(message)s",\n    filename="app.log",\n)\nlog = logging.getLogger(__name__)\n\nlog.debug("جزئیات فنی")\nlog.info("کاربر وارد شد")\nlog.warning("دیسک تقریباً پر")\nlog.error("خطا در پرداخت")\nlog.critical("سیستم قطع شد!")',
    tip: 'در production از print استفاده نکن. logging بهت اجازه می‌ده بدون تغییر کد، سطح لاگ رو کنترل کنی.'
  },

  'loop': {
    en: 'LOOP', fa: 'حلقه', cat: 'برنامه‌نویسی کاربردی',
    desc: 'دستوری که یه بلوک کد رو چند بار تکرار می‌کنه. پایتون دو نوع حلقه داره: for (روی یه مجموعه) و while (تا وقتی شرط درسته).',
    example: '# for - روی یه لیست\nfor fruit in ["سیب", "موز"]:\n    print(fruit)\n\n# with index\nfor i, fruit in enumerate(["سیب", "موز"]):\n    print(i, fruit)\n\n# while - تا وقتی شرط درسته\nn = 5\nwhile n > 0:\n    print(n)\n    n -= 1',
    tip: 'اگه تعداد تکرارها رو می‌دونی، for. اگه به یه شرط بسته‌ست، while.'
  },

  'matplotlib': {
    en: 'MATPLOTLIB', fa: 'مت‌پلات‌لیب', cat: 'حرفه‌ای',
    desc: 'کتابخانه اصلی رسم نمودار در پایتون. با چند خط کد می‌تونی هر نوع نموداری بکشی: خطی، میله‌ای، پراکندگی، هیستوگرام.',
    example: 'import matplotlib.pyplot as plt\n\nx = [1, 2, 3, 4, 5]\ny = [2, 4, 6, 8, 10]\n\nfig, ax = plt.subplots()\nax.plot(x, y, marker="o")\nax.set_xlabel("X")\nax.set_ylabel("Y")\nax.set_title("نمودار خطی")\nax.grid(True)\nplt.savefig("chart.png", dpi=150)\nplt.show()',
    tip: 'برای ذخیره با کیفیت بالا dpi=150 یا بالاتر بذار. برای محیط بدون نمایشگر از matplotlib.use("Agg") استفاده کن.'
  },

  'method': {
    en: 'METHOD', fa: 'متد', cat: 'مبانی',
    desc: 'تابعی که به یه کلاس چسبیده. فرقش با تابع آزاد اینه که متد به self دسترسی داره و روی داده‌های نمونه کار می‌کنه.',
    example: 'text = "hello world"\nprint(text.upper())        # HELLO WORLD\nprint(text.split())        # ["hello", "world"]\nprint(text.replace("h", "H"))\n\nclass Counter:\n    def __init__(self):\n        self.n = 0\n    def inc(self):          # این یه متده\n        self.n += 1',
    tip: 'متد روی نمونه (obj.method()) یا روی کلاس (@classmethod) یا مستقل از هر دو (@staticmethod) می‌تونه باشه.'
  },

  'mock': {
    en: 'MOCK', fa: 'شیء شبیه‌ساز / ماک', cat: 'ساختمان داده',
    desc: 'در تست‌ها، بجای صدا زدن یه سرویس واقعی (مثل API خارجی)، یه نسخه تقلبی جاش می‌ذاری که خودت کنترلش می‌کنی. مثل اینکه تو فیلم، بجای بازیگر واقعی از بدل استفاده کنن.',
    example: 'from unittest.mock import patch, MagicMock\n\n@patch("myapp.requests.get")\ndef test_api(mock_get):\n    mock_get.return_value.json.return_value = {"id": 1}\n    result = fetch_user(1)\n    assert result["id"] == 1\n\n# mock یک سرویس پولی:\n@patch("myapp.payment.charge")\ndef test_checkout(mock_charge):\n    mock_charge.return_value = {"status": "ok"}\n    assert buy_item()["status"] == "ok"',
    tip: 'فقط چیزهایی رو mock کن که خارج از مرز برنامه‌ان (API، دیتابیس، فایل). منطق درونی رو تست کن.'
  },

  'module': {
    en: 'MODULE', fa: 'ماژول', cat: 'برنامه‌نویسی کاربردی',
    desc: 'هر فایل .py یه ماژوله. می‌تونی کدت رو تو چند فایل جدا کنی و از هر کدوم import کنی. مثل اینکه کتابت رو به فصل‌ها تقسیم کنی تا مدیریتش راحت‌تر بشه.',
    example: '# utils.py\ndef add(a, b):\n    return a + b\n\ndef multiply(a, b):\n    return a * b\n\n# main.py\nimport utils\nprint(utils.add(2, 3))\n\n# یا:\nfrom utils import add, multiply\nprint(add(2, 3))',
    tip: 'نام ماژول‌ها رو با حروف کوچک و _ بنویس (PEP 8): user_service.py نه UserService.py.'
  },

  'mutable': {
    en: 'MUTABLE', fa: 'تغییرپذیر', cat: 'حرفه‌ای',
    desc: 'اشیائی که می‌شه محتواشون رو بعد از ساخت عوض کرد: list، dict، set. مخالفش immutable هست: str، tuple، int.',
    example: 'a = [1, 2]\nb = a              # هر دو به یه لیست اشاره می‌کنن\nb.append(3)\nprint(a)           # [1, 2, 3] ← a هم تغییر کرد!\n\nc = a.copy()       # کپی مستقل\nc.append(4)\nprint(a)           # [1, 2, 3] ← a تغییر نکرد\nprint(c)           # [1, 2, 3, 4]',
    tip: 'مقدار پیش‌فرض تابع رو هرگز mutable نذار! "def f(xs=[])" یه دام خطرناکه. از None استفاده کن.'
  },

  'namespace': {
    en: 'NAMESPACE', fa: 'فضای نام', cat: 'مبانی',
    desc: 'محلی که اسم‌ها (متغیرها، توابع) توش تعریف می‌شن. مثل یه کمد که چیزاش رو با اسم‌های مختلف توش می‌ذاری. برنامه‌های مختلف می‌تونن اسم‌های تکراری داشته باشن، چون تو namespaceهای جدا هستن.',
    example: 'import math\nprint(math.pi)          # از namespace ماژول math\n\nfrom math import pi\nprint(pi)               # مستقیم تو فضای نام ما\n\n# namespace هر ماژول جداست\nimport os\nprint(os.path)          # مسیر داخل os، نه مسیر عمومی',
    tip: 'از "from module import *" پرهیز کن — namespace رو آلوده می‌کنه و مشخص نمی‌شه چی از کجا اومده.'
  },

  'none': {
    en: 'NONE', fa: 'هیچ / تهی', cat: 'ساختمان داده',
    desc: 'مقداری که یعنی «هیچ چیز» یا «خالی». تنها نمونش NoneType است. تابعی که return نداره، None برمی‌گردونه. مثل لیوان خالی: لیوان هست، ولی توش چیزی نیست.',
    example: 'x = None\n\nif x is None:\n    print("خالیه")\n\n# تابع بدون return\nresult = print("سلام")   # اول "سلام" چاپ، بعد None\nprint(result)            # None\n\ndef find(xs, v):\n    for x in xs:\n        if x == v: return x\n    return None          # صریح بهتره\n\nif find([1,2], 3) is None:\n    print("یافت نشد")',
    tip: 'همیشه با "is None" مقایسه کن، نه "== None". این استاندارد پایتونه و امن‌تره.'
  },

  'numpy': {
    en: 'NUMPY', fa: 'نام‌پای', cat: 'برنامه‌نویسی کاربردی',
    desc: 'کتابخانه محاسبات عددی. آرایه‌های چندبعدی سریع می‌سازه و عملیات ریاضی روشون رو خیلی سریع انجام می‌ده. پایه‌ی پانداس، TensorFlow و اکثر کتابخانه‌های علمیه.',
    example: 'import numpy as np\n\na = np.array([1, 2, 3, 4])\nprint(a * 2)         # [2 4 6 8]  (عملیات برداری!)\nprint(a.sum())       # 10\nprint(a.mean())      # 2.5\n\nb = np.array([[1, 2], [3, 4]])\nprint(b.T)           # جابجایی\nprint(b @ b)         # ضرب ماتریسی',
    tip: 'از حلقه‌های پایتون روی آرایه پرهیز کن! عملیات برداری (vectorized) ده‌ها برابر سریع‌تره.'
  },

  'openapi': {
    en: 'OPENAPI', fa: 'اوپن‌ای‌پی‌آی', cat: 'حرفه‌ای',
    desc: 'یه استاندارد برای توصیف REST API. مستندات، اعتبارسنجی ورودی/خروجی و حتی تولید خودکار SDK رو ممکن می‌کنه. FastAPI خودش این رو می‌سازه.',
    example: '# FastAPI خودکار /openapi.json می‌سازه\n# Swagger UI در /docs و ReDoc در /redoc\n\n# نمونه توصیف:\nopenapi: 3.0.0\ninfo:\n  title: My API\n  version: 1.0.0\npaths:\n  /users:\n    get:\n      responses:\n        200:\n          description: لیست کاربران',
    tip: 'مستندات رو از کد استخراج کن، نه دستی. OpenAPI باعث می‌شه مستندات همیشه با کد همگام باشن.'
  },

  'operator': {
    en: 'OPERATOR', fa: 'عملگر', cat: 'مبانی',
    desc: 'نمادهایی که روی مقادیر یه عمل انجام می‌دن: +، -، *، /، ==، >، and، or، not و... . مثل علامت‌های ریاضی که تو مدرسه یاد گرفتیم.',
    example: '# حسابی\nprint(10 + 3)     # 13\nprint(10 // 3)    # 3\n\n# مقایسه‌ای\nprint(10 > 3)     # True\nprint(10 == 10)   # True\n\n# منطقی\nprint(True and False)  # False\nprint(True or False)   # True\nprint(not True)        # False\n\n# عضویت\nprint(3 in [1,2,3])    # True',
    tip: 'ترتیب اولویت: ** > * / // % > + - > مقایسه > not > and > or. از پرانتز استفاده کن تا شکی نباشه.'
  },

  'package': {
    en: 'PACKAGE', fa: 'بسته / پکیج', cat: 'ساختمان داده',
    desc: 'یه پوشه که چند تا ماژول پایتون توشه و یه فایل __init__.py داره. مثل یه پوشه که چند تا فایل مرتبط رو یه جا نگه می‌داره.',
    example: '# ساختار پکیج:\n# myapp/\n#   __init__.py\n#   models.py\n#   views.py\n#   utils.py\n\n# استفاده:\nfrom myapp import models\nfrom myapp.utils import helper\n\n# نصب پکیج از PyPI:\n# pip install requests',
    tip: 'از پایتون 3.3 به بعد __init__.py اجباری نیست ولی توصیه می‌شه — خیلی از ابزارها بدونش کار نمی‌کنن.'
  },

  'pandas': {
    en: 'PANDAS', fa: 'پانداس', cat: 'برنامه‌نویسی کاربردی',
    desc: 'کتابخانه تحلیل داده. جدول‌ها (DataFrame) و سری‌ها (Series) می‌سازه و روشون عملیات پیچیده انجام می‌ده: فیلتر، گروه‌بندی، اتصال، آمار. مثل اکسل تو پایتون، ولی هزار بار قوی‌تر.',
    example: 'import pandas as pd\n\ndf = pd.read_csv("sales.csv")\nprint(df.head())\nprint(df.describe())\n\n# فیلتر\ntop = df[df["amount"] > 1000]\n\n# گروه‌بندی\nby_city = df.groupby("city")["amount"].sum()\n\n# ذخیره\ndf.to_excel("out.xlsx", index=False)',
    tip: 'برای داده‌های بزرگ از chunksize در read_csv استفاده کن، یا dtype مناسب (int32 بجای int64) تا حافظه کم مصرف بشه.'
  },

  'parameter': {
    en: 'PARAMETER', fa: 'پارامتر', cat: 'حرفه‌ای',
    desc: 'متغیری که تو تعریف تابع می‌نویسی و هنگام صدا زدن، مقدار می‌گیره. فرقش با آرگومان: پارامتر تو تعریف، آرگومان تو فراخوانی.',
    example: 'def greet(name, greeting="سلام"):\n    #     ↑name و ↑greeting پارامتر هستن\n    return f"{greeting} {name}"\n\ngreet("علی")               # "علی" آرگومان هست\n\n# انواع:\ndef f(a, b=2, *args, **kwargs):\n    ...\n# a: اجباری\n# b: پیش‌فرض\n# args: هر تعداد positional\n# kwargs: هر تعداد keyword',
    tip: 'پارامتر پیش‌فرض رو بعد از پارامتر اجباری بذار، وگرنه SyntaxError می‌گیری.'
  },

  'pathlib': {
    en: 'PATHLIB', fa: 'پَث‌لیب (مسیر هوشمند)', cat: 'مبانی',
    desc: 'ماژول استاندارد کار با مسیرهای فایل. به‌جای اینکه با رشته کار کنی، با یه شیء کار می‌کنی که خودش می‌دونه چه سیستم‌عاملی. جادویی‌تر از os.path.',
    example: 'from pathlib import Path\n\np = Path("data") / "users.json"   # ترکیب مسیر\nprint(p.exists())                 # وجود داره؟\nprint(p.suffix)                   # .json\nprint(p.stem)                     # users\nprint(p.parent)                   # data\n\n# خوندن\nif p.exists():\n    text = p.read_text(encoding="utf-8")\n\n# ساخت پوشه\nPath("logs").mkdir(exist_ok=True)',
    tip: 'همیشه pathlib، هرگز رشته برای مسیر. کدت روی ویندوز و لینوکس یکسان کار می‌کنه.'
  },

  'performance': {
    en: 'PERFORMANCE', fa: 'کارایی', cat: 'ساختمان داده',
    desc: 'سرعت اجرا و مصرف منابع برنامه. برنامه‌ای که کارایی داره، سریع جواب می‌ده و منابع کم مصرف می‌کنه.',
    example: '# ❌ کند: چسباندن رشته در حلقه\nresult = ""\nfor s in words:\n    result += s       # هر بار رشته جدید می‌سازه\n\n# ✅ سریع: join\nresult = "".join(words)\n\n# اندازه‌گیری:\nimport timeit\nprint(timeit.timeit(lambda: "-".join(["a"]*1000), number=1000))',
    tip: 'قبل از بهینه‌سازی، اول اندازه بگیر. جای بهینه کردن یه جا که مهم نیست، ۹۰٪ وقتت رو تلف می‌کنی.'
  },

  'pip': {
    en: 'PIP', fa: 'پکیج‌منیجر', cat: 'برنامه‌نویسی کاربردی',
    desc: 'ابزار رسمی نصب پکیج‌های پایتون از مخزن PyPI. مثل اپ‌استور که باهاش اپ نصب می‌کنی، ولی برای کتابخانه‌های پایتون.',
    example: '# نصب پکیج\npip install requests\npip install "django>=4.2,<5"\n\n# لیست نصب‌شده‌ها\npip list\n\n# ذخیره لیست\npip freeze > requirements.txt\n\n# نصب از لیست\npip install -r requirements.txt\n\n# به‌روزرسانی\npython -m pip install --upgrade pip',
    tip: 'همیشه داخل venv کار کن. از "python -m pip" استفاده کن تا مطمئن باشی از pip مربوط به همین پایتون استفاده می‌کنی.'
  },

  'polymorphism': {
    en: 'POLYMORPHISM', fa: 'چندریختی', cat: 'حرفه‌ای',
    desc: 'یعنی یه نام، رفتارهای متفاوت. مثل کلمه «پرواز»: پرنده پرواز می‌کنه، هواپیما هم پرواز می‌کنه، ولی هر کدوم به روش خودشون. در پایتون، اشیاء مختلف با همون متد، رفتار متفاوت نشون می‌دن.',
    example: 'class Dog:\n    def speak(self): return "واق"\n\nclass Cat:\n    def speak(self): return "میو"\n\nclass Cow:\n    def speak(self): return "ماااا"\n\nfor animal in [Dog(), Cat(), Cow()]:\n    print(animal.speak())\n# همه speak دارن ولی هرکدوم صدای خودش',
    tip: 'در پایتون نیازی به interface صریح نداری — اگه شیء متد مورد نظر رو داشته باشه، کار می‌کنه (duck typing).'
  },

  'process': {
    en: 'PROCESS', fa: 'فرآیند', cat: 'مبانی',
    desc: 'یه نمونه مستقل از برنامه در حال اجرا با حافظه‌ی جدا. فرقش با thread: process حافظه مستقل داره، threadها حافظه مشترک دارن. برای کارهای سنگین CPU از process استفاده کن.',
    example: 'from multiprocessing import Process\nimport os\n\ndef work(name):\n    print(f"فرآیند {name} با PID {os.getpid()}")\n\nif __name__ == "__main__":\n    p1 = Process(target=work, args=("A",))\n    p2 = Process(target=work, args=("B",))\n    p1.start(); p2.start()\n    p1.join(); p2.join()',
    tip: 'برخلاف thread، process از GIL فرار می‌کنه و واقعاً موازی اجرا می‌شه. ولی overhead بیشتری داره.'
  },

  'profiling': {
    en: 'PROFILING', fa: 'پروفایل‌سازی', cat: 'ساختمان داده',
    desc: 'تحلیل کد برای پیدا کردن گلوگاه: کدوم تابع بیشترین زمان یا حافظه رو مصرف می‌کنه. مثل اینکه پزشک با دستگاه، نقطه دقیق درد رو پیدا می‌کنه.',
    example: '# خط فرمان\n# python -m cProfile -s cumtime my_script.py\n\n# در کد:\nimport cProfile\ncProfile.run("my_slow_function()")\n\n# حافظه:\n# pip install memory_profiler\n# python -m memory_profiler script.py\n\n# خط‌به‌خط:\n# pip install line_profiler',
    tip: 'قانون ۹۰/۱۰: معمولاً ۱۰٪ کد، ۹۰٪ زمان رو می‌گیره. اول اون ۱۰٪ رو پیدا کن، بعد بهینه کن.'
  },

  'project': {
    en: 'PROJECT', fa: 'پروژه', cat: 'برنامه‌نویسی کاربردی',
    desc: 'مجموعه‌ای سازمان‌یافته از فایل‌ها، ماژول‌ها و منابع که با هم یه برنامه رو می‌سازن. مثل یه دفتر با فصل‌های جدا و فهرست.',
    example: 'myproject/\n├── pyproject.toml       # تنظیمات پروژه\n├── README.md            # توضیحات\n├── .gitignore           # نادیده‌گیری گیت\n├── src/\n│   └── myproject/\n│       ├── __init__.py\n│       ├── main.py\n│       └── utils.py\n└── tests/\n    └── test_main.py',
    tip: 'ساختار "src layout" از importهای ناخواسته جلوگیری می‌کنه و تست رو واقعی‌تر می‌کنه.'
  },

  'property': {
    en: 'PROPERTY', fa: 'ویژگی محاسباتی', cat: 'حرفه‌ای',
    desc: 'دکوراتور @property که یه متد رو مثل یه attribute قابل خواندن می‌کنه. یعنی می‌تونی obj.area بنویسی، نه obj.area() — انگار که یه ویژگی ساده‌ست، ولی در واقع داره محاسبه می‌کنه.',
    example: 'class Circle:\n    def __init__(self, radius):\n        self._radius = radius\n\n    @property\n    def area(self):\n        return 3.14159 * self._radius ** 2\n\n    @property\n    def radius(self):\n        return self._radius\n\n    @radius.setter\n    def radius(self, value):\n        if value < 0:\n            raise ValueError("شعاع منفی نمی‌شه")\n        self._radius = value\n\nc = Circle(5)\nprint(c.area)         # بدون پرانتز!\nc.radius = 10          # setter فعال',
    tip: 'وقتی می‌خوای موقع خواندن یا نوشتن یه attribute، منطقی اجرا کنی، property ابزار مناسبه.'
  },

  'pyproject': {
    en: 'PYPROJECT', fa: 'فایل تنظیمات پروژه', cat: 'مبانی',
    desc: 'فایل استاندارد pyproject.toml که توش تنظیمات پروژه، وابستگی‌ها و ابزارهات رو تعریف می‌کنی. جانشین مدرن setup.py.',
    example: '[project]\nname = "myapp"\nversion = "0.1.0"\ndescription = "پروژه نمونه"\nrequires-python = ">=3.10"\ndependencies = [\n    "requests>=2.31",\n    "pydantic>=2.0",\n]\n\n[project.optional-dependencies]\ndev = ["pytest", "ruff"]\n\n[tool.ruff]\nline-length = 100',
    tip: 'ابزارهای pip، poetry، ruff، black و... همگی از pyproject می‌خونن. یه فایل، همه‌ی تنظیمات.'
  },

  'pytest': {
    en: 'PYTEST', fa: 'پای‌تست', cat: 'ساختمان داده',
    desc: 'فریم‌ورک تست‌نویسی پایتون با سینتکس ساده (فقط assert) و fixture‌های قدرتمند. جایگزین مدرن unittest.',
    example: 'def add(a, b):\n    return a + b\n\ndef test_add():\n    assert add(2, 3) == 5\n    assert add(-1, 1) == 0\n\ndef test_add_negative():\n    assert add(-2, -3) == -5\n\n# اجرا:\n# pytest -v\n# pytest --cov=myapp tests/',
    tip: 'اسم فایل با test_ و اسم تابع با test_ شروع بشه. خودش پیداشون می‌کنه و اجرا می‌کنه.'
  },

  'python': {
    en: 'PYTHON', fa: 'پایتون', cat: 'برنامه‌نویسی کاربردی',
    desc: 'یه زبان برنامه‌نویسی سطح بالا، تفسیری و همه‌منظوره. سینتکسش ساده و خواناست، کتابخانه‌هاش بی‌شماره و تو همه صنایع کاربرد داره: هوش مصنوعی، وب، علم داده، خودکارسازی.',
    example: '# ساده‌ترین برنامه پایتون\nprint("سلام دنیا")\n\n# تابع\ndef greet(name):\n    return f"سلام {name}"\n\n# کلاس\nclass User:\n    def __init__(self, name):\n        self.name = name\n\n# لیست، دیکشنری، حلقه\nnames = ["علی", "رضا"]\nages = {"علی": 30}\nfor n in names:\n    print(greet(n))',
    tip: 'پایتون رو از python.org دانلود کن و همیشه آخرین نسخه پایدار 3.12+ رو نصب کن.'
  },

  'raise': {
    en: 'RAISE', fa: 'بالا بردن خطا', cat: 'حرفه‌ای',
    desc: 'دستوری که خودت آگاهانه یه استثنا پرتاب می‌کنی. مثل آژیر خطر که وقتی مشکل دیدی، خودت روشنش می‌کنی تا همه بفهمن.',
    example: 'def withdraw(balance, amount):\n    if amount < 0:\n        raise ValueError("مبلغ نمی‌تونه منفی باشه")\n    if amount > balance:\n        raise RuntimeError(f"موجودی {balance} کافی نیست")\n    return balance - amount\n\n# خطای دامنه‌ای خودت:\nclass PaymentError(Exception):\n    pass\n\nraise PaymentError("پرداخت انجام نشد")',
    tip: 'خطای خودت رو با subclass از Exception بساز تا کاربران کدت بتونن مشخصش کنن.'
  },

  'range': {
    en: 'RANGE', fa: 'بازه', cat: 'مبانی',
    desc: 'تابعی که یه دنباله از اعداد تولید می‌کنه. حالت‌های مختلف: range(stop), range(start, stop), range(start, stop, step). عدد stop شامل نمی‌شه.',
    example: 'list(range(5))         # [0, 1, 2, 3, 4]\nlist(range(2, 8))      # [2, 3, 4, 5, 6, 7]\nlist(range(0, 10, 2))  # [0, 2, 4, 6, 8]\nlist(range(5, 0, -1))  # [5, 4, 3, 2, 1]\n\nfor i in range(3):\n    print(i)',
    tip: 'range برخلاف list، حافظه مصرف نمی‌کنه چون تنبل (lazy) هست. اگه فقط پیمایش می‌کنی، ازش استفاده کن.'
  },

  'regex': {
    en: 'REGEX', fa: 'الگوی متنی / عبارت باقاعده', cat: 'ساختمان داده',
    desc: 'زبانی برای توصیف الگوی متنی. با regex می‌تونی چیزهایی مثل شماره تلفن، ایمیل، تاریخ رو تو متن پیدا کنی، جایگزین کنی یا اعتبارسنجی کنی.',
    example: 'import re\n\n# شماره موبایل ایران\nm = re.search(r"09\\d{9}", "تماس: 09123456789")\nprint(m.group())   # 09123456789\n\n# ایمیل\nm = re.match(r"[\\w.]+@[\\w.]+", "ali@example.com")\n\n# جایگزینی\nre.sub(r"\\d+", "N", "کد 123 و 456")  # "کد N و N"\n\n# همه‌ی تطبیق‌ها\nre.findall(r"\\d+", "a1 b22 c333")  # ["1", "22", "333"]',
    tip: 'الگوهای پرتکرار رو با re.compile یک بار بساز و بارها استفاده کن — سریع‌تره.'
  },

  'repository': {
    en: 'REPOSITORY', fa: 'مخزن داده', cat: 'برنامه‌نویسی کاربردی',
    desc: 'یه لایه بین منطق برنامه و دیتابیس. مثل کتابدار که هرچی کتاب می‌خوای، از قفسه میاره. کد منطقی نمی‌دونه دیتابیس چیه، فقط با repository حرف می‌زنه.',
    example: 'class UserRepository:\n    def __init__(self, session):\n        self.session = session\n\n    def get(self, user_id):\n        return self.session.query(User).get(user_id)\n\n    def save(self, user):\n        self.session.add(user)\n        self.session.commit()\n\n    def find_by_email(self, email):\n        return self.session.query(User).filter_by(email=email).first()',
    tip: 'repository باعث می‌شه تست‌نویسی راحت بشه: به‌جای دیتابیس واقعی، یه mock repository تزریق می‌کنی.'
  },

  'request': {
    en: 'REQUEST', fa: 'درخواست', cat: 'حرفه‌ای',
    desc: 'پیامی که کلاینت (مرورگر یا برنامه) به سرور می‌فرسته. شامل متد (GET/POST/...)، آدرس، هدرها و گاهی بدنه. مثل نامه‌ای که می‌فرستی و منتظر جوابی.',
    example: 'import requests\n\nr = requests.post(\n    "https://api.example.com/users",\n    json={"name": "علی", "age": 30},\n    headers={"Authorization": "Bearer TOKEN"},\n    timeout=10,\n)\nprint(r.status_code)\nprint(r.json())',
    tip: 'همیشه timeout بذار و status_code رو چک کن. بدون این‌ها برنامه‌ات ممکنه بی‌نهایت منتظر بمونه.'
  },

  'requests': {
    en: 'REQUESTS', fa: 'کتابخانه requests', cat: 'مبانی',
    desc: 'محبوب‌ترین کتابخانه پایتون برای ارسال درخواست HTTP. با API ساده و تمیز، کار با APIها رو راحت می‌کنه.',
    example: 'import requests\n\n# GET\nr = requests.get("https://api.github.com")\nprint(r.status_code)   # 200\nprint(r.json())        # پاسخ JSON\n\n# POST\nr = requests.post(url, json={"a": 1})\n\n# با هدر\nr = requests.get(url, headers={"Auth": "token"})\n\n# با timeout\nr = requests.get(url, timeout=5)\nr.raise_for_status()   # خطای 4xx/5xx رو استثنا کن',
    tip: 'همیشه timeout بذار و از r.raise_for_status() استفاده کن تا خطاهای HTTP رو از دست ندی.'
  },

  'response': {
    en: 'RESPONSE', fa: 'پاسخ', cat: 'ساختمان داده',
    desc: 'پاسخی که سرور به درخواست کلاینت می‌ده. شامل status code، هدرها و بدنه (معمولاً JSON). مثل جواب نامه‌ای که فرستادی.',
    example: 'r = requests.get("https://api.github.com/users/torvalds")\n\nprint(r.status_code)              # 200 = OK\nprint(r.headers["content-type"])  # application/json\nprint(r.text[:100])               # بدنه پاسخ\nprint(r.json()["name"])           # Linus Torvalds\n\n# کدهای مهم:\n# 2xx = موفق\n# 3xx = ریدایرکت\n# 4xx = خطای کلاینت\n# 5xx = خطای سرور',
    tip: 'همیشه status_code رو چک کن. 200 یعنی موفق، بقیه یعنی یه جای کار می‌لنگه.'
  },

  'route': {
    en: 'ROUTE', fa: 'مسیر', cat: 'برنامه‌نویسی کاربردی',
    desc: 'نگاشت یه آدرس URL به یه تابع که اون درخواست رو پردازش می‌کنه. مثل شماره تلفن داخلی شرکت: هر داخلی به یه بخش وصله.',
    example: 'from fastapi import FastAPI\n\napp = FastAPI()\n\n@app.get("/")\ndef home():\n    return {"msg": "صفحه اصلی"}\n\n@app.get("/users/{user_id}")\ndef get_user(user_id: int):\n    return {"id": user_id}\n\n@app.post("/users")\ndef create_user(name: str):\n    return {"name": name}',
    tip: 'در REST، مسیرها رو با اسم جمع بساز: /users نه /getUser. متد (GET/POST/...) کار رو مشخص می‌کنه.'
  },

  'schema': {
    en: 'SCHEMA', fa: 'شمای داده', cat: 'حرفه‌ای',
    desc: 'تعریف ساختار داده: چه فیلدهایی داره، چه نوعی هستن، کدوم‌ها اجباری‌ان. مثل فرم استخدامی که می‌گه چه اطلاعاتی لازمه.',
    example: 'from pydantic import BaseModel, EmailStr, Field\n\nclass UserCreate(BaseModel):\n    name: str = Field(min_length=2, max_length=50)\n    age: int = Field(ge=0, le=120)\n    email: EmailStr\n    bio: str | None = None\n\n# استفاده:\nuser = UserCreate(name="علی", age=30, email="a@b.com")\n# اگه داده نامعتبر باشه، خودکار خطا می‌ده',
    tip: 'همیشه ورودی API رو با schema اعتبارسنجی کن. اجازه نده داده بد به منطق دامنه‌ات نفوذ کنه.'
  },

  'scope': {
    en: 'SCOPE', fa: 'دامنه', cat: 'مبانی',
    desc: 'محدوده‌ای که یه متغیر توش قابل دسترسیه. قانون LEGB: Local (محلی)، Enclosing (تابع دربرگیرنده)، Global (سراسری)، Built-in (توکار).',
    example: 'x = 10   # global\n\ndef outer():\n    y = 20   # enclosing\n    def inner():\n        z = 30   # local\n        print(x, y, z)   # همه قابل دسترسی\n    inner()\n\nouter()\n\n# برای تغییر global:\ncounter = 0\ndef inc():\n    global counter\n    counter += 1',
    tip: 'از global تا جای ممکن پرهیز کن. کد رو گیج می‌کنه و باگ‌های پنهان می‌سازه.'
  },

  'secret': {
    en: 'SECRET', fa: 'اطلاعات حساس', cat: 'ساختمان داده',
    desc: 'اطلاعاتی مثل رمز دیتابیس، کلید API که نباید تو کد باشن. اگه لو برن، همه‌چی به باد می‌ره.',
    example: 'import os\nfrom dotenv import load_dotenv\n\nload_dotenv()   # .env رو می‌خونه\n\nAPI_KEY = os.environ["API_KEY"]\nDB_PASSWORD = os.environ["DB_PASSWORD"]\nJWT_SECRET = os.environ["JWT_SECRET"]\n\n# فایل .env (توی گیت نذار!):\n# API_KEY=sk-abc123...\n# DB_PASSWORD=super_secret',
    tip: '.env رو حتماً تو .gitignore بذار و یه .env.example بساز که قالب رو نشون بده بدون اطلاعات واقعی.'
  },

  'security': {
    en: 'SECURITY', fa: 'امنیت', cat: 'برنامه‌نویسی کاربردی',
    desc: 'محافظت از برنامه و داده‌ها در برابر حملات: رمزنگاری رمز عبور، اعتبارسنجی ورودی، جلوگیری از injection و XSS.',
    example: 'from passlib.hash import bcrypt\nimport secrets\n\n# هش رمز عبور\nhashed = bcrypt.hash("mypassword")\nprint(bcrypt.verify("mypassword", hashed))  # True\n\n# توکن امن\ntoken = secrets.token_urlsafe(32)\n\n# HTTPS اجباری، CORS محدود، rate limiting\n# هرگز رمز رو خام ذخیره نکن!',
    tip: 'امنیت رو از روز اول طراحی کن. بعداً اضافه‌کردنش خیلی سخت‌تره.'
  },

  'service': {
    en: 'SERVICE', fa: 'سرویس', cat: 'حرفه‌ای',
    desc: 'لایه‌ای که منطق کسب‌وکار توش قرار می‌گیره، بین API (ورودی) و repository (داده). مثل مدیر که بین مشتری و انباردار قرار می‌گیره.',
    example: 'class UserService:\n    def __init__(self, repo, notifier):\n        self.repo = repo\n        self.notifier = notifier\n\n    def register(self, name, email):\n        if self.repo.find_by_email(email):\n            raise ValueError("ایمیل تکراری")\n        user = self.repo.save({"name": name, "email": email})\n        self.notifier.send_welcome(email)\n        return user',
    tip: 'سرویس نباید از HTTP یا SQL چیزی بدونه. فقط منطق دامنه.'
  },

  'set': {
    en: 'SET', fa: 'مجموعه', cat: 'مبانی',
    desc: 'مجموعه‌ای از اعضای یکتا و بدون ترتیب. برای حذف تکراری‌ها و عملیات مجموعه‌ای (اشتراک، اجتماع، تفاضل) فوق‌العاده‌ست.',
    example: 'nums = {1, 2, 2, 3, 3, 3}\nprint(nums)               # {1, 2, 3}\n\na = {1, 2, 3}\nb = {3, 4, 5}\nprint(a & b)              # اشتراک: {3}\nprint(a | b)              # اجتماع: {1,2,3,4,5}\nprint(a - b)              # تفاضل: {1, 2}\nprint(a ^ b)              # تفاضل متقارن: {1,2,4,5}\n\n# حذف تکراری‌ها از لیست:\nunique = list(set([1, 1, 2, 3, 3]))   # [1, 2, 3]',
    tip: 'عضویت در set از list سریع‌تره: O(1) در مقابل O(n). اگه زیاد چک می‌کنی «چی هست؟»، از set استفاده کن.'
  },

  'slicing': {
    en: 'SLICING', fa: 'برش', cat: 'ساختمان داده',
    desc: 'بریدن یه بخش از دنباله. با [start:stop:step] کار می‌کنه: از start (شامل) تا stop (غیرشامل) با گام step.',
    example: 'xs = [0, 1, 2, 3, 4, 5]\nprint(xs[1:4])     # [1, 2, 3]\nprint(xs[:3])      # [0, 1, 2]\nprint(xs[3:])      # [3, 4, 5]\nprint(xs[::2])     # [0, 2, 4]\nprint(xs[::-1])    # [5, 4, 3, 2, 1, 0] معکوس!\n\ns = "پایتون"\nprint(s[0:3])      # پای\nprint(s[::-1])     # نوتیاپ',
    tip: 'xs[::-1] یه روش سریع و پایتونیک برای معکوس کردن دنباله‌ست.'
  },

  'solid': {
    en: 'SOLID', fa: 'اصول سالید', cat: 'برنامه‌نویسی کاربردی',
    desc: 'پنج اصل طراحی شیءگرا که کد رو قابل نگهداری‌تر می‌کنه: تک‌مسئولیتی، باز/بسته، لیسکوف، جداسازی رابط، وارونگی وابستگی.',
    example: '# S - Single Responsibility\nclass UserValidator: pass     # فقط اعتبارسنجی\nclass UserSaver: pass          # فقط ذخیره\n\n# D - Dependency Inversion\nfrom abc import ABC, abstractmethod\n\nclass Notifier(ABC):\n    @abstractmethod\n    def send(self, msg): ...\n\nclass EmailNotifier(Notifier):\n    def send(self, msg): print(f"ایمیل: {msg}")\n\nclass UserService:\n    def __init__(self, notifier: Notifier):\n        self.notifier = notifier',
    tip: 'SOLID ابزار فکره، نه قانون مقدس. تو پروژه‌های کوچیک، انعطافش رو با پیچیدگی تلف نکن.'
  },

  'sql': {
    en: 'SQL', fa: 'اس‌کیو‌ال', cat: 'حرفه‌ای',
    desc: 'زبانی برای کار با پایگاه‌های داده رابطه‌ای. با SQL داده می‌سازی، می‌خونی، ویرایش می‌کنی و حذف می‌کنی. مثل یه زبان مخصوص دیتابیس‌ها.',
    example: '-- ساختن جدول\nCREATE TABLE users (\n    id INTEGER PRIMARY KEY,\n    name TEXT NOT NULL,\n    age INTEGER\n);\n\n-- درج\nINSERT INTO users (name, age) VALUES ("علی", 30);\n\n-- خواندن\nSELECT name, age FROM users WHERE age > 18 ORDER BY age DESC;\n\n-- به‌روزرسانی\nUPDATE users SET age = 31 WHERE id = 1;\n\n-- حذف\nDELETE FROM users WHERE id = 1;',
    tip: 'همیشه از پارامترهای bind‌شده (?) استفاده کن، نه رشته‌سازی. جلوگیری از SQL Injection حیاتیه.'
  },

  'sqlite': {
    en: 'SQLITE', fa: 'اس‌کیو‌لایت', cat: 'مبانی',
    desc: 'یه پایگاه داده سبک که تو یه فایل ذخیره می‌شه. نیازی به نصب سرور جداگانه نداره. برای پروژه‌های کوچیک و آموزش عالیه.',
    example: 'import sqlite3\n\ncon = sqlite3.connect("app.db")\ncur = con.cursor()\n\ncur.execute("""\n    CREATE TABLE IF NOT EXISTS users (\n        id INTEGER PRIMARY KEY,\n        name TEXT,\n        age INTEGER\n    )\n""")\n\ncur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("علی", 30))\ncon.commit()\n\ncur.execute("SELECT * FROM users")\nfor row in cur.fetchall():\n    print(row)\n\ncon.close()',
    tip: 'همیشه از ? برای پارامتر استفاده کن. حتی اگه داده‌ت قابل‌اعتماده — عادت خوبیه.'
  },

  'status-code': {
    en: 'STATUS-CODE', fa: 'کد وضعیت', cat: 'ساختمان داده',
    desc: 'یه عدد سه‌رقمی که نتیجه درخواست HTTP رو می‌رسونه. 2xx موفق، 3xx ریدایرکت، 4xx خطای کلاینت، 5xx خطای سرور.',
    example: '# کدهای مهم:\n# 200 OK          موفق\n# 201 Created     ساخت موفق\n# 204 No Content  موفق، بدون بدنه\n# 301/302         ریدایرکت\n# 400 Bad Request ورودی اشتباه\n# 401 Unauthorized    نیاز به لاگین\n# 403 Forbidden       دسترسی نداری\n# 404 Not Found       پیدا نشد\n# 500 Server Error    خطای سرور\n\nfrom fastapi import HTTPException\nraise HTTPException(status_code=404, detail="User not found")',
    tip: 'کد درست بفرست! کلاینت‌ها بر اساس این کدها تصمیم می‌گیرن چطور رفتار کنن.'
  },

  'string': {
    en: 'STRING', fa: 'رشته', cat: 'برنامه‌نویسی کاربردی',
    desc: 'نوع داده متن. دنباله‌ای از کاراکترها که تغییرناپذیره (immutable) و یونیکد پشتیبانی می‌کنه.',
    example: 's = "سلام دنیا"\nprint(len(s))         # تعداد کاراکتر\nprint(s.upper())      # SALAM...  (فارسی)\nprint(s[0])           # س\nprint(s[::-1])        # معکوس\nprint("دنیا" in s)    # True\nprint(s.split(" "))   # ["سلام", "دنیا"]\nprint("-".join(["a", "b"]))  # a-b\n\n# رشته چندخطی:\ntext = """خط اول\nخط دوم"""',
    tip: 'رشته‌ها تغییرناپذیرن. هر بار که "تغییرشون" می‌دی، در واقع یه رشته جدید ساخته می‌شه.'
  },

  'syntax': {
    en: 'SYNTAX', fa: 'نحو', cat: 'حرفه‌ای',
    desc: 'قواعد نگارش زبان. اگه نحو رو رعایت نکنی، پایتون قبل از اجرا خطا می‌ده. مثل دستور زبان فارسی: «من می‌روم خانه» درسته، «من رفتن خانه» غلط.',
    example: '# ✅ درست\nx = 10\nif x > 5:\n    print("بزرگ")\n\n# ❌ غلط - SyntaxError\n# if x > 5\n#     print("بزرگ")     ← دو نقطه یادت رفت\n\n# ❌ غلط\n# print("سلام"           ← پرانتز بسته نشد',
    tip: 'خطای SyntaxError با شماره خط نشون داده می‌شه. اون خط و خط قبلش رو چک کن.'
  },

  'terminal': {
    en: 'TERMINAL', fa: 'ترمینال / خط فرمان', cat: 'مبانی',
    desc: 'یه پنجره که باهاش با سیستم‌عامل حرف می‌زنی، نه با کلیک. دستور تایپ می‌کنی و Enter می‌زنی. برای اجرای پایتون لازمش داری.',
    example: '# لیست فایل‌ها\nls          # Mac/Linux\ndir         # Windows\n\n# پوشه عوض کن\ncd my-project\n\n# اجرای پایتون\npython main.py\n\n# نصب پکیج\npip install requests\n\n# در VS Code با Ctrl+` بازش کن',
    tip: 'تو VS Code با Ctrl+` (بک‌تیک) می‌تونی ترمینال داخلی رو باز کنی — خیلی راحت‌تر از پنجره جدا.'
  },

  'test': {
    en: 'TEST', fa: 'آزمون', cat: 'ساختمان داده',
    desc: 'کدی که رفتار برنامه‌ات رو خودکار چک می‌کنه. مثل چکاپ پزشکی: مطمئن می‌شی همه‌چی سالمه، بدون اینکه همه‌چی رو دستی چک کنی.',
    example: 'def add(a, b):\n    return a + b\n\ndef test_add_positive():\n    assert add(2, 3) == 5\n\ndef test_add_negative():\n    assert add(-2, -3) == -5\n\ndef test_add_zero():\n    assert add(0, 5) == 5\n\n# اجرا: pytest -v',
    tip: 'برای هر باگ که رفع می‌کنی، یه تست اضافه کن تا دیگه برنگرده.'
  },

  'testing': {
    en: 'TESTING', fa: 'تست‌نویسی', cat: 'برنامه‌نویسی کاربردی',
    desc: 'فرآیند طراحی و اجرای تست‌ها. سه سطح اصلی داره: unit (تک تابع)، integration (چند جزء)، e2e (کل سیستم).',
    example: '# هرم تست:\n#     /\\       E2E (کم)\n#    /  \\      Integration (متوسط)\n#   /____\\     Unit (زیاد)\n\n# unit test\ndef test_calculator():\n    assert calc(2, "+", 3) == 5\n\n# integration test\ndef test_user_api(db):\n    response = client.post("/users", json={"name": "Ali"})\n    assert response.status_code == 201\n    assert db.get_user(response.json()["id"])',
    tip: 'تست‌های ساده و سریع بنویس. تستی که کند اجرا می‌شه، عملاً اجرا نمی‌شه.'
  },

  'thread': {
    en: 'THREAD', fa: 'رشته اجرا / نخ', cat: 'حرفه‌ای',
    desc: 'واحد سبک اجرا درون یه process. چند thread می‌تونن همزمان کار کنن و حافظه مشترک داشته باشن. برای کارهای I/O (شبکه، فایل) عالیه.',
    example: 'import threading\n\ndef download(url):\n    print(f"دانلود {url}")\n\nt1 = threading.Thread(target=download, args=("url1",))\nt2 = threading.Thread(target=download, args=("url2",))\n\nt1.start(); t2.start()\nt1.join(); t2.join()\n\n# قفل برای بخش‌های حساس:\nlock = threading.Lock()\nwith lock:\n    counter += 1',
    tip: 'در پایتون به‌خاطر GIL، thread برای CPU کمک نمی‌کنه. برای I/O عالیه، برای محاسبات از process استفاده کن.'
  },

  'timezone': {
    en: 'TIMEZONE', fa: 'منطقه زمانی', cat: 'مبانی',
    desc: 'اختلاف زمانی یه منطقه با UTC (زمان جهانی). تهران +3:30، نیویورک -5. برای برنامه‌های بین‌المللی حیاتیه.',
    example: 'from datetime import datetime, timezone\nfrom zoneinfo import ZoneInfo\n\n# UTC\nnow_utc = datetime.now(timezone.utc)\nprint(now_utc)\n\n# تهران\ntehran = ZoneInfo("Asia/Tehran")\nnow_tehran = datetime.now(tehran)\nprint(now_tehran)\n\n# تبدیل\ndatetime.now(timezone.utc).astimezone(tehran)',
    tip: 'داده رو همیشه در UTC ذخیره کن، بعد برای نمایش به timezone کاربر تبدیل کن.'
  },

  'transaction': {
    en: 'TRANSACTION', fa: 'تراکنش', cat: 'ساختمان داده',
    desc: 'گروهی از عملیات که یا همه موفق می‌شن یا همه لغو می‌شن. مثل انتقال پول: کم شدن از یه حساب و اضافه شدن به حساب دیگه باید با هم انجام بشه، وگرنه پول گم می‌شه.',
    example: 'with connection:\n    # اگه هر کدوم خطا بده، همه rollback می‌شن\n    cur.execute("UPDATE accounts SET balance = balance - 100 WHERE id = 1")\n    cur.execute("UPDATE accounts SET balance = balance + 100 WHERE id = 2")\n    # خودکار commit می‌شه آخر بلوک\n\n# یا دستی:\ntry:\n    do_transfer()\n    con.commit()\nexcept:\n    con.rollback()\n    raise',
    tip: 'تراکنش‌ها رو کوچیک نگه دار تا قفل شدن دیتابیس و کندی پیش نیاد.'
  },

  'try': {
    en: 'TRY', fa: 'امتحان کن', cat: 'برنامه‌نویسی کاربردی',
    desc: 'بلوکی که کد مشکوک به خطا رو توش می‌ذاری. اگه خطا داد، except می‌گیره‌اش. مثل اینکه یه کار خطرناک رو با احتیاط انجام بدی.',
    example: 'try:\n    with open("data.txt") as f:\n        content = f.read()\n    number = int(content)\n    result = 100 / number\nexcept FileNotFoundError:\n    print("فایل پیدا نشد")\nexcept ValueError:\n    print("محتوای فایل عدد نیست")\nexcept ZeroDivisionError:\n    print("تقسیم بر صفر")\nelse:\n    print("همه‌چی خوب بود:", result)\nfinally:\n    print("پایان پردازش")',
    tip: 'try رو کوچیک نگه دار. فقط خط‌هایی که ممکنه خطا بدن رو داخلش بذار.'
  },

  'tuple': {
    en: 'TUPLE', fa: 'تاپل', cat: 'حرفه‌ای',
    desc: 'دنباله‌ای مثل لیست ولی تغییرناپذیر. بعد از ساخت نمی‌تونی عوضش کنی. برای داده‌هایی که نباید تغییر کنن، مثل مختصات یه نقطه یا روزهای هفته.',
    example: 'point = (3, 4)\nx, y = point              # بازکردن\nprint(x, y)\n\n# تغییر؟ غیرممکن\ntry:\n    point[0] = 5          # TypeError\nexcept TypeError:\n    print("تاپل تغییر نمی‌کنه")\n\n# تاپل تک‌عضوی - کاما لازمه:\nwrong = (5)               # این int است!\nright = (5,)              # این تاپل است\n\n# تاپل به‌عنوان کلید دیکشنری:\nd = {(1, 2): "point"}',
    tip: 'از tuple برای داده‌هایی که ثابت می‌مونن استفاده کن. immutable بودنش هم امن‌تره هم می‌تونه کلید دیکشنری باشه.'
  },

  'type-hint': {
    en: 'TYPE-HINT', fa: 'راهنمای نوع', cat: 'مبانی',
    desc: 'اعلام صریح نوع پارامترها و خروجی تابع. پایتون اجراش نمی‌کنه، ولی ابزارهایی مثل mypy ازش برای پیدا کردن خطاها قبل از اجرا استفاده می‌کنن.',
    example: 'def greet(name: str, age: int) -> str:\n    return f"{name} ({age})"\n\n# انواع پیچیده\nfrom typing import Optional, Union, List\n\ndef find(users: List[dict], uid: int) -> Optional[dict]:\n    ...\n\n# پایتون 3.10+\ndef find(users: list[dict], uid: int) -> dict | None:\n    ...',
    tip: 'با mypy یا pyright کد رو بررسی کن. خطاهای نوعی رو قبل از اجرا می‌گیری که عالیه.'
  },

  'types': {
    en: 'TYPES', fa: 'انواع داده', cat: 'ساختمان داده',
    desc: 'دسته‌بندی داده‌ها در پایتون: عدد صحیح (int)، اعشاری (float)، متن (str)، منطقی (bool)، لیست، تاپل، دیکشنری، set و... .',
    example: 'print(type(42))         # <class "int">\nprint(type(3.14))       # <class "float">\nprint(type("سلام"))     # <class "str">\nprint(type(True))       # <class "bool">\nprint(type([1, 2]))     # <class "list">\nprint(type({"a": 1}))   # <class "dict">\n\n# چک کردن:\nprint(isinstance(42, int))     # True',
    tip: 'پایتون داینامیک تایپ‌ست — یعنی نوع متغیر می‌تونه تغییر کنه. همین انعطاف‌پذیریش گاهی منبع باگه.'
  },

  'unicode': {
    en: 'UNICODE', fa: 'یونیکد', cat: 'برنامه‌نویسی کاربردی',
    desc: 'استاندارد بین‌المللی برای نمایش همه کاراکترهای دنیا: فارسی، عربی، چینی، ایموجی و... . پایتون 3 کاملاً ازش پشتیبانی می‌کنه.',
    example: 's = "سلام 🌍 دنیا"\nprint(len(s))          # تعداد کاراکتر\nprint(ord("س"))        # کد یونیکد: 1587\nprint(chr(1587))       # برگرداندن: س\nprint("\\u0633")        # س\n\n# NFD vs NFC (ترکیب‌ها):\nimport unicodedata\nunicodedata.normalize("NFC", "س")',
    tip: 'در پایتون 3 رشته‌ها یونیکد هستن. فقط موقع خوندن/نوشتن فایل، encoding="utf-8" بذار.'
  },

  'unittest': {
    en: 'UNITTEST', fa: 'یونیت‌تست', cat: 'حرفه‌ای',
    desc: 'فریم‌ورک تست استاندارد پایتون (بدون نیاز به نصب). از کلاس TestCase و متدهای assert استفاده می‌کنه. قبل از pytest بوده.',
    example: 'import unittest\n\nclass TestMath(unittest.TestCase):\n    def setUp(self):\n        self.calc = Calculator()\n\n    def test_add(self):\n        self.assertEqual(self.calc.add(2, 3), 5)\n\n    def test_divide_zero(self):\n        with self.assertRaises(ZeroDivisionError):\n            self.calc.divide(10, 0)\n\nif __name__ == "__main__":\n    unittest.main()',
    tip: 'pytest سینتکس ساده‌تری داره و توصیه می‌شه، ولی unittest بدون نصب کار می‌کنه.'
  },

  'unpacking': {
    en: 'UNPACKING', fa: 'بازکردن', cat: 'مبانی',
    desc: 'تخصیص اعضای یه iterable به چند متغیر در یه خط. مثل باز کردن یه بسته که هر آیتم بره سر جاش.',
    example: 'a, b, c = [1, 2, 3]\nprint(a, b, c)        # 1 2 3\n\n# با ستاره - گرفتن باقی:\nx, *rest = [1, 2, 3, 4]\nprint(x, rest)        # 1 [2, 3, 4]\n\nfirst, *mid, last = "abcd"\nprint(first, mid, last)   # a ["b","c"] d\n\n# تعویض متغیر:\na, b = 1, 2\na, b = b, a           # a=2, b=1\n\n# unpack کردن دیکشنری:\n\ndef greet(name, age):\n    print(f"{name} ({age})")\n\nperson = {"name": "علی", "age": 30}\ngreet(**person)',
    tip: 'برای تعویض دو متغیر نیازی به متغیر موقت نداری: a, b = b, a — یه ویژگی زیبای پایتون.'
  },

  'validation': {
    en: 'VALIDATION', fa: 'اعتبارسنجی', cat: 'ساختمان داده',
    desc: 'بررسی درستی ورودی قبل از استفاده. مطمئن می‌شی کاربر داده معتبر داده، نه چیزی که برنامه رو خراب کنه.',
    example: 'def set_age(age):\n    if not isinstance(age, int):\n        raise TypeError("سن باید عدد باشه")\n    if age < 0 or age > 150:\n        raise ValueError("سن بین 0 و 150 باشه")\n    return age\n\n# با Pydantic (حرفه‌ای‌تر):\nfrom pydantic import BaseModel, Field\n\nclass User(BaseModel):\n    name: str = Field(min_length=2)\n    age: int = Field(ge=0, le=150)\n    email: str',
    tip: 'ورودی رو همیشه در مرز برنامه اعتبارسنجی کن (API، فرم، فایل). به داده کاربر اعتماد نکن.'
  },

  'variable': {
    en: 'VARIABLE', fa: 'متغیر', cat: 'برنامه‌نویسی کاربردی',
    desc: 'اسمی که به یه مقدار اشاره می‌کنه. مثل یه برچسب که روی جعبه می‌چسبونی و بعداً با اون اسم به محتوا دسترسی داری.',
    example: 'x = 10\nname = "علی"\nis_active = True\nprices = [100, 200]\n\n# تخصیص چندتایی:\na, b, c = 1, 2, 3\nx = y = z = 0\n\n# تغییر نوع مجازه (داینامیک):\nx = 10\nx = "حالا رشته‌ام"   # مشکلی نیست',
    tip: 'اسم متغیرها معنادار باشن: total_price نه tp. کد خودش رو می‌خونه.'
  },

  'venv': {
    en: 'VENV', fa: 'محیط مجازی', cat: 'حرفه‌ای',
    desc: 'یه محیط جدا برای پایتون که کتابخانه‌های هر پروژه رو مستقل نگه می‌داره. مثل اینکه هر پروژه اتاق خودش رو داشته باشه، بدون اینکه وسایل قاطی بشن.',
    example: '# ساخت\npython -m venv venv\n\n# فعال‌سازی\n# Linux/Mac:\nsource venv/bin/activate\n# Windows:\nvenv\\Scripts\\activate\n\n# نصب پکیج (فقط تو این محیط)\npip install requests\n\n# خروج\ndeactivate\n\n# پوشه venv رو تو .gitignore بذار!',
    tip: 'برای هر پروژه یه venv جدا بساز. کتابخانه‌های همه پروژه‌ها نباید قاطی بشن.'
  },

  'visualization': {
    en: 'VISUALIZATION', fa: 'تصویرسازی', cat: 'مبانی',
    desc: 'نمایش داده به‌صورت نمودار یا گراف. مغز آدم با تصویر بهتر می‌فهمه تا با جدول اعداد. یه نمودار خوب، هزار تا عدد رو معنی‌دار می‌کنه.',
    example: 'import matplotlib.pyplot as plt\nimport seaborn as sns\n\n# نمودار خطی\nplt.plot([1, 2, 3, 4], [1, 4, 9, 16])\nplt.title("روند رشد")\nplt.xlabel("زمان")\nplt.ylabel("مقدار")\nplt.show()\n\n# هیستوگرام\nsns.histplot(data, x="age", bins=20)\n\n# پراکندگی\nplt.scatter(x, y)',
    tip: 'برای هر داده، نمودار مناسب: روند → خطی، توزیع → هیستوگرام، رابطه → پراکندگی، مقایسه → میله‌ای.'
  },

  'vscode': {
    en: 'VSCODE', fa: 'وی‌اس‌کد', cat: 'ساختمان داده',
    desc: 'ویرایشگر کد رایگان و محبوب مایکروسافت. برای پایتون افزونه‌های عالی داره: Python، Pylance، Jupyter. سبکه و سریع.',
    example: '// .vscode/settings.json\n{\n    "python.defaultInterpreterPath": "./venv/bin/python",\n    "editor.formatOnSave": true,\n    "python.analysis.typeCheckingMode": "basic",\n    "[python]": {\n        "editor.defaultFormatter": "charliermarsh.ruff"\n    }\n}',
    tip: 'افزونه‌های Python + Pylance + Ruff رو نصب کن. خودکار خطاها رو می‌گیره و کد رو تمیز می‌کنه.'
  },

  'while': {
    en: 'WHILE', fa: 'تا زمانی که', cat: 'برنامه‌نویسی کاربردی',
    desc: 'حلقه‌ای که تا وقتی شرط درسته تکرار می‌شه. تعداد تکرارها از قبل معلوم نیست، به شرط بستگی داره.',
    example: 'n = 5\nwhile n > 0:\n    print(n)\n    n -= 1\n\n# حلقه بازی:\nwhile True:\n    cmd = input("دستور: ")\n    if cmd == "exit":\n        break\n    print(f"اجرا: {cmd}")\n\n# منتظر شرط خاص:\nwhile not connected:\n    connect()',
    tip: 'دقت کن شرط بالاخره False بشه، وگرنه حلقه بی‌نهایت می‌شه. همیشه یه راه خروج داشته باش.'
  },

  'object': {
    en: 'OBJECT', fa: 'شیء', cat: 'حرفه‌ای',
    desc: 'نمونه‌ای از یه کلاس با داده و رفتار خودش. در پایتون همه‌چیز یه شیء است: عدد 5، رشته "سلام"، تابع، ماژول... همه شیء هستن.',
    example: 'class Dog:\n    def __init__(self, name):\n        self.name = name\n    def bark(self):\n        return f"{self.name}: واق!"\n\nrex = Dog("رکس")     # rex یه object هست\nprint(rex.bark())\n\nprint(isinstance(rex, Dog))   # True\nprint(isinstance(42, object)) # True — حتی اعداد هم شیء هستن!\nprint(isinstance("سلام", object))  # True',
    tip: 'در پایتون همه‌چیز شیء هست. حتی توابع هم attribute و متد دارن.'
  },

  'print': {
    en: 'PRINT', fa: 'چاپ', cat: 'مبانی',
    desc: 'تابع داخلی برای نمایش خروجی در کنسول. می‌تونی چند چیز رو با هم چاپ کنی، جداکننده بذاری، و حتی به فایل بنویسی.',
    example: 'print("سلام")\nprint("سلام", "دنیا")                # سلام دنیا\nprint("a", "b", "c", sep="-")        # a-b-c\nprint("بدون خط جدید", end=" ")\nprint("ادامه")\nprint(f"متغیرها: {x=}")              # x=10\n\n# به فایل:\nwith open("log.txt", "w") as f:\n    print("متن", file=f)\n\n# با فرمت:\nprint(f"{3.14159:.2f}")               # 3.14\nprint(f"{1234567:,}")                 # 1,234,567',
    tip: 'برای دیباگ سریع از print(f"{var=}") استفاده کن — اسم و مقدار متغیر رو یه جا نشون می‌ده.'
  },

  'if': {
    en: 'IF', fa: 'اگر', cat: 'ساختمان داده',
    desc: 'دستور شرطی که اجرای یه بلوک کد رو به True بودن یه شرط وابسته می‌کنه. مثل «اگه بارون بیاد، چتر ببر».',
    example: 'age = 20\nif age >= 18:\n    print("بزرگسال")\n\n# با else\nif age >= 18:\n    print("بزرگسال")\nelse:\n    print("کودک")\n\n# یک‌خطی\nstatus = "بزرگسال" if age >= 18 else "کودک"\n\n# با ترکیب شرط\nif age >= 18 and has_id:\n    print("می‌تونه رأی بده")',
    tip: 'در پایتون این‌ها همه falsy هستن: 0, "", [], {}, None, False. بقیه truthy.'
  },

  'for': {
    en: 'FOR', fa: 'حلقه for', cat: 'برنامه‌نویسی کاربردی',
    desc: 'حلقه‌ای برای پیمایش اعضای یه iterable (لیست، رشته، range و...). برای هر عضو، یه بار بدنه رو اجرا می‌کنه.',
    example: 'for fruit in ["سیب", "موز", "پرتقال"]:\n    print(fruit)\n\n# با اندیس:\nfor i, fruit in enumerate(["سیب", "موز"]):\n    print(i, fruit)\n\n# با دو لیست همزمان:\nnames = ["علی", "رضا"]\nages = [30, 25]\nfor name, age in zip(names, ages):\n    print(f"{name} ({age})")\n\n# دیکشنری:\nfor k, v in {"a": 1, "b": 2}.items():\n    print(k, v)',
    tip: 'هیچوقت از for i in range(len(xs)) استفاده نکن — از for x in xs یا enumerate(xs) استفاده کن.'
  },

  'return': {
    en: 'RETURN', fa: 'بازگشت', cat: 'حرفه‌ای',
    desc: 'دستوری که یه مقدار رو از تابع برمی‌گردونه و تابع رو تموم می‌کنه. تابعی که return نداره، None برمی‌گردونه.',
    example: 'def add(a, b):\n    return a + b\n\ndef check(x):\n    if x < 0:\n        return "منفی"\n    return "مثبت یا صفر"\n\ndef multiple_returns():\n    return 1, 2, 3   # عملاً یه tuple\n\nx, y, z = multiple_returns()\n\n# return زودهنگام (guard clause)\ndef divide(a, b):\n    if b == 0:\n        return None\n    return a / b',
    tip: 'از return زودهنگام برای ساده کردن تابع استفاده کن. شرط‌های منفی رو اول بذار، بعد منطق اصلی.'
  },

  'def': {
    en: 'DEF', fa: 'تعریف تابع', cat: 'مبانی',
    desc: 'کلیدواژه‌ای که یه تابع جدید تعریف می‌کنه. بعدش اسم تابع، پرانتز پارامترها و دو نقطه میاد.',
    example: 'def greet(name="دنیا"):\n    """احوال‌پرسی ساده."""\n    return f"سلام {name}!"\n\nprint(greet())           # سلام دنیا!\nprint(greet("علی"))      # سلام علی!\n\n# با نوع\ndef add(a: int, b: int) -> int:\n    return a + b\n\n# با *args و **kwargs\ndef f(*args, **kwargs):\n    print(args, kwargs)',
    tip: 'اسم تابع با حرف کوچک و کلمات با _ جدا بشن: get_user_name نه GetUserName.'
  },

  'import': {
    en: 'IMPORT', fa: 'ورود ماژول', cat: 'ساختمان داده',
    desc: 'دستوری که کد از یه ماژول یا پکیج دیگه رو میاره تو برنامه‌ات. مثل اینکه از یه کتاب، فصلی رو کپی کنی.',
    example: 'import os\nimport json\nfrom pathlib import Path\nfrom math import sqrt, pi\nimport numpy as np\nfrom myapp.utils import helper\n\n# import شرطی\ntry:\n    import uvloop\nexcept ImportError:\n    uvloop = None',
    tip: 'importها رو در بالای فایل بنویس و گروه‌بندی کن: استاندارد، third-party، پروژه خودت. با فاصله خالی جدا کن.'
  },

  'self': {
    en: 'SELF', fa: 'خود / خودشیء', cat: 'برنامه‌نویسی کاربردی',
    desc: 'اولین پارامتر همه متدهای نمونه. به شیئی که متد روش صدا زده شده اشاره می‌کنه. مثل کلمه «خودم» که وقتی از خودت حرف می‌زنی.',
    example: 'class Counter:\n    def __init__(self):\n        self.count = 0\n\n    def increment(self):\n        self.count += 1\n        return self.count\n\nc = Counter()\nc.increment()\nprint(c.count)   # 1\n\n# معادل:\n# c.increment()  ≡  Counter.increment(c)',
    tip: 'اسمش می‌تونه هرچیزی باشه (this، me)، ولی self استانداردی است که همه می‌شناسن. عوضش نکن.'
  },

  'init': {
    en: 'INIT', fa: 'سازنده / مقدارده‌ی اولیه', cat: 'حرفه‌ای',
    desc: 'متد ویژه __init__ که هنگام ساخت شیء جدید صدا زده می‌شه و مقادیر اولیه رو تنظیم می‌کنه. مثل مراسم افتتاحیه یه مغازه.',
    example: 'class User:\n    def __init__(self, name, age=0):\n        self.name = name\n        self.age = age\n        self.is_active = True\n\n    def __repr__(self):\n        return f"User({self.name!r}, {self.age})"\n\nu = User("علی", 30)\nprint(u)          # User("علی", 30)\n\n# __init__ مقداردهی می‌کنه، سازنده واقعی __new__ است',
    tip: '__init__ مقدار برمی‌گردونه نه (None). برای تنظیمات خاص، از __new__ استفاده کن (نادر).'
  }

};