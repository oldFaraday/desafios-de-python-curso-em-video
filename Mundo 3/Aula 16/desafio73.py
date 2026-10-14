#73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.

brasileirao = ("Flamengo", "Palmeiras", "Athletico Paranaence", "Fluminense", "Bahia", "Cruzeiro", "Atlético Mineiro", "Santos", "Bragantino", "São Paulo", "Coritiba", "Vitória", "Botafogo", "Vasco", "Mirassol", "Corinthians", "Internacional", "Grêmio", "Remo", "Chapecoense")
brasileirao_alfabetico = sorted(brasileirao)

print("=-"*95)
print(f"Os primeiros 5 colocados são: {brasileirao[0]}, {brasileirao[1]}, {brasileirao[2]}, {brasileirao[3]} e {brasileirao[4]}.")
print("=-"*95)
print(f"Os 4 últimos colocados são: {brasileirao[-4]}, {brasileirao[-3]}, {brasileirao[-2]} e por último o {brasileirao[-1]}.")
print("=-"*95)
print("Os 20 primeiros colocados do brasileirão em ordem alfabética são: ",end="")
for cont in range(0, len(brasileirao_alfabetico)):
    print(f"{brasileirao_alfabetico[cont]}",end="")
    if cont == len(brasileirao_alfabetico)-1:
        print(".")
    elif cont == len(brasileirao_alfabetico)-2:
        print(" e ",end="")
    else:
        print(", ",end="")
print("=-"*95)
print(f"A Chapecoense está na {brasileirao.index("Chapecoense")+1}ª posição.")
print("=-"*95)