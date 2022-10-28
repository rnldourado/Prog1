def tradutor_morse(texto):
    lista_de_codigos = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-',
                        '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..' ]
    lista_alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    
    traducao = ''
    for c in texto:
        for s in range(len(lista_de_codigos)):
            if c == lista_de_codigos[s]:
                traducao += lista_alfabeto[s]
    
    return traducao







