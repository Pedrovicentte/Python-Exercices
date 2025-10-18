'''
Escreva um programa qye compare duas listas.
Considere a primeira lista como a versão inicial e a segunda como a versão após alterações.
Utilizando operações com conjuntos, seu programa deverá imprimir a lista de modificações 
entre essas duas versões .

- a) Os elementos que não mudaram. 
- b) Os novos elementos.
- c) Elementos que foram removidos.
'''

listaX = set(["a","b","c","e", "k"])
listaY = set(["a","b","c","e","f","g","h", "i"])

print("a)")
print(listaX & listaY)

print("b)")
print(listaY - listaX)

print("c)")
print(listaX - listaY)