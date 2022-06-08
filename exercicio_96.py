# função que recebe as dimensões de um terrenos e mostra a área

def area():
    while True:
        a = float(input('Qual o valor de uma dimensão? '))
        b = float(input('Qual o valor da outra dimensão? '))
        area = a * b
        print(f'O valor da área de um terreno com {a}m de largura e {b}m de comprimento é: {area}m².')
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        while opcao not in "SsNn":
            opcao = str(input('Quer continuar? [S/N] '))
        if opcao in "Nn":
            break

area()

