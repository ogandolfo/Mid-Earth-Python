# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um NÚMERO ENTRE 0 E 10. Só que agora, o jogador vai
# tentar advinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

"""from random import randint
from time import sleep

palpites = 0
pc = randint(0, 10)  # solicita à máquina que compute um valor

print('\n')
print('-=-' * 32)
print('\033[7;30mAí, seu amontoado de carne, acerte o número entre 0 e 10 que eu computei e ganhe um belo '
      'NADA!\033[m')
print('-=-' * 32)

user = int(input('\n\033[1mHey, seu bunda mole. Digite um número: \033[m'))
print('\n\033[4mOpa, calma lá amigão. Parece que você está com pressa, mas eu não...\033[m')
sleep(1)
'''while user > 10:
      print('Você é burro ou o quê?')
      user = int(input('Digita um número VÁ-LI-DO! Manda: '))
print('Opa, calma lá amigão. Parece que você está com pressa, mas eu não...')
sleep(1)'''

while user != pc:
      palpites += 1
      if user > 10:
            print('\n\033[1mVocê é burro ou o quê?\033[m')
            sleep(0.5)
            user = int(input('\nDigita um número \033[1;31mVÁ-LI-DO!\033[m Manda: '))
            print('\n\033[4mOpa, calma lá amigão. Parece que você está com pressa, mas eu não...\033[m')
            sleep(1)
      else:
            if user < pc:
                  print('\n\033[31mMas tu é ruim ein? SOBE ESSA APOSTA!\033[m')
                  sleep(0.5)
                  user = int(input('\n\033[31mSOBE ESSA APOSTA! \033[m'))
                  print('\n\033[4mOpa, calma lá amigão. Parece que você está com pressa, mas eu não...\033[m')
                  sleep(1)
            elif user > pc:
                  print('\n\033[31mMas tu é ruim ein? DESCE ESSA APOSTA!\033[m')
                  sleep(0.5)
                  user = int(input('\n\033[31mDESCE ESSA APOSTA! \033[m'))
                  print('\n\033[4mOpa, calma lá amigão. Parece que você está com pressa, mas eu não...\033[m')
                  sleep(1)
print(f'\n\033[35mPane no sistema alguém me desconfigurou... Ah, você tentou {palpites} vezes\033[m')"""

from random import randint

computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False  # está como false porque você não acertou ainda
tentativas = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    tentativas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez: ')
print(f'Parabéns! Você tentou {tentativas} vezes.')
