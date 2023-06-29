n = int(input("Número de cubos a calcular: "))
lista = []
lista_impares = []

impar = -1
for i in range(1, n + 1):
    impar += 2
    suma = impar
    lista.append(impar)
    for j in range(2, i + 1):
        impar += 2
        suma += impar
        lista.append(impar)
    lista_impares = str(lista).replace(", ","+")        
    print(f"{i}^3 = {lista_impares} = {suma}")
    lista.clear()
    lista_impares = ""