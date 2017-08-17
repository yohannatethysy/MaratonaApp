from model.Pessoa import Pessoa
from model.Cliente import Cliente
from model.Funcionario import Funcionario
from model.Maratona import Maratona

def main():
    cliente = Cliente('Xuxa')
    funcionario = Funcionario('Beltrano')
    maratona = Maratona()

    maratona.correr(cliente)
    maratona.correr(funcionario)

    pessoa = Pessoa('Cicrana')
    print(pessoa)

if __name__ == "__main__":
    main()
    
    
