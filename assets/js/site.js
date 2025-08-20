// Global JS for multi-property site
(function () {
  // Placeholder for future enhancements (filters, search, tracking, etc.)
  console.log("Site JS loaded");

  // Simple keyboard focus outline helper
  const handleMouseDown = () => document.body.classList.add('using-mouse');
  const handleKeyDown = (e) => { if (e.key === 'Tab') document.body.classList.remove('using-mouse'); };
  window.addEventListener('mousedown', handleMouseDown);
  window.addEventListener('keydown', handleKeyDown);

  // Quick button navigates to the card's anchor href
  document.addEventListener('DOMContentLoaded', () => {
    const cards = document.querySelectorAll('.lux-card');
    cards.forEach(card => {
      const btn = card.querySelector('.quick-btn');
      const link = card.querySelector('a[href]');
      if (!btn || !link) return;
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        const href = link.getAttribute('href');
        if (href && href !== '#') {
          window.location.href = href;
        }
      });
    });
  });
})();
