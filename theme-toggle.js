// theme-toggle.js

document.addEventListener('DOMContentLoaded', () => {
    const body = document.body;

    // Function to apply the theme to the body and save it to local storage
    function applyTheme(theme) {
        if (theme === 'dark') {
            body.classList.add('dark-mode');
            localStorage.setItem('theme', 'dark');
        } else {
            body.classList.remove('dark-mode');
            localStorage.setItem('theme', 'light');
        }
    }

    // 1. Check for a saved theme preference in local storage first
    const savedTheme = localStorage.getItem('theme');

    if (savedTheme) {
        // If a preference is found, apply it
        applyTheme(savedTheme);
    } else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        // 2. If no preference is saved, check the user's operating system preference
        applyTheme('dark'); // Apply dark mode if OS prefers it
    } else {
        // 3. If no saved preference AND OS doesn't prefer dark, default to light mode
        applyTheme('light');
    }

    // No need for event listeners or button text updates since the button is removed.
});