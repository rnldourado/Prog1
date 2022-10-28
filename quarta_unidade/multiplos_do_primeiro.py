numero_de_referencia = int(input())
soma_multiplos = 0
for num in range(10):
    numero = int(input())
    if numero % numero_de_referencia == 0:
        soma_multiplos += numero

print(soma_multiplos)
