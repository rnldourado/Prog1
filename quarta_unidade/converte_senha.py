palavra = input()

palavra = list(palavra)
trocas = 0

for s in range(1, len(palavra)):
    if palavra[s] == "a" or palavra[s] == "A":
        palavra[s] = "4"
        trocas += 1
    if palavra[s] == "e" or palavra[s] == "E":
        palavra[s] = "3"
        trocas += 1
    if palavra[s] == "i" or palavra[s] == "I":
        palavra[s] = "1"
        trocas += 1
    if palavra[s] == "o" or palavra[s] == "O":
        palavra[s] = "0"
        trocas += 1

for c in range(len(palavra)):
    letra = palavra[c]
    print(f"{letra}", end="")

print(f" ({trocas} troca(s))")




