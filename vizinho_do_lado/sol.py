# Programação 1 2021.1e
# Discente: Raniel Miranda Dourado - 121110466
# Exercício: Vizinho da direita igual

#Entradas
sequencia = input()
sequencia = sequencia.split(" ")

#Operações
count = 0

for n in range(len(sequencia)-1):
    n = int(n)
    if (sequencia[n] == sequencia[(n+1)]):
       count += 1
#Saída
print(count)
