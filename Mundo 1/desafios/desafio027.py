# Faça um programa que leia um nome completo de uma pessoa
# mostrando em seguida o primeiro e o último nome separadamente

n = str(input('Digite seu nome completo: ')).strip().title()
nomes = n.split()

print('Analisando seu nome...')
print(f'Seu primeiro nome é: {nomes[0]}')
print(f'Seu último nome é: {nomes[len(nomes)-1]}')
# usar da exibição do tamanho do nome menos o resultado
