# Descubra se um número é ímpar ou par.

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 1:
    print("O número {} é ímpar.".format(numero))
else:
    print("O número {} é par.".format(numero))