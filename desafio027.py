nomeEntrada = str(input('Digite um nome:\n'))
nome = nomeEntrada.strip()
primeiroNome = nome[:nome.find(' ')].capitalize()
ultimoNome = nome[nome.rfind(' ')+1:].capitalize()

print('Primeiro nome: {}'.format(primeiroNome))
print('Último nome: {}'.format(ultimoNome))