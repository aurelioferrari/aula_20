# fazer uma função chamada maior que recebe vários parâmetros e diz qual é o maior ao final

maiornum = 0


def maior():
    cont = 0
    while True:
        valor = float(input("Digite um valor: "))
        if cont == 0:
            maiornum = valor
            cont += 1
        if valor > maiornum:
            maiornum = valor

        opcao = str(input('Você quer continuar? [S/N] '))
        while opcao not in "SsNn":
            opcao = str(input('Você quer continuar? [S/N] '))
        if opcao in "Nn":
            print(f'O maior número é: {maiornum}')
            break

maior()