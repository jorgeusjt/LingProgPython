def blackjack (a,b,c):
    soma = a + b + c
    if soma <= 21:
        return soma
    else:
        if 11 in [a,b,c]:
            return soma - 10 
        return 'ESTOUROU'
       
    print (blackjack(11, 9, 9))
    print (blackjack(1,2, 3))
    print (blackjack(3,10,10))