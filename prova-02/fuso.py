def novoHorario(hora_partida, duracao_viagem, diferenca_tempo):
    soma_horas = hora_partida + duracao_viagem + diferenca_tempo

    if soma_horas >= 24:
        soma_horas = soma_horas % 24
    elif soma_horas < 0:
        soma_horas = (soma_horas + 24) % 24
    
    return soma_horas

partida = int(input())
tempo_viagem = int(input())
diferenca_horario = int(input())

horario_chegada = novoHorario(partida, tempo_viagem, diferenca_horario)
print(f'Hora de saída: {partida}\nHora de chegada: {horario_chegada}')
