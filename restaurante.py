pedidos = [
    {
        "cliente": "Ana",
        "items": [
            {"prato": "Lasanha", "preco": 30},
            {"prato": "Suco de Laranja", "preco": 8}
        ]
    },
    {
        "cliente": "Bruno",
        "items": [
            {"prato": "Pizza", "preco": 40},
            {"prato": "Refrigerante", "preco": 6},
            {"prato": "Sobremesa", "preco": 12}
        ]
    },
    {
        "cliente": "Carla",
        "items": [
            {"prato": "Pizza", "preco": 40},
            {"prato": "Suco de Laranja", "preco": 8}
        ]
    }
]

def total_gasto(cliente_nome):
    for pedido in pedidos:
        if pedido["cliente"] == cliente_nome:
            return sum(item["preco"] for item in pedido["items"])
    return 0  

from collections import Counter

def prato_mais_vendido():
    todos_pratos = []
    for pedido in pedidos:
        for item in pedido["items"]:
            todos_pratos.append(item["prato"])
    mais_comum = Counter(todos_pratos).most_common(1)[0]
    return mais_comum[0]  

def ranking_clientes():
    gastos = []
    for pedido in pedidos:
        total = sum(item["preco"] for item in pedido["items"])
        gastos.append((pedido["cliente"], total))
    ranking = sorted(gastos, key=lambda x: x[1], reverse=True)[:3]
    return ranking

print("Total gasto por Ana:", total_gasto("Ana"))
print("Prato mais vendido:", prato_mais_vendido())
print("Ranking dos clientes:", ranking_clientes())
