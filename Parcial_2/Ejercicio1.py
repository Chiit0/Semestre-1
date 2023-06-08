palabra = input("Ingrese la palbra aquí")
print(palabra)

if palabra.lower() == palabra[::-1].lower():
    print(f"{palabra} es un palindromo") 
else:
    print(f"{palabra} no es un palindromo")