# Refaça o desafio 009, mostrando a tabuada de um npumero que o usuário escolher, só que agora usando o laço for.

n = int(input('Digite um número para ver sua taubada: '))
for c in range(1, 11):
    print(f' {n} x {c:2} = {n * c:2}')
