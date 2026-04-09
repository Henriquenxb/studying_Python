#Função que calcula a velocidade média
def calcularVelocidadeMedia(distancia, tempo): #note que foram passadas 'uma prévia de variáveis', campo onde especificamos os valores/parâmteros que serão utilizados na função


    #calcular a velocidade média
    velocidade_media = distancia/tempo #nesta etapa, fazemos a chamada daqueles valores inseridos como parâmetros


    #exibir o resultado
    print("A velocidade média é {} km/h".format(velocidade_media))



#aqui começa o programa principal
distancia = float(input("Informe a distância"))
tempo = float(input("Informe o tempo"))


#chamando a função com valores definidos pelo usuário
calcularVelocidadeMedia(distancia, tempo)

#chamando a função com valores definidos pelo programador
calcularVelocidadeMedia(15,2)