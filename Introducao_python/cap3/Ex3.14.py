'''
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como
a quantidade de dias pelos quais o carro foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$ 0,15 por km rodado.
'''

km_percorridos = float(input("Quantos Km você percorreu? "))
quantidade_dias = int(input("Quantos dias você alugou? "))

total_km = km_percorridos * 0.15
total_dia = quantidade_dias * 60
preco_final = total_km + total_dia

print(f"O total a se pagar é de R$ {preco_final:0.2f} reais.")


