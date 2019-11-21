# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
n1 = float(input('Digite um valor: '))

db = n1*2
tp = n1*3
rq = n1**(1/2)

print(' \n Você digitou {}. \n Seu dobro é: {}. \n Seu triplo é: {}. \n Sua raíz quadrada é: {:.2f}'.format(n1, db, tp, rq))
