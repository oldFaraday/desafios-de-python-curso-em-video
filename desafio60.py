#60: Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

num = int(input("Digite um número inteiro não negativo: "))
while num < 0:
    num = int(input("Valor inválido. O número deve inteiro e não negativo: "))
resultado = 1
contador = 1

while contador <= num:
    resultado = resultado * contador
    contador += 1

print("{}! = {}".format(num, resultado))