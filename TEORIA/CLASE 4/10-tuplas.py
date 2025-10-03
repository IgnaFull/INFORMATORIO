print("#### TUPLAS ####")

# se  defienen entre parentesis ()
# pueden contener cualquier tipo de dato
# son inmutables (no se pueden modificar, agregar, eliminar elementos)
# son ordenadas (elementos tienen indice)

tupla = ("manzanas", "naranjas", "frutillas", "duraznos")
print(f"valor: {tupla}, tipo: {type(tupla)}") 

print(f"primer elemento de la tupla: {tupla[0]}") # Acceder al primer elemento de la tupla
print(f"ultimo elemento de la tupla: {tupla[-1]}") # Acceder al ultimo elemento de la tupla

# slicing
print(f"primeros 2 elementos: {tupla[:2]}") # Acceder a los primeros 2 elementos
print(f"ultimos 2 elementos: {tupla[-2:]}") # Acceder a los ultimos 2 elementos
print(f"elementos del medio: {tupla[1:-1]}") # Acceder a los elementos del medio
print(f"longitud de la tupla: {len(tupla)}") # Obtener la longitud de la tupla          

# tupla[0] = "peras" # Error! No se puede modificar una tupla
# tupla.append("peras") # Error! No se puede agregar elementos a una tupla
# tupla.pop() # Error! No se puede eliminar elementos de una tupla
# tupla.remove("naranjas") # Error! No se puede eliminar elementos de una tupla
print(f"veces que aparece 'manzanas': {tupla.count('manzanas')}") # Contar cuantas veces aparece un elemento en la tupla
print(f"indice de 'frutillas': {tupla.index('frutillas')}") # Obtener el indice de un elemento en la tupla
# tuplas anidadas
tupla_anidada = (
    (1,2,3), #0
    (4,5,6), #1
    (7,8,9), #2
)
print(f"tupla anidada: {tupla_anidada}")
print(f"elemento en [1][1]: {tupla_anidada[1][1]}") # Acceder a un elemento especifico de una tupla anidada
# convertir tupla a lista
tupla_a_lista = list(tupla)
print(f"tupla convertida a lista: {tupla_a_lista}, tipo: {type(tupla_a_lista)}")
# convertir lista a tupla
lista_a_tupla = tuple(tupla_a_lista)

a,b,c=tupla

print("Desepaquetado de tupla:")
print(f"Depesaquetado: a={a}, b={b}, c={c}")



