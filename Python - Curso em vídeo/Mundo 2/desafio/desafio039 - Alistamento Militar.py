# Faça um programa que leia o ano de nascimento de uma jovem e informe, de acordo com sua idade:
# se ele AINDA VAI SE ALISTAR ao serviço militar; se é a HORA DE SE ALISTAR; se já PASSOU DO TEMPO do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import date
atual = date.today().year
nasc = int(input("Digite o ano de seu nascimento: "))
idade = (atual - nasc)  # ano atual subtrai ano de nascimento

if idade == 18:
    print('\nEstá na hora de se alistar!')
elif idade < 18:
    saldo = (18 - idade)
    ano = (atual + saldo)
    print(f'\nAinda faltam {saldo} ano(s) até o alistamento, que será em {ano}.')
else:
    saldo = (idade - 18)
    ano = (atual - saldo)
    print(f'\nVocê já deveria ter se alistado há {saldo} ano(s), especificamente em {ano}!')
