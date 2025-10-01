# Nivel 1  \ ENCUESTA SIMPLE {
#     Guarda la respuestas de vaias personas (3) en un diccionario con nombre clave y una 
#     lista de sus respuesta como valor
# EL usuario tien que tener la posbilidad de ingresar un nombre de algun producto y preguntarles si les gusto o no el producto.

encuesta = {}

producto = input("Ingrese el nombre del producto: ")

for i in range(3):
    nombre = input("Ingrese su nombre: ")
    respuesta = input(f"¿Te gustó el producto {producto}? (Si/No): ")
    if nombre in encuesta:
        encuesta[nombre].append(respuesta)
    else:
        encuesta[nombre] = [respuesta]

print(encuesta)

