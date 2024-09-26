print ("hola soy un string, " + "soy otro string") #str + str

print (f"este es un string con un numero a la par {24}") #str + int

print (f"{300} es una pelicula") # int + str

lista_1 = [1, 2, 3]
lista_2 = ["cuatro", "cinco", "seis"]
sumandolistas = (lista_1 + lista_2)
print (sumandolistas) # list + list

lista_cosas_random = [1, "pollo", "azucar", "sal", "agua", "martillo", True] #list

print (lista_cosas_random[5])

print (lista_cosas_random[2])

print (lista_cosas_random[0])

print (lista_cosas_random[6])

for cosas_random in lista_cosas_random:
    print (f"hola voy a imprimir algo de la lista a continuación:  {cosas_random}") # str + list
print ("ya se acabo la lista :)")


num_float =  10.5
num_int = 10
total = num_float + num_int
print (total) # float + int

soy_real = True
soy_falso = False
falso_real = soy_real + soy_falso
print (falso_real) #bool + bool


#programa para solicitar nombre, edad y definirlo segun la edad

name = input ("ingrese su nombre: ")
last_name = input ("ingrese su apellido: ")
age = int(input("ingrese su edad: "))

if (age >= 60):
    print (f"Estimado {name}, usted es todo un adulto mayor")
elif (age < 60 and age >= 26):
    print (f"Estimado {name}, usted es un adulto maduro")
elif (age < 26 and age >= 18 ):
    print (f"Estimado {name}, usted es un adulto joven")
elif (age < 18 and age >= 12):
    print (f"Estimado {name}, usted es un adolescente")
elif(age < 12 and age >= 6):
    print (f"Estimado {name}, usted es un niño")
else:
    print (f"Estimado {name}, usted es un bebé aun")


#Programa numero secreto 

numero = int(input("Ingrese un numero del 1 al 10: "))
while (numero != 5):
    print ("Ese no es el numero secreto intentelo de nuevo")
    numero = int(input("Ingrese un numero del 1 al 10: "))
print ("Felicidades adivino el numero secreto! :D")



#Programa numero mayor


print ("A continuacion ingrese tres numeros que desee: ")
num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))
num3 = int(input("Numero 3: "))

if num1 > num2 and num1 > num3:
    mayor = num1
elif num2 > num1 and num2 > num3:
    mayor = num2
else:
    mayor = num3

print (f"El numero mayor ingresado fue {mayor}")


#Programa notas estudiante

total_notas = int(input("Ingrese la cantidad de notas recibidas: "))
contador_notas = 1
notas_aprobadas = 0
notas_desaprobadas = 0
promedio_desaprobadas = 0
promedio_aprobadas = 0

while (contador_notas <= total_notas):
    nota_ingresada = float(input(f"Ingrese la nota numero {contador_notas}: "))
    contador_notas += 1

    if (nota_ingresada < 70):
        notas_desaprobadas = (notas_desaprobadas + 1)
        promedio_desaprobadas = (promedio_desaprobadas + nota_ingresada)
    else:
        notas_aprobadas = (notas_aprobadas + 1)
        promedio_aprobadas = (promedio_aprobadas + nota_ingresada)
promedio_total = 0
promedio_total = (notas_aprobadas + notas_desaprobadas) / total_notas

promedio_desaprobadas = promedio_desaprobadas / notas_desaprobadas
promedio_aprobadas = promedio_aprobadas / notas_aprobadas

print (f"El estudiante tiene un total de {notas_desaprobadas} notas desaprobadas")
print (f"El promedio de notas desaprobadas es de: {promedio_desaprobadas}")
print (f"El estudiante tiene un total de {notas_aprobadas} notas aprobadas")
print (f"El promedio de notas aprobadas es de: {promedio_aprobadas}")
print (f"El estudiante tiene promedio total de: {promedio_total}")

