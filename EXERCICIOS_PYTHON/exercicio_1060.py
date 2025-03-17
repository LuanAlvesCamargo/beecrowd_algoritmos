# Faça um programa que leia 6 valores. 
# Estes valores serão somente negativos ou positivos (desconsidere os valores nulos).
# A seguir, mostre a quantidade de valores positivos digitados.

# Entrada
# Seis valores, negativos e/ou positivos.

# Saída
# Imprima uma mensagem dizendo quantos valores positivos foram lidos.

positive_count = 0

for _ in range(6):
    value = float(input())
    
    if value > 0:
        positive_count += 1

print(f"{positive_count} valores positivos")