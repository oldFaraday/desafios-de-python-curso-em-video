#59: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

op = 0

while op == 0:
    #COLETA OS NÚMEROS INICIAIS
    num1 = float(input("Digite o 1º número: "))
    num2 = float(input("Digite o 2º número: "))

    #MENU
    while op < 1 or op > 5:
        print("O que você quer fazer?\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa\n")
        op = int(input("Digite sua opção: "))

    #OPÇÃO 01
    if op == 1:
        print("{} + {} = {}".format(num1,num2,num1+num2))   

    #OPÇÃO 02
    if op == 2:
        print("{} * {} = {}".format(num1,num2,num1*num2))

    #OPÇÃO 03
    if op == 3:
        if num1 == num2:
            print("Os números {} e {} são iguais.".format(num1,num2))
        elif num1 > num2:
            print("{} é maior que {}.".format(num1,num2))
        else:
            print("{} é maior que {}.".format(num2,num1))

    #OPÇÃO 04
    if op == 4:
        op = 0

    #OPÇÃO 05
    if op == 5:
        exit()