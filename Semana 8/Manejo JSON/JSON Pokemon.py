import json

#aqui lee el json existente
def pokemones_existentes (path):
    try:
        with open(path, "r") as file:
            pokemones = json.load(file)
            return pokemones
    except Exception as ex:
        print(f"Hubo un error, saliendo del programa... {ex}")
    exit()

#aqui solicita la nueva informacion

def agregar_pokemon(pokemones):
    try:
        nombre = input("Ingrese el nombre del nuevo Pokemon")
        tipo = input("Ingrese el tipo de Pokemon")

        hp = int(input("Ingrese los puntos de HP: "))
        ataque = int(input("Ingrese los puntos de Ataque: "))
        defensa = int(input("Ingrese los puntos de Defensa: "))
        ataque_especial = int(input("Ingrese los puntos de Ataque Especial: "))
        defensa_especial = int(input("Ingrese los puntos de Defensa Especial: "))
        velocidad = int(input("Ingrese los puntos de Velocidad: "))

        nuevo_pokemon = {
            "name": {
                "english": nombre
            },
            "type": tipo,
            "base": {
                "HP": hp,
                "Attack": ataque,
                "Defense": defensa,
                "Sp. Attack": ataque_especial,
                "Sp. Defense": defensa_especial,
                "Speed": velocidad
            }
        }

        pokemones.append(nuevo_pokemon)
        return pokemones
    except Exception as ex:
        print(f"Hubo un error, saliendo del programa... {ex}")
    exit()


#aqui agrega la informacion al archivo 
def guardar_pokemones(path, pokemones):
    try:
        with open(path, "w", ) as file:
            json.dump(pokemones, file, indent=4)
    except Exception as ex:
        print(f"Hubo un error, saliendo del programa... {ex}")
    exit()

def main():
    file = "pokemones.json"
    pokemones = pokemones_existentes(file)

    pokemones = agregar_pokemon(pokemones)
    
    guardar_pokemones (file, pokemones)
    print("El nuevo Pokemon ha sido guardado exitosamente")

if __name__ == "__main__":
    main()
