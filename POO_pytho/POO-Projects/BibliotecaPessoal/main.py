from livro import Livro
from usuario import Usuario

livro1 = Livro("Senhor dos Anéis", "Tolkien")
livro2 = Livro("1984", "George Orwell")

pedro = Usuario("Pedro")

pedro.pegar_livro(livro1)
pedro.pegar_livro(livro2)
pedro.mostrar_livros()

pedro.devolver_livro(livro1)
pedro.mostrar_livros() 