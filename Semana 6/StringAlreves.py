#funcion para darle vuelta a un string
def string_alreves(string):
    for characters in reversed(string):
        print (characters)

string_random = "Anita lava la tina"

string_alreves(string_random)
