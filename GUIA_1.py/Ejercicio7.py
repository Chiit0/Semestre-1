#Crear una lista con nombres de 5 trabajadores y otra lista con las edades de estos 5 trabajadores,
#Se solicita relacionar ambas listas en una sola estructura. La salida puede ser en tuplas o en un diccionario.

trabajadores=["Luis", "Pepe", "Manolo", "Benjamin", "Diego"]
edades = [23, 36, 49, 19, 40]
junta = tuple(zip(trabajadores, edades))
print(junta)