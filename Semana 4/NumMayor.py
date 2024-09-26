#Correcion ejercicio numero mayor

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