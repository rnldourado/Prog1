# Programação 1 2021.1e
# Discente: Raniel Miranda Dourado - 121110466
# Exercício: Converte Senha

#Entradas
senha = list(input())

#Operações
count = 0
s = ''

for i in range(len(senha)):
    if (senha[i] == "a" or senha[i]=="A") and i != 0:
        senha[i] = "4"
        count += 1
    if (senha[i] == "e" or senha[i]=="E") and i != 0:
        senha[i] = "3"
        count += 1
    if (senha[i] == "i" or senha[i]=="I") and i != 0:
        senha[i] = "1"
        count += 1
    if (senha[i] == "o" or senha[i]=="O") and i != 0:
        senha[i] = "0"
        count += 1
    s += senha[i]

#Saída
print(f"{s} ({count} troca(s))")
