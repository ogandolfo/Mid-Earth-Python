# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
# atingiram a maioridade (21 anos) e quantas já são maiores.

from datetime import date
atual = date.today().year
tmr = 0
tmn = 0
for p in range(1, 8):
    nasc = int(input(f'Em que ano a {p}º pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        tmr += 1
    else:
        tmn += 1
print(f'No total, são {tmr} pessoas maiores e {tmn} pessoas menores.')
