#80: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

nums = []

for c in range(1,6):
    num = int(input(f"Digite o {c}º número: "))

    if len(nums) == 0 or num > nums[len(nums)-1]:
       nums.append(num) 
    else:
        posicao = 0
        while posicao < len(nums):
            if num <= nums[p]:
                nums.insert(posicao, num)
                break
            posicao += 1
    print(nums)