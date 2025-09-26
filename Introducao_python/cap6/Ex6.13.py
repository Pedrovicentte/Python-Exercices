'''
A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista
T = [-10, -8, 0, 1, 2, 5, -2, -4]
Faça um programa que imprima a menor e a maior temperatura, assim como a temperatura média.
'''
L = [-10, -8, 0, 1, 2, 5, -2, -4]

menor = L[0]
maior = L[0]
soma = 0

for e in L:
    soma += e
    media = soma / len(L)
    if e > maior:
        maior = e
    elif e < menor:
        menor = e
print(f"Temperaturas: {L}")
print(
    f"Maior temperatura: {maior}"
    f"\nMenor temperatura: {menor}"
    f"\nMédia das temperaturas: {media}"
)
