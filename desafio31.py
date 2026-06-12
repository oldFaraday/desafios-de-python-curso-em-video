dist = float(input('Digite a distancia da viagem em Km: '))
if dist < 200:
    print('O valor da passagem é de R${:.2f}'.format(dist*0.5))
else:
    print('O valor da passagem é de R${:.2f}'.format(dist*0.45))