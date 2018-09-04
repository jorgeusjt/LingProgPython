# Atividade 01 -  
# Crie um programa que recebe uma lista de números e
# - retorne o maior elemento
# - retorne a soma dos elementos
# - retorne o número de ocorrências do primeiro elemento da lista
# - retorne a média dos elementos
# - retorne o valor mais próximo da média dos elementos
# - retorne a soma dos elementos com valor negativo
# - retorne a quantidade de vizinhos iguais



lista = []
count = 0
negativo = 0
quanti = int( input ("Insira a quantidade de números a ser inserida na lista: "))
while count < quanti :
	numeros = float(input("Digite algum número: " ))
	lista.append(numeros)
	count +=1

media = float(sum(lista)/len(lista))

for i in lista:
	if i<0 :
		negativo += i


quantidade_numeros_iguais = 0
for j in lista:
	aux = j

	
print ("\nLista: ", lista)
print ("Maior elemento: ",max(lista))
print ("Soma dos Elementos: ",sum(lista))
print ("número de ocorrências do primeiro elemento da lista: ",lista.count(lista[0]))
print ("Média dos elementos: ",media)
print ("Valor mais próximo da média dos elementos: ")
print ("Soma dos elementos com valor negativo: ", negativo)
print ("Quantidade de vizinhos iguais")

for item in range(9, -1, -2):
    print(item)

for item in range(9):
    print("\n",item)

	
