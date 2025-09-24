parenteses = list(input("Leia os pareneteses: \n"))
pilha = []
x = 0
while x < len(parenteses):
    if parenteses[x] == "(":   
        pilha.append("(")
        print(pilha)
    elif len(pilha) == 0:
        print(pilha)
        print("[ERRO] Pilha Vazia")
        break
    else:  
        pilha.pop(-1)
        print(pilha)   
    x+=1

'''
    if execucaçao == "a":  
        if parenteses[-1] == "(":
            parenteses.append(")")
        elif parenteses[-1] == ")":
            parenteses.append("(")
'''