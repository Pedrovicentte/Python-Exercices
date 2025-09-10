'''
Peça ao usuário uma frase.
Conte quantas vezes cada palavra aparece e guarde os resultados em um dicionário.
'''
# Pede uma frase ao usuário
frase = input("Digite uma frase: ")

# Quebra a frase em palavras (separadas por espaço)
palavras = frase.split()

# Cria um dicionário vazio para armazenar as contagens
contagem = {}

# Percorre cada palavra
for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1  # Se já existe, soma 1
    else:
        contagem[palavra] = 1   # Se não existe, cria com valor 1

# Mostra o resultado
print("Contagem de palavras:")
for chave, valor in contagem.items():
    print(f"{chave}: {valor}")
'''
dicionario ={



frase = input("Digite uma frase: ")
palavras = frase.split()

for chave in frase:
  dicionario[chave] = frase
  dicionario[chave] = 1
  qtd_palavras = dicionario.get(chave)
  if qtd_palavras in dicionario:
      dicionario[chave] += 1
  else:
      dicionario[chave] + 1
print(dicionario)
 
'''


