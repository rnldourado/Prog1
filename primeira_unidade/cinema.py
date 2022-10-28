quantidade_de_adultos = int(input())
quantidade_de_criancas = int(input())
preco_da_entrada = float(input())

total_a_ser_pago = (quantidade_de_adultos * preco_da_entrada) + (quantidade_de_criancas * (preco_da_entrada / 2))

print(f"Total: R$ {total_a_ser_pago :.2f}")


