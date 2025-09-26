'''
Modifique o programa anterior do Exercício 6.9 de forma a pesquisar
p e v em toda lista e informando o usuário a posição onde p e a posição 
onde v foram encontrados.
'''

L = [15, 7, 27, 39]
print(L)
p = int(input("Digite o valor                         a procurar: \n"))
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

if posi:
    print(f"{p} achado na posição {posi}.")
    print(f"{v} achado na posição {posi2}.")
    print("---------------------------------")
else:
    print(f"{p} não encontrado.")
    print(f"{v} não encontrado.")
    print("---------------------------------")


if posi < posi2:
    print(f"{p} achado primeiro, na posição {posi}")
    print("---------------------------------")
else:
    print(f"{v} achado primeiro, na posição {posi2}")
    print("---------------------------------")