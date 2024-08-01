/*
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, 
e informe-o expresso no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, 
conforme exemplo fornecido.
*/

#include <iostream>

using namespace std;

int main() {
    int N;
    cin >> N;

    int horas = N / 3600;
    N %= 3600;

    int minutos = N / 60;
    int segundos = N % 60;

    cout << horas << ":" << minutos << ":" << segundos << endl;

    return 0;
}
