# -*- coding: utf-8 -*-
"""
ترکیب دادهٔ همهٔ فصل‌ها و تزریق فیلدهای پیمایش (فصل قبلی/بعدی).

فایل‌های داده به‌تفکیک بخش دوره:
    data_a.py  → فصل‌های ۲ تا ۶    (مبانی)
    data_b.py  → فصل‌های ۷ تا ۱۰   (ساختار و ویوها)
    data_c.py  → فصل‌های ۱۱ تا ۱۵  (فرم، احراز هویت، فایل، دیتابیس)
    data_d.py  → فصل‌های ۱۶ تا ۲۰  (سیگنال، میدلور، نشست، کش، تست)
    data_e.py  → فصل‌های ۲۱ تا ۲۵  (دیباگ، DRF، سلری، بومی‌سازی)
    data_f.py  → فصل‌های ۲۶ تا ۳۰  (استقرار، کارایی، فرانت، نسخه‌ها، پروژه)

فصل ۱ دست‌نویس است (chapters/chapter-01/index.html) و تولید نمی‌شود؛
فقط در REGISTRY حضور دارد تا پیمایش فصل ۲ به آن درست اشاره کند.
"""

import data_a
import data_b
import data_c
import data_d
import data_e
import data_f

# فصل دست‌نویس شماره ۱ (برای پیمایش فصل ۲)
CHAPTER_ONE = dict(n=1, icon='🌱', title='آشنایی با جنگو')

CHAPTERS = (
    data_a.CHAPTERS
    + data_b.CHAPTERS
    + data_c.CHAPTERS
    + data_d.CHAPTERS
    + data_e.CHAPTERS
    + data_f.CHAPTERS
)

# {شماره فصل: (نماد, عنوان)} — برای ساخت پیوندهای قبلی/بعدی
REGISTRY = {c['n']: (c['icon'], c['title']) for c in CHAPTERS}
REGISTRY[1] = (CHAPTER_ONE['icon'], CHAPTER_ONE['title'])


def _inject_pagers(chapters):
    """فیلدهای prev_icon / next_icon / next_title را به هر فصل اضافه می‌کند."""
    out = []
    for ch in sorted(chapters, key=lambda c: c['n']):
        ch = dict(ch)
        n = ch['n']
        prev_meta = REGISTRY.get(n - 1)
        next_meta = REGISTRY.get(n + 1)
        ch['prev_icon'] = prev_meta[0] if prev_meta else '📗'
        if next_meta:
            ch['next_icon'], ch['next_title'] = next_meta
        out.append(ch)
    return out


ALL = _inject_pagers(CHAPTERS)

# بررسی سلامت هنگام import: شماره فصل‌ها باید ۲ تا ۳۰ و یکتا باشد
_ns = [c['n'] for c in ALL]
assert _ns == list(range(2, 31)), f'شماره فصل‌ها نامعتبر است: {_ns}'
assert len({c['icon'] for c in ALL}) >= 1


if __name__ == '__main__':
    print(f'{len(ALL)} فصل آماده تولید:\n')
    for ch in ALL:
        nxt = f"→ {ch.get('next_icon', '🏆')} {ch.get('next_title', 'پایان دوره')}"
        print(f"  {ch['n']:>2}. {ch['icon']} {ch['title']} "
              f"({ch['mins']} دقیقه، بخش {ch['cat']})  {nxt}")
