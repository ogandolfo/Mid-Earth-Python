# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio,
# indo de 10 até 0, com pausa de 1 segundo entre eles

from time import sleep
print('Atenção para a contagem regressiva!')
sleep(1)
for cont in range(10, -1, -1):
    print(cont)
    sleep(1)
print('KABUM!!!')
