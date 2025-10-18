'''
Escreva um programa que compare duas listas. Utilizando operações com conjuntos, imprima:
- a) os valores comuns às duas listas.
- b) os valores que só existem na primeira 
- c) os valores que existem apenas na segunda 
- d) uma lista com os elementos não repetidos das duas listas.
- e) a primeira lista sem os elementos repetidos na segunda lista.
'''

lista1 = set([3, 4, 8, 9, 10])
lista2 = set([1, 2 ,3 ,4, 5, 7])

print("a)")
print(lista1 & lista2)

print("b)")
print(lista1 - lista2)

print("c)")
print(lista2 - lista1)

print("d)")
print(list(lista1|lista2))

print("e)")
print(lista1 - lista2)
