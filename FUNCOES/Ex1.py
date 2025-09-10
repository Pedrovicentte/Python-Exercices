'''
Crie uma função que receba um numero, e faz um contador regressivo 
a partir dele. 
Exemplo: Se o numero for 5, a função deve imprimir na tela: 
5, 4, 3, 2, 1 0.
'''
print("-----sem input-----")
def contador_regressivo(valor_recebido):
    for i in range(valor_recebido, -1, -1):
        resultado = i
        print(resultado)
    return resultado
contador_regressivo(5)
print("-----com input-----")
valor = int(input("Digite um valor: "))
cont = []

def contador(valor):
    for c in range(valor, -1, -1):
        cont.append(c)
    return cont
resp = contador(valor)
print("Contando...", resp)