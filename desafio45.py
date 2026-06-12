#PC ESCOLHE A RESPOSTA
from random import randint
pptMaq = randint(0,2)
if pptMaq == 0:
    pptMaq = 'PEDRA'
elif pptMaq == 1:
    pptMaq = 'PAPEL'
else:
    pptMaq = 'TESOURA'

#RESPOSTA DO USUÁRIO
pptUsr = str(input('PEDRA, PAPEL OU TESOURA? ').upper().strip())
respostas = ['PEDRA', 'PAPEL', 'TESOURA']
while pptUsr not in respostas:
    pptUsr = str(input('VALOR INVÁLIDO. PEDRA, PAPEL OU TESOURA? '))

#COMPARAÇÕES E RESPOSTAS
print('=-'*20)
if pptMaq == pptUsr:
    print('\nMáquina: {}\nVocê: {}\nEMPATE...\n'.format(pptMaq,pptUsr))
else:
    if pptMaq == 'PEDRA':
        if pptUsr == 'PAPEL':
            print('\nMáquina: {}\nVocê: {}\nPAPEL embrulha PEDRA, você venceu!\n'.format(pptMaq,pptUsr))
        else: #TESOURA
            print('\nMáquina: {}\nVocê: {}\nPEDRA quebra TESOURA, você perdeu.\n'.format(pptMaq,pptUsr))
    elif pptMaq == 'PAPEL':
        if pptUsr == 'PEDRA':
            print('\nMáquina: {}\nVocê: {}\nPAPEL embrulha PEDRA, você perdeu.\n'.format(pptMaq,pptUsr))
        else: #TESOURA
            print('\nMáquina: {}\nVocê: {}\nTESOURA corta PAPEL, você venceu!\n'.format(pptMaq,pptUsr))
    else: #TESOURA
        if pptUsr == 'PEDRA':
            print('\nMáquina: {}\nVocê: {}\nPEDRA quebra TESOURA, você venceu!\n'.format(pptMaq,pptUsr))
        else: #PAPEL
            print('\nMáquina: {}\nVocê: {}\nTESOURA corta PAPEL, você perdeu.\n'.format(pptMaq,pptUsr))
print('=-'*20)