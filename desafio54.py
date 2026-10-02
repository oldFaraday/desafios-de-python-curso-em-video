#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

qtd = 0
ano_atual = date.today().year

for c in range (7):
    ano = int(input("Digite seu ano de nascimento: "))
    idade = ano_atual - ano
    if idade < 18:
        qtd += 1

print("Das 7 pessoas {} ainda são menores de idade e {} já podem beber.".format(qtd, 7-qtd))

