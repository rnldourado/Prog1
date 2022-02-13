# Programação 1 2021.1e
# Discente: Raniel Miranda Dourado - 121110466
# Exercício: Calcula ingresso do cinema

#Entradas
num_adultos = int(input())
num_criancas = int(input())
valor_ingresso = float(input())

#Operações
total = (num_adultos * valor_ingresso) + (num_criancas * (valor_ingresso / 2 ))

#Saída
print(f"Total: R$ {total:.2f}")
