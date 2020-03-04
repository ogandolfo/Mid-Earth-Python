# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade:
# até 9 anos: MIRIM; até 14 anos: INFANTIL; até 19 anos: JUNIOR; até 25 anos: SÊNIOR; acima: MASTER;

from datetime import date
from time import sleep
hoje = date.today().year

nasc = int(input('\nAno de seu nascimento: '))
idade = (hoje - nasc)
print(f'O/A atleta tem {idade} anos, portanto se encaixa na categoria...\n')
#sleep(1)

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JÚNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
