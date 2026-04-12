dicionarioCDZ = {
    "Seiya":"Cavaleiro de Pégaso",
    "Shiryu":"Cavaleiro de Dragão",
    "Hyoga":"Cavaleiro de Cisne",
    "Shun":"Cavaleiro de Andrômeda",
    "Ikki":"Cavaleiro de Fênix"
}

print(dicionarioCDZ)

#REMOVENDO chave e valor

#Forma 1 - .pop(<chave>)
#OBS: diferente do '.pop()'que usamos nas listas para apagar o último elemento, NO DICIONÁRIO ISSO NÃO FUNCIONA. Precisa informar a chave a ser apagada
dicionarioCDZ.pop("Ikki")# apagou "'Ikki': 'Cavaleiro de Fênix'"


#Forma 2 - .popitem()
#OBS: esse sim é o semelhante ao '.pop()' das listas, mas para dicionários, usamos '.popitem()'
dicionarioCDZ.popitem()#Elimina a última chave e valor do dicionário
print(dicionarioCDZ)


#Forma 3 - .clear() - apaga tudo, igual nas listas
dicionarioCDZ.clear()


