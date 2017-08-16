from model.Pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome):
        super(Cliente, self).__init__(self, nome)
        self.nome = nome

    def pagar(self):
        print('Pagando especificamente')
