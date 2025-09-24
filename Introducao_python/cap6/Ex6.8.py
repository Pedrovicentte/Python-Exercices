'''
Modifique o primeiro exemplo (no livro) de forma a realizar a mesma tarefa, mas
sem utilizar a variavel achou. 
Dica: observe a saida do while.
'''

L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar: "))
achou = 0
x = 0
while x < len(L):
    if L[x] == p:
        achou = x
        break
    x+=1

if achou:
    print(f"{p} achado na posição {x}.")
else:
    print(f"{p} não encontrado.")