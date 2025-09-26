'''
O que acontece quando dois valores são iguais?
Rastreie o Programa 6.20, mas com a lista l = [3, 3, 1, 5, 4]
'''
# O programa repete o mesmo valor 2 vezes

L = [3, 3, 1, 5, 4]

fim = 5

while fim > 1:
    trocou: False
    x = 0
    while x < (fim-1):
        if L[x] > L[x + 1]:
            trocou = True
            temp = L[x]
            L[x] = L[x + 1]
            L[x + 1] = temp
        x+= 1
    if not trocou:
        break
    fim -=1
for e in L:
    print(e)