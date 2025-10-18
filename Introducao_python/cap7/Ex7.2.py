'''
Escreva um programa que leia duas strings e gere uma terceira com os 
caracteres comuns às duas strings lidas.

1° string: AAACTBF
2° string: CBT

Resultado: CBT
'''

string1 = 'AAACTBF'
string2 = 'CBT'
caracteres_comuns = set(string1) & set(string2)

string_resultante = ""

for caractere in string2:
    if caractere in caracteres_comuns and caractere not in string_resultante:
        string_resultante += caractere

print(string_resultante)