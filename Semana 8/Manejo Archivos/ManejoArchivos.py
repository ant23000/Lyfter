def main (path, output_path):
    try:
        with open(path, "r") as file:
            lines = file.readlines()    
        lines = [line.strip() for line in lines]
        lines.sort()
        
        with open(output_path, "w") as file:
            for line in lines:
                file.write(line + '\n')
        print("Las canciones se han guardado correctamente en el archivo: CancionesOrdenadas.txt")
        print(f"Esta es la lista de las canciones ordenadas alfabeticamente: {lines}")

    except Exception as ex:
        print(f"Hubo un error, saliendo del programa... {ex}")
    exit()

main ("Canciones.txt", "CancionesOrdenadas.txt")
