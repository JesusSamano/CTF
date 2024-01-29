#include <cassert>

int main() {
    int numero = 5;

    // Supongamos que esperamos que el número sea 10
    assert(numero == 10);

    // El código continuará si la aserción es verdadera
    // Si la aserción es falsa, el depurador intervendrá y proporcionará información sobre el error

    return 0;
}
