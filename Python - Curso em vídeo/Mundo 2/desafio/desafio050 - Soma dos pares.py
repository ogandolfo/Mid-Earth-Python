# Desenvolva um programa que leia seis números inteiro e mostre a soma apenas daqueles que forem pares.

som = 0
count = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0:
        som += num
        count += 1
print(f'\nA soma do(s) {count} número(s) PAR(ES) é igual a: {som}')
