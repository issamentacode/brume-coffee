import os, re, glob

base_dir = r"c:\Users\Utilisateur\Documents\Projets\Brume_coffee"

def get_nav_html(current_page):
    links = [
        {"file": "index.html", "label": "Accueil"},
        {"file": "menu.html", "label": "Menu"},
        {"file": "histoire.html", "label": "Notre Histoire"},
        {"file": "galerie.html", "label": "Galerie"},
        {"file": "visiter.html", "label": "Nous Visiter"}
    ]
    
    desktop_links = ""
    mobile_links = ""
    
    for link in links:
        is_active = (current_page == link["file"])
        if is_active:
            desktop_class = 'text-[#384c31] dark:text-[#feae8c] border-b border-[#384c31] dark:border-[#feae8c] pb-1 font-serif text-lg tracking-tight Newsreader'
            mobile_class = 'font-serif text-4xl text-[#384c31] dark:text-[#feae8c] italic'
        else:
            desktop_class = 'text-[#4f6447] dark:text-[#c4c8be] hover:text-[#384c31] dark:hover:text-[#feae8c] transition-colors duration-300 font-serif text-lg tracking-tight Newsreader'
            mobile_class = 'font-serif text-4xl text-[#4f6447] dark:text-[#c4c8be] hover:text-[#384c31] dark:hover:text-[#feae8c] transition-colors duration-300'
            
        desktop_links += f'            <a class="{desktop_class}" href="{link["file"]}">{link["label"]}</a>\n'
        mobile_links += f'        <a class="{mobile_class}" href="{link["file"]}">{link["label"]}</a>\n'

    nav_html = f'''<!-- Mobile Menu Overlay -->
<div id="mobileMenu" class="fixed inset-0 z-40 bg-[#fcf9f3] dark:bg-[#1c1c18] flex flex-col items-center justify-center space-y-10 opacity-0 pointer-events-none transition-opacity duration-300">
{mobile_links}</div>

<!-- TopNavBar -->
<nav class="fixed top-0 w-full z-50 bg-[#fcf9f3]/85 dark:bg-[#1c1c18]/85 backdrop-blur-xl transition-all duration-300 shadow-sm border-b border-[#384c31]/5">
    <div class="flex justify-between items-center max-w-7xl mx-auto px-6 md:px-8 py-4 md:py-6 relative">
        <a class="font-serif text-2xl font-bold italic text-[#384c31] dark:text-[#fcf9f3] z-50 relative" href="index.html">Brume</a>
        
        <div class="hidden md:flex items-center space-x-12">
{desktop_links}        </div>
        
        <div class="flex items-center gap-4 z-50 relative">
            <a href="#" onclick="showReservation(event)" class="bg-[#384c31] text-white px-5 md:px-8 py-2 md:py-2.5 rounded-lg font-body text-sm font-medium tracking-wide hover:opacity-90 transition-opacity" style="display:flex; justify-content:center; align-items:center;">
                Réserver
            </a>
            <button id="mobileMenuBtn" onclick="toggleMobileMenu()" class="md:hidden text-[#384c31] dark:text-[#fcf9f3] p-1 focus:outline-none flex items-center justify-center" aria-label="Menu" style="width:40px; height:40px;">
                <span class="material-symbols-outlined text-3xl menu-icon">menu</span>
            </button>
        </div>
    </div>
</nav>'''
    return nav_html

script_js = '''
<script>
    function toggleMobileMenu() {
        const menu = document.getElementById('mobileMenu');
        const icon = document.querySelector('.menu-icon');
        if (menu.classList.contains('opacity-0')) {
            menu.classList.remove('opacity-0', 'pointer-events-none');
            document.body.classList.add('overflow-hidden');
            icon.textContent = 'close';
        } else {
            menu.classList.add('opacity-0', 'pointer-events-none');
            document.body.classList.remove('overflow-hidden');
            icon.textContent = 'menu';
        }
    }
</script>
'''

html_files = glob.glob(os.path.join(base_dir, "*.html"))

for file_path in html_files:
    basename = os.path.basename(file_path)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Determine nav borders
    # Some start with <nav ..., we will replace until </nav> completely
    nav_pattern = re.compile(r'<!-- TopNavBar -->\s*<nav.*?</nav>', re.DOTALL)
    
    nav_html = get_nav_html(basename)
    
    if nav_pattern.search(content):
        # We replace any existing Mobile Menu Overlay too if we re-run
        mobile_menu_pattern = re.compile(r'<!-- Mobile Menu Overlay -->.*?</nav>', re.DOTALL)
        if mobile_menu_pattern.search(content):
            content = mobile_menu_pattern.sub(nav_html, content)
        else:
            content = nav_pattern.sub(nav_html, content)
            
        print(f"[OK] Replaced nav in {basename}")
    else:
        # Fallback if no <!-- TopNavBar -->
        nav_only_pattern = re.compile(r'<nav.*?</nav>', re.DOTALL)
        if nav_only_pattern.search(content):
             content = nav_only_pattern.sub(nav_html, content)
             print(f"[OK] Replaced raw <nav> in {basename}")
             
    # Inject toggle script if not there
    if 'function toggleMobileMenu()' not in content:
        content = content.replace('</body>', script_js + '\n</body>')

    # Remove duplicates if any
    content = content.replace(script_js + '\n' + script_js, script_js)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Nav updated.")
