from rich import print
import time

class Livro():
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas    
        self.pagina_atual = 1
        
    def prox(self, qtd):
        self.qtd = qtd
        
        inicio = self.pagina_atual + 1
        
        fim = min(self.pagina_atual + self.qtd + 1, self.paginas + 1)
        
        for page in range(inicio, fim):
            print(f'Página {page} >', end=' ')
            time.sleep(0.7)
            
        self.pagina_atual = fim - 1
        
        if self.pagina_atual >= self.paginas:
            print(f'\nVocê alcançou o fim do livro [blue]{self.titulo}[/]')
            
        else:
            print(f'\n[blue]Você avançou {self.qtd} páginas e está na página[/] [orange1]{self.pagina_atual}[/]')
            
li = Livro('Mamamia', 20)

li.prox(2)
li.prox(4)
li.prox(16)
