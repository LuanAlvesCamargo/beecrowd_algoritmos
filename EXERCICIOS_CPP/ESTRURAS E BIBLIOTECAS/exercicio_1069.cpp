#include <iostream>
#include <string>
using namespace std;

// Função para contar a quantidade de diamantes em uma string
int contaDiamantes(const string& linha) {
    int contador = 0;
    int diamantes = 0;
    
    // Iterar sobre cada caractere da string
    for (char ch : linha) {
        if (ch == '<') {
            contador++;
        } else if (ch == '>' && contador > 0) {
            contador--;
            diamantes++;
        }
    }
    
    return diamantes;
}

int main() {
    int N;
    cin >> N;
    cin.ignore();

    // Processar cada linha de entrada
    for (int i = 0; i < N; ++i) {
        string linha;
        getline(cin, linha);
        int resultado = contaDiamantes(linha);
        cout << resultado << endl;
    }
    
    return 0;
}

