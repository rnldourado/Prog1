palavra = input()

cont = 0
inverso = len(palavra)
for c in range(len(palavra)):
    inverso -= 1
    if palavra[c] == palavra[inverso]:
        cont += 1



print(f"A palavra {palavra} contém {cont} caractere(s) coincidente(s) com a sua inversa.")
