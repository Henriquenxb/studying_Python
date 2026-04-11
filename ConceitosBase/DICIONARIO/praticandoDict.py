
#Um dicionário(dict) é uma estrutura formada por "<Chave> : <Valor>", ou seja, ela associa um valor a outro

#Para chamar um dicionário usamos "{}"
dicionarioCDZ = {
    "Seiya":"Cavaleiro de Pégaso",
    "Shiryu":"Cavaleiro de Dragão",
    "Hyoga":"Cavaleiro de Cisne",
    "Shun":"Cavaleiro de Andrômeda",
    "Ikki":"Cavaleiro de Fênix"
}

print(type(dicionarioCDZ))
print(dicionarioCDZ)


produto = {
    "nome":"Cafeteira",
    "preço": 100.00,
    "fornecedores":["Fornecedor Supimpa", "Fornecedor Maneiro", "Fornecedor Legal"]
}


#Para acessarmos um <valor>, é necessário fazermos a consulta se utilizando da <chave>
print(produto["fornecedores"][0:2])
print(produto["preço"])
print(produto)

