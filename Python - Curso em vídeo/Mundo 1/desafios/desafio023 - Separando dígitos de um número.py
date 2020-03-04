# Faça um programa que leia um númer de 0 a 9999 e mostre na tela cada um dos digitos separados

num = int(input("Digite um número entre '1' e '9999': "))

m = num // 1000 % 10
c = num // 100 % 10
d = num // 10 % 10
u = num // 1 % 10

print(f'Analisando o número {num}')
print(f'Milhar: {m}')
print(f'Centena: {c}')
print(f'Dezena: {d}')
print(f'Unidade: {u}')
