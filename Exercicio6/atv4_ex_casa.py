def monta_lista():
    lista = []
    print('OBS: Você será solicitado a inserir elementos na lista até inserir um elemento inválido')
    while True:
        item = input('Insira um número na lista: ')
        try:
            lista.append(float(item))
        except (ValueError, Exception):
            if len(lista) > 0:
                produtos = faz_produto_lista(lista)
            else:
                produtos = 0
            print(f'Lista = {lista} \nProduto dos elementos = {produtos}')
            break

## recursivo
def faz_produto_lista(lista):
        return lista[len(lista)-1] * faz_produto_lista(lista[:-1]) if len(lista) > 0 else 1
    
def f_main():
    return monta_lista()

f_main()