#funcion de prueba para accesarla desde fuera 
def funcion_prueba():
    variable_string = "String de prueba"
    return variable_string

#accesando variable dentro de funcion desde afuera guardando en otra variable
afuera = funcion_prueba()
print (afuera)

#lista como variable global para probar accesar desde una funcion 
lista_prueba = [1, 2, 3]

#funcion que agrega un nuevo elemento a la lista 
def cambio_global(elemento):
    lista_prueba.append(elemento)
    print(f"Esta lista se le agrega un elemento mas {lista_prueba}")

cambio_global(4)
