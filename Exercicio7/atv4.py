prod_lista = lambda lista: lista[len(lista) - 1] * prod_lista(lista[:-1]) if len(lista) > 0 else 1
assert(prod_lista([1,2,3,4,5,6]) == 720)
assert(prod_lista([2,2,2]) == 8)
print(prod_lista([1,2,3,4,5,6]))