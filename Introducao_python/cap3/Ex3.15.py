'''
Escreva um programa para calcular a redução do tempo de vida de um fumante. 
Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
Considere que um fumante de cigarros perde 10 min de vida a cada cigarro e 
calcule quantos dias de vida um fumante perderá.
Exiba o total em dias.
'''

qtd_cig_dia = int(input("Quantos cigarros você fuma por dia? "))
qtd_anos_fumou = int(input("Quantos anos você fuma? "))

total_cigarros = qtd_cig_dia * qtd_anos_fumou * 365
tempo_perdido = total_cigarros * 10
dias_perdidos = (tempo_perdido/60)/24

print(f"Você perdeu aproximadamente {dias_perdidos:.0f} dias de vida.")
