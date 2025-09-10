'''
Modifique o programa anterior (mostrado no livro) para imprimir de 1 até o numero digitado pelo usuario,
mas, dessa vez apenas os numeros ímpares.
'''

fim = int(input('Digite um numero: '))
x = 1
while fim > x:
    if x % 2 == 1:
        print(x)
    x = x + 1