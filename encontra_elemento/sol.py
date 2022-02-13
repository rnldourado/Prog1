# Programação 1 2021.1e
# Discente: Raniel Miranda Dourado - 121110466
# Exercício: Encontra elemento

#Entradas
n = int(input())
sequencia = input()

#Operações
lista = sequencia.split(" ")
has_number = False

for x in lista:
    if n == int(x):
        has_number = True

#Saída
if has_number:
    print("sim")
else:
    print("não")
