# Desenvolva um programa que leia o comprimento de três retas e diga se elas podem ou não formar um triângulo

print('#' * 44)
texto = ('ANALISADOR DE TRIÂNGULOS')
print('{0:^44}'.format(texto))
print('#' * 44)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo.')
