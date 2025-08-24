'''
Crie um dicionário com 3 alunos e suas notas.
Calcule e mostre a média das notas.
'''

notas = {
    "Jonas": 10, 
    "GigaChad":  6 ,
    "Paudura123": 3 
}

media_notas = sum(notas.values())/3
#media_notas = (notas["primeiro aluno"] + notas["segundo aluno"] + notas["terceiro aluno"]) / 3
print(f"A média dos 3 alunos é {media_notas:.2f}.")
print(f"Alunos: {notas.keys()}")