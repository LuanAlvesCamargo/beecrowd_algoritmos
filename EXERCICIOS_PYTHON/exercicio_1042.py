# Leia 3 valores inteiros e ordene-os em ordem crescente. 
# No final, mostre os valores em ordem crescente, 
# uma linha em branco e em seguida, 
# os valores na sequência como foram lidos.

# Entrada
# A entrada contem três números inteiros.

# Saída
# Imprima a saída conforme foi especificado.

A, B, C = map(int, input().split())

valores = [A, B, C]
valores_ordenados = sorted(valores)
for valor in valores_ordenados:
    print(valor)
print()
for valor in valores:
    print(valor)