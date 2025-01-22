'''Criar uma classe chamada carro com atributos "marca", "modelo" e "ano" 
e  crie uma função para exibir as informações'''

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibirCarro(self):
        print(f'''Carro: {self.marca} {self.marca} ano: {self.ano}''')
        
meu_carro = Carro('Toyota', 'Corola', 2020)
meu_carro.exibirCarro()
