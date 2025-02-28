'''
Criar um progrograma para cadastar clientes e exibir na tela.
'''
# Tentar aprimora
# hello

class Pessoa:
    def __init__(self):
        self.nome = None
        self.data = None
        self.email = None
        self.estado = None

    
    def cadastro(self):
        for k in self.__dict__.keys():
            if k == 'data':
                setattr(self, k, input(f'Ano de nascimento do(a) cliente: '))
            elif k == 'estado':
                setattr(self, k, input(f'{k.capitalize()} do(a) cliente: ').upper())
            else: 
                setattr(self, k, input(f'{k.capitalize()} do(a) cliente: '))
        return self

    def exibir_cliente(self):
        for k, v in self.__dict__.items():
            print(f'{k.capitalize()} : {v}')
        print(20 * '=-')


print('Cadastro de pessoa')
cadastrados = []

for i in range(1):
    cliente = Pessoa()
    cadastrados.append(cliente.cadastro())
    print('=-'*20)

for c in cadastrados:
    c.exibir_cliente()