'''
Altere o programa 6.11 de forma a imprimir o menor elemento da lista.
'''

L = [1, 7, 2, 4]

minimo = L[0]

for e in L:
    if e < minimo:
        minimo = e
print(minimo)
