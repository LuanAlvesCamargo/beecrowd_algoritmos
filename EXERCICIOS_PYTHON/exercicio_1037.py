# Você deve fazer um programa que leia um valor qualquer e apresente uma mensagem 
# dizendo em qual dos seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) este valor se encontra. 
# Obviamente se o valor não estiver em nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”.
# O símbolo ( representa "maior que". Por exemplo:
# [0,25]  indica valores entre 0 e 25.0000, inclusive eles.
# (25,50] indica valores maiores que 25 Ex: 25.00001 até o valor 50.0000000
# Entrada
# O arquivo de entrada contém um número com ponto flutuante qualquer.
# Saída
# A saída deve ser uma mensagem conforme exemplo abaixo.

numeros = input().split()
numero = float(numeros[0])

if numero >= 0 and numero <= 25:
    print("Intervalo [0,25]")
elif numero > 25 and numero <= 50:
    print("Intervalo (25,50]")
elif numero > 50 and numero <= 75:
    print("Intervalo (50,75]")
elif numero > 75 and numero <= 100:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")