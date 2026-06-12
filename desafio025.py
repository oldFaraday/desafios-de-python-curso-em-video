nome = str(input('Digite um nome:\n'))
silva = nome.find('Silva')
primeiroNome = nome[:nome.find(' ')]

if silva < 0:
    print('{} não tem Silva no nome.'.format(primeiroNome))
else:
    print('{} tem Silva no nome.'.format(primeiroNome))