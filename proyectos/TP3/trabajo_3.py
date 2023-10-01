from funciones import *


def principal():
    op = -1
    tickets = []
    while op != 0:
        print("\nMenú de opciones:")
        print("1. Cargar tickets desde archivo")
        print("2. Cargar ticket manualmente")
        print("3. Mostrar tickets ordenados por código")
        print("4. Buscar ticket por patente y país")
        print("5. Cambiar forma de pago por código")
        print("6. Contar vehículos por país")
        print("7. Calcular importe acumulado por tipo de vehículo")
        print("8. Encontrar tipo de vehículo con mayor monto acumulado")
        print("9. Calcular distancia promedio y contar vehículos")
        print("0. Salir")

        op = input("ingrese su opcion: ")

        if op == "1":
            op1(tickets)
        elif op == "2":
            tickets.append(op2())
        elif op == "3":
            op3(tickets)
        elif op == "4":
            op4(tickets)
        elif op == "5":
            op5(tickets)
        elif op == "6":
            op6(tickets)
        elif op == "7":
            op7(tickets)
        elif op == "8":
            op8(tickets)
        elif op == "9":
            op9(tickets)
        elif op == "0":
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    principal()
