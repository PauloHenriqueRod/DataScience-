# classes, por covenção, iniciam com letra maiúscula
class Livro:
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn
        print('CRONSTUTOR CHAMADO')

    def imprime(self):
        print(f'O livro {self.titulo} tem ISBN-{self.isbn}')


livro1 = Livro('A menina que roubava livros', 87879897)
livro1.imprime()
