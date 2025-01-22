"""Crie uma classe chamada ContaBancaria com atributos titular, saldo e métodos depositar(valor) e sacar(valor).
O método sacar deve garantir que o saldo nunca fique negativo."""

class ContaBancaria():
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        print(f'Depózito de {valor} foi realizado.')
        print(f'SALDO: {self.saldo}')
        self.saldo += valor

    def sacar(self, valor):
        if valor < self.saldo:
            print(f'Seu saque de {valor} foi ralizado.')
            print(f'SALDO: {self.saldo}')
            self.saldo -= valor
        else:
            print('Saldo insuficiente para o saque.')
            print(f'SALDO: {self.saldo}')

minha_conta = ContaBancaria('Rodrigo', 1000)
minha_conta.depositar(500)
minha_conta.sacar(500)
minha_conta.sacar(2000)
