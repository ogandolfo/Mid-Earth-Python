# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80KM/h, mostre uma mensagem dizendo que ele
# foi multado. A multa vai custar R$7,00 por cada KM acima do limite.

v = float(input('Insira a velocidade do veículo:'))
m = (v - 80) * 7

if v > 80:
    print(f'\n\033[1;31;40mATENÇÃO! Você foi multado por exceder o limite da via em {v-80} KM/h.\033[m')
    print(f'\033[1;31;40mO valor da multa é de R${m:.2f}.\033[m')
else:
    print('\nObrigado por respeitar as leis.')
print('\n\033[4;34mDirija com segurança.\033[m')
