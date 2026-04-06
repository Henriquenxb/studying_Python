totalCompras = int(0)
valorTotal = int(0)
i = int(0)

while i != 2:
    print("\n\nNúmero de transações: {}\nValor total gasto: {}\n".format(totalCompras,valorTotal))
    i = int(input("\nMENU\n1 - Registrar nova transação \n2 - Finalizar o dia\nDigite: "))

    

    if i == 1:
        totalCompras +=1 
        valorTotal += float(input("cadastrando nova transação...\nInforme o valor gasto: R$ "))
        print("\Trasnação cadastrada com sucesso!\n\n")
    elif i == 2:
        media = float(valorTotal/totalCompras)
        print("\nFinalizando o dia...\nNúmero de transações: {}\nTotal gasto no dia: {}\nGasto médio por transação: R$ {}\n".format(totalCompras, valorTotal, media))
    else:
        print("Opção inválida")