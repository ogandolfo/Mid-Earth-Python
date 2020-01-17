# condições (if/else)

tempo = int(input('Quantos anos tem seu carro?'))
if tempo <=3:
    print('Carro novo')
else:
    print('Carro Velho')
print('--FIM--')
print('Carro novo' if tempo <=3 else 'Carro Velho')
