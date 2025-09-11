'''
Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
O programa deve perguntar o valor da casa a comprar, salário e a quantidade de anos a pagar.
O valor da prestação mensal não pode ser superior a 30% do salário.
Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo numero de meses a pagar.
'''

valor_imovel = int(input("Qual o valor da casa que quer comprar? \n"))
salario = float(input("Qual seu salário?\n"))
anos_pagar = int(input("Qual a quantidade de anos a se pagar?\n"))

meses_totais = anos_pagar * 12 # transforma anos em meses
parcela_total = valor_imovel / meses_totais 
salario_sup = (30/100)*salario # faz o calculo pra ver o valor do salario sendo 30%


if parcela_total > salario_sup: # ve se a parcela é maior que 30% do salário
    print(f"Valor de R${salario_sup} não acessível ao cliente. Superior a 30% do salário.")
else:
    print(f"O total de parcelas é de {meses_totais} e o valor é de R${parcela_total:.2f} por mes.")