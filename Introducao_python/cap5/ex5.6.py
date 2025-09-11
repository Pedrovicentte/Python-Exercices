'''
Aletre o programa anterior (mostrado no livro) para exibir os resultados
no mesmo formato de uma tabuada
'''

n = int(input("Tabuada de: "))
x = 0
while x <= 10:
    print(f"{n}x{x} = {n*x}")
    x = x + 1