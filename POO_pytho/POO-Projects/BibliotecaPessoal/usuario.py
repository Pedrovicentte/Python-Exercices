class Usuario():
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestados = []
        
        
    def pegar_livro(self, livro):
        if livro.disponivel:
            livro.emprestar()
            self.livros_emprestados.append(livro)
        else:
            print(f"Atenção: O livro '{livro.titulo}' já está com outra pessoa.")
    
    def devolver_livro(self, livro):
        for i in self.livros_emprestados:
            if livro == i:
                self.livros_emprestados.remove(livro)
                livro.devolver()
                break        
                  
    def mostrar_livros(self):
        for i in self.livros_emprestados:
            print(f"- {i.titulo}")