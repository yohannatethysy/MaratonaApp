class Pessoa():
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print('Falando genericamente')

    def andar(self):
        print('Andando genericamente')

    def pagar(self):
        print('Pagando genericamente')
        
    def __str__(self):
        return('Nome do objeto pessoa: %s') % self.nome
