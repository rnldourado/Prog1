quantidade = int(input())
soma = 0
for mpt in range(quantidade):
    nota = float(input())
    soma += nota

media = soma / quantidade

if quantidade == 1:
    saida = "Aluno ainda não aprovado na unidade"
elif quantidade == 2:
    if media >= 6:
        saida = "Aluno aprovado na unidade"
    else:
        saida = "Aluno ainda não aprovado na unidade"
elif quantidade > 2:
    media -= 0.5
    if media >= 6:
        saida = "Aluno aprovado na unidade"
    else:
        saida = "Aluno ainda não aprovado na unidade"

print(f"{media:.1f}")
print(saida)