#84: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

pessoa = []
pessoas = []

while True:
    pessoa.append(input("Digite o nome: "))
    pessoa.append(float(input("Digite o peso: ")))
    pessoas.append(pessoa[:])
    pessoa.clear()

    continua = ""
    while continua != "S" and continua != "N":
        continua = input("Deseja continuar?\n[S/N] ").upper().strip()
    if continua == "N":
        break

print(f"Foram cadastradas: {len(pessoas)} pessoas.")

pesadas = sorted(pessoas, key=lambda x: x[1], reverse=True)
print("As pessoas mais pesadas são: ",end="")
for c in pesadas:
    print(c[0],end=" ")
print("")


leves = sorted(pessoas, key=lambda x: x[1])
print("As pessoas mais leves são: ",end="")
for c in leves:
    print(c[0],end=" ")
print("")

####### PRECISA DE AJUSTES #######