def divisor(num, lista):
    if num == 0:
        exit()
    
    divisores = 0
    for c in range(len(lista)):
        if (lista[c] % num) == 0:
            divisores += 1
            saida = c
            break
    
    if divisores == 0:
        saida = -1

    return saida 

