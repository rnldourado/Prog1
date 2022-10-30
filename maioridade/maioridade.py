def maioridade(nomes, idades):
    maiores = list
    for i in range(nomes.split()):
        maior = False
        for b in range(idades.split()):
            if idades[b] >= 18:
                maiores.append(nomes[i])
                return maiores

lista1 = ["joao pedro ana"]
lista2 = ["15 19 25"]
assert maioridade(lista1, lista2)
