soma = 0
for numeros in range(3):
    numero = float(input())
    soma += numero

n = float(input())

media = soma / 3

diferenca = n - media

print(f"{diferenca:.1f}")


