'''
Reesceva o Programa 5.1 de forma a contunuar executando até que o valor digitado seja 0.
Utilize repetições aninhadas.
'''


cedulas = 0
atual = 100


while True:
   valor = int(input("Digite o valor a pagar: "))
   apagar = valor
   if valor == 0:
        print("Programa finalizado.")
        break
   while valor > 0:
    if atual <= apagar:
      apagar -= atual
      cedulas += 1
    else:    
      print(f"{cedulas} cédula(s) de R${atual}")
      if apagar == 0:
        break
      if atual == 100:
         atual = 50
      elif atual == 50:
         atual = 20
      elif atual == 20:
         atual = 10
      elif atual == 10:
         atual= 5
      elif atual == 5:
         atual = 1 
      cedulas = 0
   