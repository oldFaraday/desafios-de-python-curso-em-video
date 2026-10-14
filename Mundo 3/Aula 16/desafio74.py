#74: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
aleatorios = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print("Números gerados: ",end="")
for cont in range(0, len(aleatorios)):
    print(f"{aleatorios[cont]}",end="")
    if cont == len(aleatorios)-1:
        print(".")
    elif cont == len(aleatorios)-2:
        print(" e ",end="")
    else:
        print(", ",end="")
print(f"O maior número gerado foi {max(aleatorios)}.")
print(f"O menor número gerado foi {min(aleatorios)}.")