'''
Escreva uma programa que leia duas strings. 
Verifique se a segunda ocorre dentro da primeira e imprima a posição de início.
1° string: AABBEFAATT
2° string:  BE

Resultado: BE encontrado na posição 3 de AABBEFAATT.
'''

s = 'AABBEFAATT'
j = 'BE'

print(f"{j} Encontrado na posição {s.rfind(j)} de {s}")
