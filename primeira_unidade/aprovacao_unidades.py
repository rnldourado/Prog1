unidade = int(input('Unidade? '))
media = float(input('Média de aprovação na unidade? '))

proxima_unidade = unidade + 1
msg = f'O aluno vai para a unidade {proxima_unidade} com média {media:.1f}.'

print("")
print(msg)