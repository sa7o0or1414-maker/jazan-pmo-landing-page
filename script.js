// script.js - Custom JavaScript for Jazan PMO Landing Page

// Language Toggle Functionality
document.addEventListener('DOMContentLoaded', function() {
    const langToggle = document.getElementById('lang-toggle');
    const langText = document.getElementById('lang-text');
    const html = document.documentElement;
    const body = document.body;

    // Function to update text content based on language
    function updateLanguage(lang) {
        // Select all non-goals elements with data-en or data-ar attributes
        const textElements = document.querySelectorAll('[data-en], [data-ar]');
        textElements.forEach(element => {
            // Skip the goals list for now, it's handled separately
            if (element.id === 'goals-list') return;

            if (lang === 'ar') {
                element.textContent = element.getAttribute('data-ar');
            } else {
                element.textContent = element.getAttribute('data-en');
            }
        });

        // Goals list content conversion.
        const goalsList = document.getElementById('goals-list');
        if (goalsList) {
            const source = lang === 'ar' ? goalsList.getAttribute('data-ar') : goalsList.getAttribute('data-en');
            const items = source.split('|').map(item => item.trim()).filter(Boolean);
            goalsList.innerHTML = items.map(item => `<li>${item}</li>`).join('');

            // text-start behavior depending on direction
            if (lang === 'ar') {
                goalsList.classList.remove('text-start');
                goalsList.classList.add('text-end');
            } else {
                goalsList.classList.remove('text-end');
                goalsList.classList.add('text-start');
            }
        }

        // Update HTML dir attribute and body class
        if (lang === 'ar') {
            html.setAttribute('dir', 'rtl');
            html.setAttribute('lang', 'ar');
            body.classList.add('arabic');
            langText.textContent = 'AR';
            langToggle.setAttribute('data-lang', 'ar');
        } else {
            html.setAttribute('dir', 'ltr');
            html.setAttribute('lang', 'en');
            body.classList.remove('arabic');
            langText.textContent = 'EN';
            langToggle.setAttribute('data-lang', 'en');
        }
    }

    // Toggle language on button click
    langToggle.addEventListener('click', function() {
        const currentLang = langToggle.getAttribute('data-lang');
        const newLang = currentLang === 'en' ? 'ar' : 'en';
        updateLanguage(newLang);
    });

    // Smooth Scrolling for Navigation Links
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetSection = document.getElementById(targetId);
            if (targetSection) {
                targetSection.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Initialize with English
    updateLanguage('en');
});