import csv

def ingreso_info_videojuegos():
    try:
        nombre = input("Ingrese el nombre del videojuego: ")
        genero = input("Ingrese el genero del videojuego: ")
        desarrollador = input("Ingrese el desarrollador del videojuego: ")
        clasificacion = input("Ingrese la clasificacion ESRB del videojuego: ")
        return {
            "nombre ": nombre,
            "genero ": genero,
            "desarrollador ": desarrollador,
            "clasificacion ": clasificacion
        }    
    except Exception as ex:
        print(f"Hubo un error, saliendo del programa... {ex}")
    exit()

videojuegos_headers= (
    "nombre ",
    "genero ",
    "desarrollador ",
    "clasificacion ",
)

def creacion_csv(path, data, headers):
    try:
        with open(path, "w", encoding="utf-8", newline= "") as file:
            writer = csv.DictWriter(file, headers)
            writer.writeheader()
            writer.writerows(data)
    except Exception as ex:
        print(f"Hubo un error, saliendo del programa... {ex}")
    exit()

def main():
    cantidad = int(input("Cuantos videojuegos desea ingresar? "))
    videojuegos = [ingreso_info_videojuegos() for i in range(cantidad)]
    print("Los datos se han guardados en el archivo: videojuegos.csv ")
    creacion_csv("videojuegos.csv", videojuegos, videojuegos_headers)
main()
