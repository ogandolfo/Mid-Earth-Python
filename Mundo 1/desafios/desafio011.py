# Faça um programa que leia a largura e a altura de uma parede em metros
# calcula sua área e a quantidade de tinta necessária para pintá-la
# sabendo que cada litro de tinta pinta uma área de 2m²

h = float(input(' Insira o valor da altura da parede em metros: '))
l = float(input(' Insira o valor da largura da parede em metros: '))

print(f'\n A dimensão da parede é {h} x {l} m.'
      f'\n A área a ser pintada possui {h*l} m².'
      f'\n Você precisará de {((h*l)/2)} l de tinta.')
