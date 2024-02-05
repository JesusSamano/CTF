import pickle

# Definir la clase que representa el estado del programa
class EstadoPrograma:
    def __init__(self):
        self.variable_estado = "Hola, este es mi estado inicial."

# Nombre del archivo donde se almacenará el estado
archivo_estado = "estado_programa.pkl"

# Función para guardar el estado en un archivo
def guardar_estado(estado):
    with open(archivo_estado, 'wb') as archivo:
        pickle.dump(estado, archivo)

# Función para cargar el estado desde un archivo
def cargar_estado():
    try:
        with open(archivo_estado, 'rb') as archivo:
            estado = pickle.load(archivo)
        return estado
    except FileNotFoundError:
        # Devolver un nuevo estado si el archivo no existe
        return EstadoPrograma()

# Función principal del programa
def programa_principal():
    # Cargar el estado almacenado (o crear uno nuevo si no existe)
    estado = cargar_estado()

    # Realizar operaciones con el estado
    print("Estado actual:", estado.variable_estado)
    nuevo_valor = input("Ingrese un nuevo valor para el estado: ")
    estado.variable_estado = nuevo_valor

    # Guardar el estado actual antes de salir
    guardar_estado(estado)
    print("Estado guardado. Cierre el programa y vuelva a ejecutar para cargar el estado.")

# Ejecutar el programa principal
if __name__ == "__main__":
    programa_principal()
