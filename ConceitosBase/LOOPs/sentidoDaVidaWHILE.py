resposta = str("")
tentativas = 0

while resposta != "42":
    resposta = str(input("Qual é a resposta para a vida, o universo e tudo mais?\n"))
    tentativas +=1

print("Parabéns! Você acertou!\nNão esqueça a sua toalha!\n\nVocê precisou de {} tentativas.".format(tentativas))