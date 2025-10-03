# Ejercicio 2: Contar apariciones
# Dada la lista:
# colores = ["rojo", "azul", "verde", "rojo", "azul", "rojo"]
# 1- Mostrá cuántas veces aparece “rojo” usando .count().
# 2- Reemplazá el primer “verde” por “amarillo”
# 3- Mostrá la lista final
# El objetivo es usar el método .count(), acceso por índice, asignación de valor.

print("\nEjercicio 2: Contar apariciones\n")

print("1- Contá cuántas veces aparece 'rojo' en la lista colores:\n")

print("2- Reemplazá el primer 'verde' por 'amarillo':\n")

print("3- Mostrá la lista final:\n")

# Solución al Ejercicio 2

colores = ["rojo", "azul", "verde", "rojo", "azul", "rojo"]  # Lista inicial
# Solución al punto 1
print("-1:")
cantidad_rojo = colores.count("rojo")  # Contar apariciones de "rojo"
print(f"La palabra 'rojo' aparece {cantidad_rojo} veces en la lista.")  # Mostrar el conteo
# Solución al punto 2
print("\n-2:")
indice_verde = colores.index("verde")  # Encontrar el índice del primer "verde"
colores[indice_verde] = "amarillo"  # Reemplazar "verde
print("Se ha reemplazado 'verde' por 'amarillo'.")  # Confirmar el reemplazo
# Solución al punto 3
print("\n-3:")
print("Lista final de colores:", colores)  # Mostrar la lista final
# Salida esperada: ['rojo', 'azul', 'amarillo', 'rojo', 'azul', 'rojo']