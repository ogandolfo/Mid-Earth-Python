# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a BASE DE CONVERSÃO:
# 1 para BINÁRIO, 2 para OCTAL e 3 para HEXADECIMAL.

num = int(input('Digite um número inteiro: '))

print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))

if opção == 1:
    print(f'{num} convertido para BINÁRIO é {bin(num)[2:]}')

elif opção == 2:
    print(f'{num} convertido para OCTAL é {oct(num)[2:]}')

elif opção == 3:
    print(f'{num} convertido para HEXADECIMAL é {hex(num)[2:]}')

else:
    opção == 0
    print('ERRO')
