"""Crie uma classe chamada Retangulo com os atributos largura e altura. 
Adicione métodos para calcular:
A área do retângulo.
O perímetro do retângulo."""

class Retangulo():
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def calcular_area(self):
        print(f'A área do retangulo é de {self.altura * self.largura}')

    def calcular_perimetro(self):
        print(f'O perímetro do retangulo é de {(self.largura * 2) + (self.altura * 2)}')

retangulo = Retangulo(5, 3)
retangulo.calcular_area()
retangulo.calcular_perimetro()
