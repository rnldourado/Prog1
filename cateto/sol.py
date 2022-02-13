# Programação 1 2021.1e
# Discente: Raniel Miranda Dourado - 121110466
# Exercício: Cateto

#Entradas
hipotenusa = float(input("hipotenusa? "))
cateto = float(input("cateto? "))
#Operações
cateto2 = ( (hipotenusa ** 2) - (cateto**2) ) ** 0.5

#Saída
print(f"hipotenusa: {hipotenusa:.2f}\ncateto 1: {cateto:.2f}\ncateto 2: {cateto2:.2f}")
