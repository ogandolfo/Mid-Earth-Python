# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a
# média atingida: média abaixo de 5.0: REPROVADO; média entre 5.0 e 6.9: RECUPERAÇÃO; média 7.0 ou superior: APROVADO

print('-=-' * 7)
print('\033[1;36;40mCALCULADORA DE MÉDIAS\033[m')
print('-=-' * 7)

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = ((n1 + n2) / 2)

if media < 5:
    print(f'\n\033[1:31mO aluno foi REPROVADO com a média {media:.1f}. Lamento!\033[m')

elif 5 <= media <= 6.9:  # simplificação do sistema
    print(f'\n\033[1;33mO aluno ficou em RECUPERAÇÃO com a média {media:.1f}. Estude mais!\033[m')

else:
    print(f'\n\033[1;34mO aluno foi APROVADO com a media {media:.1f}. Parabéns!\033[m')

print('\nObrigado por usar nosso sistema. Volte sempre!')