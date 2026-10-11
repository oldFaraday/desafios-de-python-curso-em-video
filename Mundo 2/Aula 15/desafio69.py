#69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

adulto = 0
homens = 0
mulheres = 0
total = 0

while True:
    idade = int(input("Qual a idade? "))

    sexo = ""
    while sexo != "M" and sexo != "F":
        sexo = input("Qual o sexo? [M/F] ").upper().strip()

    if idade > 18:
        adulto += 1

    if sexo == "M":
        homens += 1

    if sexo == "F" and idade < 20:
        mulheres += 1

    total += 1

    continua = ""
    while continua != "S" and continua != "N":
        continua = input("Deseja continuar? [S/N] ").upper().strip()
    if continua == "N":
        print("=-"*35)
        break
    print("=-"*35)

print(f"Entre as {total} pessoas cadastradas:\n{adulto} são adultos.\n{homens} são homens.\n{mulheres} são mulheres com menos de 20 anos.")
print("=-"*35)