#include <cassert>

int main() {
    int numero = 5;

    // Supongamos que esperamos que el n�mero sea 10
    assert(numero == 10);

    // El c�digo continuar� si la aserci�n es verdadera
    // Si la aserci�n es falsa, el depurador intervendr� y proporcionar� informaci�n sobre el error

    return 0;
}
