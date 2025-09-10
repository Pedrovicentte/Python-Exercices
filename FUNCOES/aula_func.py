def minha_funcao():
    nome = "cu preto"
    idade = 32
    print(f"Esta é a minha função!,Prazer {nome}! Sua idade é {idade} anos.")

#Parametro é o que a funcao recebe
#Argumentos é o que a gente envia para a função

def somar (n1, n2):
    resultado = n1 + n2
    #print(f"A soma de {n1} + {n2} é {resultado}")
    return resultado

resultado_soma = somar(5, 10)
print(resultado_soma)

def saudacao(nome):
    print(f"Olá, {nome}! Seja bem-vindo(a)!")


def vericar_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

def soamr_lista(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado
#soma_da_lista = soamr_lista(1, 2, 3, 4, 5, 6, 7, 8, 9)
#print(f"A soma da lista é {soma_da_lista}")

def calcular_media(*notas):
    qtd = len(notas)
    soma = 0
    for nota in notas:
        soma += nota
    media = soma / qtd
    return media
#resultado = calcular_media(8, 7, 9, 6, 10)
#print(f"A média é {resultado}")

def informacoes_pessoais(**informacoes):
    for chave, valor in informacoes.items():
        print(f"{chave}: {valor}")

informacoes_pessoais(nome="João", idade=30, cidade="São Paulo")