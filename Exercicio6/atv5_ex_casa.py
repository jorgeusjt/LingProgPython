def monta_lista():
    lista = []
    print('OBS: Você será solicitado a inserir elementos na lista até inserir um elemento inválido')
    while True:
        item = input('Insira um número inteiro na lista: ')
        try:
            lista.append(int(item))
        except (ValueError, Exception):
            if len(lista) > 0:
                resultado = verifica_par(lista)
                print(resultado)
                break
            else:
                print('A lista está vazia!')

## recursivo
def verifica_par(lista):
    return True if len(lista)> 0 and (lista[len(lista)-1] % 2 == 0 or verifica_par(lista[:-1])) else False
    
def f_main():
    return monta_lista()

f_main()