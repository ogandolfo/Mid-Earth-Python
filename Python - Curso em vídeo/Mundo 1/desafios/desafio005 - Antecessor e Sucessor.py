# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e o seu antecessor
n = int(input('Digite um valor:'))
a = n-1
s = n+1
print(' O antecessor de {} é: {}'.format(n, a))
print(' O sucessor de {} é: {}'.format(n, s))

print(f'\nAnalisando o valor {n}, seu antecessor é {n-1} e seu sucessor é {n+1}.')