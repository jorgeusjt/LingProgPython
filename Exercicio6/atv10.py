def monta_lista():
    lista = []
    n_lista = []
    print('OBS: Você será solicitado a inserir elementos na lista até inserir um elemento inválido')
    while True:
        item = input('Insira um número inteiro na lista: ')
        try:
            lista.append(int(item))
        except (ValueError, Exception):
            print(f'Lista = {lista}')
            n_lista = inverte(lista)
            print(f'Lista Invertida = {n_lista}')
            break

## recursivo
inverte = lambda lista: (inverte(lista[1:]) + lista[:1] if lista else [])
    
def f_main():
    return monta_lista()

f_main()