def soma_nat (n):
        return 1 if n == 1 else n + soma_nat(n - 1)
print(soma_nat(2), soma_nat(1), soma_nat(5))