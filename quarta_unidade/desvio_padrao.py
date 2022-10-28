sequencia1 = input().split()
sequencia2 = input().split()

#calcula a media de cada sequencia
soma1 = soma2 = 0
for s in range(len(sequencia1)):
    soma1 += float(sequencia1[s])
for s in range(len(sequencia2)):
    soma2 += float(sequencia2[s])

if soma1 == 0: media1 = 0
if soma1 > 0:
    media1 = soma1 / len(sequencia1)
if soma2 == 0: media2 = 0
if soma2 > 0:
    media2 = soma2 / len(sequencia2)

#calcula a diferenca entre cada elemento da sequencia e a media e eleva o resultado a quadrado, alocando o quadrado a uma lista
quadrados_das_diferencas1 = []
for v in range(len(sequencia1)):
    diferenca = float(sequencia1[v]) - media1
    quadrado = diferenca * diferenca
    quadrados_das_diferencas1.append(quadrado)

quadrados_das_diferencas2 = []
for v in range(len(sequencia2)):
    diferenca = float(sequencia2[v]) - media2
    quadrado = diferenca * diferenca
    quadrados_das_diferencas2.append(quadrado)

#soma os valores dos quadrados das diferencas
soma_dos_quadrados1 = 0
for l in range(len(quadrados_das_diferencas1)):
    soma_dos_quadrados1 += quadrados_das_diferencas1[l]

soma_dos_quadrados2 = 0
for l in range(len(quadrados_das_diferencas2)):
    soma_dos_quadrados2 += quadrados_das_diferencas2[l]

#divide a soma dos quadrados de cada sequencia pelo tamanho da sequencia menos um e calcula a raiz quadrada obtendo o resultado final.
if len(sequencia1) != 1:
    desvio1 = (soma_dos_quadrados1 / (len(sequencia1) - 1)) ** 0.5
if len(sequencia1) == -1: desvio1 = 0
if len(sequencia2) != 1:
    desvio2 = (soma_dos_quadrados2 / (len(sequencia2) - 1)) ** 0.5
if len(sequencia2) == 1: desvio2 = 0
#saida
if desvio1 > desvio2:
    saida = f"A sequência 1 possui o maior desvio padrão ({desvio1:.2f})."
elif desvio1 < desvio2:
    saida = f"A sequência 2 possui o maior desvio padrão ({desvio2:.2f})."
elif desvio1 == desvio2:
    saida = f"As sequências possuem o mesmo desvio padrão ({desvio1:.2f})."

print(saida)




