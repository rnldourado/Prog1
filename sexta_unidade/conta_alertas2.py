def conta_alertas_acude(medicoes):
    conta_alertas = 0
    for i in range(1, len(medicoes)):
        if medicoes[i] < 17:
            if abs(medicoes[i] - medicoes[i-1]) < 10:
                conta_alertas += 1
    
    return conta_alertas
