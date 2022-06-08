# criar função contador que recebe inicio, fim e passo
# mostrar a contagem de uma entrada personalizada
from time import sleep

soma = 0




def contador(a, b, c):
    if b > a and c > 0:
        soma = a
        print(f'{soma}', end=' ')
        sleep(0)
        while soma < b:
            soma = soma + c
            print(f'{soma}', end=' ')
            sleep(0)
    if b < a and c < 0:
        soma = a
        print(f'{soma}', end=' ')
        sleep(0)
        while soma > b:
            soma = soma + c
            print(f'{soma}', end=' ')
    print()


def contador_p():
    a = int(input('Qual o início da contagem? '))
    b = int(input('Qual o fim da contagem? '))
    c = int(input('Qual o passo? '))
    if c == 0:
        c += 1
    if b > a and c > 0:
        soma = a
        print(f'{soma}', end=' ')
        sleep(0)
        while soma < b:
            soma = soma + c
            print(f'{soma}', end=' ')
            sleep(0)
    if b < a and c < 0:
        soma = a
        print(f'{soma}', end=' ')
        sleep(0)
        while soma > b:
            soma = soma + c
            print(f'{soma}', end=' ')
    if a > b and c > 0:
        soma = a
        while soma >= b:
            print(f'{soma}', end=' ')
            soma = soma - c
    if a < b and c < 0:
        print('Formatação incorreta.')


    print()





contador(1, 10, 1)
contador(10, 0, -2)
contador_p()


