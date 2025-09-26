'''
Modifique o programa 6.6 usando for.
Explique por que nem todos os while podem ser transformados em for.
'''

L = []

while True:
    n = int(input("Digite um número (0 sai): "))
    if n == 0:
        print("Programa finalizado!")
        break
    L.append(n)
    for x in L:
        print(L)

# Nem todos os whiles precisam ser removidor por que só um percorre a lista,
# o primeiro so faz um loop infinito.

