'''
Escreva um programa que pergunte a distancia que um passageiro deseja em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200km
e, R$ 0,45 para viagens mais longas.
'''

distancia = int(input("Qual a distancia a ser viajada? (EM KM/H)\n"))

if distancia <= 200:
    valor = distancia * 0.50
    print(f"O valor desta viagem é de {valor}")
else:
    valor = distancia * 0.45 # 
    print(f"O valor total é R${valor:0.2f} reais.")