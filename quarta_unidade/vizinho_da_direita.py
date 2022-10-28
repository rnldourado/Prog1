numeros = input()

numeros = list(numeros)
igual = 0
numeros_sem_espaco = list()

for s in range(0, len(numeros)):
    if numeros[s] != ' ':
        numeros_sem_espaco += numeros[s]

for s in range(0, len(numeros_sem_espaco)):
    if (s + 1) < len(numeros_sem_espaco) and numeros_sem_espaco[s] == numeros_sem_espaco[s + 1]:
        igual += 1

print(igual)
