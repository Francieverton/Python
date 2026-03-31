meta = 0.05
taxa = 0
rendeu = 0.30

if rendeu > 0.20:
    taxa = 0.04
    print('Taxa de {}, pq o valor que rendeu é maior que 20%.'.format(taxa))

elif rendeu > meta:
    taxa = 0.02
    print('Taxa de apenas {}.'.format(taxa))

else:
    print('sem taxa')
