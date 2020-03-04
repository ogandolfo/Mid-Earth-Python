# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

pr = float(input(' Digite o preço do produto: R$'))

print(f' O preço do produto era de R$ {pr:.2f}. Com o desconto de 5%, seu novo preço será R$ {(pr-(pr*(5/100))):.2f}.')
