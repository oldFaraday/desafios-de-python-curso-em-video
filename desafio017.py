from math import pow, sqrt
cat_oposto = float(input('Digite o valor do cateto oposto: '))
cat_adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = sqrt(pow(cat_oposto, 2)+pow(cat_adjacente, 2))
print('A hipotenusa desse triângulo retangulo é {:.2f}'.format(hipotenusa))
