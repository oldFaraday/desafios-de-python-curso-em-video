#COLETA 2 NÚMEROS
x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))

# MAIOR / MENOR / IGUAL
if x > y:
    print('O maior número é: {}.'.format(x))
elif y > x:
    print('O maior número é: {}.'.format(y))
else:
    print('O número {} e {} são iguais.'.format(x,y))