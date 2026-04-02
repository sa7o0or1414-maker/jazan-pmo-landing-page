// script.js - Custom JavaScript for Jazan PMO Landing Page

// Language Toggle Functionality
document.addEventListener('DOMContentLoaded', function() {
    const langToggle = document.getElementById('lang-toggle');
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
            // Update globe icon color for Arabic
            langToggle.style.color = '#007bff';
        } else {
            html.setAttribute('dir', 'ltr');
            html.setAttribute('lang', 'en');
            body.classList.remove('arabic');
            // Update globe icon color for English
            langToggle.style.color = '#fff';
        }
    }

    // Language Toggle Button - Switch to English when clicked
    langToggle.addEventListener('click', function() {
        updateLanguage('en');
    });

    // Smooth Scrolling for Navigation Links (navbar, hero overlay, and custom nav links)
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link, .hero-nav-link, .nav-link-custom');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetSection = document.getElementById(targetId);
            if (targetSection) {
                targetSection.scrollIntoView({
                    behavior: 'smooth',
                    block: 'center'
                });
            }
        });
    });

    // Feedback buttons behavior
    const feedbackButtons = document.querySelectorAll('.feedback-btn');
    const feedbackMessage = document.getElementById('feedback-message');

    feedbackButtons.forEach(button => {
        button.addEventListener('click', () => {
            feedbackButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');

            const rate = button.getAttribute('data-rating');
            const msg = {
                1: { en: 'Very Dissatisfied', ar: 'غير راضٍ جدًا' },
                2: { en: 'Dissatisfied', ar: 'غير راضٍ' },
                3: { en: 'Neutral', ar: 'محايد' },
                4: { en: 'Satisfied', ar: 'راضٍ' },
                5: { en: 'Very Satisfied', ar: 'راضٍ جدًا' }
            };

            const activeLang = langToggle.getAttribute('data-lang');
            feedbackMessage.textContent = activeLang === 'ar' ? msg[rate].ar : msg[rate].en;
        });
    });

    // Initialize with Arabic
    updateLanguage('ar');
});
