# Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X, 
# um valor por linha, inclusive o X ser for o caso.

# Entrada
# A entrada será um valor inteiro positivo.

# Saída
# A saída será uma sequência de seis números ímpares.

X = int(input())

count = 0

while count < 6:
    if X % 2 != 0:
        print(X)
        count += 1
    X += 1