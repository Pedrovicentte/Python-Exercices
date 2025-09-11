'''
Escreva um programa que leia números inteiros do teclado.
O programa deve ler os números até que o usuário digite 0 (zero).
No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritimética.
'''
soma = 0
num_digitados = 0
media = 0


while True:
    num_digitados += 1
    num = int(input("Digite números: "))
    if num == 0:
        num_digitados -= 1
        print("Programa finalizado!")
        break
    soma += num
    media = soma / num_digitados

print(f"Digitados: {num_digitados}")
print(f"Soma: {soma}")
print(f"Média: {media}")