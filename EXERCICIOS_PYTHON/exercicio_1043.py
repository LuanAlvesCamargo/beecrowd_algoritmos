# Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. 
# Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:
# Perimetro = XX.X
# Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem
# Area = XX.X
# Entrada
# A entrada contém três valores reais.
# Saída
# O resultado deve ser apresentado com uma casa decimal.


# Function to check if three sides can form a triangle
def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

# Function to calculate the perimeter of a triangle
def calculate_perimeter(a, b, c):
    return a + b + c

# Function to calculate the area of a trapezoid
def calculate_area(a, b, c):
    return ((a + b) * c) / 2

# Read input values
a, b, c = map(float, input().split())

# Check if the values form a triangle
if is_triangle(a, b, c):
    perimeter = calculate_perimeter(a, b, c)
    print(f"Perimetro = {perimeter:.1f}")
else:
    area = calculate_area(a, b, c)
    print(f"Area = {area:.1f}")