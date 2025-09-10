'''
Reescreva o programa anterior para escrever os 10 primeiros multiplos de 3.
'''

fim = int(input("Digite até que número quer contar: "))
x = 1
contador = 0

while x <= fim and contador < 10:   # roda até o número final ou até achar 10 múltiplos
    if x % 3 == 0:                  # verifica se é múltiplo de 3
        print(x)                    # printa na tela
        contador += 1               # aumenta a contagem de múltiplos
    x += 1                          # passa para o próximo número


 