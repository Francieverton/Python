produtos = ['tv', 'celular', 'geladeira', 'forno', 'computador']
vendas = [1000, 1500, 2000, 3000, 5000]

mais_vendido = vendas.index(max(vendas))
menos_vendido = vendas.index(min(vendas))

mais_vendido = produtos[mais_vendido]
menos_vendido = produtos[menos_vendido]

print('O produto mais vendido é {}, e o menos vendido é {}'.format(mais_vendido, menos_vendido))