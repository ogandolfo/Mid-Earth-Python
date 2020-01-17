# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

cart = float(input(' Quanto dinheiro você tem? R$'))
dol = cart / 4.205
bc = cart / 34964.14
print(f'\nVocê possui R$ {cart:.2f}, podendo comprar US$ {dol:.2f}.')
print(f'\nVocê também pode comprar {bc:.2f} bitcoins.')
