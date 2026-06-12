dias = int(input('Quantos dias você ficou com o carro? '))
kms = float(input('Quantos Kms você rodou com o carro? '))
resultado = dias*60+kms*0.15
print('O valor a pagar é de R${:.2f}'.format(resultado))