#Crear un algoritmo que solicite por consola las 3 notas de los laboratorios realizados en el ramo de Programaci´on. Luego obtener el promedio ponderado de la
#siguiente manera:
#Promedio Ponderado = Lab1 * 0,3 + Lab2 * 0,4 + Lab3 * 0,3
#Si el promedio es menor a 4,0 debe imprimir el mensaje que el estudiante reprob´o
#la asignatura. Si el promedio es superior a 4,0, indicar que el estudiante aprobo
#la asignatura. Si la nota es superior 6,0, debe mostrar el mensaje: el estudiante
#aprobo con distinci´on.

Lab1 = float(input("Ingrese la nota del primer laboratorio: "))
Lab2 = float(input("Ingrese la nota del segundo laboratorio: "))
Lab3 = float(input("Ingrese la nota del tercer laboratorio: "))

promedio = Lab1*0.3 + Lab2*0.4 + Lab3*0.3
if promedio > 6 and promedio <= 7:
    print(f"¡con un promedio de {round(promedio,1)} El estudiante aprobo con distinción!")
elif promedio > 4 and promedio < 6:
    print(f"El estudiante aprobo con un promedio de {round(promedio,1)}")
elif promedio < 4 and promedio > 1:
    print(f"El estudiante reprobo con un promedio de {round(promedio,1)}")
else:
    print("Error, las notas ingresadas no son validas")