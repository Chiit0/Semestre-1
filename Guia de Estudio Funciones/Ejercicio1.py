counter = int(input("¿Cuantos números desea ingresar?\n"))
lista_numeros = []

def ingresar_numeros():
    print("Ingresa los números aquí:")
    for i in range(counter):
        lista_numeros.append(int(input(">")))

def suma_numeros(numbers):
    return sum(numbers)

def suma_pares(numbers):
    return sum(j if j%2 == 0 else 0 for j in numbers)

def suma_impares(numbers):
    return sum (x if x%2 == 1 else 0 for x in numbers)


ingresar_numeros()

print("suma todos los numeros",end=": ")
print(suma_numeros(lista_numeros))

print("suma todos los pares",end=": ")
print(suma_pares(lista_numeros))

print("suma todos los impares",end=": ")
print(suma_impares(lista_numeros))