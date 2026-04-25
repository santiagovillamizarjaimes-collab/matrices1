%%writefile main.py

from operaciones_matrices import sumar_matrices, multiplicar_matrices, hadamard_matrices, kronecker
from entrada import ingresar_matriz
from menu import mostrar_menu

def ejecutar():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == 5:
          break

        print("Matriz A:")
        A = ingresar_matriz()
        print("Matriz B:")
        B = ingresar_matriz()


        try:

            if opcion == 1:
              print("Resultado:\n", sumar_matrices(A, B))

            elif opcion == 2:
              print("Resultado:\n", multiplicar_matrices(A, B))

            elif opcion == 3:
              print("Resultado:\n", hadamard_matrices(A, B))

            elif opcion == 4:
              print("Resultado:\n", kronecker(A, B))

            elif opcion == 5:
              print("Saliendo del programa")
              break

        except ValueError:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    ejecutar_programa() 
