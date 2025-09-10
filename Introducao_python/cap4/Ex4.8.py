'''
Escreva um programa que leia dois números e qye pergunte qual operação você deseja realizar.
Você deve calcular a soma(+), subtração(-), multiplicação(*) e divisão(/).
Exiba o resultado da operação solicitada.  
'''
n1 = float(input("Digite um número: "))
n2 = float(input("Digite um número: "))
operador = input("Qual tipo de operação deseja fazer?\n" \
"(+) soma - (-)subtração - (*)multiplicação - (/)divisão\n")

if operador == '+':
    res = n1 + n2
elif operador == '-':
    res = n1 - n2
elif operador == '*':
    res = n1*n2
elif operador == '/':
    res = n1 / n2
else:
    print("[ERRO] Digite um operador válido!")

print(f"O resultado da operação é {res:.2f}.")

