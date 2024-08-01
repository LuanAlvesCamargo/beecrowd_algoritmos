/*
Considerando a entrada de valores inteiros não negativos, ordene estes valores segundo o seguinte critério:

Primeiro os Pares
Depois os Ímpares
Sendo que deverão ser apresentados os pares em ordem crescente e depois os ímpares em ordem decrescente.

Entrada
A primeira linha de entrada contém um único inteiro positivo N (1 < N <= 105) 
Este é o número de linhas de entrada que vem logo a seguir. As próximas N linhas conterão, 
cada uma delas, um valor inteiro não negativo.

Saída
Apresente todos os valores lidos na entrada segundo a ordem apresentada acima. 
Cada número deve ser impresso em uma linha, conforme exemplo abaixo.*
*/

#include <iostream>
#include <queue>

using namespace std;

int main() {
    int N;
    cin >> N;

    priority_queue<int, vector<int>, greater<int>> pares;
    priority_queue<int> impares;

    for (int i = 0; i < N; ++i) {
        int num;
        cin >> num;

        if (num % 2 == 0) {
            pares.push(num);
        } else {
            impares.push(num);
        }
    }

    while (!pares.empty()) {
        cout << pares.top() << endl;
        pares.pop();
    }

    while (!impares.empty()) {
        cout << impares.top() << endl;
        impares.pop();
    }

    return 0;
}


/*
#include <iostream>
#include <queue> // Inclui a biblioteca para usar a estrutura de dados priority_queue

using namespace std;

int main() {
    int N; // Variável para armazenar o número de valores de entrada
    cin >> N; // Lê o número de valores de entrada fornecidos pelo usuário

    // Declaração das filas de prioridade para armazenar os números pares e ímpares
    priority_queue<int, vector<int>, greater<int>> pares; // Para números pares, ordenados em ordem crescente
    priority_queue<int> impares; // Para números ímpares, ordenados em ordem decrescente

    // Loop para ler e classificar os valores de entrada
    for (int i = 0; i < N; ++i) {
        int num; // Variável para armazenar cada valor de entrada
        cin >> num; // Lê o valor de entrada

        // Verifica se o número é par ou ímpar e o insere na fila de prioridade apropriada
        if (num % 2 == 0) { // Se o número for par
            pares.push(num); // Insere o número na fila de prioridade de pares
        } else { // Se o número for ímpar
            impares.push(num); // Insere o número na fila de prioridade de ímpares
        }
    }

    // Impressão dos números na ordem correta
    // Primeiro os pares em ordem crescente
    while (!pares.empty()) { // Enquanto a fila de prioridade de pares não estiver vazia
        cout << pares.top() << endl; // Imprime o número no topo da fila de prioridade de pares
        pares.pop(); // Remove o número do topo da fila de prioridade de pares
    }

    // Depois os ímpares em ordem decrescente
    while (!impares.empty()) { // Enquanto a fila de prioridade de ímpares não estiver vazia
        cout << impares.top() << endl; // Imprime o número no topo da fila de prioridade de ímpares
        impares.pop(); // Remove o número do topo da fila de prioridade de ímpares
    }

    return 0; // Retorna 0 para indicar que o programa foi executado com sucesso
}

*/