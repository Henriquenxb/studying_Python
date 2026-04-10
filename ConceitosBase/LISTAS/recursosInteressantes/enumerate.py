filaDoSus = ["José Marcos", "Patrícia Vilela", "Wesley Cobra", "Danilo Emanuel", "Rosana da Silva", "Victor Macedo", "Todoido do Zorra Total"]

senha = [95,96,97,98,99,100,101]



#No Python, o enumerate() transforma sua lista básica em algo assim:
#['José Marcos', 'Patrícia Vilela'] para >>>>> [(0, 'José Marcos'), (1, 'Patrícia Vilela')]

# Na hora de escrever o código, nós "desempacotamos" esses dois valores em duas variáveis diferentes:

#Nesse caso as duas variáveis são "i" e "paciente"


for i, paciente in enumerate(filaDoSus):
    print(f"{paciente} é o paciente número {senha[i]} e chegou na fila {i+1}º lugar.")

# O "i" funciona como uma variável que navega entre os índices, por isso é possível acessar e exibir dados de outras listas utilizando a var "i" como um parâmetro.