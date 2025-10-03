# Ejercicio 3: Diccionario de estudiante
# Dado este diccionario:
# estudiante = {
# "nombre": "Ana",
# "edad": 20,
# "materias": ["Matemática", "Historia"]
# }
# 1- Mostrá el nombre y la edad
# 2- Agregá una materia nueva a la lista materias
# 3- Mostrá cuántas materias cursa con len()
# 4- Usá .get() para obtener la clave “promedio” con valor por defecto 0
# El objetivo es obtener acceso al diccionario, lista dentro de diccionario y aprender .get() y len()

print("Ejercicio 3: Diccionario de estudiante")

estudiante = {
    "nombre": "Ana",
    "edad": 20,
    "materias": ["Matemática", "Historia"]
}

# 1- Mostrá el nombre y la edad
print(f"Nombre: {estudiante["nombre"]}, Edad: {estudiante["edad"]}") 

# 2- Agregá una materia nueva a la lista materias
estudiante["materias"].append("Programacion")
print(f"Materias actualizadas: {estudiante["materias"]}")

# 3- Mostrá cuántas materias cursa con Len()
cantidad_materias = len(estudiante["materias"])
print(f"Cantidad de materias cursadas: {cantidad_materias}")

# 4- Usá .get() para obtener la clave “promedio” con valor por defecto 0
promedio = estudiante.get("promedio", 0)
print(f"Promedio: {promedio}")
# El objetivo es obtener acceso al diccionario, lista dentro de diccionario y aprender .get() y len()