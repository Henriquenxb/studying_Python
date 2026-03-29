# Para fazer contas, vocÊ precisa garantir que as variáveis são de tipo numérico.

idade = int(input('Digite sua idade: '))
anoAtual = int(input('Digite o ano atual: '))

anoDeNascimento = anoAtual - idade
print(f'Você nasceu em {anoDeNascimento}')