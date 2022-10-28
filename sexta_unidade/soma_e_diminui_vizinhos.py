def soma_diminui_vizinhos(lista):
    if not lista: 
        resultado = 0
    else:
        resultado = lista[0]
        for i in range(len(lista)-1):
            if (i+1) % 2 != 0:
                resultado += lista[i+1]
            else:
                resultado -= lista[i+1]
    
    return resultado

