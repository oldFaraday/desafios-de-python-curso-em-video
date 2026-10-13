#70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

soma = 0
caros = 0
baratoNome = ""
baratoPreco = 0

while True:
    nome = input("Digite o nome do produto: ").strip()
    preco = float(input(f"Digite o preço do produto: "))

    soma += preco

    if preco > 1000:
        caros += 1

    if baratoNome == "":
        baratoNome = nome
        baratoPreco = preco
    elif baratoPreco > preco:
        baratoNome = nome
        baratoPreco = preco

    continua = ""
    while continua != "S" and continua != "N":
        continua = input("Deseja adicionar outro produto?\n[S/N]: ").upper().strip()

    print("=-"*35)

    if continua == "N":
        break

print(f"Total de R${soma:.2f};\n{caros} produtos acima de R$1.000;\n[{baratoNome}] foi o produto mais barato.")