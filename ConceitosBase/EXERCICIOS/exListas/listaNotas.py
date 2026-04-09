#Crie um programa onde o professor digite notas de uma quantidade indeterminada ao terminar, exibir a média aritmética.

notas = []

while input("Deseja inserir uma nota? S - Sim, N - Não\nDigite a resposta: ").upper() != "N":
    notas.append(float(input("Por favor, insira a nota: ")))


media_aritmetica = sum(notas)/len(notas)
print(f"Para as notas digitadas, a média foi de: {media_aritmetica}")