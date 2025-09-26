'''for t in range(3, 33, 3):
    print(t, end='') # end faz com que o resultado da expressão nao pule de linha
print()
'''

'''L = list(range(100, 1100, 50))
print(L)
'''
'''L = [5, 9, 13]

for x, e in enumerate(L):
    print(f"[{x}] {e}")'''

'''lugares_vagos = [10, 2, 1, 3, 0]
while True:
    sala = int(input("Sala (0 sai): "))
    if sala == 0:
        print("Fim")
        break
    if sala > len(lugares_vagos) or sala < 1:
        print("Sala Inválida")
    elif lugares_vagos[sala - 1] == 0:
        print("Desculpe, sala lotada!")
    else:
        lugares = int(input(f"Quantos lugares você deseja ({lugares_vagos[sala - 1]})"))
        if lugares > lugares_vagos[sala - 1]:
            print("Esse número de lugares não está disponível!")
        elif lugares < 0:
            print("Numero Inválido")
        else: 
            lugares_vagos[sala - 1] -= lugares
            print("Lugares vendidos")
print("Utilização das salas")
for x, l in enumerate(lugares_vagos):
    print(f"Sala {x + 1} - {l} lugar(es) vazio(s)")'''

'''
# Programa 6.15
L = ["maças", "peras", "kiwis"]
for s in L:
    for letra in s:
        print(letra)'''

'''
#Programa 6.20
L = [7, 4, 3,12,8]

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
'''
L = [6, 4, 2, 1, 9]
L.sort()
print(L, sorted(L))