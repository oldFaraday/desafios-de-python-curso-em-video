#73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.

brasileirao = ("Flamengo", "Palmeiras", "Athletico Paranaence", "Fluminense", "Bahia", "Cruzeiro", "Atlético Mineiro", "Santos", "Bragantino", "São Paulo", "Coritiba", "Vitória", "Botafogo", "Vasco", "Mirassol", "Corinthians", "Internacional", "Grêmio", "Remo", "Chapecoense")
brasileirao_ordenado = sorted(brasileirao)

print(f"Os primeiros 5 colocados são: {brasileirao[0]}, {brasileirao[1]}, {brasileirao[2]}, {brasileirao[3]} e {brasileirao[4]}.")

print(f"Os 4 últimos colocados são: {brasileirao[-4]}, {brasileirao[-3]}, {brasileirao[-2]} e por último o {brasileirao[-1]}.")

print(f"[DEBUG: len(brasileirao_ordenado) == {len(brasileirao_ordenado)}]")

print("Os times em Ordem alfabética são: ",end="")
for c, brasileirao_ordenado in enumerate(brasileirao_ordenado):
    print(brasileirao_ordenado, end="")
    if c == len(brasileirao_ordenado):
        print(".")
    else:
        print(", ",end="")