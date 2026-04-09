#o 'RETURN' é utilizado quando a função precisa entregar um valor/resultado para algo. Como um prestação de contas. 
#Uma função, não necessariamente, precisa ter um print, você pode utilizar o 'return' para guardar o resultado da função dentro de uma outra variável ou mesmo fazer o print diretamente


# #Função que calcula a velocidade média
# def calcularVelocidadeMedia(distancia, tempo):
#     #calcular a velocidade média
#     velocidade_media = distancia/tempo
#     #exibir o resultado
#     return velocidade_media 

# #aqui começa o programa principal
# dist = float(input("Informe a distância"))
# temp = float(input("Informe o tempo"))
# #chamando a função com valores definidos pelo usuário
# print("A velocidade média é {}".format(calcularVelocidadeMedia(dist, temp)))


def velocidade_media(distancia, tempo):
    vm = distancia / tempo
    return vm 

    #nessa etapa, a função está 'exportando' um resultado de seu trabalho. Nesse exemplo, ela está entregando um resultado, uma variável que recebeu o valor de uma conta feita dentro da função que utilizou os argumentos informados ao chamar a função.

velocidades_medias = []
dias_semana = ["segunda", "terça", "quarta", "quinta", "sexta"]
for dia in dias_semana:
    distancia = float(input(f"Insira a distânca percorrida na {dia} em Km: "))
    tempo = float(input(f"Insira a duranção da viagem da {dia} em horas: "))
    velocidades_medias.append(velocidade_media(distancia, tempo))

print(f"As velocidades médias da semana foram {velocidades_medias}")