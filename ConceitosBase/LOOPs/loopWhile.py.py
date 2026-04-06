# O loop WHILE é usado quando não temos ideia do número de vezes necessárias para a finalização do laço de repetição.

#criação da variável com um valor inicial
i = 0
#enquanto a variável contadora não chegar ao limite
while (i<10):
    #para cada uma das repetições uma mensagem é exibida
    print("Mais uma mensagem, com i valendo: {}".format(i))
    i = i + 1


print("A variável contadora (i) finalmente chegou ao limite do laço de repetição ({}).".format(i))