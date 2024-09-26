#funcion para contabilizar mayusculas y minusculas de un string 

def contabilizador (string):
    mayusculas = sum(1 for characters in string if characters.isupper())
    minusculas = sum(1 for characters in string if characters.islower())

    print(f"En este string hay {mayusculas} mayusculas y {minusculas} minusculas")


string_prueba = "Utilizar MAYUSCULAS es como gritar"
#se utiliza la funcion con un string asignado
contabilizador (string_prueba)
