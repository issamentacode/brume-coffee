/**
 * API.js - Data-Driven Architecture pour le Menu, Merch et Wall of Fame
 * Lit les Google Sheets publics de la propriétaire.
 */

// Ces URLs devront être remplacées par l'URL CSV de publication du Google Sheet
const GOOGLE_SHEETS_URLS = {
    // URL CSV/JSON de publication du Google Sheet
    menu: 'https://docs.google.com/spreadsheets/d/13Ithp4C69c3OzJrDpzN7IVSlAE1sEzxV_H8RCF0ZO7Y/gviz/tq?tqx=out:json&headers=1', 
    merch: 'https://docs.google.com/spreadsheets/d/13Ithp4C69c3OzJrDpzN7IVSlAE1sEzxV_H8RCF0ZO7Y/gviz/tq?tqx=out:json&headers=1',
    wallOfFame: 'https://docs.google.com/spreadsheets/d/1yQovY7kICYmxEsjcseLt9Iy4yOzv67JkTDBbqNUZn0I/gviz/tq?tqx=out:json&headers=1'
};

// L'utilisation des données Mockées est supprimée, la vraie API est en place !

// --- RENDERERS ---

async function fetchAndRenderMerch() {
    const container = document.getElementById('merch-container');
    if (!container) return;

    // Loading State
    container.innerHTML = `
        <div class="col-span-1 md:col-span-3 text-center">
            <div class="rituel-loader"></div>
            <p class="font-body text-sm font-light mt-4 opacity-70">Extraction des merveilles...</p>
        </div>
    `;

    try {
        const response = await fetch(GOOGLE_SHEETS_URLS.merch);
        const text = await response.text();
        const jsonContent = text.substring(47).slice(0, -2);
        const data = JSON.parse(jsonContent);
        
        let html = '';
        // No skip header row needed
        data.table.rows.forEach(row => {
            if(!row.c[0] || !row.c[0].v) return;

            const name = row.c[0] ? row.c[0].v : '';
            const price = row.c[1] ? row.c[1].v : '';
            const image = row.c[2] && row.c[2].v ? row.c[2].v : 'assets/baristas.jpg'; // fallback image
            const emojis = row.c[3] ? row.c[3].v : '';
            const tags = row.c[4] ? row.c[4].v : '';

            let reveals = '';
            const allWords = [...(tags ? tags.split(',') : []), ...(emojis ? emojis.split(' ') : [])].filter(w => w && w.trim() !== '');
            allWords.forEach((word, index) => {
                reveals += `<span class="reveal-item" style="transition-delay: ${index * 50}ms">${word.trim()}</span>`;
            });

            html += `
                <div class="reveal-container bg-surface-low rounded-[24px] p-6 shadow-sm hover:shadow-md transition-shadow">
                    <div class="aspect-square rounded-[24px_24px_0_24px] overflow-hidden mb-6">
                        <img src="${image}" class="w-full h-full object-cover" alt="${name}" />
                    </div>
                    <div class="flex justify-between items-baseline">
                        <h3 class="font-serif text-2xl text-[var(--accent-color)]">${name}</h3>
                        <span class="font-bold text-lg">${price}</span>
                    </div>
                    
                    <div class="reveal-overlay">
                        ${reveals}
                    </div>
                </div>
            `;
        });

        if (html === '') html = '<div class="col-span-full py-12 text-center text-on-surface-variant italic">Le petit marché se prépare... bientôt de nouvelles choses.</div>';
        container.innerHTML = html;
        
    } catch(e) {
        console.error("Error fetching merch sheets:", e);
        container.innerHTML = '<div class="col-span-full py-12 text-center text-on-surface-variant italic">Oups ! Impossible de contacter la boutique.</div>';
    }
}

async function fetchAndRenderWallOfFame() {
    const container = document.getElementById('walloffame-container');
    if (!container) return;

    // Loading State
    container.innerHTML = `
        <div class="col-span-1 md:col-span-3 text-center">
            <div class="rituel-loader"></div>
            <p class="font-body text-sm font-light mt-4 opacity-70">Création des souvenirs...</p>
        </div>
    `;

    try {
        const response = await fetch(GOOGLE_SHEETS_URLS.wallOfFame);
        const text = await response.text();
        const jsonContent = text.substring(47).slice(0, -2);
        const data = JSON.parse(jsonContent);
        
        let html = '';
        // No skip header row needed
        data.table.rows.forEach(row => {
            if(!row.c[0] || !row.c[0].v) return;

            const name = row.c[0] ? row.c[0].v : '';
            const image = row.c[1] && row.c[1].v ? row.c[1].v : 'assets/brume_photo_5.jpg'; // fallback image
            const emojis = row.c[2] ? row.c[2].v : '';
            const words = row.c[3] ? row.c[3].v : '';

            let reveals = '';
            const allWords = [...(words ? words.split(',') : []), ...(emojis ? emojis.split(' ') : [])].filter(w => w && w.trim() !== '');
            allWords.forEach((word, index) => {
                reveals += `<span class="reveal-item" style="transition-delay: ${index * 50}ms">${word.trim()}</span>`;
            });

            html += `
                <div class="reveal-container rounded-[24px] overflow-hidden shadow-sm aspect-[4/5] relative group">
                    <img src="${image}" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" alt="Client ${name}" />
                    <div class="absolute bottom-0 left-0 right-0 p-6 bg-gradient-to-t from-black/60 to-transparent">
                        <h3 class="font-serif text-3xl italic text-white">${name}</h3>
                    </div>
                    <div class="reveal-overlay">
                        ${reveals}
                    </div>
                </div>
            `;
        });

        if (html === '') html = '<div class="col-span-full py-12 text-center text-on-surface-variant italic">La grande famille Brume s\'agrandit... bientôt de nouveaux visages.</div>';
        container.innerHTML = html;

    } catch(e) {
        console.error("Error fetching Wall of Fame sheets:", e);
        container.innerHTML = '<div class="col-span-full py-12 text-center text-on-surface-variant italic">Le journal est fermé pour l\'instant.</div>';
    }
}

// Initialise fetching on explicit pages
document.addEventListener('DOMContentLoaded', () => {
    if (document.getElementById('merch-container')) {
        fetchAndRenderMerch();
    }
    if (document.getElementById('walloffame-container')) {
        fetchAndRenderWallOfFame();
    }
});
