# Crie um programa que faça o computador jogar JOKENPÔ com você

from time import sleep
from random import randint

print('Vamos jogar JOKENPÔ?')

print('As opções são:\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA')

user = int(input('Faça sua jogada: '))
opções = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0, 2)

while user >= 3:
    print('Você é burrão ein... Digita direito cara...')
    user = int(input('Joga de novo, gênio: '))

print('\nVocê escolheu {}:'.format(opções[user]))
print('A máquina escolheu {}\n'.format(opções[pc]))

if pc == 0:  # computador jogou PEDRA
    if user == 0:
        print('Ih rapaz, rolou empate...')
    elif user == 1:
        print('Eita caraio, você ganhou.')
    elif user == 2:
        print('Calma lá amigão. Parece que eu ganhei!')
    else:
        print('JOGADA INVÁLIDA!')

elif pc == 1:  # computador jogou PAPEL
    if user == 0:
        print('Calma lá amigão. Parece que eu ganhei!')
    elif user == 1:
        print('Ih rapaz, rolou empate...')
    elif user == 2:
        print('Eita caraio, você ganhou.')
    else:
        print('JOGADA INVÁLIDA!')

elif pc == 2:  # computador jogou TESOURA
    if user == 0:
        print('Eita caraio, você ganhou.')
    elif user == 1:
        print('Calma lá amigão. Parece que eu ganhei!')
    elif user == 2:
        print('Ih rapaz, rolou empate...')
    else:
        print('JOGADA INVÁLIDA!')
