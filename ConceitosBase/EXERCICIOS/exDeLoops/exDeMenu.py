
opcao = int(0)

while opcao != 4:
    print("\n\n1 - Rodar funcionalidade 1")
    print("2 - Rodar funcionalidade 2")
    print("3 - Rodar funcionalidade 3")
    print("4 - Sair do sistema\n")
    opcao = int(input("Informe a opção desejada:"))

    if opcao == 1:
        print("Rodando funcionalidade 1")
    elif opcao == 2:
        print("Rodando funcionalidade 2")
    elif opcao == 3:
        print("Rodando funcionalidade 3")
    elif opcao == 4:
        print("Saindo do sistema...")
    else:
        print("Opção inválida!")