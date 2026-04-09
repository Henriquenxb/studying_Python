jedi = ['Yoda', 'Luke', 'Obi-Wan', 'Anakin']
print(f"Essa é a lista origial:\n{jedi}\n")


# Remoção do último valor
jedi.pop()
print(f"Essa é a lista após a remoção do último valor:\n{jedi}\n")


# Remoção de um valor em posição específica 
jedi.pop(1) #remove o elemento que está na posição especificada
print(f"Essa é a lista após a remoção do valor que estava na posição indicada pelo parâmetro fornecido:\n{jedi}\n")


# Remoção de um item específico
jedi.remove("Yoda")
print(f"Essa é a lista após a remoção de um valor específico, ao utilizar o '.remove('<valor que será removido>')'\n{jedi}\n")


# Apagar a lista toda
jedi.clear()
print(f"Essa é a lista após usar o '.clear()'\n{jedi}\n")