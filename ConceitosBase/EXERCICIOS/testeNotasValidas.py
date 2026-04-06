# Inserir notas válidas de 0 a 10.

nota = int(input('Insira uma nota de 0 a 10: '))

if nota >= 0 and nota <=10:
    print("nota válida")
else:
    print("nota inválida")