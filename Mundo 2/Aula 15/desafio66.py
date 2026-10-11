#66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

soma = 0
quantidade = 0

while True:
    num = int(input("Digite um número inteiro (999 para o programa): "))
    if num == 999:
        break
    soma += num
    quantidade += 1

print(f"A soma dos {quantidade} números é {soma}.")