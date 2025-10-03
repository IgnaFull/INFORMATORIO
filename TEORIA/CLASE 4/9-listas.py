print("#### LISTAS ####")

# Se definen entre corchetes [].
# Pueden contener cualquier tipo de dato.
# Son mutables (se pueden modificar, agregar, eliminar elementos)
# Son ordenadas (elemntos tienen indice)

#          0    1    2      3
lista= ["info", 10, 1.75, True]
print(f"valor: {lista}, tipo: {type(lista)} ")

#                 -1
#          0 1 2 3 4 
numeros = [1,2,3,4,5,3,"info","info","algo"]
print(f"Primer elemento de la lista: {numeros[0]}")  # Acceder al primer elemento de la lista
print(f"Ultimo elemento de la lista: {numeros[-1]}") # Acceder al ultimo elemento de la lista

#slicing

#                 12345678
print(f"Primero 3 elementos: {numeros[:3]}") # Acceder a los primeros 3 elementos
print(f"Ultimos 2 elementos: {numeros[-2:]}") # Acceder a los ultimos 2 elementos
print(f"elementos del medio: {numeros[1:-1]}") # Acceder a los elementos del medio

print(f"longitud de la lista: {len(numeros)}") # Obtener la longitud de la lista

print(f"veces que aparece el 3: {numeros.count(3)}") # Contar cuantas veces aparece un elemento en la lista

numeros.append(6) # Agregar un elemento al final de la lista
print(f"Lista despues de agregar un elemento: {numeros}")

numeros [0] = True
print(f"despues de modificar: {numeros}")

numeros.pop() # Eliminar el ultimo elemento de la lista
print(f"Lista despues de eliminar el ultimo elemento: {numeros}")

numeros.remove(3) # Eliminar un elemento especifico de la lista
print(f"Lista despues de eliminar un elemento especifico: {numeros}")



matriz = [
    #0 1 2
    [1,2,3], #0
    [4,5,6], #1
    [7,8,9], #2
]   

print(f"matriz: {matriz}")

print (f"elemnto en [1][1]: {matriz[1][1]}") # Acceder a un elemento especifico de una matriz (lista de listas)


