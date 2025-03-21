# Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo,
# sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.

# Entrada
# A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo.

# Saída
# Apresente a duração do jogo conforme exemplo abaixo.

start, end = map(int, input().split())

if start < end:
    duration = end - start
else:
    duration = 24 - start + end

print(f"O JOGO DUROU {duration} HORA(S)")