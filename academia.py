atletas = [
    {
        "nome": "Lucas",
        "idade": 20,
        "modalidades": ["Natação", "Corrida"],
        "treinos": {"Natação": 12, "Corrida": 8}
    },
    {
        "nome": "Mariana",
        "idade": 25,
        "modalidades": ["Musculação", "Yoga", "Pilates"],
        "treinos": {"Musculação": 15, "Yoga": 10, "Pilates": 5}
    },
    {
        "nome": "João",
        "idade": 22,
        "modalidades": ["Corrida", "Ciclismo"],
        "treinos": {"Corrida": 20, "Ciclismo": 18}
    }
]

def media_idade(atletas, esporte):
    idades = [a["idade"] for a in atletas if esporte in a["modalidades"]]
    if len(idades) == 0:
        return 0
    return sum(idades) / len(idades)

def esporte_mais_treinado(atleta):
    return max(atleta["treinos"], key=atleta["treinos"].get)

def atletas_multiesporte(atletas):
    return [a["nome"] for a in atletas if len(a["modalidades"]) > 2]

print("Média de idade (Corrida):", media_idade(atletas, "Corrida"))  
print("Média de idade (Ciclismo):", media_idade(atletas, "Ciclismo"))  
print("Esporte mais treinado (lucas):", esporte_mais_treinado(atletas[0]))  
print("Esporte mais treinado (Mariana):", esporte_mais_treinado(atletas[1]))  
print("Atletas com mais de 2 modalidades:", atletas_multiesporte(atletas))  
