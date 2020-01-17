# Crie um programa que leia um número e mostre na tela se ele é par ou ímpar

n = float(input('Digite um número e descubra se ele é par ou impar: '))

if float(n) % 2 == 0:  # se o número é divisível por 2, o resto é zero, sendo assim, é par
    print(f'Você digitou {n}, que é um número par')
else:
    print(f'Você digitou {n}, que é um número ímpar')
