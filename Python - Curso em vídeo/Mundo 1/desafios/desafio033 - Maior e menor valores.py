# Faça um programa que leia três número e mostre qual é o MAIOR e qual é o MENOR.

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
# Verificando quem é menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
# Verificando quem é o maior
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print(f'O maior valor digitado foi {maior}.')
print(f'O menor valor digitado foi {menor}.')
