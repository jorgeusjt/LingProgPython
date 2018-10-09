def contem_parQ(w):
    return False if len(w) == 0 or (w[len(w) - 1] % 2 != 0 and not contem_parQ(w[:-1])) else True
assert(contem_parQ([2,3,1,2,3,4]) == True)
assert(contem_parQ([1,3,5,7]) == False)