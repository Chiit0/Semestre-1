#9. Se tiene la siguiente lista de enteros:
#numeros = [4, 3, 8, 12, 6, 10, 14, 3, 6]
#Se solicita:
#a) Eliminar el ´ultimo elemento de la lista
#b) Agregar en la primera posici´on el n´umero 2
#c) Eliminar los n´umeros duplicados de la lista
#d) Obtener la media y la mediana de la lista
numeros = [4, 3, 8, 12, 6, 10, 14, 3, 6]
numeros.pop(-1)
numeros.insert(0,2)
numeros = set(numeros)
numeros = list(numeros)
numeros.sort()

media = sum(numeros) / len(numeros)

indice = len(numeros)//2
if len(numeros)%2 == 0:
    mediana = (numeros[indice] + numeros[indice-1]) / 2
else:
    mediana = numeros[indice]


print(f"la media de la lista es: {media}")
print(f"la mediana de la lista es: {mediana}")