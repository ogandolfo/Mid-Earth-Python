# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar:
# o VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar. Calcule o valor da prestação mensal sabendo
# que ela não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Digite o valor da casa: R$ '))  # preço da casa
salario = float(input('Digite o seu salário: R$ '))  # valor do salário
anos = int(input('Em quantos anos irá pagar? '))  # tempo em anos
vm = salario * 0.3  # valor máximo das parcelas
prestacao = casa / (anos * 12)  # valor das prestações

if prestacao < vm:
    print(f'Parabéns, seu empréstimo foi aprovado! Você deverá pagar R${prestacao:.2f} ao mês, durante um período de {anos} anos.')
elif prestacao == vm:
    print(f'Suas parcelas alcançaram o valor máximo de R${vm}, que corresponde a 30% do seu salário. '
          'Revise o período do seu financiamento.')
else:
    print('Lamento, seu empréstimo foi negado.')
