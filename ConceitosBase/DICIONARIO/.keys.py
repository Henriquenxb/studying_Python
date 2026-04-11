produto = {
    "nome":"Cafeteira",
    "preço": 100.00,
    "fornecedores":["Fornecedor Supimpa", "Fornecedor Maneiro", "Fornecedor Legal"]
}

#Use o método '.keys()' para acessar todas as <chaves> de um dicionário
print(produto.keys())
for chave in produto.keys():
    print(chave)

#Use o método '.values()' para acessar todas os <valores> de um dicionário
print(produto.values())
for chave in produto.values():
    print(chave)



