#79: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

nums = []

cont = 0
while True:
    cont += 1
    temp_num = int(input(f"Digite o {cont}º número: "))

    if temp_num not in nums:
        nums.append(temp_num)

    continua = ""
    while continua != "S" and continua != "N":
        continua = input("Deseja continuar?\n[S/N] ").upper().strip()

    if continua == "N":
        break

print(sorted(nums))