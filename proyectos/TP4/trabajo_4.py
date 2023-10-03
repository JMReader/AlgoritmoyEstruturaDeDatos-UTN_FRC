from funciones import *

paises = [ #paises en los que se puede COBRAR en su respectivo orden de craga
    "Argentina",
    "Bolivia",
    "Brasil",
    "Paraguay",
    "Uruguay",
]
vehiculos = ["motocicletas ","automoviles ","camiones"] #tipos de vehiculos en su respectivo orden de carga

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
            matriz = op6()
            cant = len(matriz)
            for i in range(cant):
                # tambien podemos poner 5 pero para hacerlo escalable lo dejamos asi
                j = len(matriz[i])
                for k in range(j):
                    print("cantidad de", vehiculos[i], "que pasaron por el pais ", paises[k], "son:", matriz[i][k])
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
