# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
# custa R$60 por dia e R$0,15 por km rodado.

d = float(input(' Quantos dias o veículo ficou alugado? '))
k = float(input(' Quantos quilômetros foram percorridos? '))
a = (d*60)+(k*0.15)

print(f'\n O valor a ser pago será de R${a:.2f}.')
