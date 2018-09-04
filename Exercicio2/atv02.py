# Atividade 2 
# Faça um programa que receba duas listas e retorne True se são
# iguais ou False caso contrario.
# Duas listas são iguais se possuem os mesmos valores e na mesma
# ordem.

lista=[]
lista2=[]
count=0
count1=0
while count < 4 :
	numeros = int(input("Insira na 1º lista: "))
	lista.append(numeros)
	count +=1

print("\n")

while count1 < 4 :
	numeros2 = int(input("Insira na 2º lista: "))
	lista2.append(numeros2)
	count1 +=1

print ("\n listas:", lista,lista2)
print("As listas são iguais: " ,lista==lista2)

