prim_alg = lambda n: n if n<10 else prim_alg(n//10)

assert(prim_alg(5649) == 5)
assert(prim_alg(7) == 7)


print(prim_alg(5649))
print(prim_alg(7))