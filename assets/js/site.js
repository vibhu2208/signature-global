// Global JS for multi-property site
(function () {
  // Navigation functionality
  document.addEventListener('DOMContentLoaded', function() {
    const navToggle = document.querySelector('.nav-toggle');
    const navLinks = document.querySelector('.nav-links');
    const navItems = document.querySelectorAll('.nav-links a');
    
    // Toggle mobile menu
    if (navToggle) {
      navToggle.addEventListener('click', function() {
        const isExpanded = this.getAttribute('aria-expanded') === 'true' || false;
        this.setAttribute('aria-expanded', !isExpanded);
        navLinks.classList.toggle('active');
        document.body.style.overflow = navLinks.classList.contains('active') ? 'hidden' : '';
      });
    }
    
    // Close mobile menu when clicking on a nav item
    navItems.forEach(item => {
      item.addEventListener('click', () => {
        if (navLinks.classList.contains('active')) {
          navLinks.classList.remove('active');
          navToggle.setAttribute('aria-expanded', 'false');
          document.body.style.overflow = '';
        }
      });
    });
    
    // Sticky navbar on scroll
    const navbar = document.querySelector('.navbar');
    if (navbar) {
      window.addEventListener('scroll', function() {
        if (window.scrollY > 10) {
          navbar.style.padding = '0.5rem 0';
          navbar.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
        } else {
          navbar.style.padding = '1rem 0';
          navbar.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.05)';
        }
      });
    }
  });

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
