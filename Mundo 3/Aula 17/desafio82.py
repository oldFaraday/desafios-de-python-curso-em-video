#82: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

loops_cont = 0
nums = []
nums1 = []
nums2 = []

while True:
    loops_cont += 1
    num = int(input(f"Digite seu {loops_cont}º número: "))

    nums.append(num)
    if num % 2 == 0:
        nums1.append(num)
    else:
        nums2.append(num)

    continua = ""
    while continua != "S" and continua != "N":
        continua = input("Desja continuar?\n[S/N] ").upper().strip()
    if continua == "N":
        break

print("="*70)
print(f"Lista completa: {nums}")
print(f"Números pares: {nums1}")
print(f"Números impares: {nums2}")
print("="*70)