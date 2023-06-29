lista_numeros = []

def ingresar_numeros():
    number = int(input("Ingrese los numeros naturales aquí (escriba '-1' para terminar) \n>"))
    while number != -1:
        if number <= 0:
            number = int(input("Solo se permiten números naturales, ingrese otro \n>"))
        else:
            lista_numeros.append(number)
            number = int(input(">"))

def numero_mayor():
    return max(lista_numeros)

def suma_numeros():
    return sum(lista_numeros)

def suma_pares():
    return sum(p if p%2 == 0 else 0 for p in lista_numeros)

def suma_impares():
    return sum(i if i%2 == 1 else 0 for i in lista_numeros)

def promedio():
    return suma_numeros() // len(lista_numeros) #Si el ejemplo dio 5, entonces el promedio deneria los decimales

def comparar_max_a_promedio():
    if numero_mayor() > promedio():
        print(f"El número mayor ({numero_mayor()}) es mayor que el promedio ({promedio()})")
    elif numero_mayor() < promedio():
        print(f"El número mayor ({numero_mayor()}) es menor que el promedio ({promedio()})")
    else:
        print(f"El número mayor ({numero_mayor()}) es igual al promedio ({promedio()})")

ingresar_numeros()

print(f"El numero mayor ingresado fue: {numero_mayor()}")
print(f"La suma total es: {suma_numeros()}")
print(f"La suma de pares es: {suma_pares()}")
print(f"La suma de impares es: {suma_impares()}")
print(f"El promedio es: {promedio()}")

comparar_max_a_promedio()
