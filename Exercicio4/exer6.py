def espiao(lista):
    for x in range(0, len(lista)):
        if lista[x] == 0 and x + 1 < len(lista):
            y = x + 1
            for y in range(y, len(lista)):
                if lista[y] == 0 and y + 1 < len(lista):
                    z = y + 1
                    for z in range(z, len(lista)):
                        if lista[z] == 7:
                            return True
    return False 