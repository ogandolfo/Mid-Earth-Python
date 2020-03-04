# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão

print('=' * 20)
print('10 TERMOS DE UMA P.A')
print('=' * 20)

termo = int(input('Digite o primeiro termo: '))
rz = int(input('Digite a razão: '))
dcm = termo + (10 - 1) * rz
for c in range(termo, dcm + rz, rz):
    print(c, end=' -> ')
print('ACABOU!')
