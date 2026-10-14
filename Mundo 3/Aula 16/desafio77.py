#77: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

vogais = ("a", "e", "i", "o", "u")
palavras = ("coelho", "notebook", "lapis", "raposa", "mulher", "rato", "gaiola", "doce", "banana")

for palavra in (palavras):
    print(palavra.capitalize(),end=": ")
    
    vogais_palavra = [letra for letra in palavra if letra in vogais]
    for cont in range(0, len(vogais_palavra)):
        print(f"{vogais_palavra[cont]}",end="")
        if cont == len(vogais_palavra)-1:
            print(".")
        else:
            print(", ",end="")