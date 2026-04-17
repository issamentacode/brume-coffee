import os
import re
import glob

BASE = r"c:\Users\Utilisateur\Documents\Projets\Brume_coffee"
html_files = glob.glob(os.path.join(BASE, "*.html"))

new_tailwind_config = """        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    "colors": {
                        "surface": "var(--bg-primary)",
                        "on-surface": "var(--text-main)",
                        "primary": "var(--accent-color)",
                        "on-primary": "var(--inverse-color)",
                        "surface-container-low": "var(--surface-low)",
                        "surface-container-high": "var(--surface-low)",
                        "surface-container": "var(--bg-primary)",
                        "secondary-container": "var(--surface-low)",
                        "on-secondary-container": "var(--text-main)",
                        "secondary": "var(--text-main)",
                        "on-surface-variant": "var(--text-main)",
                        "outline-variant": "transparent"
                    },
                    "fontFamily": {
                        "headline": ["'The Seasons'", "serif"],
                        "body": ["Inter", "sans-serif"],
                        "label": ["Inter", "sans-serif"],
                        "serif": ["'The Seasons'", "serif"]
                    }
                }
            }
        }"""

for path in html_files:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Replace tailwind config
    content = re.sub(
        r'tailwind\.config\s*=\s*\{.*?\n        \}(?=\s*</script>)',
        new_tailwind_config,
        content,
        flags=re.DOTALL
    )

    # 2. Add CSS and JS links in <head>
    if 'assets/css/theme.css' not in content:
        content = content.replace(
            '</head>',
            '    <link rel="stylesheet" href="assets/css/theme.css" />\n    <script src="assets/js/theme.js"></script>\n    <script src="assets/js/api.js"></script>\n</head>'
        )

    # 3. Add Theme Toggle Button next to Réserver button
    if 'id="theme-toggle"' not in content:
        toggle_btn = '\n                <button id="theme-toggle" class="p-2 rounded-full hover:bg-surface-low transition-colors text-primary flex items-center justify-center mr-2"><span class="material-symbols-outlined text-xl">dark_mode</span></button>'
        content = re.sub(
            r'<div class="flex items-center gap-4 z-50 relative">',
            r'<div class="flex items-center gap-4 z-50 relative">' + toggle_btn,
            content
        )

    # 4. Remove dark: classes as tailwind variables handle it now
    # This regex is an approximation, removes 'dark:text-[...]' or 'dark:bg-[...]'
    content = re.sub(r'dark:bg-\[[^\]]+\]', '', content)
    content = re.sub(r'dark:text-\[[^\]]+\]', '', content)
    content = re.sub(r'dark:border-\[[^\]]+\]', '', content)
    content = re.sub(r'dark:hover:text-\[[^\]]+\]', '', content)

    # 5. Global fixes for "No-line rule" (removing border classes in nav and other places)
    content = content.replace('border-b border-[#384c31]/5', 'border-none')
    content = content.replace('border-b border-[#384c31]', 'border-none')
    content = content.replace('border-t border-[#384c31]/10', 'border-none')
    content = content.replace('border border-outline-variant/50', 'border-none')
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {os.path.basename(path)}")
