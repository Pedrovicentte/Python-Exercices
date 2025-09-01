'''
Escreva um programa que converta uma temperatura digitadra em C° em F°.
A formula para esssa conversao é f= 9 * C / 5 + 32
'''

temperatura = float(input("Qual a temeperatura?\nEm Celsius -> Fahrenheit:  "))
conversao = 9 * temperatura / 5 + 32

print(f"A temperatura convertida fica em {conversao} F°")