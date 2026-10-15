#78: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

#VARIÁVEIS
nums = []
nums.append(int(input("Digite o 1º número: ")))
nums.append(int(input("Digite o 2º número: ")))
nums.append(int(input("Digite o 3º número: ")))
nums.append(int(input("Digite o 4º número: ")))
nums.append(int(input("Digite o 5º número: ")))
max_positions = []
min_positions = []

#PREENCHE AS LISTAS DE MENOR E MAIOR VALOR
for num in range(len(nums)):
    if max(nums) == nums[num]:
        max_positions.append(num)

for num in range(len(nums)):
    if min(nums) == nums[num]:
        min_positions.append(num)

#IMPRIME O RESULTADO
print("="*70)

print(f"O maior valor digitado foi o {max(nums)}, ",end="")
if len(max_positions) > 1:
    print("nas posições ", end="")
    for c in range(len(max_positions)):
        if len(max_positions) == c + 1:
            print(" e ",end="")
        elif c == 0:
            print("",end="")
        else:
            print(", ",end="")
        print(max_positions[c],end="")
else:
    print(f"na posição {max_positions[0]}",end="")
print(".")

print(f"O menor valor digitado foi o {min(nums)}, ",end="")
if len(min_positions) > 1:
    print("nas posições ", end="")
    for c in range(len(min_positions)):
        if len(min_positions) == c + 1:
            print(" e ",end="")
        elif c == 0:
            print("",end="")
        else:
            print(", ",end="")
        print(min_positions[c],end="")
else:
    print(f"na posição {min_positions[0]}",end="")
print(".")

print("="*70)