#include <iostream>
#include <cstring>

bool verificaBalancoParenteses(char *);

int main() {
    char expressao[1100];

    while (std::cin >> expressao) {
        if (verificaBalancoParenteses(expressao))
            std::cout << "correct" << std::endl;
        else
            std::cout << "incorrect" << std::endl;
    }

    return 0;
}

bool verificaBalancoParenteses(char *str) {
    short qtsP = 0;

    if (*str == ')')
        return false;

    while ((*str) && (qtsP >= 0)) {
        if (*str == '(')
            qtsP++;
        if (*str == ')')
            qtsP--;

        str++;
    }

    if (qtsP == 0)
        return true;
    else
        return false;
}
