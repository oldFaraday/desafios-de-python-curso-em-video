#83: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = input("Digite a expressão: ")

pilha = []
for caractere in expressao:
    if caractere == "(":
        pilha.append("(")
    elif caractere == ")":
        if pilha:
            pilha.pop()
        else:
            pilha.append(")")
            break

if not pilha:
    print("Quantidade de parênteses: OK")
else:
    print("Ops! Parece que tem algo errado.")
