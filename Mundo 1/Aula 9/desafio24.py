cidade = input('Nome da cidade:\n')
espaco = cidade.find(' ')

if espaco < 0:
    if(cidade == 'Santo'):
        print('O nome da cidade começa com Santo')
    else:
        print('O nome da cidade não começa com Santo')
else:
    if cidade[:espaco] == 'Santo':
        print('O nome da cidade começa com Santo')
    else:
        print('O nome da cidade não começa com Santo')