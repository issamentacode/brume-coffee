import re

def reconstruct_galerie():
    with open('index.html', 'r', encoding='utf-8') as f:
        idx_content = f.read()

    # 1. Nav & Head
    head_nav = idx_content.split('<main class="pt-32 pb-24">')[0]
    # Highlight Galerie in nav (if not already handled by common structure, but it's okay)
    head_nav = head_nav.replace('href="galerie.html" class="text-on-surface hover:text-primary transition-colors duration-300 font-serif text-lg tracking-tight"', 'href="galerie.html" class="text-primary border-b border-primary pb-1 font-serif text-lg tracking-tight"')

    # 2. Main Galerie Header
    galerie_header = """    <main class="pt-32 pb-24">
        <header class="max-w-7xl mx-auto px-8 mb-16 text-center brume-reveal">
            <h1 class="text-6xl md:text-8xl font-headline italic text-primary mb-6">Galerie Brume</h1>
            <p class="text-xl font-body text-on-surface-variant max-w-2xl mx-auto">Instants de douceur et de partage. Chaque image est une infime partie de notre quotidien...</p>
        </header>
"""
    # 3. Block 1: Asymmetric Editorial Gallery
    block_1 = """        <section class="max-w-7xl mx-auto px-8">
            <div class="grid grid-cols-12 gap-y-24 md:gap-y-48 gap-x-8">
                <!-- Large Vertical Image & Quote -->
                <div class="col-span-12 md:col-span-7 relative">
                    <div class="aspect-[4/5] rounded-xl overflow-hidden shadow-sm"
                        style="border-bottom-right-radius: 0;">
                        <img class="w-full h-full object-cover"
                            data-alt="Brume Galerie"
                            src="assets/galerie_img1.jpg" />
                    </div>
                    <div class="mt-8 md:absolute md:-right-16 md:bottom-24 md:w-80 bg-surface-container-lowest p-8 md:shadow-lg rounded-2xl">
                        <span class="block font-headline text-3xl italic text-secondary mb-4">"Le goût de l'authentique"</span>
                        <p class="font-body text-sm text-on-surface-variant leading-relaxed">
                            Le goût des choses vraies. Nos créations sont le fruit d'une passion sincère et d'une patience infinie.
                        </p>
                    </div>
                </div>
                <!-- Text Interstitial -->
                <div class="col-span-12 md:col-span-4 md:col-start-9 flex flex-col justify-center">
                    <h2 class="font-headline text-4xl text-primary mb-6">Chaleur Humaine</h2>
                    <p class="font-body text-lg text-on-surface-variant mb-8 leading-relaxed">
                        Plus qu'un lieu, Brume est un refuge. Une table où l'on se retrouve, une parenthèse enchantée dans le tumulte du quotidien.
                    </p>
                    <div class="w-16 h-0.5 bg-secondary opacity-30"></div>
                </div>
                <!-- Bento Grid Layout for Smaller Moments -->
                <div class="col-span-12 grid grid-cols-1 md:grid-cols-3 gap-12">
                    <div class="flex flex-col">
                        <div class="aspect-square bg-surface-container-low rounded-xl overflow-hidden mb-6">
                            <img class="w-full h-full object-cover grayscale-[20%] hover:grayscale-0 transition-all duration-700"
                                src="assets/matcha_brewing.jpg" />
                        </div>
                        <h3 class="font-headline text-2xl text-on-surface italic">Moments partagés</h3>
                        <p class="font-body text-sm text-on-surface-variant mt-2">La douceur d'être ensemble.</p>
                    </div>
                    <div class="hidden md:flex flex-col justify-center items-center text-center p-8 border border-outline-variant/20 rounded-xl">
                        <span class="material-symbols-outlined text-4xl text-secondary mb-4">auto_awesome</span>
                        <p class="font-headline text-xl text-primary px-4 italic">"La simplicité est le luxe suprême."</p>
                    </div>
                    <div class="flex flex-col">
                        <div class="aspect-square bg-surface-container-low rounded-xl overflow-hidden mb-6" style="border-top-left-radius: 0;">
                            <img class="w-full h-full object-cover" src="assets/baristas.jpg" />
                        </div>
                        <h3 class="font-headline text-2xl text-on-surface italic">Fait Maison</h3>
                        <p class="font-body text-sm text-on-surface-variant mt-2">Des ingrédients locaux, un savoir-faire intact.</p>
                    </div>
                </div>
            </div>
        </section>
"""

    # 4. Avis Clients
    # Find avis clients in index.html, it starts with: <!-- Avis Clients Section --> or <section class="py-24 bg-surface-container-high
    avis_start = idx_content.find('<section class="py-24 bg-surface-container-high overflow-hidden relative">')
    avis_end = idx_content.find('</section>', avis_start) + 10
    if avis_start == -1:
        # try the id=avis
        avis_start = idx_content.find('<section id="avis"')
        if avis_start == -1:
            pass # We need to handle this
    avis_content = idx_content[avis_start:avis_end] + "\n"

    # 5. Block 2: Signature Editorial + Journal CTA
    block_2 = """
        <section class="max-w-7xl mx-auto px-8 mt-24 md:mt-48">
            <div class="grid grid-cols-12 gap-y-24 md:gap-y-48 gap-x-8">
                <!-- Signature Editorial Section -->
                <div class="col-span-12 bg-surface-container-low p-12 md:p-24 rounded-3xl grid md:grid-cols-2 gap-16 items-center">
                    <div>
                        <h2 class="font-headline text-5xl text-primary leading-tight mb-8 italic">Une atmosphère,<br />une émotion.</h2>
                        <div class="space-y-12">
                            <div class="flex gap-6">
                                <span class="font-headline text-4xl text-secondary opacity-50 italic">01</span>
                                <div>
                                    <h4 class="font-body font-semibold text-on-surface mb-2">La Tendresse</h4>
                                    <p class="font-body text-on-surface-variant leading-relaxed">Un accueil doux dès le seuil de la porte, une attention sincère pour que vous vous sentiez ici chez vous.</p>
                                </div>
                            </div>
                            <div class="flex gap-6">
                                <span class="font-headline text-4xl text-secondary opacity-50 italic">02</span>
                                <div>
                                    <h4 class="font-body font-semibold text-on-surface mb-2">La transmission</h4>
                                    <p class="font-body text-on-surface-variant leading-relaxed">Chaque préparation porte une histoire, transmise avec émotion par nos artisans passionnés.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="relative h-full min-h-[400px] rounded-2xl overflow-hidden group">
                        <div class="absolute inset-0 bg-primary/10 group-hover:bg-transparent transition-colors duration-500"></div>
                        <img class="w-full h-full object-cover" src="assets/galerie_img2.jpg" />
                        <div class="absolute inset-0 flex items-center justify-center">
                            <a href="#" onclick="event.preventDefault(); openGalleryLightbox();" class="bg-surface-bright/90 backdrop-blur-md p-6 rounded-full shadow-lg group-hover:scale-110 transition-transform cursor-pointer flex items-center justify-center">
                                <span class="material-symbols-outlined text-primary text-3xl">play_arrow</span>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Journal CTA -->
        <section class="max-w-7xl mx-auto px-8 mt-48 text-center pb-24">
            <div class="inline-block px-6 py-2 border border-outline-variant/30 rounded-full mb-8">
                <span class="font-body text-xs uppercase tracking-[0.2em] text-on-surface-variant">Rejoignez l'expérience</span>
            </div>
            <h2 class="font-headline text-6xl text-primary italic mb-12">Vivez l'instant présent.</h2>
            <button onclick="showReservation(event)" class="bg-primary text-on-primary px-12 py-4 rounded-lg font-body font-medium hover:opacity-90 transition-all transform hover:-translate-y-1">
                Passer nous voir
            </button>
        </section>
    </main>
"""

    # 6. Lightbox + Footer
    footer_start = idx_content.find('<!-- Footer -->')
    lightbox_and_footer = """
        <!-- Gallery Lightbox -->
        <div class="gallery-lightbox" id="galleryLightbox">
            <button class="gallery-close" onclick="closeGalleryLightbox()">
                <span class="material-symbols-outlined" style="font-size:24px;">close</span>
            </button>
            <h3>Galerie Brume</h3>
            <div class="gallery-grid">
                <img src="assets/baristas.jpg" alt="Brume Coffee" onload="this.classList.add('loaded')">
                <img src="assets/brume_photo_1.jpg" loading="lazy" alt="Brume Coffee" onload="this.classList.add('loaded')">
                <img src="assets/brume_photo_2.jpg" loading="lazy" alt="Brume Coffee" onload="this.classList.add('loaded')">
                <img src="assets/brume_photo_3.jpg" loading="lazy" alt="Brume Coffee" onload="this.classList.add('loaded')">
                <img src="assets/brume_photo_4.jpg" loading="lazy" alt="Brume Coffee" onload="this.classList.add('loaded')">
                <img src="assets/brume_photo_5.jpg" loading="lazy" alt="Brume Coffee" onload="this.classList.add('loaded')">
                <img src="assets/brume_photo_6.jpg" loading="lazy" alt="Brume Coffee" onload="this.classList.add('loaded')">
                <img src="assets/brume_photo_7.jpg" loading="lazy" alt="Brume Coffee" onload="this.classList.add('loaded')">
                <img src="assets/brume_photo_8.jpg" loading="lazy" alt="Brume Coffee" onload="this.classList.add('loaded')">
                <img src="assets/brume_photo_9.jpg" loading="lazy" alt="Brume Coffee" onload="this.classList.add('loaded')">
                <img src="assets/brume_photo_10.jpg" loading="lazy" alt="Brume Coffee" onload="this.classList.add('loaded')">
                <img src="assets/brume_photo_11.jpg" loading="lazy" alt="Brume Coffee" onload="this.classList.add('loaded')">
                <img src="assets/brume_photo_12.jpg" loading="lazy" alt="Brume Coffee" onload="this.classList.add('loaded')">
                <img src="assets/brume_photo_13.jpg" loading="lazy" alt="Brume Coffee" onload="this.classList.add('loaded')">
                <img src="assets/brume_photo_14.jpg" loading="lazy" alt="Brume Coffee" onload="this.classList.add('loaded')">
                <img src="assets/brume_photo_20.jpg" loading="lazy" alt="Brume Coffee" onload="this.classList.add('loaded')">
                <img src="assets/brume_photo_21.jpg" loading="lazy" alt="Brume Coffee" onload="this.classList.add('loaded')">
                <img src="assets/brume_photo_22.jpg" loading="lazy" alt="Brume Coffee" onload="this.classList.add('loaded')">
                <img src="assets/brume_photo_23.jpg" loading="lazy" alt="Brume Coffee" onload="this.classList.add('loaded')">
                <img src="assets/brume_photo_24.jpg" loading="lazy" alt="Brume Coffee" onload="this.classList.add('loaded')">
                <img src="assets/brume_photo_25.jpg" loading="lazy" alt="Brume Coffee" onload="this.classList.add('loaded')">
                <img src="assets/brume_photo_26.jpg" loading="lazy" alt="Brume Coffee" onload="this.classList.add('loaded')">
                <img src="assets/brume_photo_30.jpg" loading="lazy" alt="Brume Coffee" onload="this.classList.add('loaded')">
                <img src="assets/brume_photo_31.jpg" loading="lazy" alt="Brume Coffee" onload="this.classList.add('loaded')">
                <img src="assets/brume_photo_32.jpg" loading="lazy" alt="Brume Coffee" onload="this.classList.add('loaded')">
                <img src="assets/brume_photo_33.jpg" loading="lazy" alt="Brume Coffee" onload="this.classList.add('loaded')">
                <img src="assets/brume_photo_40.jpg" loading="lazy" alt="Brume Coffee" onload="this.classList.add('loaded')">
                <img src="assets/brume_photo_41.jpg" loading="lazy" alt="Brume Coffee" onload="this.classList.add('loaded')">
                <img src="assets/brume_photo_42.jpg" loading="lazy" alt="Brume Coffee" onload="this.classList.add('loaded')">
                <img src="assets/brume_photo_50.jpg" loading="lazy" alt="Brume Coffee" onload="this.classList.add('loaded')">
                <img src="assets/galerie_img1.jpg" loading="lazy" alt="Brume Coffee" onload="this.classList.add('loaded')">
                <img src="assets/galerie_img2.jpg" loading="lazy" alt="Brume Coffee" onload="this.classList.add('loaded')">
            </div>
        </div>
        <script>
            function openGalleryLightbox() {
                const lb = document.getElementById('galleryLightbox');
                lb.classList.add('active');
                document.body.style.overflow = 'hidden';
                setTimeout(() => lb.classList.add('visible'), 10);
            }
            function closeGalleryLightbox() {
                const lb = document.getElementById('galleryLightbox');
                lb.classList.remove('visible');
                setTimeout(() => {
                    lb.classList.remove('active');
                    document.body.style.overflow = '';
                }, 400);
            }
            document.getElementById('galleryLightbox').addEventListener('click', function (e) {
                if (e.target === this) closeGalleryLightbox();
            });
        </script>
""" + "\n" + idx_content[footer_start:]

    final_content = head_nav + galerie_header + block_1 + avis_content + block_2 + lightbox_and_footer

    with open('galerie.html', 'w', encoding='utf-8') as f:
        f.write(final_content)

reconstruct_galerie()
