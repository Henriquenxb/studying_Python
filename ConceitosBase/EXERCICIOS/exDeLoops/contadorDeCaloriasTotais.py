totalRefeicoes = int(0)
totalCalorias = int(0)
i = int(0)

while i != 2:
    print("\n\nNúmero de refeições: {}\nNúmero de calorias consumidas: {}\n".format(totalRefeicoes,totalCalorias))
    i = int(input("\nMENU\n1 - Registrar nova refeição \n2 - Finalizar o dia\nDigite: "))

    

    if i == 1:
        totalRefeicoes +=1 
        totalCalorias += int(input("cadastrando nova refeição...\nInforme o número de calorias: "))
        print("\nRefeição cadastrada com sucesso!\n\n")
    elif i == 2:
        print("\nFinalizando o dia...\nNúmero de refeições: {}\nNúmero de calorias consumidas {}\n".format(totalRefeicoes,totalCalorias))
    else:
        print("Opção inválida")