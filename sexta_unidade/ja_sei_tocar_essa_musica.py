def funcao_in(lista, termo):
    saida = False
    for i in lista:
        if i == termo:
            saida = True

    return saida
    

def sei_tocar_musica(musica, acordes):
    saida = True
    for i in musica:
        if not (funcao_in(acordes, i)):
            saida = False

    return saida
