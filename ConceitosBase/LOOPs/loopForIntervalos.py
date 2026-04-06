# Essa é uma ótima opção para quando conhecemos o intervalo de valores

for dia in ["segunda", "terça", "quarta", "quinta", "sexta"]:

    print("\nHoje é {}".format(dia))

    if dia == "segunda" or dia =="quarta" or dia =="sexta":
        print("É dia de colocar o lixo para o coletor.")