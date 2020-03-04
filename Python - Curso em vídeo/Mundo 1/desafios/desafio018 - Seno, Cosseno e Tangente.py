# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

from math import sin, cos, tan, radians

ag = float(input("Digite um valor de ângulo: "))

sn = (sin(radians(ag)))
print(f'O valor do SENO de {ag} é: {sn:.2f}')
csn = (cos(radians(ag)))
print(f'O valor do COSSENO de {ag} é: {csn:.2f}')
tgt = (tan(radians(ag)))
print(f'O valor da TANGENTE de {ag} é: {tgt:.2f}')
