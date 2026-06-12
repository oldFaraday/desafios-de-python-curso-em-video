num = int(input('Digite um número até 9999:\n'))

while num > 9999:
    num = int(input('Valor inválido. Digite um número até 9999:\n'))

strNum = str(num).zfill(4)
resposta = '{} {} {} {}'.format(strNum[0], strNum[1], strNum[2], strNum[3])
print(resposta.strip())
