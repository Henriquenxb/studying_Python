# Case: Loja de roupa
# Oferecer 10% de desconto no total da compra ao receber o cupom de desconto 'NIVER10'

cupom = str('NIVER10')
porcentagemDescontoComCupom = float(0.9)
valorCompra = float(input('Digite o valor da compra: R$ '))
cupomDigitado = str(input('Agora digite o cupom de desconto: '))


# User função '.upper()' para fazer o cupomDigitado sempre ser lido como maiúsculo.
cupomDigitado = cupomDigitado.upper()

if cupomDigitado == cupom:
    valorCompra *= porcentagemDescontoComCupom
    
else:
    print('Cupom inválido.')

print('O valor total da compra é de R$ {:.2f}'.format(valorCompra))
