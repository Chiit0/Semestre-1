#Escribir un programa que pida al usuario ingresar dos palabras y las guarde en
#dos variables diferentes. Luego imprimir cu´al palabra tiene m´as caracteres y cu´al
#tiene menos caracteres
palabra1=input("Ingrese la primera palabra")
palabra2=input("Ingrese la segunda palabra")

if len(palabra1) > len(palabra2):
    print(f"{palabra1} es la palabra mayor")
elif len(palabra2) > len(palabra1):
    print(f"{palabra2} es la palabra mayor")
else:
    print("son igual de largas")