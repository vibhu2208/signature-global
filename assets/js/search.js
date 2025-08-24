document.addEventListener('DOMContentLoaded', function() {
  // Get DOM elements
  const searchInput = document.querySelector('.luxury-hero .search-input');
  const searchButton = document.querySelector('.luxury-hero .search-button');
  const categoryFilters = document.querySelectorAll('.category-btn');
  const propertyCards = document.querySelectorAll('.lux-card');
  const propertySections = document.querySelectorAll('.section');

  // Search function
  function performSearch(searchTerm) {
    const term = searchTerm.toLowerCase().trim();
    const searchSections = {
      'industrial plots': '.section:first-child',
      'premium property': '.section:nth-child(2)',
      'independent floors': '.section:nth-child(3)',
      'sco plots': '.section:last-child'
    };
    
    // Hide all properties first
    propertyCards.forEach(card => card.style.display = 'none');
    
    if (!term) {
      // If search is empty, show all properties
      propertyCards.forEach(card => card.style.display = 'block');
      propertySections.forEach(section => section.style.display = 'block');
      return;
    }
    
    // Check if it's a category search
    const matchingSection = searchSections[term] || '';
    
    if (matchingSection) {
      // Show only the matching section and hide others
      propertySections.forEach(section => {
        section.style.display = 'none';
      });
      
      const targetSection = document.querySelector(matchingSection);
      if (targetSection) {
        targetSection.style.display = 'block';
        const cards = targetSection.querySelectorAll('.lux-card');
        cards.forEach(card => card.style.display = 'block');
      }
    } else {
      // Regular text search across all properties
      let hasMatches = false;
      
      propertyCards.forEach(card => {
        const cardText = card.textContent.toLowerCase();
        if (cardText.includes(term)) {
          card.style.display = 'block';
          hasMatches = true;
        }
      });
      
      // Show/hide sections based on matches
      propertySections.forEach(section => {
        const sectionCards = section.querySelectorAll('.lux-card');
        const visibleCards = Array.from(sectionCards).some(card => card.style.display === 'block');
        section.style.display = visibleCards ? 'block' : 'none';
      });
    }

    // Scroll to results if there's a search term
    if (term) {
      const firstSection = document.querySelector('.section[style*="display: block"]');
      if (firstSection) {
        firstSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }
  }

  // Quick search tag functionality
  const quickSearchTags = document.querySelectorAll('.quick-search-tag');
  quickSearchTags.forEach(tag => {
    tag.addEventListener('click', () => {
      const searchTerm = tag.getAttribute('data-search');
      searchInput.value = searchTerm;
      performSearch(searchTerm);
      
      // Add active state
      quickSearchTags.forEach(t => t.classList.remove('active'));
      tag.classList.add('active');
    });
  });

  // Event listeners
  searchButton.addEventListener('click', () => performSearch(searchInput.value));
  
  searchInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
      performSearch(searchInput.value);
      // Remove active state from all tags when doing a manual search
      quickSearchTags.forEach(t => t.classList.remove('active'));
    }
  });

  // Category filter functionality
  categoryFilters.forEach(button => {
    button.addEventListener('click', () => {
      // Toggle active state
      categoryFilters.forEach(btn => btn.classList.remove('active'));
      button.classList.add('active');
      
      // Perform search with category
      const category = button.textContent.trim();
      searchInput.value = category;
      performSearch(category);
    });
  });
});
