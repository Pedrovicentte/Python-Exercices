from produto import Produto
from jogo import Jogo
from dlc import DLC
from carrinho import Carrinho

# 1. Criando os produtos

jogo1 = Jogo("Lethal Company", 32.99, "Terror/Co-op")
jogo2 = Jogo("Hades", 73.99, "Roguelike")
dlc1 = DLC("Shadow of the Erdtree", 199.90, "Elden Ring")

print("-" * 40)
# 2. Testando o Polimorfismo
print(jogo1.mostrar_detalhes())
print(jogo2.mostrar_detalhes())
print(dlc1.mostrar_detalhes())
print("-" * 40)

# 3. Criando o carrinho e associando os produtos
meu_carrinho = Carrinho()
meu_carrinho.adicionar_item(jogo1)
meu_carrinho.adicionar_item(dlc1)

# 4. Calculando o total matemático
valor_final = meu_carrinho.calcular_total()
print(f"\nTotal a pagar: R$ {valor_final:.2f}")
print("-" * 40)