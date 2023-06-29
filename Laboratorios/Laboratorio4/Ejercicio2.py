a = [10,80,15,30,20]
b = [20,45,80,20,10]
c = [20,35,60,90,20]

intersect = []

def valores_comunes():
    for d in a:
        for e in b:
            for f in c:
                if e == d == f:
                    intersect.append(e)
    return set(intersect)

global lista_completa
lista_completa = []

def concatenar():
    lista_completa = a + b + c
    return lista_completa
lista_completa = concatenar()

def eliminar_duplicados(lista):
    lista = set(lista)
    return lista
lista_completa = eliminar_duplicados(lista_completa)


def descendente(lista):
    lista = list(lista)
    lista.sort()
    lista = lista[::-1]
    return lista
lista_completa = descendente(lista_completa)

def reemplazo(lista):
    lista[6] = 100
    return lista 
lista_completa = reemplazo(lista_completa)

print(lista_completa)