#include <iostream>
#include <cstdio>

using namespace std;

int main() {
    int numeroDoFuncionario;
    int numeroDeHoras;
    double valorHora;

    cin >> numeroDoFuncionario;
    cin >> numeroDeHoras;
    cin >> valorHora;

    double salario = valorHora * numeroDeHoras;

    cout << "NUMBER = " << numeroDoFuncionario << endl;
    printf("SALARY = U$ %.2f\n", salario); 

    return 0;
}
