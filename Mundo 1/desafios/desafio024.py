# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')
#n2 = n1.title()
#n3 = n2.find('Santo', 5)
#if n3 < 0:
#    print('Não começa com "Santo".')
#else:
#    print('O nome da cidade começa com "Santo". ')
