cnpj_raiz = input()

soma = 0
for num in range(len(cnpj_raiz)):
    if num != 2 and num != 6:
        soma += int(cnpj_raiz[num])

soma += 1

digito_verificador = str(soma)

if soma < 10:
    digito_verificador = '0' + digito_verificador

print(f"{cnpj_raiz}/0001-{digito_verificador}")