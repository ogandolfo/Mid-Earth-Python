# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
# Para salários superiores a R$1250,00, calcule um aumento de 10%
# para os inferiores ou iguais, o aumento será de 15%

slr = float(input('Digite o valor do seu salário: R$ '))
if slr <= 1250:
    amt = slr * (15/100)
    sa = (slr+amt)
    print(f'O aumento será de R${amt:.2f}, portanto o novo salário será R${sa:.2f}.')
else:
    amt = slr * (10/100)
    sa = (slr+amt)
    print(f'O aumento será de R${amt:.2f}, portanto o novo salário será R$ {sa:.2f}.')
