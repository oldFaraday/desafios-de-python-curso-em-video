#75: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

num1 = int(input("Digite o 1º valor: "))
num2 = int(input("Digite o 2º valor: "))
num3 = int(input("Digite o 3º valor: "))
num4 = int(input("Digite o 4º valor: "))
nums = (num1, num2, num3, num4)

print(f"O número 9 apareceu {nums.count(9)} vez(es).")

if 3 in nums:
    print(f"O número 3 apareceu pela primeira vêz na posição {nums.index(3)}.")
else:
    print("O número 3 não foi digitado.")

print("Os números pares são: ",end="")
for count in range(len(nums)):
    if nums[count] % 2 == 0:
        print(nums[count],end=" ")