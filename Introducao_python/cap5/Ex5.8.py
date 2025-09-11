'''
Escreva um program que leia dois números.
Imprima o resultado da multiplicação do primeiro pelo segundo.
Utilize apenas os operadores de soma e subtração para calcular o resultado.
Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles.
Assim 4 x 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4
'''

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
res = 0
cont = 1

while cont <= n1:
    res = res + n2
    print(res)
    cont = cont + 1