# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

n1 = str(input('Digite seu nome: ')).strip().title()
n2 = 'Silva' in n1
print(f'Seu nome tem Silva? {n2}')
