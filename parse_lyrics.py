#!/usr/bin/env python3
import re
import os
from pathlib import Path

# Song data from the index page
songs = [
    ("Campana Sobre Campana", "CampanaSobreCampana", "Campana%20Sobre%20Campana.mp3"),
    ("Vamos Pastorcitos", "VamosPastorcitos", "Vamos%20Pastorcitos.mp3"),
    ("Fum, Fum, Fum", "FumFumFum", "Fum%20Fum%20Fum.mp3"),
    ("Campanas Navideñas", "CampanasNavidenas", "Campanas%20Navidenas.mp3"),
    ("Los Peces en El Rio", "LosPecesenElRio", "Los%20Peces%20en%20El%20Rio.mp3"),
    ("La Virgen Va Caminando", "LaVirgenVaCaminando", "La%20Virgen%20Va%20Caminando.mp3"),
    ("Tutaina", "Tutaina", "Tutaina.mp3"),
    ("Rodolfo El Reno", "RodolfoElReno", "Rodolfo%20El%20Reno.mp3"),
    ("La Burriquita", "LaBurriquita", "La%20Burriquita.mp3"),
    ("Ay del Chiquirritín", "AydelChiquirritin", "Ay%20del%20Chiquirritin.mp3"),
    ("Rin Rin", "RinRin", "Rin%20Rin.mp3"),
    ("Blanca Navidad", "BlancaNavidad", "Blanca%20Navidad.mp3"),
    ("El Niño del Tambor", "ElNinodelTambor", "El%20Nino%20del%20Tambor.mp3"),
    ("A Medianoche Se Oyó", "AMedianocheSeOyo", "A%20Medianoche%20Se%20Oyo.mp3"),
    ("Adeste Fideles", "AdesteFideles", "Adeste%20Fideles.mp3"),
    ("Noche de Paz", "NochedePaz", "Noche%20de%20Paz.mp3"),
]

# Categories
categories = [
    ("Warmup: fun and easy", 0, 7),
    ("Christmas Pop Rock", 7, 8),
    ("Faster with tongue twisters (trabalenguas)", 8, 11),
    ("Old favorites shared across cultures", 11, 16),
]

def extract_lyrics(html_file):
    """Extract lyrics from HTML file"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the container div content
    match = re.search(r'<div class="container">(.*?)</div>\s*<script', content, re.DOTALL)
    if not match:
        return None

    container = match.group(1)

    # Extract all paragraphs
    paragraphs = re.findall(r'<p>(.*?)</p>', container, re.DOTALL)

    # Clean up the paragraphs
    lyrics = []
    for p in paragraphs:
        # Remove HTML entities and clean up
        p = p.strip()
        p = p.replace('﻿', '')
        if p:
            lyrics.append(p)

    return '\n\n'.join(lyrics)

# Extract lyrics for all songs
lyrics_data = {}
for title, filename, mp3 in songs:
    html_path = f"lyrics_pages/{filename}.html"
    if os.path.exists(html_path):
        lyrics = extract_lyrics(html_path)
        if lyrics:
            lyrics_data[filename] = lyrics
            print(f"Extracted: {title}")
        else:
            print(f"FAILED: {title}")
    else:
        print(f"MISSING: {html_path}")

print(f"\nTotal extracted: {len(lyrics_data)}/{len(songs)}")
