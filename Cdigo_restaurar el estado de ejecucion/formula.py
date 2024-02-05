# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 21:57:18 2024

@author: ThinkPad T440
"""

import pickle

# Clase que representa un formulario
class Formulario:
    def __init__(self, id, nombre, edad):
        self.id = id
        self.nombre = nombre
        self.edad = edad

# Nombre del archivo donde se almacenará la lista de formularios
archivo_formularios = "formularios.pkl"

# Función para guardar la lista de formularios en un archivo
def guardar_formularios(formularios):
    with open(archivo_formularios, 'wb') as archivo:
        pickle.dump(formularios, archivo)

# Función para cargar la lista de formularios desde un archivo
def cargar_formularios():
    try:
        with open(archivo_formularios, 'rb') as archivo:
            formularios = pickle.load(archivo)
        return formularios
    except FileNotFoundError:
        # Devolver una lista vacía si el archivo no existe
        return []

# Función para mostrar la lista de formularios
def mostrar_lista_formularios(formularios):
    print("\nLista de Formularios:")
    for formulario in formularios:
        print(f"ID: {formulario.id}, Nombre: {formulario.nombre}, Edad: {formulario.edad}")

# Función principal para ingresar y gestionar formularios
def gestionar_formularios():
    # Cargar la lista de formularios almacenada
    formularios = cargar_formularios()

    while True:
        print("\n1. Ingresar Nuevo Formulario")
        print("2. Ver Lista de Formularios")
        print("3. Salir")

        opcion = input("Seleccione una opción (1/2/3): ")

        if opcion == "1":
            # Ingresar un nuevo formulario
            id = int(input("Ingrese el ID: "))
            nombre = input("Ingrese el Nombre: ")
            edad = int(input("Ingrese la Edad: "))

            nuevo_formulario = Formulario(id, nombre, edad)
            formularios.append(nuevo_formulario)

            # Guardar la lista actualizada
            guardar_formularios(formularios)
            print("Formulario ingresado correctamente.")

        elif opcion == "2":
            # Ver la lista de formularios
            mostrar_lista_formularios(formularios)

        elif opcion == "3":
            # Salir del programa
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, ingrese 1, 2 o 3.")

# Ejecutar el programa principal
if __name__ == "__main__":
    gestionar_formularios()
