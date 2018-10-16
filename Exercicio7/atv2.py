div = lambda m,n: 1 + div(m - n, n) if m >= n else 0
assert(div(7,2) == 3)
print (div(7,2))