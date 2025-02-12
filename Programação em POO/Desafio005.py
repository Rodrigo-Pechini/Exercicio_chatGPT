"""Crie uma classe chamada Produto com os atributos nome e preco. Em seguida, 
crie uma classe chamada Loja, que mantém um inventário de produtos. Adicione métodos para:
Adicionar produtos.
Exibir o inventário."""

class Produto():
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Loja():
    def __init__(self):
        self.inventario = []

    def adicionar_produto(self, produto):
        self.inventario.append(produto)

    def exibir_inventario(self):
        print('Produtos na loja')
        for e, p in enumerate(self.inventario, start=1):
            print(f'{e}. {p.nome} - R${p.preco}')

produto1 = Produto("Notebook", 3000)
produto2 = Produto("Teclado", 150)

loja = Loja()
loja.adicionar_produto(produto1)
loja.adicionar_produto(produto2)
loja.exibir_inventario()
