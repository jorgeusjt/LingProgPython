# 4. Faça um Programa que leia três números e mostre-os em ordem
# decrescente.

contador =1
lista = []


while contador< 4:
	numero = int(input('Digite a %sº nota:' %contador))
	contador +=1 
	lista.append(numero)

	lista.sort()
for n in reversed(lista):
    print(n)