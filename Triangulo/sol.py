# Programação 1 2021.1e
# Discente: Raniel Miranda Dourado - 121110466
# Exercício: Triangulo
import math
#Entradas
a = float(input())
b = float(input())
c = float(input())
#Operações
if(math.fabs(b - c)< a and (b + c) > a) and (math.fabs(a - c)< b and (a + c) > b) and (math.fabs(a - b)< c and (b + a) > c):
   print(f"triangulo valido. {(a+b+c):.0f}")
else:
    print("triangulo invalido.")

#Saída
