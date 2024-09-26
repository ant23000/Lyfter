
#Dic Informacion sobre hotel

info_hotel = {
    "nombre": "hotelito bonito",
    "numero_de_estrellas": 3,
    "habitaciones": [
        {"numero": 1, "piso": 5, "precio_por_noche": 200},
        {"numero": 2, "piso": 50, "precio_por_noche": 2000},
        {"numero": 3, "piso": 500, "precio_por_noche": 20000},
    ]
}


#Dic de 2 listas    

lista_keys = ["nombre", "color", "edad"]
lista_values = ["Pablo", "rojo", 90]

diccionario_1 = {}
for index in range (len(lista_keys)):
    diccionario_1[lista_keys[index]] = lista_values[index]

print (diccionario_1)


#Lista para elementos eliminados 

diccionario_random = {
    "nombre" : "Rigoberto",
    "musica" : "rock",
    "apellido" : "Araya",
    "edad" : 75,
    "email" : "rigaraya1@gmail.com",
}

deleted_info = {}
info_to_delete = ["musica", "apellido"]
for info in info_to_delete:
    deleted_info[info] = diccionario_random.pop(info)

print(diccionario_random)
print(f"Info deleted: {deleted_info}")



#Ejercicio ventas

lista_ventas = [
    {
        "date" : "6/2/2024",
        "customer_email" : "josepablo@gmail.com",
        "items": [
            {
                "name" : "Arroz",
                "upc" : "C1",
                "unit_price" : 3000,
            },
            {
                "name" : "Frijoles",
                "upc" : "C2",
                "unit_price" : 500,
            },
            {
                "name" : "Pan",
                "upc" : "C3",
                "unit_price" : 700,
            },
            {
                "name" : "Azucar",
                "upc" : "C4",
                "unit_price" : 8000,
            }
        ],
    },
    {
        "date" : "5/17/2024",
        "customer_email" : "mariamario@yahoo.com",
        "items": [
            {
                "name" : "Harina",
                "upc" : "C5",
                "unit_price" : 600,
            },
            {
                "name" : "Aguacate",
                "upc" : "C5",
                "unit_price" : 2000,
            },
            {
                "name" : "Arroz",
                "upc" : "C1",
                "unit_price" : 3000,
            }
        ],
    },
]

ventas_por_item = {}

for venta in lista_ventas:
    for item in venta["items"]:
        upc = item["upc"]
        precio_item = item["unit_price"]
        if upc in ventas_por_item:
            ventas_por_item[upc] += precio_item
        else:
            ventas_por_item[upc] = precio_item

print (ventas_por_item)