entrada1 = input()
entrada2 = input()

#utiliza um loop para diferenciar numeros de letras usando da funcao ord(), converte os numeros em letras utilizando a chave e adiciona na variavel resposta os caracteres em str.
resposta = ''
for s in range(len(entrada1)):
    if  48 <= ord(entrada1[s]) <= 57:
        resposta += entrada2[int(entrada1[s])]
    else:
        resposta += entrada1[s]
        

print(resposta)
