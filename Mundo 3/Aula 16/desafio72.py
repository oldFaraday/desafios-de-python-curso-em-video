#72: Crie um programa que tenha uma Tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

contagem = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
alvo = int(input("Digite um número de 0 à 20: "))+1

print (contagem[:alvo])

#Refazer exercício: o print deve mostrar o nome escrito por extenço.