'''
Escreva um program para controlar uma pequena máquina registradora.
Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada.
Utulize a tabela de códigos a seguir para obter o preço de cada produto.

[TABELA NO LIVRO]

Seu programa deve exibir o total das compras depois que o usuário digitar 0.
Qualquer outro código deve gerar a mensagem de erro "Código Inválido".
'''

total_compras = 0
print(
" ________________\n"
"| CÓDIGO | PREÇO |" \
"\n------------------"   
"\n|    1   |  0,50 |" \
"\n|    2   |  1,00 |" \
"\n|    3   |  4,00 |" \
"\n|    5   |  7,00 |" \
"\n|    9   |  8,00 |" \
"\n------------------")

while  True:
    produto = int(input("Digite o código do produto: "))
    if produto == 0:
        print("Compra finalizada")
        total_compras += produto
        print(f"O total deu R$ {total_compras:.2f} reais.")
        break
    elif produto != 1 and produto != 2 and produto != 3 and produto != 5 and produto != 9:
        print("[ERRO] Código Invláido!")
    elif produto == 1:
        total_compras += 0.50
    elif produto == 2:
        total_compras += 1.00
    elif produto == 3:
        total_compras += 4.00
    elif produto == 5:
        total_compras += 7.00
    elif produto == 9:
        total_compras += 8.00 