# Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

# Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

# Entrada
# Quatro números inteiros representando a hora de início e fim do jogo.

# Saída
# Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .

start_hour, start_minute, end_hour, end_minute = map(int, input().split())

start_total_minutes = start_hour * 60 + start_minute
end_total_minutes = end_hour * 60 + end_minute

if start_total_minutes < end_total_minutes:
    duration_minutes = end_total_minutes - start_total_minutes
else:
    duration_minutes = (24 * 60 - start_total_minutes) + end_total_minutes

duration_hours = duration_minutes // 60
duration_minutes = duration_minutes % 60

print(f"O JOGO DUROU {duration_hours} HORA(S) E {duration_minutes} MINUTO(S)")