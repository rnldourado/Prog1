sequencia = input().split() 
fator = int(input())

#transformar os elementos da sequencia em inteiros
for s in range(len(sequencia)):
    sequencia[s] = int(sequencia[s])

#analise dos pares
contador = 0
lista_de_pares = []
for v in range(0, len(sequencia)):
    if v < len(sequencia)-1 and (sequencia[v] != 0):
        if (sequencia[v] / sequencia[v+1] == fator) or (sequencia[v+1] / sequencia[v] == fator):
            contador += 1
            lista_de_pares.append(sequencia[v])
            lista_de_pares.append(sequencia[v+1])
        
#saida

print(f"{contador} par(es)")
indice1 = 0
indice2 = 1
for r in range(contador):
    print(lista_de_pares[indice1], lista_de_pares[indice2])
    indice1 += 2
    indice2 += 2

