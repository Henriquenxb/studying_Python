funcionarios = {}

while input("Quer inserir um funcionário?\n'S' - Sim\n'N'- Não\nDigite...").upper() !="N":
    nome = input("Informe o nome do funcionário: ")
    funcao = input("Informe a função do funcionário: ")
    funcionarios.update({nome:funcao})
    #funcionarios[nome]=funcao

print(funcionarios)