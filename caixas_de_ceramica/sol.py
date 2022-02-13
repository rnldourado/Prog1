# Programação 1 2021.1e
# Discente: Raniel Miranda Dourado - 121110466
# Exercício: Caixas de Cerâmicas

#Entradas

revestimento = float(input("Capacidade de revestimento? "))
print("\n== Dados do vão a revestir ==")
comprimento = float(input("Comprimento? "))
largura = float(input("Largura? "))
altura = float(input("Altura? "))

#Operações
area = (comprimento * largura) + (largura * altura * 2) + (comprimento * altura * 2)
caixas = int(area // revestimento)

#Saída
print(f"\n== Resultados ==\nÁrea total a revestir: {area:.1f} m2\nNúmero de caixas: {caixas:.0f}")
