from rich import print
from rich.panel import Panel
from rich.table import Table
from rich.traceback import install
install()

#Cores e emojis 
'''
print("[red]Olá Mundo[/] :earth_americas:")
print("Olá, [bold blue on green]Pequeno Gafanhoto[/] :vulcan_salute:")
print(":+1: :goblin: :-1:")
'''

#Exemplos de Paineis
'''
caixa = Panel("[white]Esse aqui é um painel de exemplo.[/]",
            title="[white]Mensagem[/]", 
            style='red', 
            width=50)
print(caixa)
'''
#Tabelas 

'''
tabela = Table(title="Tabela de Preços")
tabela.add_column("Nome", 
                  justify="center",
                  style="red")
tabela.add_column("Preço", 
                  justify="center",
                  style="blue")
tabela.add_row("Lápis", "R$ 1,50")
tabela.add_row("Borracha", "R$ 5,00")


print(tabela)
'''

# Melhorando o erro

def divisao(x, y):
    return x/y

print(divisao(50, 0))