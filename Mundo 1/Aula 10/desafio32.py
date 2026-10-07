ano = int(input('Digite um ano qualquer: '))
u = ano // 1 % 10
d = ano // 10 % 10
c = ano // 100 % 10
m = ano // 1000 % 10

if d == 0 and u == 0:
    if ano % 400 == 0:
        print('É um ano bisexto!')
    else:
        print('Não é um ano bisexto.')
else:
    if ano % 4 == 0:
        print('É um ano bisexto!')
    else:
        print('Não é um ano bisexto.')