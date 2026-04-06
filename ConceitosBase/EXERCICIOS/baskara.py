a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))

delta = b**2 - 4*a*c
xPositivo = (-b + delta**0.5) / (2*a)
xNegativo = (-b - delta**0.5) / (2*a)

if delta == 0:
    print("O X não é um valor real.")
else:
    print("O X pode ser {} ou {}.".format(xPositivo, xNegativo))