# Pedrinho está organizando um evento em sua Universidade. 
# O evento deverá ser no mês de Abril, iniciando e terminando dentro do mês. 
# O problema é que Pedrinho quer calcular o tempo que o evento vai durar, 
# uma vez que ele sabe quando inicia e quando termina o evento.

# Sabendo que o evento pode durar de poucos segundos a vários dias, 
# você deverá ajudar Pedrinho a calcular a duração deste evento.

# Entrada
# Como entrada, na primeira linha vai haver a descrição “Dia”, s
# eguido de um espaço e o dia do mês no qual o evento vai começar. 
# Na linha seguinte, será informado o momento no qual o evento vai iniciar, 
# no formato hh : mm : ss. Na terceira e quarta linha de entrada haverá outra 
# informação no mesmo formato das duas primeiras linhas, 
# indicando o término do evento.

# Saída
# Na saída, deve ser apresentada a duração do evento, no seguinte formato:

# W dia(s)
# X hora(s)
# Y minuto(s)
# Z segundo(s)

# Obs: Considere que o evento do caso de teste para o problema tem 
# duração mínima de 1 minuto.

def convert_to_seconds(day, hour, minute, second):
    return day * 86400 + hour * 3600 + minute * 60 + second

start_day = int(input().split()[1])
start_time = list(map(int, input().split(" : ")))
start_hour, start_minute, start_second = start_time

end_day = int(input().split()[1])
end_time = list(map(int, input().split(" : ")))
end_hour, end_minute, end_second = end_time

start_total_seconds = convert_to_seconds(start_day, start_hour, start_minute, start_second)
end_total_seconds = convert_to_seconds(end_day, end_hour, end_minute, end_second)

duration_seconds = end_total_seconds - start_total_seconds

days = duration_seconds // 86400
duration_seconds %= 86400
hours = duration_seconds // 3600
duration_seconds %= 3600
minutes = duration_seconds // 60
seconds = duration_seconds % 60

print(f"{days} dia(s)")
print(f"{hours} hora(s)")
print(f"{minutes} minuto(s)")
print(f"{seconds} segundo(s)")