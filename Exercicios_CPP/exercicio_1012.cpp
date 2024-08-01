/*
Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida,
calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.
Entrada
O arquivo de entrada contém três valores com um dígito após o ponto decimal.

Saída
O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima,
sempre com mensagem correspondente e um espaço entre os dois pontos e o valor. 
O valor calculado deve ser apresentado com 3 dígitos após o ponto decimal.
*/

#include <iostream>
#include <cstdio>

using namespace std;

int main() {
    double A, B, C;
    const double PI = 3.14159;

    cin >> A >> B >> C;

    double areaTriangulo = (A * C) / 2;
    double areaCirculo = PI * C * C;
    double areaTrapezio = ((A + B) * C) / 2;
    double areaQuadrado = B * B;
    double areaRetangulo = A * B;

    printf("TRIANGULO: %.3lf\n", areaTriangulo);
    printf("CIRCULO: %.3lf\n", areaCirculo);
    printf("TRAPEZIO: %.3lf\n", areaTrapezio);
    printf("QUADRADO: %.3lf\n", areaQuadrado);
    printf("RETANGULO: %.3lf\n", areaRetangulo);

    return 0;
}
