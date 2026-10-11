#68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
vitorias = 0

while True:
    num = randint(0, 10)

    teste = ""
    while teste != "P" and teste != "I":
        teste = input("Você quer par ou impar? [P/I]").upper().strip()

    usr = int(input("Digite um número: "))
    gabarito = (num + usr)%2

    if gabarito == 0:
        gabarito = "P"
    else:
        gabarito = "I"

    if gabarito == teste:
        vitorias += 1
        print("Parabens, você ganhou!")
        print("=-"*35)
    else:
        break

print("Parece que você perdeu!",end=" ")
if vitorias != 0:
    print(f"Parebéns pela(s) {vitorias} vitória(s)!")