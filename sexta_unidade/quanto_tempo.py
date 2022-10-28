def quanto_tempo(horario1, horario2):
    hora1 = int(horario1[0] + horario1[1])
    minuto1 = int(horario1[3] + horario1[4])
    hora2 = int(horario2[0] + horario2[1])
    minuto2 = int(horario2[3] + horario2[4])

    total_minutos = (hora2 - hora1)*60 + (minuto2 - minuto1)
    horas_de_diferenca = total_minutos // 60
    minutos_de_diferenca = total_minutos % 60
     
    return f"{horas_de_diferenca} hora(s) e {minutos_de_diferenca} minuto(s)" 
