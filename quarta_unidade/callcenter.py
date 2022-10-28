total = 0
for atendimentos in range(7):
    atendimento = int(input())
    total += atendimento
    
media = total / 7

print(f"Total: {total}\n"
      f"Média: {media:.2f}")
