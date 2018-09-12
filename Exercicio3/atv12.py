# 12. Uma fruteira está vendendo frutas com a seguinte tabela de
# preços:
# Até 5 Kg Acima de 5 Kg
# Morango R$ 2,50 por Kg R$ 2,20 por Kg
# Maçã R$ 1,80 por Kg R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da
# compra ultrapassar R$ 25,00, receberá ainda um desconto de 10%
# sobre este total. Escreva um algoritmo para ler a quantidade (em
# Kg) de morangos e a quantidade (em Kg) de maças adquiridas e
# escreva o valor a ser pago pelo cliente.



preco = 0
kgMorg = float(input("Insira a quantidade em kg de morangos: "))
kgMaca = float(input("Insira a quantidade em kg de maçãs: "))

if kgMorg < 5:
    total_morango = kgMorg * 2.5
else:
    total_morango= kgMorg * 2.2
    
if kgMaca < 5:
    total_maca = kgMaca * 1.8
    total = total_morango + total_maca
else:
    total_maca = kgMaca * 1.5
    total = total_morango + total_maca
    
if total > 25.00:
    total *= 0.90

    
print ('Valor do Morango: ', total_morango)
print ('Valor da maça: ', total_maca)
print('Valor total: ', total)