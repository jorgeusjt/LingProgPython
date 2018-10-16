pertenceQ = lambda w,n: True if n in w else False

assert(pertenceQ([1,2,3],1) == True)
assert(pertenceQ([1,2,3],2) == True)
assert(pertenceQ([1,2,3],3) == True)
assert(pertenceQ([1,2,3],4) == False)

print(pertenceQ([1,2,3],1))
print(pertenceQ([1,2,3],2))
print(pertenceQ([1,2,3],3))
print(pertenceQ([1,2,3],4))