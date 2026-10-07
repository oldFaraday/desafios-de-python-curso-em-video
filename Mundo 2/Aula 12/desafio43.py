print('VAMOS CALCULAR SEU IMC?')
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
IMC = peso/(altura*altura)

print('Seu IMC é de {:.2f}.'.format(IMC))
if IMC < 19:
    print('Você está ABAIXO DO PESO.')
elif IMC < 25:
    print('Seu peso está NORMAL.')
elif IMC < 30:
    print('Parece que você está com SOBREPESO.')
elif IMC < 35:
    print('CUIDADO! Você tem OBESIDADE I.')
elif IMC < 41:
    print('CUIDADO! Você tem OBESIDADE II.')
else:
    print('CUIDADO! Você tem OBESIDADE MORBIDA.')