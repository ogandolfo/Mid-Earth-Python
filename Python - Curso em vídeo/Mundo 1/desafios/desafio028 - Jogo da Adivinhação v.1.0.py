# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça
# para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá
# escrever na tela se o usuário venceu ou perdeu

from random import randint
from time import sleep

pc = randint(0, 9)  # faz o computador "pensar"
print('\n')
print('-=-' * 33)
print('\033[7;30mAí, seu amontoado de carne, tente acertar o número entre 0 e 9 que eu computei e ganhe um belo '
      'NADA!\033[m')
print('-=-' * 33)

user = int(input('\n\033[1mDigite um número, reles mortal: \033[m'))  # humano tenta advinhar

while user > 9:
    print('\nVocê digitou um número inválido, \033[1;31mIDIOTA!\033[m')

    user = int(input('\n\033[1mObedeça as regras do jogo e digite um número válido: \033[m'))

print('\n\033[4mPOR QUE A PRESSA? TENHO TODO TEMPO POSSÍVEL...\033[m')
sleep(2)

if user == pc:
    print('\n\033[35mImpossível, você hackeou meu sistema? Para minha desgraça, você acertou...\033[m')

else:
    print(f'\n\033[31mQue previsível, obviamente você errou. Eu computei o número {pc}\033[m')

#while user > 5:
#    print('\nVocê digitou um número inválido, \033[1;31mIDIOTA!\033[m')
#
#    user = int(input('\n\033[1mDigita aí um número, reles mortal: \033[m'))
#    if user == pc:
#        print('\n\033[35mImpossível, você hackeou meu sistema? Para minha desgraça, você acertou...')
#    else:
#        print(f'\n\033[31mQue previsível, obviamente você errou. Eu computei o número {pc}\033[m')
#elif user >5:
#     print('\nVocê digitou um número inválido, idiota.')