#funcion para definir si los numeros son primos 

def si_primo (num):
    if num < 2:
        return False
    for i in range (2, num):
        if num % i == 0:
            return False
    else: return True

#funcion para crear la lista de los numeros primos 
def filtro_primos (lista):
    return [num for num in lista if si_primo(num)]

lista_random = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_primos =  filtro_primos (lista_random)
print (f"La lista de los numeros primos es {lista_primos}")

