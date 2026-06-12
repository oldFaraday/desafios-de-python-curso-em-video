h = float(input('Qual a altura da parede? '))
b = float(input('Qual a base da parede? '))
area = h * b
print('Essa parede tem uma área de {}m² e para pinta-la vamos precisar de {}L de tinta.'.format(area, area / 2))