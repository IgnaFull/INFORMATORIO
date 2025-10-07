####### DICCIONARIOS ######

# Un diccionario es una estructura de datos que almacena pares de clave-valor.
# Se definen entre llaves {}
# Son mutables (se pueden modificar, agregar, eliminar elementos)
# Son desordenados (no tienen indice) 
# Las claves deben ser únicas y de un tipo inmutable (string, numero, tupla inmutable)
# Los valores pueden ser de cualquier tipo de dato (incluso otros diccionarios)
# Se accede a los valores mediante su clave
# Se pueden recorrer con bucles for
# Se pueden anidar (diccionarios dentro de diccionarios)
# Se pueden convertir a otros tipos de datos (listas, tuplas, conjuntos)
# Se pueden copiar (shallow copy y deep copy)
# Se pueden eliminar elementos (del, pop, popitem, clear)
# Se pueden actualizar (update)
# Se pueden obtener las claves (keys), valores (values) y pares (items)
# Se pueden ordenar (sorted)
# Se pueden buscar elementos (in, get)
# Se pueden contar elementos (len)
# Se pueden fusionar (merge)
# Se pueden comprimir (zip)

# Crear un diccionario

mi_diccionario = {
    "nombre": "Juan",   # clave: valor
    "edad": 30,
    "ciudad": "Madrid",
    "es_estudiante": False,
    "notas": [8, 9, 7.5],
    "direccion": {
        "calle": "Calle Falsa 123",
        "codigo_postal": "28080",
    }
}

estudiante = {
    "nombre": "Ana",
    "edad": 22,
    "altura": 1.65,
    "cursos": {
        "Programacion": {
            "profesor": "Romero",
            "Horario":[
                "8:00",
                "10:00",
            ]
        },
        "Diseño": {
            "profesor": "Elias",
            "Horario":[
                "10:00",
                "12:00",
            ]
        }
    }
}

print(f"valor: {estudiante}, tipo: {type(estudiante)}")

print("El nombre del estudiante es:", estudiante["nombre"])
print(f"Los cursos en los que esta son: {estudiante['cursos']}")
print(f"El horario del curso de diesño es {estudiante['cursos']['Diseño']['Horario']}")
print(f"La hora de inicio del curso de diseño es {estudiante['cursos']['Diseño']['Horario'][0]}")
print(f"La hora de final del curso de diseño es {estudiante['cursos']['Diseño']['Horario'][1]}")
print(f"El profe del curso de diseño es: {estudiante['cursos']['Diseño']['profesor']}")

print("\n###### METODOS DE DICCIONARIOS ######\n")

# Acceder a un valor

print(f"\nClaves del diccionario: {list(estudiante.keys())}") # Devuelve una vista de las claves del diccionario
print(f"\nValores del diccionario: {estudiante.values()}") # Devuelve una vista de los valores del diccionario
print(f"\nPares clave-valor del diccionario: {estudiante.items()}") # Devuelve una vista de los pares clave-valor del diccionario



