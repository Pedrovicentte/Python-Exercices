'''
Escreva um programa uqe pergunte a velocidade do carro de um usuário. Caso ultrapasse 80km/h,
exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$5
por Km acima de 80km/h.
'''

velocidade = int(input("Qual é sua velocidade atual?\nVelocidade da via 80km/h\n"))
#Pega a velocidade permitida da via e ve quantos km ele ultrapassou
velocidade_permitida = velocidade - 80
multa = 0

if velocidade < 80:
    print("Você está na velocidade correta!")
if velocidade > 80:
    multa = velocidade_permitida * 5
    print("Você está acima da velocidade e foi multado")
    print(f"Sua multa é de R${multa}.")