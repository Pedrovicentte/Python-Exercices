'''
Modifique o exemplo para pesquisar 2 valores.
Em vez de apena p leia outro valor v que também será procurado.
Na impressão, indique qual dos valores foi achado primeiro.
'''

L = [15, 7, 27, 39]
print(L)
p = int(input("Digite o valor a procurar: \n"))
v = int(input("Digite outro valor a procurar: \n"))
print("---------------------------------")

posi2 = -1
posi = -1
x = 0
while x < len(L):
    if L[x] == p:
        posi = x
    if L[x] == v:
        posi2 = x
    x+=1
    
if posi < posi2:
    print(f"{p} achado primeiro.")
    print("---------------------------------")
else:
    print(f"{v} achado primeiro.")
    print("---------------------------------")