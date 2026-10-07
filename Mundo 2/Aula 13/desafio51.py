#51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

termo = int(input("Digite o primeiro número da PA: "))
razao = int(input("Digite a razão da PA: "))
limite = termo + (10 * razao)
s = 0

for c in range(termo, limite, razao):
    s += c
print("A soma dos 10 primeiros números dessa PA é {}".format(s))