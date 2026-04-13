#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de correction global pour tous les fichiers HTML de Brume Coffee.
"""
import os
import re
import glob

BASE = r"c:\Users\Utilisateur\Documents\Projets\Brume_coffee"

# --- Données réelles ---
REAL_EMAIL   = "essaievendredi123@gmail.com"
REAL_PHONE   = "07 75 86 76 47"
REAL_PHONE_INT = "+33 7 75 86 76 47"

html_files = glob.glob(os.path.join(BASE, "*.html"))

for path in html_files:
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()

    original = c

    # 1. Supprimer le doublon Material Symbols
    c = re.sub(
        r'(<link href="https://fonts\.googleapis\.com/css2\?family=Material\+Symbols\+Outlined[^"]*" rel="stylesheet"/>)\s*\r?\n\s*\1',
        r'\1',
        c
    )

    # 2. Corriger les fautes dans les modales et partout
    c = c.replace("Reserver une table", "Réserver une table")
    c = c.replace("Confirmer la reservation", "Confirmer la réservation")
    c = c.replace("Telephone / E-mail", "Téléphone / E-mail")
    c = c.replace("Nous sommes fermes a cette heure.", "Nous sommes fermés à cette heure.")
    c = re.sub(r"de 09h30 a 12h00", "de 09h30 à 12h00", c)
    c = re.sub(r"de 16h00 a 18h00", "de 16h00 à 18h00", c)
    c = re.sub(r"de 08h30 a 18h00", "de 08h30 à 18h00", c)
    c = re.sub(r"de 09h00 a 18h00", "de 09h00 à 18h00", c)
    c = re.sub(r"de 10h00 a 18h00", "de 10h00 à 18h00", c)
    c = re.sub(r"de 10h00 a 15h00", "de 10h00 à 15h00", c)
    c = c.replace("Nous vous attendons le", "Nous vous attendons le")
    c = c.replace("A tres vite chez Brume", "À très vite chez Brume")
    c = c.replace("ete envoyee", "été envoyée")
    c = c.replace("a bien ete", "a bien été")
    c = c.replace("Je souhaite reserver", "Je souhaite réserver")
    c = c.replace("reservation a bien", "réservation a bien")

    # 3. Remplacer les infos fictives de contact partout
    # Email fictif -> email réel
    c = c.replace("bonjour@brume.fr", REAL_EMAIL)
    c = c.replace("contact@brume-coffee.fr", REAL_EMAIL)
    c = c.replace("reservation@brume-coffee.fr", REAL_EMAIL)

    # Téléphone fictif -> vrai téléphone
    c = c.replace("07 00 00 00 00 (Numéro Fictif)", REAL_PHONE)
    c = c.replace("+33 1 00 00 00 00", REAL_PHONE_INT)

    # 4. Open Graph meta tags — ajout si absent
    og_block = f"""
    <!-- Open Graph / Social Sharing -->
    <meta property="og:type" content="website"/>
    <meta property="og:locale" content="fr_FR"/>
    <meta property="og:site_name" content="Brume Coffee"/>
    <meta property="og:title" content="Brume — Votre cocon de douceur et de slow living"/>
    <meta property="og:description" content="Café de spécialité, matcha de cérémonie et pâtisseries artisanales à Levallois-Perret. Un refuge pensé pour savourer l'instant présent."/>
    <meta property="og:image" content="assets/brume_photo_5.jpg"/>
    <meta name="twitter:card" content="summary_large_image"/>"""

    if 'property="og:type"' not in c:
        c = c.replace("</head>", og_block + "\n</head>", 1)

    # 5. Ajouter lazy loading aux images de la galerie lightbox
    c = re.sub(r'(<img src="assets/brume_photo_[^"]*")', r'\1 loading="lazy"', c)

    # 6. Review cards - hauteur min (via style inline si review-card)
    c = c.replace(
        'flex: 0 0 auto; width: 350px; background: var(--surface, #fcf9f3); border-radius: 1rem;\n            padding: 2rem; margin-right: 1.5rem; white-space: normal; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);',
        'flex: 0 0 auto; width: 350px; min-height: 220px; background: var(--surface, #fcf9f3); border-radius: 1rem;\n            padding: 2rem; margin-right: 1.5rem; white-space: normal; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); display: flex; flex-direction: column; justify-content: space-between;'
    )

    # 7. Scroll reveal — ajouter le script JS si absent
    scroll_reveal_script = """
<script>
/* Scroll Reveal Animation */
(function(){
    const observer = new IntersectionObserver(function(entries){
        entries.forEach(function(entry){
            if(entry.isIntersecting){
                entry.target.classList.add('brume-visible');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1, rootMargin: '0px 0px -60px 0px' });
    document.querySelectorAll('.brume-reveal').forEach(function(el){
        observer.observe(el);
    });
})();
</script>"""

    scroll_reveal_css = """
<style>
.brume-reveal {
    opacity: 0;
    transform: translateY(28px);
    transition: opacity 0.7s ease, transform 0.7s ease;
}
.brume-visible {
    opacity: 1;
    transform: translateY(0);
}
</style>"""

    if 'brume-reveal' not in c:
        c = c.replace("</head>", scroll_reveal_css + "\n</head>", 1)
        c = c.replace("</body>", scroll_reveal_script + "\n</body>", 1)

        # Ajouter la classe brume-reveal aux sections h2 principales
        c = re.sub(
            r'(<(section|div)[^>]*class="[^"]*py-24[^"]*")',
            r'\1',
            c
        )

    if c != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(c)
        print(f"[OK] Updated: {os.path.basename(path)}")
    else:
        print(f"[--] No changes: {os.path.basename(path)}")

print("\nAll corrections applied!")
