"""
A List Comprehension é, em essência, uma "fábrica de listas" em uma única linha. Ela é a maneira "Pythônica" de criar novas listas a partir de outras sequências (como listas, strings ou dicionários) sem precisar escrever várias linhas de código com for e append.

Para aprender de verdade, vamos comparar a forma "antiga" com a forma "List Comprehension".
"""
#------------------------------------------------------------------------------------------
"""
O Cenário: Filtrando uma lista de preços

Imagine que você tem uma lista de preços de produtos e quer criar uma nova lista apenas com os produtos que custam mais de 50 reais, mas aplicando um desconto de 10% neles.

1. Do jeito tradicional (Usando for)
"""

precos = [20, 100, 45, 80, 30]
promocao = []

for preco in precos:
    if preco > 50:
        promocao.append(preco*0.9)

print(promocao) #Resultado: [90.0, 72.0]

"""
2. Com List Comprehension
"""

precos = [20, 100, 45, 80, 30]
#     [ O QUE EU QUERO | DE ONDE VEM | CONDIÇÃO ]
promocao = [preco * 0.9 for preco in precos if preco > 50]
print(promocao)

#------------------------------------------------------------------------------------------

nomes = ["Alice","Bob","Caio"]
nomes_gritando = [nome.upper() for nome in nomes]
# Resultado: ['ALICE', 'BOB', 'CAIO']

# nomes_gritando = []
# for nome in nomes:
#     nomes_gritando.append(nome.upper())

print(nomes_gritando)