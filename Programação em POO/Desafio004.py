"""Crie uma classe chamada Livro com os atributos titulo e autor. 
Em seguida, crie uma classe chamada Biblioteca, que armazena livros em uma lista. Adicione métodos para:
Adicionar um livro.
Listar todos os livros."""

class Livro():
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Biblioteca():

    def __init__(self):
        self.livros = []
    
    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        for e, l in enumerate(self.livros, start=1):
            print(f'{e}. {l.titulo}, por {l.autor}')

livro1 = Livro("O Hobbit", "J.R.R. Tolkien")
livro2 = Livro("1984", "George Orwell")

biblioteca = Biblioteca()
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.listar_livros()
