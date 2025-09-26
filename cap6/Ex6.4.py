'''
O que acontece quando não verificamos se a lista está vazia antes de chamarmos o método pop?
Quando não tiver mais clientes para atender o programa vai dar erro.
'''
#Programa 6.7 (Livro)

ultimo = 10
fila = list(range(1, ultimo + 1))

while True:
    print(f"\nExistem {len(fila)} clientes na fila.")
    print(f"Fila atual: {fila}")
    print("Digite F para adicionar um cliente ao fim da fila")
    print("ou A para realizar o atendimento. S sair.")
    
    operação = input("Operação (F, A ou S)").lower()
    if operação == "a":
        if len(fila) > 0:
            atentido = fila.pop(0) #->retorna o valor do elemento e o exclui da fila
            print(f"Cliente {atentido} atendido.")
        else:
            print("Fila vazia! Nimguém para atender.")
    elif operação == "f":
        ultimo += 1 #Incrementao ticket do novo cliente
        fila.append(ultimo)
    elif operação == "s":
        break
    else:
        print("Operação inválida! Digite apenas F, A ou S")
 
