'''
Reescreva o programa anterior para escrever os 10 primeiros multiplos de 3.
'''

fim = int(input("Digite ate que número quer contar: "))
x = 3
contador = 0
while x <= contador:# faz o loop para contar de fim(valor do usuario) ate x 
    if fim % 3 == 0: # verifica se o numero é multiplo de 3
        contador = contador + 1 
        print(fim)
    x = x + 1
