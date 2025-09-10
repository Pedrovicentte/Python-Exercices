'Escreva um expressão para determinar se uma pessoa deve ou não pagar imposto. Considere que pagam'
'imposto pessoas cujo salário é maior que R$1.200,00'

salario = 1100 
imposto = 1200

valor_pago = salario > imposto or salario < imposto

print("Eu pago imposto?")
print(valor_pago)