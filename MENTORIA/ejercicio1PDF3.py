print("\nEjercicio 1: Gestión de una lista de compras\n")

print("1- Crea una lista vacía llamada lista_compras:\n")
print("2- Agregá 3 productos usando .append()\n")
print("3- Mostrá cuántos productos hay con len()\n")
print("4- Eliminá el último producto con .pop()\n")
print("5- Mostrá la lista actualizada\n")
print("El objetivo es aprender .append(), .pop() y .len()\n")


# Solución al Ejercicio 1
print("-1:\n")
lista_compras = []  # Crear una lista vacía
print(f"La lista vacias: {lista_compras}")  # Mostrar la lista vacía

# Solucion al Ejercicio 2
print("\n-2:")
lista_compras.append("manzanas")# Agregar primer producto
lista_compras.append("pan")  # Agregar segundo producto
lista_compras.append("leche")  # Agregar tercer producto
print("lista de compras:", lista_compras)  # Mostrar la lista con productos

# Solución al Ejercicio 3
print("\n-3:")
print("Cantidad de productos en la lista:", len(lista_compras))  # Mostrar la cantidad de productos

# Solución al Ejercicio 4
print("\n-4:")
lista_compras.pop()  # Eliminar el último producto
print("Lista después de eliminar el último producto:", lista_compras)  # Mostrar la lista actualizada

# Solución al Ejercicio 5
print("\n-5:")
print("Lista actualizada de compras:", lista_compras)  # Mostrar la lista actualizada


