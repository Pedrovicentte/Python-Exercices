'''
Modifique o programa anterior de forma que o usuário também digite o início
e o fim da tabuada, em vez de começar com 1 e 10.
'''

n = int(input("Tabuada de: "))
inicio = int(input("Inicio: "))
fim  = int(input("fim: "))

cont = inicio

while cont <= fim:
     print(f"{n}x{cont} = {n*cont}")
     cont = cont + 1