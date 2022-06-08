# fazer uma função chamada maior que recebe vários parâmetros e diz qual é o maior ao final

def maior(* num):
    count = 0
    maiornum = 0
    for valor in num:
        if count == 0:
            maiornum = valor
            count += 1
        else:
            if valor > maiornum:
                maiornum = valor
    print(f'O maior número é {maiornum}')

maior(2, 11, 1, 444, 34)
maior(-1, 33, 1000, 2)
