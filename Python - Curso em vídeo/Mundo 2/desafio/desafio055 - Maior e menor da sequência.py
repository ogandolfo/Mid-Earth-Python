# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Peso da {p}ª pessoa: '))
    if p == 1:  # vai ler o peso da primeira pessoa como maior e menor simultaneamente
        maior = peso
        menor = peso
    else:
        if peso > maior:  # lê os outros pesos e os reorganiza
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi {maior:.1f} KG enquanto o menor foi {menor:.1f}KG.')
