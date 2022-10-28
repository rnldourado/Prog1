n = int(input())

cont_impar = cont_par = soma_impar = soma_par = 0
for numeros in range(n):
    numero = int(input())
    if numero % 2 == 0:
        soma_par += numero
        cont_par += 1
    elif numero % 2 != 0:
        soma_impar += numero
        cont_impar += 1

media_impar = soma_impar / cont_impar
media_par = soma_par / cont_par

print(f"pares: {cont_par}\n"
      f"ímpares: {cont_impar}\n"
      f"média pares: {media_par:.1f}\n"
      f"média ímpares: {media_impar:.1f}")

