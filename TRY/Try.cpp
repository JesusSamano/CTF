

#include <iostream>



int main() {
    try {
        int divisor = 0;
        int resultado = 10 / divisor;  // Intento de divisi�n por cero
        std::cout << "Resultado: " << resultado << std::endl;
    } catch (const std::exception& e) {
        // Capturando excepciones de tipo std::exception
        std::cerr << "Error: " << e.what() << std::endl;
    } catch (...) {
        // Capturando cualquier otra excepci�n no espec�fica
        std::cerr << "Error desconocido." << std::endl;
    }

    return 0;
}

