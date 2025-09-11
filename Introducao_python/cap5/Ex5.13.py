'''
Escreva um programa que pergunte o valor inicial de uma divida e o juros mensal.
Pergunte também o valor mensal que será pago. 
Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago.
'''

divida_inicial = int(input("Qual o valor inicial da dívida?\n"))
juros_mensal = int(input("Qual o juros mensal?\n"))
valor_pago = int(input("Qual o valor a ser pago?\n"))

divida = divida_inicial # Acumulador da divida
total_juros = 0         # Acumulador do juros
total_pago = 0          # Acumulador do valor total
meses = 0

while divida > 0:                       # O programa executa enquanto a divida for maior que 0
    juros = divida * (juros_mensal/100) # Calcula a quantidade de juros dentro da divida inicial
    if valor_pago < juros:              # Verifica se o valor pago vai ser maior que o juros e retorna um alerta
        print("[ERRO] Juros maiores que o pagamento!")
        break 
    divida =  divida + juros - valor_pago # Calcula a divida com o juros e já retira o valor pago
    total_juros = total_juros + juros     # Calcula o total de juros 
    if divida <= valor_pago:              # Identifica se o valor da divida é menor que o total a pagar   
        total_pago = total_pago + divida  # Soma so o restante em vez do valor completo  
    else:                           
        total_pago = total_pago + valor_pago  # Calcula normalmente se for maior
    meses = meses + 1                         # Conta em quantos meses a divida vai ser paga

print(f"Total Pago: R${total_pago:.2f}")
print(f"Total de Juros Pago: R${total_juros:.2f}")
print(f"Total de Meses: {meses} meses.")

