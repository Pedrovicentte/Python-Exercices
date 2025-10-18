palavras = input("Digite sua frase:\n")

frase = palavras

dict = {}

for letra in frase:
    if letra in dict:
        dict[letra] += 1
    else:
        dict[letra] = 1
print(dict)

''''''