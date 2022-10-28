tamanho_da_arvore = int(input())

quantidade_de_o = 1
for c in range(1, tamanho_da_arvore+1):
    espacos = (tamanho_da_arvore - c) * " "
    
    if c != 1:
        o = (quantidade_de_o + 2) * 'o'
        quantidade_de_o += 2
    else:
        o = 'o'
    print(espacos + o)

base = (quantidade_de_o // 2) * " " + 'o'
print(base)



