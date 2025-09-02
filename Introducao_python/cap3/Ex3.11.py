'''
Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto.
Exiba o valor do desconto e o preço a pagar.
'''

preco = int(input("Qual o valor do produto? "))
desconto = int(input("Qual a porcentagem de desconto? "))

valor_desconto = (desconto/100)*preco
total_desconto = preco - valor_desconto

print(f"Você teve o desconto de {valor_desconto:.0f} reais no produto.\nO valor total ficou em R${total_desconto:.2f}.")

