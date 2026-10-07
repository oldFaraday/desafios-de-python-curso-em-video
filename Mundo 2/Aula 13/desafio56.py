#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

homem = ""
homem_idade = 0
media_idade = 0
mulher = 0

qtd = int(input("Quantas pessoas quer tratar? "))
while qtd <= 0:
    print("=-"*35,"\nValor inválido.")
    qtd = int(input("Quantas pessoas quer tratar? "))

for c in range(1,qtd+1):
    nome_temp  = input("Digite o {}º nome: ".format(c))
    idade_temp = int(input("Agora digite a idade de {}: ".format(nome_temp)))
    genero_temp = input("Qual o gênero de {}?\n[M] Masculino\n[F] Feminino\nDigite sua resposta: ".format(nome_temp)).upper().strip()
    while genero_temp != "M" and genero_temp != "F":
        genero_temp = input("Genero inválido. Qual o gênero de {}?\n[M] Masculino\n[F] Feminino\nDigite sua resposta: ".format(nome_temp)).upper().strip()

    media_idade += idade_temp

    if genero_temp == "M":
        if homem == "":
            homem = nome_temp
            homem_idade = idade_temp
        elif homem_idade < idade_temp:
            homem = nome_temp
            homem_idade = idade_temp

    if genero_temp == "F" and idade_temp < 20:
        mulher += 1
        
print("=-"*35,"\n")
media_idade = media_idade / qtd
print("A média das idades é {}.".format(media_idade))
print("=-"*35,"\n")
if homem == "":
    print("Não há homens entre as pessoas")
else:
    print("O homem mais velho é o {}.".format(homem))
print("=-"*35,"\n")
print("Entre as {} pessoas {} são mulheres com menos de 20 anos.".format(qtd, mulher))
print("=-"*35,"\n")