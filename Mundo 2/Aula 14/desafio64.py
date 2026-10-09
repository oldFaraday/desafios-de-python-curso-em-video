#64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

valor = int(input("Digite um número: "))
quantidade = 0
soma = 0

while valor != 999:
    quantidade += 1
    soma += valor
    valor = int(input("Digite um número: "))

print("A soma dos {} valores digitados é de {}".format(quantidade, soma))