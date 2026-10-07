num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro núumero: '))

if num1 > num2:
    if num1 > num3:
        print('O número {} é o maior.'.format(num1))
    else:
        print('O número {} é o maior.'.format(num3))
else:
    if num2 > num3:
        print('O número {} é o maior.'.format(num2))
    else:
        print('O número {} é o maior.'.format(num3))

if num1 < num2:
    if num1 < num3:
        print('O número {} é o menor.'.format(num1))
    else:
        print('O número {} é o menor.'.format(num3))
else:
    if num2 < num3:
        print('O número {} é o menor.'.format(num2))
    else:
        print('O número {} é o menor.'.format(num3))