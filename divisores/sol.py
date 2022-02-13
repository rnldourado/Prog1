# Programação 1 2021.1e
# Discente: Raniel Miranda Dourado - 121110466
# Exercício: divisores

#Entradas
num = int(input())

#Operações


for divisores in range(1,num):
    if num % divisores == 0:
        print(divisores)
