''''
Escreva um programa que leia a quantidade de dias,horas ,minutos e seguntos do usuário.Calcule o total em segundos.

'''

dias = int(input("Quantos dias? "))
horas = int(input("Quantas horas? "))
min = int(input("Quantos minutos? "))
seg = int(input("Quantos segundos? "))

total_dias = dias*86400
total_horas = horas*3600
total_min = min*60
total_sec = total_dias + total_horas + total_min + seg

print(f"O total do tempo em segundos é {total_sec} segundos.")