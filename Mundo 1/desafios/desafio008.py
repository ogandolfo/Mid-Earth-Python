# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

v = float(input(' Digite um valor em metros: '))

print(f' \n Você digitou {v} m. \n \n Seus resultados serão: \n {v/1000} km, {v/100} hm, {v/10} dam, \n {v*10} dm, {v*100} cm, {v*1000} mm.')
