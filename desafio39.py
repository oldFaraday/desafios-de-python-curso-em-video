from datetime import datetime

nascimento = int(input('Digite o ano que nasceu: '))
ano = datetime.now().year
idade = ano - nascimento


if idade > 18:
    print('A época de se alistar já passou.\nVocê está atrasado {} anos.'.format(idade-18))
elif idade < 18:
    print('Sei que está animado para se alistar, mas você está {} anos adiantado.'.format(18-idade))
else:
    print('Olha! Parece que você está no periodo de alistamento. Meus pesames...')