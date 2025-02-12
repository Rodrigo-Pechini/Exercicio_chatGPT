"""Crie uma classe chamada Pessoa com os atributos nome e idade. 
Adicione um método chamado aniversario que aumenta a idade da pessoa em 1."""

class Pessoa():
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1

pessoa1 = Pessoa("João", 30)
print(f"Idade de {pessoa1.nome}: {pessoa1.idade}")
pessoa1.aniversario()
print(f"Idade de {pessoa1.nome} após aniversário: {pessoa1.idade}")

