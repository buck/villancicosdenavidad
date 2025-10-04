#!/usr/bin/env python3
import re
import os

# Song data from the index page
songs = [
    ("Campana Sobre Campana", "CampanaSobreCampana", "Campana_Sobre_Campana.mp3"),
    ("Vamos Pastorcitos", "VamosPastorcitos", "Vamos_Pastorcitos.mp3"),
    ("Fum, Fum, Fum", "FumFumFum", "Fum_Fum_Fum.mp3"),
    ("Campanas Navideñas", "CampanasNavidenas", "Campanas_Navidenas.mp3"),
    ("Los Peces en El Rio", "LosPecesenElRio", "Los_Peces_en_El_Rio.mp3"),
    ("La Virgen Va Caminando", "LaVirgenVaCaminando", "La_Virgen_Va_Caminando.mp3"),
    ("Tutaina", "Tutaina", "Tutaina.mp3"),
    ("Rodolfo El Reno", "RodolfoElReno", "Rodolfo_El_Reno.mp3"),
    ("La Burriquita", "LaBurriquita", "La_Burriquita.mp3"),
    ("Ay del Chiquirritín", "AydelChiquirritin", "Ay_del_Chiquirritin.mp3"),
    ("Rin Rin", "RinRin", "Rin_Rin.mp3"),
    ("Blanca Navidad", "BlancaNavidad", "Blanca_Navidad.mp3"),
    ("El Niño del Tambor", "ElNinodelTambor", "El_Nino_del_Tambor.mp3"),
    ("A Medianoche Se Oyó", "AMedianocheSeOyo", "A_Medianoche_Se_Oyo.mp3"),
    ("Adeste Fideles", "AdesteFideles", "Adeste_Fideles.mp3"),
    ("Noche de Paz", "NochedePaz", "Noche_de_Paz.mp3"),
]

# Categories
categories = [
    ("Warmup: fun and easy", 0, 7),
    ("Christmas Pop Rock", 7, 8),
    ("Faster with tongue twisters (<em>trabalenguas</em>)", 8, 11),
    ("Old favorites shared across cultures", 11, 16),
]

