# função escrever que recebe um texto e mostra uma mensagem com tamanho adaptável

def escreva():
    mensagem = str(input('Digite um texto aqui: '))
    print('-'* (len(mensagem) + 6))
    print(f'   {mensagem}')
    print('-'* (len(mensagem) + 6))


escreva()
