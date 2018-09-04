# 2. Faça um Programa que verifque se uma letra digitada é vogal ou
# consoante.

letra = input("Digite uma letra: ")

if(letra.upper()=='a' or letra.upper()=='e' or letra.upper()=='i' or letra.upper()=='o' or letra.upper()=='u'  ):
	print("Essa letra '%s' é uma vogal" %(letra))
else:
	print("Essa letra '%s' é uma consoante" %(letra))