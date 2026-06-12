#ler um número inteiro
#escolher a base de conversão
#--[1] Binário
#--[2] Ocatal
#--[3] Hexadecimal
#Exibir a conversão

#COLETA O CANDIDATO
num = int(input('Digite qualquer número inteiro: '))

#COLETA A BASE
print('[1] Binário\n[2] Octal\n[3] Hexadecimal')
base = int(input('Qual a base para conversão? '))
#--verifica se a base de calculo é valida
while base < 1 or base > 3:
    base = int(input('VALOR INVÁLIDO\n Digite um valor válido: '))

#ESCOLHE QUAL VALOR EXIBIR
if base == 1:
    binario = bin(num)
    print('O valor em binário é {}'.format(binario))
elif base == 2:
    octal = oct(num)
    print('O valor em octal é {}'.format(octal))
else:
    hexadec = hex(num)
    print('O valor em hexadecimal é {}'.format(hexadec))