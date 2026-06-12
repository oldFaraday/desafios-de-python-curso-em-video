idade = int(input('Digite sua idade: '))

while idade < 0:
    idade = int(input('Valor inválido!\nDigite sua idade: '))

print('Categoria: ')
if idade < 10:
    print('Mirim')
elif idade < 15:
    print('Infantil')
elif idade < 20:
    print('Junior')
elif idade < 21:
    print('Sênior')
else:
    print('Master')