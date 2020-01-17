# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# equilátero: todos os lados iguais; isósceles: dois lados iguais; Escaleno: todos os lados diferentes;


texto = ('===== ANALISADOR DE TRIÂNGULOS 2.0 =====')

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo que será: ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')  # todos os lados iguais
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')  # todos os lados diferentes
    else:
        print('ISÓSCELES!')  # dois lados iguais
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo.')
