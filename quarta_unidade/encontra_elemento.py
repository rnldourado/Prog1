elemento = int(input())

sequencia = input().split()

esta = 0

for s in range(0, len(sequencia)):
    if elemento == int(sequencia[s]):
        esta += 1

if esta == 0:
    print("não")
else:
    print("sim")

