#58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
num = randint(0, 10)
usr = int(input('Digite um número inteiro de 0 à 10: '))
ttv = 1

while usr != num:
    ttv += 1
    usr = int(input('Ops! Valor errado. Digite outro número inteiro de 0 à 10: '))

print("=-"*35)
print("O número é {}. Você acertou!\nVocê levou {} tentativas pra acertar! Tente fazer melhor.".format(num, ttv))
print("=-"*35)