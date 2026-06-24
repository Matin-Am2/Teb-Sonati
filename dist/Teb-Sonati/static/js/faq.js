document.addEventListener('DOMContentLoaded', () => {
    const questions = document.querySelectorAll('.faq-question');
  
    questions.forEach(btn => {
      const panel = btn.nextElementSibling;
  
      btn.addEventListener('click', () => {
        const isOpen = btn.getAttribute('aria-expanded') === 'true';
  
        // بستن همه سوال‌ها (آکاردئون)
        document.querySelectorAll('.faq-question').forEach(q => {
          q.setAttribute('aria-expanded', 'false');
        });
        document.querySelectorAll('.faq-answer').forEach(a => {
          a.hidden = true;
        });
  
        // باز کردن فقط همین یکی
        if (!isOpen) {
          btn.setAttribute('aria-expanded', 'true');
          panel.hidden = false;
        }
      });
    });
  });
  