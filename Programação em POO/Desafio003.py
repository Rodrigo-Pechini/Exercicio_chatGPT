"""Crie uma classe chamada Aluno com os atributos nome e notas (uma lista de notas).
Adicione um método chamado calcular_media para retornar a média das notas."""

class Aluno():
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
         return sum(self.notas)/len(self.notas)

aluno1 = Aluno('Maria', [8.5, 7.0, 9.0])
media = aluno1.calcular_media()
print(f'Média de {aluno1.nome}: {media:.2f}')
