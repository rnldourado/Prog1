def maior_palavra(frase):
    for c in frase:
        cont_letras = 0
        maior_quant_letras = 0
        palavra = ''
        for c in frase:
            if c != " ":
                cont_letras += 1
                palavra += c
            if c == " " or c == frase[len(frase)-1]:
                if cont_letras >= maior_quant_letras:
                    maior_palavra = palavra
                    maior_quant_letras = cont_letras
                palavra = ''
                cont_letras = 0

    return maior_palavra

