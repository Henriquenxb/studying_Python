#Desempacotar
#No Phyton,as tuplas podem ser desempacotadas
#desde que as do lado esquerdo do sinal de igual ('=')
#tenhamos a mesma quantidade de variáveis que tivermos na tupla



tupla = (1,2,3)
a, b, c = tupla

print(a,b,c)


chamada = ("Ana", "Bianca", "Carla", "Daniel")


aluno1, aluno2, aluno3, aluno4 = chamada 
print(aluno1, aluno2, aluno3, aluno4)



produto = {
    "nome":"Cafeteira",
    "preço": 100.00,
    "fornecedores":["Fornecedor Supimpa", "Fornecedor Maneiro", "Fornecedor Legal"]
}
for item in produto.items():
    valorX,valorY = item
    print(f"Ao desempacotar, esse é o valor X: {valorX}; e esse é o valor de Y: {valorY} ")