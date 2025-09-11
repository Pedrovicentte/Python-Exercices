'''
Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
Pergunte a quantidade de kWh consumida e o tipo de instalação:
R para Residencias
I para Industrias
C para comercios
Calcule o preço de acordo com a tabela a seguir:
(TABELA NO LIVRO)
'''

energia_consumida = int(input("Qual a quantidade de energia consumida? "))
tipo_instalacao = input("Qual o tipo de instalação?\n" \
"R - Residencial | I - Industrias | C - Comércios\n").lower() # O lower deixa todas as letras digitadas em letra minuscula para evitae erros no código.

# VERIFICAÇÃO 
if tipo_instalacao != 'r'and tipo_instalacao != 'i' and tipo_instalacao != 'c':
    print("[ERRO] Valor inválido, tente de novo.")

# VALOR RESIDENCIAL

elif tipo_instalacao == 'r': # Fazer primeiro a verificação para depois começar a calcular(importante para o aninhamneto e para o programa ser mais eficiente.)
    if energia_consumida <= 500:
        valor = energia_consumida * 0.40
        print(f"O valor total é de R${valor:.2f}.")
    else:
        valor = energia_consumida * 0.65
        print(f"O valor total é de R${valor:.2f}")

# VALOR INDUSTRIAL

elif tipo_instalacao == 'i':
    if energia_consumida <= 5000:
        valor = energia_consumida * 0.55
        print(f"O valor total é de R${valor:.2f}") 
    else:
        valor = energia_consumida * 0.60
        print(f"O valor total é de R${valor:.2f}")

#VALOR COMERCIAL
        
elif tipo_instalacao == 'c':
    if energia_consumida <= 1000:
        valor = energia_consumida * 0.55
        print(f"O valor total é de R${valor:.2f}")
    else:
        valor = energia_consumida * 0.60
        print(f"O valor total é de R${valor:.2f}")


