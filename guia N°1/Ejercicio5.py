import random
lista = []

for i in range(20):
    numero = random.randint(40,350) 
    lista.append(numero)
print(lista)


buscar = input("¿Que número desea buscar en la lista? >")
ocurrencias = lista.count(numero)
if ocurrencias > 1:
    print(f"El número {buscar} se repite {ocurrencias} veces en la lista")
elif ocurrencias == 1:
    print(f"El número {buscar} se repite {ocurrencias} vez en la lista")
else:
    print(f"El número {buscar} no se encuentra en la lista en la lista")
