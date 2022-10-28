def espacos_por_virgula(frase, indice_i, indice_j):
    resposta = ''
    for c in range(indice_i, indice_j):
        if c == indice_j-1:
            if frase[c] == ' ':
                resposta += ','
            else:
                resposta += frase[c]
        else:
            if frase[c] == ' ':
                resposta += ',' + ' '
            else:
                resposta += frase[c] + ' '

    return resposta


frase = input()
indice_i = int(input())
indice_j = int(input())

print(espacos_por_virgula(frase, indice_i, indice_j))
