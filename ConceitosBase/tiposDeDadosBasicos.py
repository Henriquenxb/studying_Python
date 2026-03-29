# int
# Números inteiros
# ex: 1, 2, 100


# float
# Números reais (ponto flutuante)
# ex: 1.5, 2.07, 50.29


# complex
# Números complexos
# ex: 4j, 5+2j, 15j


# bool
# Valores lógicos
# ex: True, False, 1, 0


# string (str)
# Textos
# ex:"Texto", "a", "10"



# Conversão de tipos de dados em Python

valor1 = input("Por favor, digite o primeiro valor: ")
valor2 = input("Por favor, digite o segundo valor: ")
soma = float(valor1) + float(valor2)
print("A soma entre os valores é {}".format(soma))



# Calculadora totalmente implementada em Python
valor1 = input("Por favor, digite o primeiro valor: ")
valor2 = input("Por favor, digite o segundo valor: ")

soma = float(valor1) + float(valor2)
print("A soma entre os valores é {}".format(soma))

subtracao = float(valor1) - float(valor2)
print("A subtração entre os valores é {}".format(subtracao))

divisao = float(valor1) / float(valor2)
print("A divisão entre os valores é {}".format(divisao))

multiplicacao = float(valor1) * float(valor2)
print("A multiplicação entre os valores é {}".format(multiplicacao))