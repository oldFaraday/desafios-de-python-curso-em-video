#65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

quantidade = 0
soma = 0
maior = 0
menor = 0
continua = True

while continua == True:
    valor = int(input("Digite um número: "))
    quantidade += 1
    soma += valor

    if quantidade == 1:
        maior = valor
        menor = valor
    else:
        if valor > maior:
            maior = valor

        if valor < menor:
            menor = valor

    flag = input("Deseja continuar? [S/N]\n").upper().strip()
    while flag != "S" and flag != "N":
        flag = input("Deseja continuar? [S/N]\n").upper().strip()
    if flag == "N":
        continua = False

media = soma / quantidade
print("A média dos valores digitados é {:.2f}.".format(media))
print("O maior valor foi {} e o menor valor foi {}.".format(maior, menor))