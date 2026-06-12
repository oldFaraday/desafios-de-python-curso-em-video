reta1 = float(input('Digite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digite o comprimento da terceira reta: '))

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('Podemos fazer um triangulo com essas retas!')
    if reta1 == reta2 and reta2 == reta3:
        print('Esse triangulo será EQUILÁTERO.')
    elif reta1 == reta2 or reta2 == reta3:
        print('Esse triângulo será ISÓCELES.')
    else:
        print('Esse triângulo será ESCALENO.')
else:
    print('Não podemos criar um triangulo assim, sinto muito.')