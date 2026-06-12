preco = float(input('Digite o preço do produto: R$ '))
desconto = preco * 0.05
preco_final = preco - desconto

print('O preço do produto com 5% de desconto é: R$ {}'.format(preco_final))