vel = float(input('Entre com a velocidade do veículo: '))
multa = (vel - 80) * 7
if vel > 80:
    print('Você foi multado!')
    print('O valor da multa é de R${:.2f}.'.format(multa))