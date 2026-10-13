#71: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

saque = int(input("Digite o valor a ser sacado: R$"))
print("=-"*35)
notas50 = notas20 = notas10 = notas1 = 0
if saque >= 50:
    notas50 = saque // 50
    saque = saque % 50
if saque >= 20:
    notas20 = saque // 20
    saque = saque % 20
if saque >= 10:
    notas10 = saque // 10
    saque = saque % 10
if saque >= 1:
    notas1 = saque // 1
    saque = saque % 1
if notas50 != 0:
    print(f"Notas de R$50,00: {notas50}")
if notas20 != 0:
    print(f"Notas de R$20,00: {notas20}")
if notas10 != 0:
    print(f"Notas de R$10,00: {notas10}")
if notas1 != 0:
    print(f"Notas de R$1,00: {notas1}")
print("=-"*35)