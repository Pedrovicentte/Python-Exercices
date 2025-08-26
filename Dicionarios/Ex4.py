'''
Peça ao usuário uma frase.
Conte quantas vezes cada palavra aparece e guarde os resultados em um dicionário.
'''


dicionario ={

}

frase = input("Digite uma frase: ").split()
for chave in frase:
  dicionario[chave] = frase
  dicionario[chave] = 1
  qtd_palavras = dicionario.get(chave)
  if qtd_palavras in dicionario:
      chave += 1
  else:
      chave + 1
print(dicionario)
 



