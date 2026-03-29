# Operadores de identidade

# Quando precisamos comparar se dois objetos utilizam a mesma posição de memória no Python, usamos os operadores de identidade: is e not is. O operador de identidade é diferente do operador relacional de igualdade ==, pois o operador de identidade analisa o endereço e o de igualdade analisa o valor.



# O método id() retorna o endereço de memória de um objeto, podemos utilizá-lo em conjunto com o comando print para exibir este endereço em tela.


cidade_p1 = "São Paulo"
cidade_p2 = "São Paulo"
cidade_p3 = "Rio de Janeiro"
print(id(cidade_p1))
print(id(cidade_p2))
print(id(cidade_p3))
print(cidade_p1 is cidade_p2) #True - pq os IDs são iguais
print(cidade_p1 is not cidade_p3) #True - pq os IDs são diferentes
print(cidade_p1 is cidade_p3) #False - pq os IDs não são iguais