# Crie um programa que leia um frase qualquer e diga se ela é um palíndromo desconsiderando os espaços

frase = str(input('Digite uma frase: ')).strip().upper()  # torna tudo maiuscula e remove espaços antes e  depois
palavras = frase.split()  # faz a separação de termos em palavras
junto = ''.join(palavras)  # reagrupa as palavras sem espaçamento
inverso = ''  # inverte e ordem das palavras
inverso = junto[::-1]  # usando fatiamento também é possível fazer
'''for letra in range(len(junto) - 1, -1, -1):  # começa do 0 ao 19, vai até a ultima letra de forma retrograda.
    inverso += junto[letra]'''
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo.')
else:
    print('Não temos um palíndromo.')
