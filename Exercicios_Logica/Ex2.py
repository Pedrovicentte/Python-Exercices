print("----|Transformador de temperatura|----")
print("Qual temperatura você deseja transformar:\n" \
"           Digite F para F -> C° \n" \
"           Digite C para C -> F° \n")

tipo = input("Tipo: ")
temp = int(input("Qual a temperatura: "))

if (tipo == "F" or tipo == "f"):
    fah = (temp - 32) * 5 / 9
    print("A temperatura atual é: ", round(fah, 2), "graus F°.")
elif(tipo == "C" or tipo == "c"):
    cel = 9/5 * temp + 32
    print("A temperatura atual é: ", round(cel, 2), "graus C°.") 
else:
    print("[ERRO] - Tipo ou Temperatura inválidos.")
print("-------------------------------------")