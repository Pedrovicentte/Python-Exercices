'''
Faça um programa que calcule o aumento de um salário.
Ele deve solicitar o valor do salário e a porcentagem do aumento. 
Exiba o valor do aumento e do novo salário.
'''

salario = int(input("Informe o valor do seu salario: R$ "))
porcento = int(input("Quanto por cento ele vai aumentar? "))

salario_aumento = (porcento/100)*salario
aumento = salario + salario_aumento

print(f"O seu salário aumentou em R$ {salario_aumento:.2f}. Agora seu salário é R${aumento:3.2f} reais.")