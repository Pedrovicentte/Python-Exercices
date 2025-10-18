'''
Altere o programa 6.22 de forma a solicitar ao usuário o produto e a quantidade vendida.
Verifique se o nome do produto digitado existe no dicionário e só então e fetue a baixa em estoque.
'''

estoque = {
    "tomate": [1000, 2.30],
    "alface": [500, 0.45],
    "batata": [2001, 1.20],
    "feijão": [100, 1.50]
}

total = 0 
print("Digite 'fim' para sair\n")

while True: 
    for produto, dados in estoque.items():
          print(f"Produtos: {produto}, Quantidade = {dados[0]}, Preço = R${dados[1]:.2f}")

    produto = input("\nProduto: \n").lower()
    quantidade = int(input("Quantidade: \n"))
    venda = [produto, quantidade]

    if produto == "fim":
        print("Programa Finalizado!")
        break
    elif quantidade > estoque[produto][0]:
        print("Produto Indisponível.")
    elif produto not in estoque:
         print("Produto não encontrado! Tente novamente.")
         continue
    else:
        print(" ")
        
    print("Vendas:\n")
    preço = estoque[produto][1]
    custo = preço * quantidade
    print(f"{produto:12s}: {quantidade:3d} x {preço:6.2f} = {custo:6.2f}")
    estoque[produto][0] -= quantidade
    total += custo
   
    print(f"Custo total: {total:21.2f}\n")
    print("Estoque:\n")
    for chave, dados in estoque.items():
        print("Descrição: ", chave)
        print("Quantidade: ", dados[0])
        print(f"Preço: {dados[1]:6.2f}\n")