n1 = float(input("Escreva um valor: ")) 
n2 = float(input("Escreva outro valor: ")) 

print("Selecione o calculo que deseja fazer: \n" \
"         + - adição \n" 
"         - - subtração\n" \
"         / - divisão\n" \
"         * - multiplição")
tipo = input("Tipo: ")

if (tipo == "+"):
    s = n1 + n2
elif(tipo == "-"):
    s = n1-n2
elif(tipo == "/"):
    s = n1/n2
elif(tipo == "*"):
    s = n1*n2
else:
    ("[ERRO] - Valor inválido")
print("O valor da operação é ", s)