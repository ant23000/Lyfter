#Ejercicio de imprimir 2 listas al mismo tiempos

lista_1 = ["Hola", "es", "prueba", "imprimir", "de 2 listas"] 
lista_2 = ["esto", "una", "para", "valores", "al mismo tiempo"] 

index = 0
for index in range (0, len(lista_1 and lista_2)):
    print (f" {lista_1[index]} {lista_2[index]}") 



#String deletreado en reversa

string_prueba = "Esto es un string al reves"

for characters in reversed(string_prueba):
    print (characters)



#Intercambio primer y ultimo elemento de una lista

lista_intercambio = [1, 2, 3 ,4 ,5]

primer_index = 0
ultimo_index = len(lista_intercambio) - 1

for index in range(len(lista_intercambio)):
    if index == primer_index:
        lista_intercambio[primer_index], lista_intercambio[ultimo_index] = lista_intercambio[ultimo_index], lista_intercambio[primer_index]

print(lista_intercambio)


#Eliminar todos los numeros impares de una lista 

lista_par_impar = [2, 4, 5, 6, 8, 10, 11, 12, 13, 14]

for num in lista_par_impar:
    if num % 2 != 0:
        lista_par_impar.remove(num)
print (lista_par_impar)



#Ingresar 10 mnumeros y mostrar mayor 

lista_numeros = []

for index in range(10):
    num = int(input(f"Ingrese el número {index + 1}: "))
    lista_numeros.append(num)

mayor = lista_numeros[0]

for num in lista_numeros:
    if num > mayor:
        mayor = num

print(f"La lista de los numeros ingresados es: {lista_numeros}")

print(f"El numero mas alto ingresado fue: {mayor}")



