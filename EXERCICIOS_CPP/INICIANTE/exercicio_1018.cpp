/*
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) 
no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. 
A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, 
conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, 
caso contrário seu programa apresentará a mensagem: “Presentation Error”.
*/

#include <iostream>

using namespace std;

int main() {
    int N;
    cin >> N;
    
    cout << N << endl;
    
    int notas100 = N / 100;
    N %= 100;
    
    int notas50 = N / 50;
    N %= 50;
    
    int notas20 = N / 20;
    N %= 20;
    
    int notas10 = N / 10;
    N %= 10;
    
    int notas5 = N / 5;
    N %= 5;
    
    int notas2 = N / 2;
    N %= 2;
    
    int notas1 = N;
    
    cout << notas100 << " nota(s) de R$ 100,00" << endl;
    cout << notas50 << " nota(s) de R$ 50,00" << endl;
    cout << notas20 << " nota(s) de R$ 20,00" << endl;
    cout << notas10 << " nota(s) de R$ 10,00" << endl;
    cout << notas5 << " nota(s) de R$ 5,00" << endl;
    cout << notas2 << " nota(s) de R$ 2,00" << endl;
    cout << notas1 << " nota(s) de R$ 1,00" << endl;
    
    return 0;
}
