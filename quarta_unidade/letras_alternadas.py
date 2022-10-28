palavra = input()

saida = ''
for c in range(0, len(palavra), 2):
    saida += palavra[c]

print(saida)
