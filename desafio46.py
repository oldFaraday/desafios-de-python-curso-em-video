#IMPORTAÇÃO
from time import sleep

#INICIAR SISTEMA
start = str(input('Digite "INICIAR" para começar: ')).upper().strip()
while start != 'INICIAR':
    start = str(input('Digite "INICIAR" para começar: ')).upper().strip()

#MENSAGEM INICIAL
print('=-'*20)
print('Vamos começar a contagem de ANO NOVO!')
print('=-'*20,'\n')

#CONTAGEM REGRESSIVA
for c in range(10, -1, -1):
    print(c,'...')
    sleep(1)

#MENSAGEM FINAL
print('=-'*20)
print('FELIZ ANO NOVO!')
print('=-'*20)