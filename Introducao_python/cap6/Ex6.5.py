'''
Altere o Programa 6.7 de forma a poder trabalhar com vários comandos 
digitados de uma só vez.
Atualmente, apenas um comando pode ser inserido por vez.
Altere-o de forma a considerar operação como uma string.

Exemplo: FFFAAAS significaria três chegadas de novos clientes, três atendimentose,
finalmente, a saída do programa.
'''

ultimo = 10
fila = list(range(1, ultimo + 1))
sair = False # Flag de controle

while True:
    print(f"\nExistem {len(fila)} clientes na fila.")
    print(f"Fila atual: {fila}")
    print("Digite F para adicionar um cliente ao fim da fila")
    print("ou A para realizar o atendimento. S sair.")
    if sair == True:                                        # Como a flag mudou de false para true o loop quebra
        print("Programa Finalizado")
        break   
    operação = list(input("Operação (F, A ou S)\n").lower()) # Se o usuario digitar s aqui
    print("____________________________________________")
    x= 0
    while x < len(operação):    
        if operação[x] == "a":
            if len(fila) > 0:
                atentido = fila.pop(0) 
                print(f"Cliente {atentido} atendido.")
            else:
                print("Fila vazia! Nimguém para atender.")
        elif operação[x] == "f":
            ultimo += 1 
            fila.append(ultimo)
        elif operação[x] == "s":
            sair = True                                    # Aqui recebe valor "s" true e muda a flag(sair)
            break
        else:
            print("Operação inválida! Digite apenas F, A ou S")
        x+=1
   