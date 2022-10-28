string1 = input()
string2 = input()



for s in range(len(string2)):
    resposta = []
    saida = ''
    for v in range(len(string1)):
        if string1[v] == string2[s]:
            resposta.append(v)

    if len(resposta) > 0:
        for r in resposta:
            if r != resposta[-1]:
                saida += str(r) + " "
            else:
                saida += str(r)
    else:
         saida = -1


    print(saida)


        

