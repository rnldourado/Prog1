def calcula_digitos_verificacao(cpf):
    soma, fator = 0, 2
    for digito in range(len(cpf)-1, -1, -1):
        soma += (int(cpf[digito]) * fator)
        fator += 1

    digito_verificador1 = (soma * 10) % 11
    if digito_verificador1 == 10:
        digito_verificador1 = 0   
    
    cpf += str(digito_verificador1)

    soma, fator = 0, 2
    for digito in range(len(cpf)-1, -1, -1):
        soma += (int(cpf[digito]) * fator)
        fator += 1
    
    digito_verificador2 = (soma * 10) % 11
    if digito_verificador2 == 10:
        digito_verificador2 = 0

    digitos_verificadores = str(digito_verificador1) + str(digito_verificador2)

    return digitos_verificadores

