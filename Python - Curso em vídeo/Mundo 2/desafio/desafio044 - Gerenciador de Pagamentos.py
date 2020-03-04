# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu PREÇO NORMAL e CONDIÇÃO DE
# PAGAMENTO: à vista DINHEIRO/CHEQUE: 10% de desconto; à vista no CARTÃO: 5% de desconto; em até 2x NO CARTÃO: normal;
# 3x OU MAIS no cartão: 10% de juros;

lista = ['À VISTA (DINHEIRO/CHEQUE)', 'À VISTA (CARTÃO)', '2x (CARTÃO)', '3x ou mais (CARTÃO)']

print('\033[1;35m===== FULL HOUSE STORE =====\033[m')

n1 = float(input('\n\033[36mDigite o valor do(s) produto(s):\033[m R$ '))

print('\n\033[1;35mFORMAS DE PAGAMENTO\033[m\n')
print('\033[34m[ 0 ] À VISTA (DINHEIRO/CHEQUE)\033[m')  # 10 % de desconto
print('\033[34m[ 1 ] À VISTA (CARTÃO)\033[m')  # 5$ de desconto
print('\033[34m[ 2 ] 2x NO CARTÃO\033[m')  # preço se mantém o mesmo
print('\033[34m[ 3 ] 3x ou mais NO CARTÃO\033[m')  # 10% de juros

n2 = int(input('\n\033[1;35mQual a forma de pagamento?\033[m '))

if n2 == 0:
    valor = (n1 - (n1 * 0.1))
    print('\nVocê escolheu {} como forma de pagamento.'.format(lista[n2]))
    print(f'O valor de sua compra é R$ {valor:.2f}')

elif n2 == 1:
    valor = (n1 - (n1 * 0.05))
    print('\nVocê escolheu {} como forma de pagamento.'.format(lista[n2]))
    print(f'O valor de sua compra é R$ {valor:.2f}')

elif n2 == 2:
    valor = n1
    parcelas = (n1 / 2)
    print('\nVocê escolheu {} como forma de pagamento.'.format(lista[n2]))
    print(f'O valor de sua compra é R${valor:.2f}, em 2 parcelas de R${parcelas:.2f}')

elif n2 == 3:
    valor = (n1 + (n1 * 0.1))
    n3 = int(input('\033[1mQuantas parcelas?\033[m '))
    parcelas = (valor / n3)
    print('\nVocê escolheu {} como forma de pagamento.'.format(lista[n2]))
    print(f'O valor de sua compra é R${valor:.2f}, em {n3} parcelas de R${parcelas:.2f}')

else:
    total = 0
    print(f'\n\033[7;31mOpção de inválida. Tente novamente\033[m')

print('\n\033[1;36mObrigado por comprar conosco. Volte sempre!\033[m')
