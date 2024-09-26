def menu_calculadora ():
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Borrar resultado")


def main ():
    numero_actual = 0
    while True:
        try:
            menu_calculadora()
            print(f"El numero actual es: {numero_actual}")
            solicitud = int(input("Por favor ingrese el numero de solicitud siguiendo el menu"))
            if solicitud == 1:
                while True:
                    try: 
                        num = float(input("Ingrese el numero que desea sumar: "))
                        numero_actual += num
                        break
                    except ValueError as ex:
                        print("El numero ingresado no es valido, intente de nuevo")
            elif solicitud == 2:
                while True:
                    try:
                        num = float(input("Ingrese el numero que desea restar: "))
                        numero_actual -= num
                        break
                    except ValueError as ex:
                        print("El numero ingresado no es valido, intente de nuevo")
            elif solicitud == 3:
                while True:
                    try:
                        num = float(input("Ingrese el numero que desea multiplicar: "))
                        numero_actual *= num
                        break
                    except ValueError as ex:
                            print("El numero ingresado no es valido, intente de nuevo")
            elif solicitud == 4:
                while True:
                    try:
                        num = float(input("Ingrese el numero que desea dividir: "))
                        numero_actual /= num
                        break
                    except ValueError as ex:
                        print("El numero ingresado no es valido, intente de nuevo")
            elif solicitud == 5:
                while True:
                    try:
                        numero_actual = 0
                        break
                    except ValueError as ex:
                        print("El numero ingresado no es valido, intente de nuevo")
            else:
                print("Numero de solcitud no es valida")
        except ZeroDivisionError as ex:
            print("No se puede hacer una division por cero, intentelo de nuevo")
        except ValueError as ex:
            print(f"El valor ingresado no es valido {ex}")
        except Exception as ex:
            print(f"Hubo un error, saliendo del programa... :( {ex}")
            break

main()
