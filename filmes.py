filmes = [
    {
        "titulo": "Inception",
        "diretor": "Christopher Nolan",
        "bilheteria": 830,
        "avaliacoes": [9, 10, 8, 9, 10],
    },
    {
        "titulo": "Avengers: Endgame",
        "diretor": "Anthony Russo",
        "bilheteria": 2797,
        "avaliacoes": [9, 9, 10, 10, 9],
    },
    {
        "titulo": "The Dark Knight",
        "diretor": "Christopher Nolan",
        "bilheteria": 1005,
        "avaliacoes": [10, 10, 9, 10, 10],
    },
    {
        "titulo": "Jurassic Park",
        "diretor": "Steven Spielberg",
        "bilheteria": 1029,
        "avaliacoes": [8, 9, 9, 8, 9],
    },
]

def media_avaliacoes(filme):
    return sum(filme["avaliacoes"]) / len(filme["avaliacoes"])

def top_bilheteria(filmes):
    return sorted(filmes, key=lambda f: f["bilheteria"], reverse=True)[:3]

def top_avaliacao(filmes):
    return sorted(filmes, key=lambda f: media_avaliacoes(f), reverse=True)[:3]

def bilheteria_por_diretor(filmes):
    resultado = {}
    for f in filmes:
        diretor = f["diretor"]
        resultado[diretor] = resultado.get(diretor, 0) + f["bilheteria"]
    return resultado

def campeao(filmes):
    return max(filmes, key=lambda f: (f["bilheteria"] * media_avaliacoes(f)))

print("Top 3 Bilheteiras:")
for f in top_bilheteria(filmes):
    print(f["titulo"], "-", f["bilheteria"], "milhões")

print("\nTop 3 Melhor Avaliados:")
for f in top_avaliacao(filmes):
    print(f["titulo"], "-", round(media_avaliacoes(f), 2))

print("\nBilheteria por Diretor:")
print(bilheteria_por_diretor(filmes))

print("\nCampeão Absoluto:")
vencedor = campeao(filmes)
print(vencedor["titulo"], "- Bilheteria:", vencedor["bilheteria"], "- Média:", round(media_avaliacoes(vencedor), 2))
