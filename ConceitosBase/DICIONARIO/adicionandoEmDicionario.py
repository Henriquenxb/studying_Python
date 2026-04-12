dicionario = {
    "Henrique Nogueira":"Aluno",
    "Isabela Nogueira":"Aluno"
}

#adicionando chave e valor dentro de um dicionário

#Primeira maneira:
dicionario["Rosangela Nogueira"] = "Professor"

#Segunda maneira- usando função '.update()':
dicionario.update({"Fábio Luiz":"Técnico"})





#Diferentes formas de exibição e retorno
print(dicionario) #retorna o dicionário
print(dicionario.items()) #retorna o dicionário agrupando as respectivas chaves com seus valores dentro de tuplas "()"
print(dicionario.values())#retorna uma lista com os <valores>
print(dicionario.keys())#retorna uma lista com as <chaves>
print(dicionario.get("Henrique"))#none
print(dicionario.get("Isabela Nogueira"))#Aluno

dicionario.clear()#limpa o dicionário
print(dicionario)
