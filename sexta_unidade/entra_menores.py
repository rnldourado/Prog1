def encontra_menores(num, lista):
    saida = -1
    for itens in lista:
        if num > itens:
            saida = itens 
            break
    
    return saida


    