#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
#APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

#COLHE A FRASE
frase = input("Digite uma frase: ").strip().lower()
while frase == "":
    frase = input("Sem caracteres não há frase. Digite uma frase: ").strip().lower()

#NORMALIZA A STRING
frase = frase.split()
frase = ''.join(frase)

#INICIALIZA AS VARIÁVEIS
tamanho = len(frase)
loop = len(frase)//2
flag = True

#VERIFICA SE É UM PALINDROMO
for c in range(loop):
    if frase[c] != frase[tamanho - 1 - c]:
        flag = False

#MOSTRA O RESULTADO
if not flag:
    print("A frase não é um palindromo.")
else:
    print("Sim, essa frase é um palindromo.")