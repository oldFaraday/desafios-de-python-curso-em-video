from datetime import date
atual = date.today().year
nascimento = int(input('Digite o ano do seu nascimento: '))
idade = atual - nascimento

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