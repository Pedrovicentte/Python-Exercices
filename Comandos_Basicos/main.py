'''
----INPUT----

#nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade "))
peso = float(input("Digite seu peso: "))
print(nome)
print(type(idade))
print(type(peso))

----OPERADORES----

soma = 1 + 1
multiplicacao = 4 * 4
divisao = 30 / 2
potencia = 7 ** 2

print("soma: ", soma)
print("multiplicação: ", multiplicacao)
print("divisao: ", divisao)
print("potencia: ", potencia)

----CONDICIONAIS----

idade = int(input("Informe sua idade: "))

if idade >= 18:
    print("PERMITIDO")
else:
    print("BLOQUEADO")

-------------------------

----LAÇOS DE REPETIÇÃO----

notas = []

for x in range(2):                      <- Le a quantidade de alunos
    codigo_aluno = int(input("RM: "))   <- matriculo do aluno
    nota = float(input("Nota: "))       <- nota do aluno
    resultado = [codigo_aluno, nota]    <- coloca a matricula e nota dentro do resultado
    notas.append(resultado)             <- coloca o resultado dentro da lista

print("Quantidade de notas", len(notas))

for n in notas:
    codigo_aluno= n[0]  <- le os elentos de codigo aluno iniciando em [0]
    nota = n[1]         <- le os elentos de nota iniciando em [1]
    print("O RM", codigo_aluno, "tirou", nota)

notas = []

contador = 1

while contador <= 5:
    codigo_aluno = input("RM:")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)
    contador+=1

print("Quantidade de Notas", len(notas))

for n in notas:
    codigo_aluno =n[0]
    nota = n[1]
    print("O RM", codigo_aluno, "tirou", nota)

-----------------------------------------------------    

----DICIONÁRIOS----
 

pessoa = {

    "nome": "Programador Python",
    "idade": 21,
    "peso": 54.6
}

print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['peso'])

----------------------------

----FUNÇÕES----
    '''

def minha_funcao(valor1, valor2):
    return valor1 + valor2

resposta = minha_funcao(10,10)
print("resposta", resposta)