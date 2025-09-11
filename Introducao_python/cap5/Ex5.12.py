'''
Aletere o programa anterior de forma a perguntar também o valor depositado mensalmente.
Esse valor será depositado no início de cada mês, e você deve considerá-lo para o cálculo de juros
do mes seguinte.
'''

deposito_inicial = float(input("Qual o seu depósito inicial? \n"))
valor_mensal = float(input("Qual o valor mensal a ser depositado?\n"))
taxa_juros = int(input("Qual a taxa de juros? \n"))

contador = 1
saldo_atual = deposito_inicial

while contador <= 24:                         
    juros = saldo_atual * (taxa_juros / 100)     
    saldo_atual = (saldo_atual + valor_mensal) + juros 
    print(f"{contador}°mês: {saldo_atual:.2f} reais.")
    contador = contador + 1 
 