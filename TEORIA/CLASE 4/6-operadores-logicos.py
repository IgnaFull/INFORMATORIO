print("#### OPERADORES LOGICOS ####")

a=10
b=3
c=20

#AND
print("Operador AND")

#           true   and    true = true
#           true   and   false = false
#           false  and   false = false
resultado = 10 > 3 and 10 < 5
print(f"10 > 3 and 10 < 5: {resultado}")

#OR
print("Operador OR")

#           true   or   true = true
#           true   or  false = true
#           false  or  false = false
resultado = 10 > 3 or 10 < 5
print(f"10 > 3 or 10 < 5: {resultado}")

#NOT
print("Operador NOT")

#           not true = false
#           not false = true
resultado = (10 > 3)
print(f"(10 > 3): {resultado}")

resultado = not(10 > 3)
print(f"not(10 > 3): {resultado}")

#ejemplo con not.

esta_autenticado = True
if not esta_autenticado:
    print("Porfavor, incia sesion")









