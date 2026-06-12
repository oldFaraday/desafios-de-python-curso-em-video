frase = str(input('Digite uma frase:\n'))
fraseLower = frase.lower()
contA = fraseLower.count('a')
findLA = fraseLower.find('a') + 1
findRA = fraseLower.rfind('a') + 1

print('Existem {} A na frase.'.format(contA))
print('Ele aparece pela primeira vez na posição {}.'.format(findLA))
print('Ele aparece pela última vez na posição {}.\n'.format(findRA))