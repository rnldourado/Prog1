def funcao_in(lista, termo):
    saida = False
    for i in lista:
        if i == termo:
            saida = True
    
    return saida

def filtra_divisores(lista):

    remover = []
    for i in lista:
        soma = 0
        for g in str(i):
            soma += int(g)
        if i % soma != 0:
            remover.append(i)
    
    for c in range(len(lista)-1,-1,-1):
        if funcao_in(remover, lista[c]):
            lista.pop(c)


