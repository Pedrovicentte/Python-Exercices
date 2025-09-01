'''
Escreva um programa que calcule o tempo de uma viagem de carro.
Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
'''

distancia = int(input("Qual a distância a ser percorrida?\nEm KM/H: "))
velcidade_media = int(input("Qual a velocidade média?\nEm KM/H: "))

tempo = distancia/velcidade_media

print(f"O tempo estimado é de {tempo:0.0f} horas.")