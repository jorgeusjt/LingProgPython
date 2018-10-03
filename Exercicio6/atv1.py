from logging import exception
class Contato:
    def __init__ (self, nome, numero):
        self.nome = nome
        self.numero = numero
    def __str__ (self):
    return f'Nome: {self.nome}, Número: {self.numero}'


    def cadastro_de_contato ():
        menu = "1-Cadastrar\n2-Listar\n0-Sair\n"
        
      op = int (input (menu))
    if op == 1:
    try:
        f = open ("agenda.txt","a")
        nome = input("Digite o nome")
        numero = input("Digite o numero")
        f.write(nome + ": " + numero "\n")
        f.close()
        
    except IOError:
        print('Não deu certo')
    finally:
        print('Realmente passou por aqui')
    
    if op == 2:
        
        
    if op == 3:
    
    
    
    
    
   