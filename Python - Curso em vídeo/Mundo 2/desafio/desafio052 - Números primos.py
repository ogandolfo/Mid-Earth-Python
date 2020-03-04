# faça um programa que leia um numero inteiro e diga se ela é ou não um número primo

num = int(input('Digite um número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print(c, end='\033[m')
print(f'\n\033[0mO número {num} foi divisível {total} vezes.')
if total == 2:
    print('Portanto, ele é primo')
else:
    print('Portanto ele não é primo')
