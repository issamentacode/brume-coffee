#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enrichit le footer de toutes les pages HTML avec l'adresse et les horaires.
"""
import os, glob, re

BASE = r"c:\Users\Utilisateur\Documents\Projets\Brume_coffee"

RICH_FOOTER = '''<!-- Footer -->
<footer class="bg-[#f6f3ed] w-full pt-16 pb-8 px-8 border-t border-[#384c31]/10">
<div class="max-w-7xl mx-auto">
    <div class="grid grid-cols-1 md:grid-cols-4 gap-12 mb-12">
        <!-- Brand -->
        <div class="md:col-span-1 space-y-4">
            <span class="font-serif text-2xl italic text-[#384c31] font-bold">Brume</span>
            <p class="text-sm text-[#384c31]/60 leading-relaxed">Un cocon de douceur et de slow living au coeur de Levallois-Perret.</p>
            <a href="https://www.instagram.com/brume.levallois/" target="_blank" class="inline-flex items-center gap-2 text-[#384c31]/70 hover:text-[#384c31] transition-colors text-sm font-medium">
                <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
                @brume.levallois
            </a>
        </div>
        <!-- Navigation -->
        <div class="space-y-4">
            <h4 class="font-serif text-[#384c31] font-semibold text-sm uppercase tracking-widest">Pages</h4>
            <nav class="flex flex-col space-y-2">
                <a href="index.html" class="text-sm text-[#384c31]/60 hover:text-[#384c31] transition-colors">Accueil</a>
                <a href="menu.html" class="text-sm text-[#384c31]/60 hover:text-[#384c31] transition-colors">La Carte</a>
                <a href="histoire.html" class="text-sm text-[#384c31]/60 hover:text-[#384c31] transition-colors">Notre Histoire</a>
                <a href="galerie.html" class="text-sm text-[#384c31]/60 hover:text-[#384c31] transition-colors">Galerie</a>
                <a href="visiter.html" class="text-sm text-[#384c31]/60 hover:text-[#384c31] transition-colors">Nous Visiter</a>
            </nav>
        </div>
        <!-- Hours -->
        <div class="space-y-4">
            <h4 class="font-serif text-[#384c31] font-semibold text-sm uppercase tracking-widest">Horaires</h4>
            <table class="text-sm text-[#384c31]/60 w-full">
                <tr><td class="pr-4 py-0.5">Lundi</td><td class="text-right">09:30–12:00, 16:00–18:00</td></tr>
                <tr><td class="pr-4 py-0.5">Mardi – Vendredi</td><td class="text-right">08:30–18:00</td></tr>
                <tr><td class="pr-4 py-0.5">Samedi</td><td class="text-right">10:00–18:00</td></tr>
                <tr><td class="pr-4 py-0.5">Dimanche</td><td class="text-right">10:00–15:00</td></tr>
            </table>
        </div>
        <!-- Contact -->
        <div class="space-y-4">
            <h4 class="font-serif text-[#384c31] font-semibold text-sm uppercase tracking-widest">Contact</h4>
            <div class="text-sm text-[#384c31]/60 space-y-2">
                <p>2 Rue Camille Pelletan<br/>92300 Levallois-Perret</p>
                <p><a href="tel:+33775867647" class="hover:text-[#384c31] transition-colors">07 75 86 76 47</a></p>
                <p><a href="mailto:essaievendredi123@gmail.com" class="hover:text-[#384c31] transition-colors">essaievendredi123@gmail.com</a></p>
            </div>
        </div>
    </div>
    <!-- Bottom bar -->
    <div class="border-t border-[#384c31]/10 pt-8 flex flex-col md:flex-row justify-between items-center gap-4">
        <span class="text-xs text-[#384c31]/40">&copy; 2026 Brume Coffee — Levallois-Perret</span>
        <a href="#" onclick="showMentionsLegales(event)" class="text-xs text-[#384c31]/40 hover:text-[#384c31]/80 underline decoration-[#feae8c] transition-colors">Mentions Légales</a>
    </div>
</div>
</footer>'''

html_files = glob.glob(os.path.join(BASE, "*.html"))

for path in html_files:
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()

    original = c

    # Replace all footer variants with the rich footer
    # Match "<footer ..." to "</footer>"
    c = re.sub(r'<!-- Footer(?:[^<]|<(?!footer))*?-->\s*<footer[\s\S]*?</footer>', RICH_FOOTER, c)

    if c != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(c)
        print(f"[OK] Footer updated: {os.path.basename(path)}")
    else:
        print(f"[--] No footer match: {os.path.basename(path)}")

print("\nDone!")