def extract_lyrics(html_file):
    """Extract lyrics from HTML file"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.search(r'<div class="container">(.*?)</div>\s*<script', content, re.DOTALL)
    if not match:
        return ""

    container = match.group(1)
    paragraphs = re.findall(r'<p>(.*?)</p>', container, re.DOTALL)

    lyrics_html = []
    for p in paragraphs:
        p = p.strip().replace('﻿', '')
        if p:
            # Keep the <br/> tags as they are for line breaks within stanzas
            lyrics_html.append(f'<p>{p}</p>')

    return '\n'.join(lyrics_html)

# HTML template
html_template = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Villancicos de Navidad - Música y Letras</title>
    <style>
        body {{
            font-family: Georgia, serif;
            max-width: 1000px;
            margin: 0 auto;
            padding: 20px;
            background-color: white;
            color: #000;
            font-size: 20px;
        }}
        h1 {{
            color: #c41e3a;
            text-align: center;
            font-size: 2em;
            margin-bottom: 10px;
        }}
        h3 {{
            text-align: center;
            color: #165b33;
            font-weight: normal;
            font-size: 1.2em;
            margin-top: 5px;
        }}
        .intro {{
            padding: 20px 0;
            margin: 20px 0;
            font-size: 1.1em;
            line-height: 1.6;
        }}
        .category {{
            margin-top: 40px;
        }}
        .category h2 {{
            background: #165b33;
            color: white;
            padding: 12px;
            margin: 30px 0 15px 0;
            font-size: 1.8em;
        }}
        .song {{
            margin: 30px 0;
            padding: 15px 0;
        }}
        .song h3 {{
            color: #c41e3a;
            margin-top: 0;
            text-align: left;
            cursor: pointer;
            font-size: 2em;
            font-weight: bold;
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 10px 0;
        }}
        .song h3:hover {{
            color: #32CD32;
        }}
        .song h3:hover .lyrics-toggle {{
            color: #32CD32;
        }}
        .lyrics-toggle {{
            font-size: 0.6em;
            color: #666;
            font-weight: normal;
            display: flex;
            align-items: center;
            gap: 5px;
        }}
        .lyrics {{
            margin-top: 20px;
            font-size: 1.4em;
            line-height: 1.4;
        }}
        .lyrics p {{
            margin: 0 0 1.5em 0;
        }}
        audio {{
            width: 100%;
            margin: 15px 0;
        }}
        .hidden {{
            display: none;
        }}
        footer {{
            margin-top: 60px;
            padding-top: 20px;
            border-top: 2px solid #999;
            text-align: center;
            color: #666;
            font-size: 1em;
        }}
    </style>
</head>
<body>
    <h1>Villancicos de Navidad - Música y Letras</h1>
    <h3>Spanish Christmas Carols</h3>

    <div class="intro">
        <p>
            For several years, <strong>La Mesa Española</strong>, a social group for practicing Spanish in Houston,
            Texas, collected to sing Spanish Christmas carols, known as <em>villancicos de navidad</em>.
            This collection includes matched pairs of music and lyrics for traditional Spanish Christmas songs.
        </p>
        <p>
            Click on any song title to show or hide the lyrics. Use the audio player to listen to each song.
        </p>
    </div>

{songs_html}

    <footer>
        <p>Original site created by Lester Buck for La Mesa Española, Houston, Texas</p>
        <p>Restored {year}</p>
    </footer>

    <script>
        function toggleLyrics(id) {{
            const lyrics = document.getElementById('lyrics-' + id);
            const toggle = document.getElementById('toggle-' + id);

            if (lyrics.classList.contains('hidden')) {{
                lyrics.classList.remove('hidden');
                toggle.innerHTML = '▼ Hide lyrics';
            }} else {{
                lyrics.classList.add('hidden');
                toggle.innerHTML = '▶ Show lyrics';
            }}
        }}

        // Pause all other audio players when one starts playing
        document.addEventListener('DOMContentLoaded', function() {{
            const audioElements = document.querySelectorAll('audio');

            audioElements.forEach(function(audio) {{
                audio.addEventListener('play', function() {{
                    // Pause all other audio elements
                    audioElements.forEach(function(otherAudio) {{
                        if (otherAudio !== audio) {{
                            otherAudio.pause();
                        }}
                    }});
                }});
            }});
        }});
    </script>
</body>
</html>'''

# Build songs HTML
songs_html = ""
for cat_name, start_idx, end_idx in categories:
    songs_html += f'    <div class="category">\n'
    songs_html += f'        <h2>{cat_name}</h2>\n'

    for i in range(start_idx, end_idx):
        title, filename, mp3 = songs[i]

        # Extract lyrics
        html_path = f"lyrics_pages/{filename}.html"
        lyrics = ""
        if os.path.exists(html_path):
            lyrics = extract_lyrics(html_path)

        mp3_url = f"mp3/{mp3}"

        # Add note for instrumental
        note = ""
        if "A Medianoche" in title:
            note = " <em>(instrumental)</em>"

        songs_html += f'''        <div class="song">
            <h3 onclick="toggleLyrics({i})">
                <span>{title}{note}</span>
                <span class="lyrics-toggle" id="toggle-{i}">▶ Show lyrics</span>
            </h3>
            <audio controls preload="none">
                <source src="{mp3_url}" type="audio/mpeg">
                Your browser does not support the audio element.
            </audio>
            <div id="lyrics-{i}" class="lyrics hidden">{lyrics}</div>
        </div>
'''

    songs_html += '    </div>\n\n'

# Generate final HTML
from datetime import datetime
year = datetime.now().year

final_html = html_template.format(songs_html=songs_html, year=year)

# Write index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("✓ index.html created successfully!")
print(f"✓ {len(songs)} songs with lyrics")
print("\nYou can now open index.html in your browser to test it.")
