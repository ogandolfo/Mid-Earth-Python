# Crie um programa que leia um número REAL qualquer pelo teclado e mostre na tela a sua porção inteira
from math import floor
n = float(input(' Digite um número: '))

print(f' O número {n} tem a parte inteira igual a {floor(n)}.')
