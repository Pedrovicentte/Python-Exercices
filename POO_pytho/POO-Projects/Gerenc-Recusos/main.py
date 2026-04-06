from app import Aplicativo
from computador import Computador

# Criando os aplicativos
app1 = Aplicativo("Navegador Web", 1500)
app2 = Aplicativo("Editor de Video", 2000)
app3 = Aplicativo("Jogo Pesado", 2500)

# Criando um PC com 4000 MB de RAM
meu_pc = Computador(4000)

meu_pc.abrir_app(app1) # Deve abrir e sobrar 2500
meu_pc.abrir_app(app2) # Deve abrir e sobrar 500
meu_pc.mostrar_desempenho()

meu_pc.abrir_app(app3) # O PC deve barrar e dar aviso de falta de RAM!

meu_pc.fechar_app(app2) # Fecha o editor e devolve os 2000 de RAM
meu_pc.mostrar_desempenho()
meu_pc.abrir_app(app3) # Agora o jogo pesado deve abrir!
meu_pc.mostrar_desempenho()