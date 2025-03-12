# Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente,
# de modo que o lado A representa o maior dos 3 lados. 
# A seguir, determine o tipo de triângulo que estes três lados formam, 
# com base nos seguintes casos, sempre escrevendo uma mensagem adequada:

# se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
# se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
# se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
# se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
# se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
# se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES
# Entrada
# A entrada contem três valores de ponto flutuante de dupla precisão A (0 < A) , B (0 < B) e C (0 < C).

# Saída
# Imprima todas as classificações do triângulo especificado na entrada.

A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)

if A >= B and A >= C:
    maior = A
    if B >= C:
        meio = B
        menor = C
    else:
        meio = C
        menor = B
elif B >= A and B >= C:
    maior = B
    if A >= C:
        meio = A
        menor = C
    else:
        meio = C
        menor = A
else:
    maior = C
    if A >= B:
        meio = A
        menor = B
    else:
        meio = B
        menor = A

if maior >= meio + menor:
    print("NAO FORMA TRIANGULO")
else:
    if maior ** 2 == meio ** 2 + menor ** 2:
        print("TRIANGULO RETANGULO")
    if maior ** 2 > meio ** 2 + menor ** 2:
        print("TRIANGULO OBTUSANGULO")
    if maior ** 2 < meio ** 2 + menor ** 2:
        print("TRIANGULO ACUTANGULO")
    if maior == meio == menor:
        print("TRIANGULO EQUILATERO")
    if maior == meio != menor or maior == menor != meio or meio == menor != maior:
        print("TRIANGULO ISOSCELES") 
