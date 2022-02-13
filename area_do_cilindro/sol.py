# Programação 1 2021.1e
# Discente: Raniel Miranda Dourado - 121110466
# Exercício: xxxx
from math import pi

#Entradas
print("Cálculo da Superfície de um Cilindro\n---")
diametro = float(input("Medida do diâmetro? "))
altura = float(input("Medida da altura? "))
print("---")

#Operações

area = (((pi * (diametro / 2) ** 2 ) * 2) + (altura * (pi * 2 * (diametro / 2))) )

#Saída
print(f"Área calculada: {area:.2f}")
