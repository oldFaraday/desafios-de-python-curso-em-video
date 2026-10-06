#Desafio 28

from random import randint
num = randint(0, 5)
usr = int(input('Digite um número inteiro de 0 à 5: '))
if num == usr:
    print('Parabéns, você acertou!\n')
else:
    print('Ops, parece que você errou. O número era {}. \n'.format(num))