// script.js - تعاملات دوره امنیت وب
(function() {
    'use strict';
    var storageOK = true;
    try { localStorage.setItem('__wsc__','1'); localStorage.removeItem('__wsc__'); }
    catch(e) { storageOK = false; }

    // نوار پیشرفت مطالعه
    var bar = document.getElementById('reading-bar');
    function updateBar() {
        if (!bar) return;
        var h = document.documentElement;
        var max = h.scrollHeight - h.clientHeight;
        bar.style.width = (max > 0 ? (h.scrollTop/max)*100 : 0) + '%';
    }
    window.addEventListener('scroll', updateBar, { passive: true });
    updateBar();

    // Scroll Spy برای TOC
    var tocLinks = Array.prototype.slice.call(document.querySelectorAll('.toc-list a'));
    var parts = tocLinks.map(function(a){ return document.querySelector(a.getAttribute('href')); });
    if (tocLinks.length) {
        var spyTimer = null;
        window.addEventListener('scroll', function() {
            if (spyTimer) return;
            spyTimer = setTimeout(function() {
                spyTimer = null;
                var pos = window.scrollY + 130, current = 0;
                parts.forEach(function(el, i){ if (el && el.offsetTop <= pos) current = i; });
                tocLinks.forEach(function(a, i){ a.classList.toggle('active', i === current); });
            }, 90);
        }, { passive: true });
    }

    // ذخیره پیشرفت
    var doneBtn = document.getElementById('mark-done');
    var KEY = 'wsc_finished_v1';
    function getFinished() {
        if (!storageOK) return {};
        try { return JSON.parse(localStorage.getItem(KEY)) || {}; } catch(e) { return {}; }
    }
    if (doneBtn) {
        var chId = doneBtn.getAttribute('data-chapter');
        if (getFinished()[chId]) {
            doneBtn.classList.add('done');
            doneBtn.innerHTML = '✅ این فصل را تمام کرده‌اید';
        }
        doneBtn.addEventListener('click', function() {
            if (!storageOK) { alert('مرورگر شما اجازه ذخیره پیشرفت را نمی‌دهد.'); return; }
            var f = getFinished();
            if (f[chId]) delete f[chId]; else f[chId] = Date.now();
            try { localStorage.setItem(KEY, JSON.stringify(f)); } catch(e) {}
            if (f[chId]) {
                doneBtn.classList.add('done');
                doneBtn.innerHTML = '✅ این فصل را تمام کرده‌اید';
            } else {
                doneBtn.classList.remove('done');
                doneBtn.innerHTML = '✔️ این فصل را تمام کردم';
            }
        });
    }

    // نشان فصل‌های خوانده‌شده در صفحه اصلی
    var marks = document.querySelectorAll('.done-mark');
    if (marks.length) {
        var f = getFinished();
        marks.forEach(function(m){
            if (f[m.getAttribute('data-id')]) m.textContent = '✔';
        });
    }

    // باز/بستن همه پاسخ‌ها
    var openAll = document.getElementById('btn-open-answers');
    var closeAll = document.getElementById('btn-close-answers');
    if (openAll) openAll.addEventListener('click', function(){
        document.querySelectorAll('details').forEach(function(d){ d.open = true; });
    });
    if (closeAll) closeAll.addEventListener('click', function(){
        document.querySelectorAll('details').forEach(function(d){ d.open = false; });
    });

    // پیمایش با کلیدهای جهت‌دار
    document.addEventListener('keydown', function(e) {
        if (e.target && /^(INPUT|TEXTAREA|SELECT)$/.test(e.target.tagName)) return;
        var prev = document.getElementById('prev-link');
        var next = document.getElementById('next-link');
        if (e.key === 'ArrowRight' && next) { e.preventDefault(); next.click(); }
        else if (e.key === 'ArrowLeft' && prev) { e.preventDefault(); prev.click(); }
    });

    // کپی کد
    document.querySelectorAll('pre').forEach(function(pre) {
        var btn = document.createElement('button');
        btn.textContent = '📋 کپی';
        btn.className = 'copy-btn';
        btn.style.cssText = 'float:left;background:#00d97e;color:#0b1220;border:none;border-radius:6px;padding:2px 10px;font-size:0.75rem;cursor:pointer;margin-bottom:5px;';
        pre.parentNode.insertBefore(btn, pre);
        btn.addEventListener('click', function(){
            navigator.clipboard.writeText(pre.innerText).then(function(){
                btn.textContent = '✅ شد';
                setTimeout(function(){ btn.textContent = '📋 کپی'; }, 1500);
            });
        });
    });

    console.log('🛡️ دوره امنیت وب بارگذاری شد');
})();
