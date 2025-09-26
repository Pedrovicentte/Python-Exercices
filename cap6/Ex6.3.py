'''
Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.
'''

lista1 = [1,2,3,4,5]
lista2 = [4,5,6,7,8]
lista3 = []

x = 0
while x < len(lista1):
 lista1[x] # lendo cada valor da lista1 na posição x 
 lista3.append(lista1[x])
 x+=1

x = 0
while x < len(lista2):
 if lista2[x] not in lista3: #Se o elemento da lista2 na posição x não estiver dentro da lista3,     
    lista3.append(lista2[x]) # então adiciona ele.      
 x+=1
print(lista3)


