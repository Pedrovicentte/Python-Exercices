'''
    Escreva uma expressão que será utilizada para decidir se um aluno foi aprovado ou não aprovado. Para ser 
    aprovado, todas as médias do aluno devem ser maiores que 7.Considere que o aluno curso apenas tres matérias, e que 
    a nota de cada uma está armazenada nas seguintwa variáveis: matéria1, matéria2 e matéria3.
'''

materia1 = 10
materia2 = 8
materia3 = 8

resltado = materia1 > 7 and materia2 > 7 and materia3 > 7

print("O aluno está aprovado?")
print(resltado)