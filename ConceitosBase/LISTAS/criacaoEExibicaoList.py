#Criação de uma lista vazia
jedi = []
print(type(jedi))

#Criação de uma lista com os Jedi Yoda, Luke, Obi-Wan, Anakin
jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]


#Exibição de uma lista completa
print(jedi) #['Yoda', 'Luke', 'Obi-Wan', 'Anakin']


#Exibição de uma posição espedífica na lista
print(jedi[1]) #exibe: Luke


#Exibição dos últimos elementos
print(jedi[-1]) #exibe: Anakin
#obs: do primeiro ao último índice a lista começa do índice 0 à n
# do último para o primeiro, utilizamos -1 à -n

#Exibição de um intervalo de elementos
print(jedi[1:3])# exibe: ['Luke', 'Obi-Wan']
#obs: o segundo índice informado, é excludente por isso o nome "Anakin" não foi exibido

#Exibição de cada item da lista
for nome in jedi:
    print(nome) 
#Yoda
#Luke
#Obi-Wan
#Anakin