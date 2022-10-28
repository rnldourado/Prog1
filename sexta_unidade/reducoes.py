def reducoes(lista):
    if not lista or len(lista) == 1:
        return []
    
    subtracoes = []
    for i in range(len(lista)-1):
        if lista[i] - lista[i+1] < 0:
            subtracoes.append(0)
        else:
            subtracoes.append(lista[i] - lista[i+1])
    
    return subtracoes

