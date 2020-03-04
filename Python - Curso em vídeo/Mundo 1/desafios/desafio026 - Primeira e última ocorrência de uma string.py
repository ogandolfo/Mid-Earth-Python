# Faça um programa que leia uma frase e mostre
# 1 - Quantas vezes aparece a letra A
# 2 - Em que posição ela aparece a primeira vez
# 3 - Em que posição ela aparece a última vez
# Espaços estão sendo contados

frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {} '.format(frase.find('A')+1))  # procura somando uma posição
print('A última letra A apareceu na posição {} '.format(frase.rfind('A')+1))  # procura de trás pra frente
