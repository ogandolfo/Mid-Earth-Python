# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a
# tabela: abaixo de 18.5: abaixo do peso; entre 18.5 e 25: peso ideal; de 25 até 30: sobrepeso; de 30 a 40: obesidade;
# acima de 40 obesidade mórbida

peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em M: '))
IMC = (peso / (altura ** 2))
print(f'{IMC:.2f}')

if IMC <= 18.5:
    print(f'Você está abaixo do peso.')
elif IMC <= 25:
    print(f'Você está no peso ideal')
elif IMC <= 30:
    print(f'Você está em sobrepeso')
elif IMC <= 40:
    print(f'Você está em obesidade')
else:
    print(f'Você está em obesidade mórbida')
