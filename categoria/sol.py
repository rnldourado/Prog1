# Programação 1 2021.1e
# Discente: Raniel Miranda Dourado - 121110466
# Exercício: xxxx

#Entradas
nome = input()
idade = int(input())

#Operações
if idade < 5:
    print(f"{nome}, {idade} anos, Não pode competir.")

elif idade >= 5 and idade <= 7:
    print(f"{nome}, {idade} anos, Infantil A.")

elif idade >= 8 and idade <= 10:
    print(f"{nome}, {idade} anos, Infantil B.")

elif idade >= 11 and idade <= 13:
    print(f"{nome}, {idade} anos, Juvenil A.")

elif idade >= 14 and idade <= 17:
    print(f"{nome}, {idade} anos, Juvenil B.")

elif idade > 17:
    print(f"{nome}, {idade} anos, Senior.")

#Saída
