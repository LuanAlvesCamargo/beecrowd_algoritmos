# Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”.
#  Utilize a fórmula:



# Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, 
# portanto é necessário para chegar no resultado esperado.

# Entrada
# O arquivo de entrada contém três valores inteiros.

# Saída
# Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".

from decimal import Decimal

a, b, c = map(Decimal, input().split())

maiorAB = (a + b + abs(a - b)) / 2
resultado = (maiorAB + c + abs(maiorAB - c)) / 2

print(f'{resultado:.0f} eh o maior')