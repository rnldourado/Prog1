def maioridade_penal(nomes, idades):
    nomes = nomes.split()
    idades = idades.split()
    maiores_de_idade = []
    for nome in range(len(nomes)):
        if int(idades[nome]) >= 18:
            maiores_de_idade.append(nomes[nome])
    
    resultado = ""
   
    for maiores in range(len(maiores_de_idade)):
        if maiores == len(maiores_de_idade) - 1:
            resultado += maiores_de_idade[maiores]
        else:
            resultado += maiores_de_idade[maiores] + " "

    return resultado

