document.addEventListener('DOMContentLoaded', () => {
    // 1. Theme Toggle Logic
    const themeToggleBtn = document.getElementById('theme-toggle');
    const htmlElement = document.documentElement;

    // Fonction pour appliquer le thème
    function applyTheme(isDark) {
        if (isDark) {
            htmlElement.classList.add('dark');
            htmlElement.classList.remove('light');
            if(themeToggleBtn) themeToggleBtn.innerHTML = '<span class="material-symbols-outlined text-xl">light_mode</span>';
        } else {
            htmlElement.classList.remove('dark');
            htmlElement.classList.add('light');
            if(themeToggleBtn) themeToggleBtn.innerHTML = '<span class="material-symbols-outlined text-xl">dark_mode</span>';
        }
    }

    // Déterminer le thème initial
    const storedTheme = localStorage.getItem('theme');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

    if (storedTheme === 'dark' || (!storedTheme && prefersDark)) {
        applyTheme(true);
    } else {
        applyTheme(false);
    }

    // Ecouteur sur le bouton manuel s'il existe
    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', () => {
            const isDarkNow = htmlElement.classList.contains('dark');
            applyTheme(!isDarkNow);
            localStorage.setItem('theme', !isDarkNow ? 'dark' : 'light');
        });
    }

    // Ecouteur sur la préférence système
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
        if (!localStorage.getItem('theme')) {
            applyTheme(e.matches);
        }
    });

    // 2. Logic for Click to Reveal (Emoij / Adjectives)
    // Utile pour le Wall of Fame et la Merch
    document.body.addEventListener('click', (e) => {
        const container = e.target.closest('.reveal-container');
        if (container) {
            container.classList.toggle('active');
        } else {
            // Fermer si on clique ailleurs
            document.querySelectorAll('.reveal-container.active').forEach(el => {
                el.classList.remove('active');
            });
        }
    });
});
