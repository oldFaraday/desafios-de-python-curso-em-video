#72: Crie um programa que tenha uma Tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

contagem = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte", )
alvo = int(input("Digite um número de 0 à 20: "))
while alvo < 0 or alvo > 20:
    alvo = int(input("Número Inválido. Digite um número de 0 à 20: "))

print (contagem[alvo])