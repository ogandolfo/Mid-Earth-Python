# Faça um programa que leia um ano qualquer e mostre se ele é bissexto

from datetime import date
ano = int(input('Qual ano deseja analisar? Digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year  # analisa o ano atual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:  # multiplo de 4, exceto multiplos de 100 não multiplos de 400
    print(f'{ano} é ano bissexto.')
else:
    print(f'{ano} não é ano bissexto')
