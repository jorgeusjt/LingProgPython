def monta_lista():
    lista = []
    print('OBS: Você será solicitado a inserir elementos na lista até inserir um elemento inválido')
    while True:
        item = input('Insira um número inteiro na lista: ')
        try:
            lista.append(int(item))
        except (ValueError, Exception):
            print(f'Lista = {lista}')
            numero =  insere_inteiro()
            resultado = pertence_q(lista, numero)
            print(resultado)
            break
            
def insere_inteiro():
    return int(input('Digite um número inteiro: '))

## recursivo
def pertence_q(lista, numero):
    return True if len(lista)> 0 and (numero in lista or pertence_q(lista[:-1],numero)) else False
        
def f_main():
    return monta_lista()

f_main()