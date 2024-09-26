#funcion para order palabras dentro de un string 

def ordenando_strings (string):
    lista_palabras = string.split ("-")
    lista_palabras.sort ()
    string_ordenado = "-".join(lista_palabras)
    return string_ordenado

string_palabras = "papas-lechuga-agua-bebida-comida"
string_ordenado = ordenando_strings (string_palabras)
print (string_ordenado)