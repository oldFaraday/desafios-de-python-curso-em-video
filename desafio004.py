#CAPTURAR INPUT
varInt = int(input('Digite um número Inteiro: '))
varFloat = float(input('Digite um número Real: '))
varBool = bool(input('Digite um valor Booleano: '))
varStr = str(input('Digite uma cadeia de caracteres: '))

print(' ') #---ESPAÇO---

#MOSTRAR O TIPO
print('ESSES SÃO OS TIPOS DOS VALORES QUE DIGITOU:')
print('O tipo do valor {} é "{}".'.format(varInt, type(varInt)))
print('O tipo do valor {} é "{}".'.format(varFloat, type(varFloat)))
print('O tipo do valor {} é "{}".'.format(varBool, type(varBool)))
print('O tipo do valor {} é "{}".'.format(varStr, type(varStr)))

print(' ') #---ESPAÇO---

#MOSTRAS AS INFORMAÇÕES DO INPUT --- USAR ".IS__________"

print('INFORMAÇÕES VARIAVEL INTEIRA')
print(varInt.is_integer())

print(' ') #---ESPAÇO---

print('INFORMAÇÕES VARIAVEL REAL')
print(varFloat.is_integer())

print(' ') #---ESPAÇO---

print('INFORMAÇÕES VARIAVEL BOLEANA')
print(varBool.is_integer())

print(' ') #---ESPAÇO---

print('INFORMAÇÕES VARIAVEL STRING')
print(varStr.isalnum())
print(varStr.isalpha())
print(varStr.isidentifier())
print(varStr.isascii())
print(varStr.isdecimal())
print(varStr.isdigit())
print(varStr.islower())
print(varStr.isnumeric())
print(varStr.isprintable())
print(varStr.isspace())
print(varStr.istitle())
print(varStr.isupper())
