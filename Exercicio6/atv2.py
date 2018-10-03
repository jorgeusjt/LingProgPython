def div (divivendo, divisor):
    return 0 if dividendo < divisor else 1 + div (dividendo - divisor, divisor)
    print (div (5,2))
    print (div (2,3))