# O loop FOR é um loop baseado em um 'intervalo'
# É um loop onde a vairável assume valores que existem no intervalo definido
# enquanto a função range é capaz de nos gerar esse ValueError



# A função range pode ser utilizada de 3 maneiras:

# 1ª  Passar o valor final
# ex: range(1000)
# - nesse range o loop é feito até que a variável assuma o valor de 999
# - isso acontece pq a função range é excludente.
# - assume-se que o valor inicial sempre será '0' e o incremento será de 1 em 1. 


# 2ª  Passar o valor inicial e o final
# ex: range(1,1001)
# - nesse range o loop é feito até que a variável assuma o valor de 1000
# - o loop inicia a partir do número '1' pq o valor inicial é '1' e o incremento será de 1 em 1. 


# 3ª  Passar o valor inicial, final e o incremento
# ex: range(1,1001,2)
# - nesse range o loop é feito até que a variável assuma o valor de 999
# - o loop inicia a partir do número '1' pq o valor inicial é '1' e o incremento será de 1 em 1. 

for variavel in range(1,1001,2):
    print(variavel)