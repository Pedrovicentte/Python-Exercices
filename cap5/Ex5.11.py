'''
Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
Exiba os valores mês a mês para os 24 primeiros meses.
Escreva o total ganho com juros.
'''

print("------|Calculando Juros Compostos|------")

deposito_inicial = int(input("Qual o seu depósito inicial? \n"))
taxa_juros = int(input("Qual a taxa de juros? \n"))

contador = 1
saldo_atual = deposito_inicial

while contador <= 24:                         # Quando voltar novamente o valor vai estar atualizado
    juros = saldo_atual * (taxa_juros / 100)  # Calcula o juros total e guarda em juros
    saldo_atual = saldo_atual + juros         # Calcula o valor mais o juros
    print(f"{contador}°mês: {saldo_atual:.2f} reais.")
    contador = contador + 1
 