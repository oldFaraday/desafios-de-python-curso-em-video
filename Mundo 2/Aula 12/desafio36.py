val = float(input('Digite o valor da casa: R$'))
sal = float(input('Digite o valor do seu salário: R$'))
ano = int(input('Digite em quantos anos você quer quitar sua casa: '))

if val/(ano*12) < sal/100*30:
    print('FINANCIAMENTO APROVADO!\nO valor da parcela é de R${:.2f}'.format(val/(ano*12)))
else:
    print('Infelizmente não podemos aprovar o seu financiamento.')
