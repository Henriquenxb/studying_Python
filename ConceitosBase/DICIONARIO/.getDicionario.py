produto = {
    "nome":"Cafeteira",
    "preço": 100.00,
    "fornecedores":["Fornecedor Supimpa", "Fornecedor Maneiro", "Fornecedor Legal"]
}


#Ao realizarmos a consulta de valores através das chaves
#é importante nos previnirmos de erros durante a execução
#para isso usamos o método '.get()'

print(produto.get("preço")) # 100.00
print(produto.get("Evandro")) # 'none' - não há essa chave no dicionário


#Caso você procure por algum <valor> ou alguma chave inexistente, o terminal não apontará erro, será retornado "none"
#O get serve apenas para encontrar puxar um valor. Você PRECISA conhecer a chave para dar certo

resultado = float(produto.get("preço"))

if resultado == 100.00:
    print("Ao usar o '.get(______)' você obteve a resposta {}".format(resultado))
else:
    print("Ao usar o '.get(______)' você obteve a resposta {}".format(resultado))