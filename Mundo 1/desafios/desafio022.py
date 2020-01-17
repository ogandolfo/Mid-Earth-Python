# Crie um pograma que leia o nome compelto de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas minúsculas
# Quantas letras no total (sem considerar espaços)
# Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
nomes = nome.split()

print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é: {nome.upper()}')
print(f'Seu nome em minúsculas é: {nome.lower()}')
#print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))  # isso deu trabalho
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))  #também deu trabalho
print(f'Seu primeiro nome é {nomes[0]} e ele tem {len(nomes[0])} letras')
