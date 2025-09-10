'''
Crie um dicionário onde as chaves são os nomes das pessoas e os valores são os números de telefone.
Peça para o usuário digitar um nome e mostre o telefone correspondente.
'''


nome_da_agenda = input("Digite o nome que quer ver da Lista: ").lower()

agenda = {
    "joão pires": "(32)97944-5360",
    "pedro lucas": "(31)98369-2018",
    "maria elizabeth": "(32)97967-3201"
}

if nome_da_agenda in agenda:
        print(f"O número de {nome_da_agenda.title()} é {agenda[nome_da_agenda].title()}.")
else:
    print("[ERRO] número não encontrado.")