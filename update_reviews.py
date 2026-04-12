import re

reviews = [
    ("Lilia Mahfoudi", "J’ai découvert le matcha chez Brume pour la toute première fois… et j’ai adoré ! Très doux, bien équilibré, pas trop sucré… une super découverte. Les gâteaux faits maison sont aussi délicieux, on sent que tout est préparé avec soin."),
    ("Morgan Farley", "Very passionate and welcoming owner. I would recommend a trip to brume to anyone in the area! A cozy vibe and all handmade treats."),
    ("Teresa Lorkiewicz", "Polecam , pyszna kawa , smaczna matcha , bardzo miła obsługa , uroczy lokal . 👌"),
    ("Nuria Catalán", "Sehr schönes Café. Tolle Matcha Latte und Kaffe ✨👌🏼"),
    ("Juliette Valor", "Très bonne expérience chez Brume, le matcha au caramel était très bon (le sirop de caramel est fait maison !), et le carrot cake (maison aussi) était délicieux. Olga la gérante est très gentille et accueillante !"),
    ("Milena", "I love Japan culture. Matcha prepared very profesionally Taste lovely. 10/10"),
    ("Grzegorz Dziechciarz", "Super kawa. To jest ten smak :) Fajne, przyjazne miejsce na mapie Paryża. polecam"),
    ("Guillaume Fournier", "Excellent service and peaceful atmosphere, the owner told us the story of how they build the coffee shop and types of coffee. I highly recommend :)"),
    ("Emi BECAERT", "Très bonne adresse, qui vient d’ouvrir. Le lieu est très cosy et les matchas délicieux ! Je reviendrai avec plaisir"),
    ("Szczęście wPlecaku", "Matcha najwyższej jakości. Miałam okazję uczestniczyć w ich spotkaniu z dostawcą matchy prosto z ekologicznych plantacji z Japonii. Smak mówi sam za siebie. Polecam sprawdzić"),
    ("Sara dumitrean", "Étant amatrice de matcha, celui-là je vous le conseille à 100% les yeux fermés. On sent bien le mélange sans avoir un goût d’herbe, l’ambiance est superbe avec de bonnes musiques relaxantes et le personnel est très agréable. Foncez !!!"),
    ("Joan Rwamba", "If you need a good matcha this is the only place in Paris you can get it 🥰🥰🥰😩"),
    ("Adrian Kiełtyka", "Ważny punkt na mapie - zdecydowanie warto odwiedzić 🍵"),
    ("Paola MANZONI", "Accueil très sympathique par cette jeune propriétaire et sa maman... Apparemment ils sont spécialisés dans la préparation du matcha, perso j’ai pris un cappuccino qui était très bon. Mention spéciale au gâteau à la clémentine!"),
    ("Jull j", "Super miejsce!! Polecam ♥️"),
    ("Joshua Balata", "Very passionate owner, kind, cheerful and full of energy."),
    ("Eloidee Fernando", "Personnel adorable et chaleureuse. Il y a un grand choix de boisson qu'on ne voit pas à Levallois. Le matcha était doux et les patisseries très gourmands. Je recommande fortement pour un moment chill ☺️"),
    ("Michał Lupa", "Best Matcha in Paris.")
]

card_template = """            <div class="review-card">
                <div class="flex items-center gap-1 mb-4 text-secondary-container">
                    ★★★★★
                </div>
                <p class="font-body text-on-surface-variant italic mb-6">"{text}"</p>
                <div class="font-bold text-primary">- {author}</div>
            </div>"""

cards_html = "\n".join([card_template.format(text=text, author=author) for author, text in reviews])

# We need two batches for the marquee effect to loop properly
marquee_content = f"""        <div class="marquee-content">
            <!-- Batch 1 -->
{cards_html}
            
            <!-- Batch 2 (Duplicate for continuous loop) -->
{cards_html}
        </div>"""

files = ['c:/Users/Utilisateur/Documents/Projets/Brume_coffee/index.html', 'c:/Users/Utilisateur/Documents/Projets/Brume_coffee/galerie.html']

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We replace from <div class="marquee-content"> to the closing </div> that matches it.
    # Since regex is greedy, we need to be careful, BUT we can just match up to the FIRST <!-- End Marquee Content --> or similar context
    # Alternatively, just replace everything inside <div class="marquee-wrapper">
    
    new_content = re.sub(
        r'<div class="marquee-content">.*?</div>\s*</div>\s*(?:</section>|<section)',
        marquee_content + '\n    </div>\n',
        content,
        flags=re.DOTALL
    )
    
    # If the regex above fails to match because it relies on </section> which might be placed further down,
    # Let's do a reliable replace:
    new_content = re.sub(
        r'<div class="marquee-content">.*?</div>\s*(?=</div>)',
        marquee_content + '\n',
        content,
        flags=re.DOTALL
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Updated reviews!")
