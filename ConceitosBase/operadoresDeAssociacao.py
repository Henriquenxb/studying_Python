# "s" in resposta
# usar operador 'in'


# "s" not in resposta
# usar operador 'not in'



resposta = "sim"
texto = "Brasil"
print("s" in resposta) #true - tem 's' na palavra 'sim'
print("n" not in resposta) #true - pq 'not in' aponta que o 'n' não está na palavra 'sim', e realmente não está
print("b" in texto) #false - A letra B na palavra 'Brasil' é maiúscula e não minúscula 
print("B" in texto) #true - exite o 'B' (maiúsculo) na str(Brasil)