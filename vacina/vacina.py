sim = 0
nao = 0
entrada = input()

while entrada != "###" :
    indice = -1
    contador = 0
    while entrada[indice] != "c" or entrada[indice] != "i":
        if entrada[indice] == "a":
            indice -= 1
            contador += 1
        elif entrada[indice] == "c" or entrada[indice] == "i":
            if "a" in entrada[indice:0]:
                nao += 1
            else:
                sim += 1
    entrada = input()

print(f"sim: {sim}")
print(f"não: {nao}")

   
    

