#include <iostream>
#include <vector>

using namespace std;

// Função para calcular a posição do último sobrevivente no problema de Josephus
int josephus(int n, int k) {
    int pos = 0;
    for (int i = 1; i <= n; i++) {
        pos = (pos + k) % i;
    }
    return pos + 1;  // Ajustamos para retornar a posição 1-based
}

int main() {
    int NC;  // Número de casos de teste
    cin >> NC;

    for (int i = 1; i <= NC; i++) {
        int n, k;
        cin >> n >> k;

        // Calcula a posição do sobrevivente
        int resultado = josephus(n, k);

        // Imprime o resultado no formato desejado
        cout << "Case " << i << ": " << resultado << endl;
    }

    return 0;
}
