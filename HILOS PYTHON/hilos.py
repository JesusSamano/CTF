import threading
import multiprocessing
import time
import random

def descargar_archivo(nombre):
    tiempo_descarga = random.randint(1, 5)
    print(f"Iniciando descarga de {nombre}. Tiempo estimado: {tiempo_descarga} segundos.")
    time.sleep(tiempo_descarga)
    print(f"Descarga de {nombre} completa.")

if __name__ == "__main__":
    # Descarga de archivos usando hilos
    archivos = ["archivo1", "archivo2", "archivo3"]
    hilos_descarga = []

    for archivo in archivos:
        hilo = threading.Thread(target=descargar_archivo, args=(archivo,))
        hilos_descarga.append(hilo)
        hilo.start()

    for hilo in hilos_descarga:
        hilo.join()

    print("Descargas con hilos completadas.\n")

    # Descarga de archivos usando procesos
    procesos_descarga = []

    for archivo in archivos:
        proceso = multiprocessing.Process(target=descargar_archivo, args=(archivo,))
        procesos_descarga.append(proceso)
        proceso.start()

    for proceso in procesos_descarga:
        proceso.join()

    print("Descargas con procesos completadas.\n")

    # Descarga de archivos usando procesos demonio
    procesos_demonio_descarga = []

    for archivo in archivos:
        proceso_demonio = multiprocessing.Process(target=descargar_archivo, args=(archivo,))
        proceso_demonio.daemon = True
        procesos_demonio_descarga.append(proceso_demonio)
        proceso_demonio.start()

    time.sleep(3)  # Esperar un tiempo antes de que el programa principal termine
    print("Programa principal ha terminado.")
