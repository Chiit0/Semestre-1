def sumar_lista(lista):
    suma = 0
    for elemento in lista:
        if isinstance(elemento, list):
            suma += sumar_lista(elemento)
        else:
            suma += elemento
    return suma
mi_lista = [21, 20, 18, 15, 15, 12, 12, 12, 10, 9, 9, 8, 8, 3, 3, 2, [4, 5, 6]]
resultado = sumar_lista(mi_lista)
print(resultado)