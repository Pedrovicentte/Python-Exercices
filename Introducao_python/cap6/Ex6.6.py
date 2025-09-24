'''
Modifique o programa para trabalhar com duas filas.
Para facilitar seu trabalho, considere o comando 
    A para atendimento da fila 1 e
    B para atendimento da fila 2.
O mesmo para a chegada de clientes 
    F fila 1
    G para fila 2
'''

ultimo1 = 10
ultimo2 = 10
fila1 = list(range(1, ultimo1 + 1))
fila2 = list(range(1, ultimo2 + 1))
sair = False # Flag de controle

while True:
    print("-------------------------------------------")
    print(f"\nExistem {len(fila1)} clientes na primeira fila.")
    print(f"\nExistem {len(fila2)} clientes na segunda fila.")
    print("-------------------------------------------")
    print(f"Primeira Fila: {fila1}")
    print(f"Segunda Fila: {fila2}")
    print("-------------------------------------------")
    print("Digite F para adicionar um cliente ao fim da primeira fila e B para adicionar um cliente ao fim da segunda fila")
    print("A para realizar o atendimento da primeira fila e G para realizar o atendimento da segunda fila. S sair.")
    if sair == True:                                       
        print("Programa Finalizado")
        break   
    operação = list(input("Operação\n F | Add primeira fila \n A | Atnd Primeira Fila\n B | Add Segunda fila\n G | Atnd Segunda Fila\n S (sair)\n").lower()) 
    print("-------------------------------------------")
    x= 0
    while x < len(operação):    
        # ATENDIMENTO FILA 1
        if operação[x] == "a":
            if len(fila1) > 0:
                atentido = fila1.pop(0) 
                print(f"Cliente {atentido} - 1º fila atendido.")
            else:
                print("Fila vazia! Nimguém para atender.")
        elif operação[x] == "f":
            ultimo1 += 1 
            fila1.append(ultimo1)         
        # ATENDIMENTO FILA 2
        if operação[x] == "b":
            if len(fila2) > 0:
                atentido = fila2.pop(0) 
                print(f"Cliente {atentido} - 2º fila atendido.")
            else:
                print("Fila vazia! Nimguém para atender.")
        elif operação[x] == "g":
            ultimo2 += 1 
            fila2.append(ultimo2)
        elif operação[x] == "s":
            sair = True                                    
            break        
        x+=1