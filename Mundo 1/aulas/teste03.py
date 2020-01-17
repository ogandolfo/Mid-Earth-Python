import random
lista = []
x = random.randint(0, 100)
num = int(input("Insira um número inteiro entre 0 e 100: "))
lista.append(num)
while num != x:
    if num < x:
        num = int(input("Insira um número maior: "))
        lista.append(num)
    if num > x:
        num = int(input("Insira um número menor: "))
        lista.append(num)
if num == x:
        print(f"O número era: {x}")
