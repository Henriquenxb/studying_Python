#Ordenando valor fora de ordem:

valores = [1,7,7,19,3,2,11,15,6,1,5,3.5]
print(f'A lista atual é: {valores}\n')

valores.sort()
print(f"Essa é a lista após aplicar o '.sort()':\n{valores}")

valores.sort(reverse=True)
print(f"Essa é a lista após aplicar o '.sort(reverse=True)':\n{valores}")