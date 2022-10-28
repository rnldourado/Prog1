lista_de_lucros = []
for c in range(12):
    entradas_e_saidas = input().split()
    lucro = float(entradas_e_saidas[0]) - float(entradas_e_saidas[1])
    lista_de_lucros.append(lucro)

lista_de_meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']

for saida in range(12):
    if lista_de_lucros[saida] >= 0:
        print(f"{lista_de_meses[saida]}  {lista_de_lucros[saida]:.1f}")
    else:
        print(f"{lista_de_meses[saida]} {lista_de_lucros[saida]:.1f}")

