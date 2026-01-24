// Get your elements
const container = document.querySelector('.search-container');
const input = document.querySelector('.search-input');

// Add click listener
container.addEventListener('click', function() {
    // Toggle expanded class
    container.classList.toggle('expanded');
    // Focus input when expanded
    if (container.classList.contains('expanded')) {
        input.focus();
    }
});