# Faça um programa que leia o comprimento do CATETO OPOSTO e do CATETO ADJACENTE
# de um TRIÂNGULO RETÂNGULO, calcule e mostre a comprimento da hipotenusa
from math import hypot
cto = float(input(' Digite o comprimento do CATETO OPOSTO: '))
cta = float(input(' Digite o comprimento do CATETO ADJACENTE: '))

print(f'O valor da hipotenusa será: {hypot(cto, cta):.2f}')
