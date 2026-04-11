#Diferentemente das listas, as tuplas são invocadas usando "()"
#As tuplas não podem ser alteradas enquanto o sistema é executado
categorias = ("Youngling", "Padawan", "Jedi", "Mestre")

print(categorias[-1])#Mestre
print(categorias.count("Jedi"))#1

for categoria in categorias:
    print(categoria)

#////////////////////////////////////////
print("\nNOVO EXEMPLO\n")
#////////////////////////////////////////


categoriasCNH = ("A", "B", "C", "D", "E")

categoria = input("Insira a categoria da sua CNH: ")

if categoria in categoriasCNH:
    print("Categoria existente!")
else:
    print("Categoria inexistente!")