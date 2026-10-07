#61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

termo = int(input("Digite o primeiro número da PA: "))
razao = int(input("Digite a razão da PA: "))
passo = termo
s = 0
c = 1

while c < 11:
    print("{}".format(passo), end='')
    print(" + " if c < 10 else " = ", end='')
    s += passo
    passo += razao
    c += 1

print("{}".format(s))