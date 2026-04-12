produto = {
    "nome":"Cafeteira",
    "preço": 100.00,
    "fornecedores":["Fornecedor Supimpa", "Fornecedor Maneiro", "Fornecedor Legal"]
}

#Utilize o '.items()' para buscar todos os itens do dicionário
print(produto.items())

for chave, valor in produto.items():
    print(f"O personagen {chave} é um {valor}")