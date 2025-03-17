
# Faça um programa que leia 5 valores inteiros. 
# Conte quantos destes valores digitados são pares e mostre esta informação.

# Entrada
# O arquivo de entrada contém 5 valores inteiros quaisquer.

# Saída
# Imprima a mensagem conforme o exemplo fornecido, 
# indicando a quantidade de valores pares lidos.

even_count = 0
for _ in range(5):
    value = int(input())
    
    if value % 2 == 0:
        even_count += 1

print(f"{even_count} valores pares")