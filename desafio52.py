#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input("Digite um número: "))
verificador = True

if num <= 1:
    verificador = False
elif num != 2:
    if num % 2 == 0 and num > 2:
        verificador = False
    else:
        raiz = int(num ** 0.5)

        for c in range(3, raiz + 1, 2):
            if num % c == 0:
                verificador = False

if verificador == True:
    print("Sim, o número {} é primo.".format(num))
else:
    print("O número {} não é primo.".format(num))