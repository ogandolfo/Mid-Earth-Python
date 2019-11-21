# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

sl = (float(input(' Digite o salário: ')))

nv = sl + (sl * (15/100))

print(f' O valor atual do salário é R$ {sl}. Após o aumento o valor do salário será de R$ {nv:.2f}.')
