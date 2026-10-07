from random import choice
aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))

sequencia = [aluno1, aluno2, aluno3, aluno4]
escolha = choice(sequencia)

print('Quem vai limpar o quadro hoje vai ser o(a) {}\n'.format(escolha))
