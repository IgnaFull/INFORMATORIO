print("#### OPERADORES DE PERTENENCIA ####")

texto = "Hola Info Python" 
palabra = "Info"

resutlado = palabra in texto
print(f"palabra in texto: {resutlado}")

lista = [10, 40, 20, 55]
numero= 5

resutlado = numero in lista
print(f"numero in lista: {resutlado}")


resutlado = numero not in lista
print(f"numero not in lista: {resutlado}")