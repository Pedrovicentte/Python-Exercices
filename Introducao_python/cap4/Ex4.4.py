'''
Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
Para salários superiores a R$ 1.250,00 calcule um aumento de 10%. 
Para os infeiores ou iguais, de 15%.
'''
salario = float(input("Qual seu salário?\n"))
aumento = 0
if salario > 1250:
    aumento = salario * 0.10
    print(f"Seu aumento foi de 10%, seu salário agora é de {aumento + salario}")
else:
    aumento = salario * 0.15
    print(f"Seu aumento foi de 15%, seu salário agora é de {aumento + salario}")
