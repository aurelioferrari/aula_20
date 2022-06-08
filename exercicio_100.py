# fazer um programa que tenha uma lista
# ter duas funçoes
# 1) sortear 5 números e adicionar na lista
# 2) mostrar a soma dos números pares dessa lista

import random
numeros = []

soma = 0


def sorteio():
    for i in range(0, 5):
        num = random.randint(1, 10)
        numeros.append(num)


def sompar():
    global soma
    for n in numeros:
        if n % 2 == 0:
            soma = soma + n




sorteio()
sompar()
print('Os números sorteados foram')
for n in numeros:
    print(f'{n}', end=' ')
print(f'\nA soma dos números pares é {soma}.')

