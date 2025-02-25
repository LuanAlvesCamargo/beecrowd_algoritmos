/*
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem
“eh o maior”. Utilize a fórmula:

Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). 
Um segundo passo, portanto é necessário para chegar no resultado esperado.

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".
*/

#include <iostream>
#include <cstdio>
#include <cmath> // Para usar a função abs()

using namespace std;

int main() {
    int a, b, c;

    // Lendo os valores de a, b e c
    cin >> a >> b >> c;

    // Usando a fórmula para encontrar o maior entre a e b
    int maiorAB = (a + b + abs(a - b)) / 2;

    // Usando a fórmula novamente para encontrar o maior entre maiorAB e c
    int maior = (maiorAB + c + abs(maiorAB - c)) / 2;

    // Imprimindo o resultado
    printf("%d eh o maior\n", maior);

    return 0;
}