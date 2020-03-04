# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o prçeo da passagem, cobrando R$0,50
# por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

d = float(input('Insira a distância do trajeto: '))

if d <= 200:
    p = 0.5 * d
    print(f'\nSeu trajeto possui {d} quilômetros, portanto o valor da sua passagem será de R${p:.2f}.')
else:
    p = 0.45 * d
    print(f'\nSeu trajeto possui {d} quilômetros, portanto o valor da sua passagem será de R${p:.2f}')
print('\n-----Obrigado por usar nossos serviços. Boa viagem!-----')
