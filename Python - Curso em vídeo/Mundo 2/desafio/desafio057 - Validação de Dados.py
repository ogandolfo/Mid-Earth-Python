# Faça um programa que leia o SEXO de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a
# digitação novamente até ter um valor correto.

"""sexo = 'M' or 'F'"""

nome = str(input('Qual seu nome? '))
sexo = str(input('Com qual sexo você se identifica? [M/F] ')).strip().upper()[0]  # retira os espaços, torna maiusculo e aplica fatiamente, pegando somente primeiro caracter
while sexo not in 'MF':
    sexo = str(input('Informação Inválida. Com qual sexo você se identifica? [M/F] ')).strip().upper()[0]
"""    if sexo != 'M' or sexo != 'F':
        print('Por favor, insira um valor correto.')
    else:
        print('Informação registrada.')"""
print(f'Seu nome é {nome}. Você se identifica com o sexo {sexo}.')
