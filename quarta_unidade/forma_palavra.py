palavra1 = input()
palavra2 = input()
palavra3 = input()
nova_palavra = ''

for letra in range(len(palavra1)):
    if ord(palavra1[letra]) >= ord(palavra2[letra]) and ord(palavra1[letra]) >= ord(palavra3[letra]):
        nova_palavra += palavra1[letra]
    elif ord(palavra2[letra]) >= ord(palavra1[letra]) and ord(palavra2[letra]) >= ord(palavra3[letra]):
        nova_palavra += palavra2[letra]
    elif ord(palavra3[letra]) >= ord(palavra1[letra]) and ord(palavra3[letra]) >= ord(palavra2[letra]):
        nova_palavra += palavra3[letra]
    

print(nova_palavra)