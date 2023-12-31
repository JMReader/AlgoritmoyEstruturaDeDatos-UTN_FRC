from funciones import *

paises = [  # paises en los que se puede COBRAR en su respectivo orden de craga
    "Argentina",
    "Bolivia",
    "Brasil",
    "Paraguay",
    "Uruguay",
]
vehiculos = ["motocicletas ", "automoviles ", "camiones"]  # tipos de vehículos en su respectivo orden de carga


def principal():
    op = -1
    while op != 0:
        print("\nMenú de opciones:")
        print("1. almacenar tickets desde archivo")
        print("2. almacenar ticket manualmente")
        print("3. Mostrar tickets almacenados")
        print("4. Buscar ticket por patente")
        print("5. Buscar ticket por código de identificación")
        print("6. Mostrar cantidad de vehículos que pasaron por las cabinas de cada pais")
        print("7. Mostrar cantidad total de vehículos por tipo y pais")
        print("8. Mostrar la distancia promedio desde la última cabina recorrida entre todos los vehículos")
        print("0. Salir")

        op = input("ingrese su opción: ")

        if op == "1":
            op1()
        elif op == "2":
            op2()
        elif op == "3":
            op3()
        elif op == "4":
            op4()
        elif op == "5":
            print("ingrese el código identificador que desea buscar.")
            cod = input()
            op5(cod)
        elif op == "6":
            matriz = op6()
            imprimir(matriz)
        elif op == "7":
            op7(op6())
        elif op == "8":
            op8()
        elif op == "0":
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    principal()
