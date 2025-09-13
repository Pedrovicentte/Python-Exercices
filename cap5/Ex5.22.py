'''
Escreva um programa que exiba um a lista de opções(menu):
adição, multiplicação, divisão, subtração e sair.
Imprima a tabuada da operação escolhida.
Repita até que a opção saida seja escolhida.
'''

while True:
     contador = 0 
     tabuada = 0
     opr = input("Digite a opção desejada: \n"
     "|+ - adição|- subtração|/ - divisão|* multiplicação| 0 - sair\n")
     if opr == "0":
        print("Programa finalizado!")
        break
     elif opr != "+" and opr != "-" and opr != "/" and opr != "*":
        print("[ERRO] Simbolo errado!")
     num = int(input("Qual numero deseja fazer a operação:\n"))
     while tabuada <= 10:
      if opr == "+":   
       print(f"{contador} {opr} {num} = {contador + num}")
      elif opr == "-":   
        print(f"{contador} {opr} {num} = {contador - num}")
      elif opr == "/":   
        print(f"{contador} {opr} {num} = {contador / num}") 
      else:   
        print(f"{contador} {opr} {num} = {contador * num}")      
      tabuada += 1
      contador +=1
