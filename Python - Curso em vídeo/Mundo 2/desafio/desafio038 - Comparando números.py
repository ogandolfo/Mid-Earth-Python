# Escreva um programa que leia DOIS NÚMEROS inteiros e compare-os, mostrando na tela uma mensagem:
# o PRIMEIRO VALOR é MAIOR; o SEGUNDO VALOR é MAIOR; NÃO EXISTE valor maior, os dois são IGUAIS

n1 = int(input('Digite um número INTEIRO: '))
n2 = int(input('Digite outro número INTEIRO: '))

if n1 > n2:
    print('O primeiro valor é maior')
elif n2 > n1:
    print('O segundo valor é maior')
else:
    print(f'Obviamente são iguais')
