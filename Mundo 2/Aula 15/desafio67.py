#67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    termo = int(input("Qual o termo que deseja ver a tabuada? "))
    if termo < 0:
        break

    for operador in range(11):
        print(f"{termo} X {operador} = {termo*operador}")

print("[PROGRAMA ENCERRADO]")