#76: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ("Mouse", 49.00, "Monitor", 499.90, "Mesa", 1045.30, "Caneta", 3.00)

print("="*40)
print(f"{'LISTAGEM DE PREÇOS':^38}")
print("="*40)
for count in range(0, len(produtos), 2):
    print(f"{produtos[count]:.<30}R${produtos[count+1]:.2f}")
print("="*40)