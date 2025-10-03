print("#### STRINGS INTRO A F-STRINGS ####")

nombre= "Pepe"
apellido = "Fulanito"

mensaje= f"Hola {nombre} {apellido}"
print(mensaje)

mensaje_dos= "Hola {} {}".format(nombre, apellido)
print(mensaje_dos)

num_1 = 5
num_2 = 10

mensaje_tres= f"El resultado de sumar {num_1} + {num_2} es: {num_1 + num_2}"
print(mensaje_tres)

mensaje_tres= f"El resultado de sumar {num_1} + {num_2} es:\n {num_1 + num_2}"
print(mensaje_tres)

cadena = "Hola info " 
cadena_repetida = cadena * 3
print(cadena_repetida)

Texto = "cinco"
longitud = len(Texto)
print(f"La longitud de la cadena '{Texto}' es: {longitud}")

texto_dos ="Hola info ☺"
subcadena = texto_dos[0:11]
print(subcadena)

cadena_invertida = texto_dos[::-1]
print(cadena_invertida)

cadena_mayusculas = texto_dos.upper()
print(cadena_mayusculas)

cadena_minuscula = texto_dos.lower()
print(cadena_minuscula)

nobmre_dos = "diego oscar"
cadena_capitalizada = nobmre_dos.capitalize()
print(cadena_capitalizada)

cadena_tabulada = "\tHola\tinfo"
print(cadena_tabulada)

comillas_escapada = "en el" 'caso' 'tal cosa'
print(comillas_escapada)
comillas_escapada = "en el \"caso\" tal cosa"
print(comillas_escapada)