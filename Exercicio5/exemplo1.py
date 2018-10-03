from errno import ENOMEM
class Pessoa:
#variável de classe
contador = 0
#construtor
def __init__ (self, nome):
#nome agora é uma variável de instância, por ter sido acessada com self
self.nome = nome
# de classe, portanto pode ser acessada com o nome da classe
Pessoa.contador += 1
#errado, pois tenta criar uma variável contador local e já usá-la
#contador = contador + 1
jose = Pessoa ("José")
print (jose.contador)
maria = Pessoa ("Maria")
print (maria.contador)
print (jose.nome)
print (maria.nome)
print(Pessoa.contador)