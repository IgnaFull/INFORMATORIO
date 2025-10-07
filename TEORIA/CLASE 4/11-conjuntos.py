######### Conjuntos #########+

# los conjuntos se definene entre llaves {}
# No permiten elementos duplicados
# No son ordenados (no tienen indice)
# Son mutables (se pueden modificar, agregar, eliminar elementos)
# Se pueden realizar operaciones matematicas como union, interseccion, diferencia

print("#### CONJUNTOS ####")

colores = {"rojo", "verde", "azul"}

print(f"valor: {colores}, tipo: {type(colores)} ")

colores.add("amarillo") # Agregar un elemento al conjunto
print(f"conjunto despues de agregar un elemento: {colores}")

colores.remove("verde") # Eliminar un elemento del conjunto
print(f"conjunto despues de eliminar un elemento: {colores}")

# colores[0] # No se puede acceder a un elemento por su indice

colores.discard("naranja") # Eliminar un elemento del conjunto si existe, si no existe no hace nada
print(f"conjunto despues de intentar eliminar un elemento que no existe: {colores}")

