"""Exercício 11: Biblioteca de Livros
Crie duas classes: Livro e Biblioteca.
1. A classe Livro terá atributos título e autor.
2. A classe Biblioteca terá um atributo acervo, que começa como uma lista vazia [].
3. A Biblioteca deve ter dois métodos:
○ adicionar_livro(livro): recebe um objeto Livro e o adiciona à lista acervo.
○ listar_livros(): percorre a lista acervo e imprime o título e o autor de cada livro.
Crie uma biblioteca, crie alguns objetos Livro e adicione-os à biblioteca. Depois, liste os livros."""


class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Biblioteca:
    def __init__(self):
        self.acervo = []  

    def adicionar_livro(self, livro):
        self.acervo.append(livro)

    def listar_livros(self):
        if not self.acervo:
            print("A biblioteca está vazia.")
        else:
            print(" Livros na biblioteca:")
            for livro in self.acervo:
                print(f"- {livro.titulo}, de {livro.autor}")


livro1 = Livro("Dom Casmurro", "Machado de Assis")
livro2 = Livro("O Hobbit", "J.R.R. Tolkien")
livro3 = Livro("1984", "George Orwell")

biblioteca = Biblioteca()
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

biblioteca.listar_livros()
