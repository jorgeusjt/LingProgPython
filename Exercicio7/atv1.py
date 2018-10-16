somannat = lambda n: 1 if n==1 else n + somannat(n-1)

assert(somannat(5) == 15)
print(somannat(5))