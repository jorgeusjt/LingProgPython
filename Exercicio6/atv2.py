def  div ( divivendo , divisor ):
    return  0  if divivendo < divisor else  1 + div (divivendo - divisor, divisor)
    print (div (5,2))
    print (div (2,3))