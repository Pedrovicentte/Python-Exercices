'''
Faça um programa que leia uma expressão com parênteses.
Usando pilhas, verifique se os parênteses foram abertos e fechados na ordem correta.
EXEMPLO:
        (())        OK
        ()()(()())  OK
        ())         ERRO
Você pode adicionar elementos à pilha sempre que encontrar abre parênteses e desempilhá-la a cada fecha de parenteses.
Ao desempilhar, verifiuqe se o topo da pilha é um abre parênteses.
Se a expressão estiver correta, sua pilha estará vazia no final.
'''

parenteses = list(input("Leia os pareneteses: \n"))
pilha = []
x = 0
while x < len(parenteses):
    if parenteses[x] == "(":   
        pilha.append("(")
        print(pilha)
    elif len(pilha) == 0:
        print("[ERRO] Pilha Vazia")
        break
    elif parenteses[x] == ")":  
        pilha.pop(-1)
        print(pilha) 
    x+=1
