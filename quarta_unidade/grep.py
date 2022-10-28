palavra = input()
quantidade_frases = int(input())

for f in range(quantidade_frases):
    frases = input()
    frase = frases.split()
    for p in range(len(frase)):
        letras = frase[p]
        for l in range(len(letras)):
            if l < len(letras) - 2:
                if (letras[l] + letras[l+1] + letras[l+2] == palavra):
                    print(frases)
                    break
        

            

    




