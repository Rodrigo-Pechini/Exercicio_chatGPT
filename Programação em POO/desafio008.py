"""Crie uma classe chamada Calculadora com métodos para realizar as quatro operações básicas 
(somar, subtrair, multiplicar, dividir). 
O método de divisão deve verificar se o divisor é zero antes de realizar a operação."""

class Calculadora():
    def __init__(self):
        pass

    def somar(self, valor1, valor2):
        return valor1 + valor2
    
    def subtrair(self, valor1, valor2):
        return valor1 - valor2

    def multiplicar(self, valor1, valor2):
        return valor2 * valor1
    
    def dividir(self, valor1, valor2):
        if valor2 == 0:
            return'ERRO!!! Não se divide para zero'
        else:
            return valor1 / valor2 

calc = Calculadora()
print(f"Soma: {calc.somar(10, 5)}")
print(f"Subtração: {calc.subtrair(10, 5)}")
print(f"Multiplicação: {calc.multiplicar(10, 5)}")
print(f"Divisão: {calc.dividir(10, 5)}")
print(f"Divisão por zero: {calc.dividir(10, 0)}")
