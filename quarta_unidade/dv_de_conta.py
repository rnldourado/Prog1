numero_principal = input()

soma = 0
for digito in range(len(numero_principal)):
    soma += int(numero_principal[digito])

if soma % 11 == 10:
    digito_verificador = 'X'
else:
    digito_verificador = soma % 11

print(f"{numero_principal}-{digito_verificador}")