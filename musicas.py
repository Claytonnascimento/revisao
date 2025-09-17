musicas = [
    {
        "titulo": "Back in Black",
        "artista": "AC/DC",
        "downloads": 6800,
        "avaliacoes": [5, 4, 5, 5, 4, 5],
    },
    {
        "titulo": "Stairway to Heaven",
        "artista": "Led Zeppelin",
        "downloads": 8900,
        "avaliacoes": [5, 5, 4, 5, 5, 5],
    },
    {
        "titulo": "Enter Sandman",
        "artista": "Metallica",
        "downloads": 8100,
        "avaliacoes": [5, 5, 5, 4, 4, 5],
    },
]

def calcular_media(musica):
    return sum(musica["avaliacoes"]) / len(musica["avaliacoes"])

def artista_mais_downloads(musicas):
    downloads_por_artista = {}
    for m in musicas:
        artista = m["artista"]
        downloads_por_artista[artista] = downloads_por_artista.get(artista, 0) + m["downloads"]
    artista_top = max(downloads_por_artista, key=downloads_por_artista.get)
    return artista_top, downloads_por_artista[artista_top]

def ranking_musicas(musicas):
    ranking = sorted(musicas, key=lambda m: calcular_media(m), reverse=True)
    return [(m["titulo"], calcular_media(m)) for m in ranking]

print("Média de cada música:")
for m in musicas:
    print(m["titulo"], "→", round(calcular_media(m), 2))

artista, total = artista_mais_downloads(musicas)
print("\nArtista com mais downloads:", artista, "(", total, ")")

print("\nRanking das músicas mais bem avaliadas:")
for pos, (titulo, media) in enumerate(ranking_musicas(musicas), 1):
    print(f"{pos}º {titulo} - Média {round(media, 2)}")
