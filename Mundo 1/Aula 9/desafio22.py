nome = str(input('Digite seu nome completo:\n'))
stripedName = nome.strip()

# NOME TODO EM MAIÚSCULO
print('\nNome todo em maiúsculo:')
print(nome.upper(), '\n')

# NOME TODO EM MINÚSCULO
print('Nome todo em minúsculo:')
print(nome.lower(), '\n')

# QUANTAS LETRAS SEM ESPAÇOS
print('O nome tem {} letras.\n'.format(len(stripedName) - stripedName.count(' ')))

# QUANTAS LETRAS TEM NO PRIMEIRO NOME
print('Seu primeiro nome é {}.'.format(nome[:nome.find(' ')]))
