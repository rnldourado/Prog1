# Programação 1 2021.1e
# Discente: Raniel Miranda Dourado - 121110466
# Exercício: Formata CPF

#Entradas
cpf1 = int(input())
cpf2 = int(input())
cpf3 = int(input())

#Operações
prefixo_cpf1 = cpf1 // 100
sufixo_cpf1 = cpf1 - prefixo_cpf1 * 100
soma_digito_cpf1 = (sufixo_cpf1 // 10) + (sufixo_cpf1 % 10)

prefixo_cpf2 = cpf2 // 100
sufixo_cpf2 = cpf2 - prefixo_cpf2 * 100
soma_digito_cpf2 = (sufixo_cpf2 // 10) + (sufixo_cpf2 % 10)

prefixo_cpf3 = cpf3 // 100
sufixo_cpf3 = cpf3 - prefixo_cpf3 * 100
soma_digito_cpf3 = (sufixo_cpf3 // 10) + (sufixo_cpf3 % 10)

#Saídas
print(f"{prefixo_cpf1}-{sufixo_cpf1}\n{soma_digito_cpf1}")
print(f"{prefixo_cpf2}-{sufixo_cpf2}\n{soma_digito_cpf2}")
print(f"{prefixo_cpf3}-{sufixo_cpf3}\n{soma_digito_cpf3}")
