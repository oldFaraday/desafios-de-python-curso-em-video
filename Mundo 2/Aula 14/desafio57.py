#57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

gen = input("Qual seu gênero?\n[M] Masculino\n[F] Feminino\n").upper().strip()

while gen != "M" and gen != "F":
    print("=-"*35)
    gen = input("Genero inválido. Qual seu gênero?\n[M] Masculino\n[F] Feminino\n").upper().strip()

if gen == "M":
    print("Seu gênero é [MASCULINO]")
else:
    print("Seu gênero é [FEMININO]")