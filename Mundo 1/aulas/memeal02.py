print('\n')
print('*' * 73)
print('\033[7mFaça nosso incrível teste de personalidade e descubra se você é o Batman!\033[m')
print('*' * 73)

nome = str(input('\033[4mDigite seu magnífico nome:\033[m ')).strip().upper()

if nome == 'BRUCE WAYNE':
    print('\n\033[1m Caramba, você é realmente o Batman!')
else:
    print('\nCara, você não é o Batman.')
