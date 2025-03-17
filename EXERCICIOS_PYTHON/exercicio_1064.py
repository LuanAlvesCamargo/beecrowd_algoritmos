# Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos.
# Na próxima linha, deve-se mostrar a média de todos os valores positivos digitados, com um dígito após o ponto decimal.

# Entrada
# A entrada contém 6 números que podem ser valores inteiros ou de ponto flutuante.
# Pelo menos um destes números será positivo.

# Saída
# O primeiro valor de saída é a quantidade de valores positivos. 
# A próxima linha deve mostrar a média dos valores positivos digitados.

positive_count = 0
positive_sum = 0.0

for _ in range(6):
    value = float(input())
    
    if value > 0:
        positive_count += 1
        positive_sum += value

if positive_count > 0:
    positive_average = positive_sum / positive_count
else:
    positive_average = 0.0

print(f"{positive_count} valores positivos")
print(f"{positive_average:.1f}")