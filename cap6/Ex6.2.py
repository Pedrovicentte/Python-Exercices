'''
Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras.
'''
lista_a = []
lista_b = []
lista_c = []

x = 0
while x < 3:    
    n= int(input("Digite 3 valores: "))
    if n == 0:
        break
    lista_a.append(n)
    x+=1

x = 0
while x < 3:
     x = 3
     n= int(input("Digite mais 3 valores: "))
     if n == 0:
        break
     lista_b.append(n)
     x+=1

lista_c = lista_a + lista_b
print(lista_c)