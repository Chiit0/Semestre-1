def ingresar_nombres():
    nombres = []

    nombre = input("Ingrese los nombres aquí ('q' para finalizar):  \n>")
    while nombre != "q":
        nombres.append(nombre)
        nombre = input(">")
    return nombres

def longitud_palabras():
    return [len(w) for w in nombres]

def imprimir():
    print("Longitud de cada nombre:")
    for i in range(len(nombres)):
        print(f"{nombres[i]} = {letras[i]}")

nombres = ingresar_nombres()
letras = longitud_palabras()
imprimir()


