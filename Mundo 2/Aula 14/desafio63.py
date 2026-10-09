#63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
#Exemplo: 1 – 1 – 2 – 3 – 5 – 8

loops = int(input("Quantos números quer ver? "))
contator = 1
termo1 = 0
termo2 = 1
termo3 = 0

print("1 - ",end="")

while contator < loops:

    termo3 = termo1 + termo2
    print("{} - ".format(termo3), end="")
    termo1 = termo2
    termo2 = termo3

    contator += 1

print("[FIM]")