import re

with open(r'c:\Users\Utilisateur\Documents\Projets\Brume_coffee\menu.html', 'r', encoding='utf-8') as f:
    html = f.read()

merch_block = """
        <!-- Merch Section -->
        <section class="mt-24 mb-12">
            <div class="flex items-center justify-between mb-12 border-b border-surface-low border-opacity-10 pb-4">
                <div>
                    <span class="text-secondary font-label tracking-widest uppercase text-sm mb-2 block">Souvenirs & Maison</span>
                    <h2 class="font-serif text-4xl text-primary">Le Petit Marché</h2>
                </div>
                <span class="material-symbols-outlined text-4xl text-primary" data-icon="shopping_bag">shopping_bag</span>
            </div>
            <div id="merch-container" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-10">
                <!-- Data injected by api.js -->
            </div>
        </section>
"""

# Find the closing tag of the main grid
html = html.replace('        </div>\n\n        <!-- Footer -->', merch_block + '        </div>\n\n        <!-- Footer -->')

with open(r'c:\Users\Utilisateur\Documents\Projets\Brume_coffee\menu.html', 'w', encoding='utf-8') as f:
    f.write(html)
