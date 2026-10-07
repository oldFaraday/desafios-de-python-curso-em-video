nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2

if media > 7:
    print('Parabens, você foi aprovado.')
elif media < 5:
    print('Ops, parece que você reprovou.')
else:
    print('Você está de recuperação. Esforce-se que ainda dá tempo.')