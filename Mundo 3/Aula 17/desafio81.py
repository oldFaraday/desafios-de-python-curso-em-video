#81: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

loops_cont = 0
nums = []

while True:
    loops_cont += 1
    nums.append(int(input(f"Digite seu {loops_cont}º número: ")))

    continua = ""
    while continua != "S" and continua != "N":
        continua = input("Desja continuar?\n[S/N] ").upper().strip()
    if continua == "N":
        break

print("="*70)
print(f"Foram digitados {len(nums)} número(s).")
print(f"Valores em ordem decrescente: {sorted(nums, reverse=True)}")
if 5 in nums:
    print("O número 5 foi digitado.")
else:
    print("O número 5 NÃO foi digitado.")