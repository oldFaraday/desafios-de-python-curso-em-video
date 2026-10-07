valor = float(input('Digite o valor: '))

while valor < 0:
    valor = float(input('VALOR INVÁLIDO!\nDigite o valor: '))

pagto = str(input('Qual será a forma de pagamento?\n[DINHEIRO]\n[CHEQUE]\n[CARTAO]\n').upper().strip())
fPagto = ['DINHEIRO', 'CHEQUE', 'CARTAO']
cartao = '#ERRO'
fCartao = ['DEBITO', 'CREDITO', 'CREDITO 2X', 'CREDITO 3X']

while pagto not in fPagto:
    print('FORMA DE PAGAMENTO INVÁLIDA!')
    pagto = str(input('Qual será a forma de pagamento?\n[DINHEIRO]\n[CHEQUE]\n[CARTAO]\n').upper().strip())

if pagto == 'CARTAO':
    while cartao not in fCartao:
        cartao = str(input('Qual a opção do cartão?\n[DEBITO]\n[CREDITO]\n[CREDITO 2X]\n[CREDITO 3X]\n').upper().strip())

    if cartao == 'DEBITO' or cartao == 'CREDITO':
        print('O valor cobrado será de R${:.2f}'.format(valor-(valor/100*5)))
    elif cartao == 'CREDITO 2X':
        print('O valor cobrado será de R${:.2f}'.format(valor))
    else:
        print('O valor cobrado será de R${:.2f}'.format(valor+(valor/100*20)))
else:
    print('O valor cobrado será de R${:.2f}'.format(valor-(valor/100*10)))
