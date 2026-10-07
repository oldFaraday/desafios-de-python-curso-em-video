#62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiro = int(input("Digite o primeiro número da PA: "))
razao = int(input("Digite a razão da PA: "))

termo = primeiro
contador = 1
total = 0
continuar = 10

while continuar != 0:
    total += continuar

    while contador <= total:
        print("{} -> ".format(termo), end="")
        termo += razao
        contador += 1

    print("[PAUSA]")

    continuar = int(input("\nDeseja imprimir mais quantos resultadas? "))

print("\nProgressão finalizada com {} termos mostrados no total.".format(total))