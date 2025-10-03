#conjuntos (sets) en Python
# Un conjunto es una colección desordenada de elementos únicos.
# Se definen utilizando llaves {} o la función set().

frutas = {"manzana", "pera", "manzana", "naranja"} # Crear un conjunto con elementos duplicados
frutas2=set()  # Crear un conjunto vacío

print(frutas)  # Salida: {'naranja', 'pera', 'manzana'}
print(frutas2)  # Salida: set()
print(type(frutas))  # Salida: <class 'set'>
print(type(frutas2))  # Salida: <class 'set'>

frutas.add("frutilla")  # Agregar un elemento al conjunto
print(frutas)  # Salida: {'naranja', 'pera', 'manzana', 'frutilla'}
frutas.remove("pera")  # Eliminar un elemento del conjunto
print(frutas)  # Salida: {'naranja', 'manzana', 'frutilla'}
frutas.discard("kiwi")  # Eliminar un elemento que no existe (no genera error)
print(frutas)  # Salida: {'naranja', 'manzana', 'frutilla'}
print(len(frutas))  # Salida: 3 (número de elementos en el conjunto)


A={1, 2, 3, 4}
B={3, 4, 5, 6}

print(A.union(B))  # Unión de conjuntos: {1, 2, 3, 4, 5, 6}
print(f"se puede hacer la union con el simbolo | : {A | B}")  # Unión usando el operador |
print(A.intersection(B))  # Intersección de conjuntos: {3, 4 }
print(f"se puede hacer la interseccion con el simbolo & : {A & B}")  # Intersección usando el operador &
print(A.difference(B))  # Diferencia de conjuntos: {1, 2}
print(f"se puede hacer la diferencia con el simbolo - : {A - B}")  # Diferencia usando el operador -
print(A.issubset(B))  # Verificar si A es subconjunto de B: False
print(f"A es subconjunto de B?: se hace con A<=B {A <= B}")  # Verificar subconjunto usando el operador <=
print(A.issuperset(B))  # Verificar si A es superconjunto de B: False
print(f"A es superconjunto de B? {A >= B}")  # Verificar superconjunto usando el operador >=


          
