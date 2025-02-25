
class Pessoa:
    def __init__(self):
        self.nome = None
        self.idade = None
        self.email = None
        self.estado = None

    
    def cadastro(self):
        for k in self.__dict__.keys():
            setattr( self, k, input(f'{k.capitalize()} do(a) cliente: '))
        return self

    def exibir_cliente(self):
        for k, v in self.__dict__.items():
            print(f'{k.capitalize()} : {v}')
        print(20 * '=-')


print('Cadastro de pessoa')
cadastrados = []

for i in range(0, 2):
    cliente = Pessoa()
    cadastrados.append(cliente.cadastro())
    print('=-'*20)

for c in cadastrados:
    c.exibir_cliente()