from funciones import *


def principal():
    op = -1
    while op != 0:
        print("\nMenú de opciones:")
        print("1. Cargar tickets desde archivo")
        print("2. Cargar ticket manualmente")
        print("3. Mostrar tickets almcenados")
        print("4. Buscar ticket por patente y país")
        print("5. Cambiar forma de pago por código")
        print("6. Contar vehículos por país")
        print("7. Calcular importe acumulado por tipo de vehículo")
        print("8. Encontrar tipo de vehículo con mayor monto acumulado")
        print("9. Calcular distancia promedio y contar vehículos")
        print("0. Salir")

        op = input("ingrese su opcion: ")

        if op == "1":
            print("Si carga los datos del archivo csv perdera sus datos almacenados actualmente en su archivo .dat")
            opcion = int(input("¿Desea continuar? 1) si 2)no "))
            if opcion==1:
                op1()
        elif op == "2":
            op2()
        elif op == "3":
            op3()
        elif op == "4":
            op4()
        elif op == "5":
            op5()
        elif op == "6":
            op6()
        elif op == "7":
            op7()
        elif op == "8":
            op8()
        elif op == "9":
            op9()
        elif op == "0":
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    principal()
