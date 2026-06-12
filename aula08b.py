from math import sqrt, pow
num = float(input('Digite um número: '))
raiz = sqrt(num)
potencia = pow(num, 2)
print('A raiz de {} é {:.2f} e {} ao quadado é {:.2f}'.format(num, raiz, num, potencia))
