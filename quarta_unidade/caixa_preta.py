n = int(input())

cont_dados_validos = numeros_negativos = 0

for s in range(n):
    dados = input().split()
    for v in range(3):
        if int(dados[v]) < 0 and numeros_negativos == 0:
            numeros_negativos += 1
            if v == 0:
                print('dado inconsistente. peso negativo.')
            elif v == 1:
                print('dado inconsistente. combustível negativo.')
            elif v == 2:
                print('dado inconsistente. altitude negativa.')
        elif int(dados[v]) > -1 and numeros_negativos == 0:
            cont_dados_validos += 1


print(f"{cont_dados_validos} dados válidos.")
