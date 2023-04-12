#VARIABLES NUMERICAS
estatura = 1.71
peso = 70
complejo = 1 +4j

print("Impresion del número complejo:", complejo)

#OPERACIÓN ARITMETICA BASICA
imc = peso/estatura**2
print(imc)

#02 DATOS DE TIPO CADENA DE CARACTERES
asignatura = "Programación"
carrera = "Ingenierría Civil en Informatíca"

print("la asignatura de", asignatura, "corresponde a la carrera de", carrera)


#VALORES BOOLEANOS
ampolleta = False
interruptor = True

#Con type sabemos el tipo de datos
print(type(ampolleta))

#DATOS DE TIPO ARRAY
estudiantes = ["Matias", "Marco", "Cristobal", "Sebastian"]
num = [1,2,3,4,5,6]
print(estudiantes)
print(num)

nueva_lista = list()
print("esta es una lista vacia", nueva_lista)
print("hola pepe")

#ARRAY Y LISTAS
estudiantes = ("Matias", "Marco", "Cristobal", "Sebastian")
num = (1,2,3,4,5,6,7)
lenguaje = ("Python")

print(estudiantes[1])
print(estudiantes[-2])
#nose

print(list("Pyhton"))
print(list(range(10)))
print("\n")

print("suma de listas", estudiantes + num)
data = [1,"Matias",True,100,"Caballo"]
codigo, minombre, estado, peso, animal = data
print(data)
print(minombre)


# - TUPLAS - 

grupo1=("Daniel", "Cristian", 10, False, 300)
print(type(grupo1))

print("Daniel se repite", grupo1.count("Daniel"), "veces")
print("Daniel esta en la posicipon", grupo1.index("Daniel"))

### grupo1[0]="Pepe" NO funciona, las tuplas no son mutables, no soportan reasignación de items ###

#obteniendo  un trozo de la tupla
print(grupo1[0:3]) 

#¿como modifico una tupla entonce'?
grupo1=(list(grupo1))
print(type(grupo1))
print("\n")


# - SET (conjuntos) -
# formas de iniciar un set

conjunto_vacio=(set())
conjunto_vacio = {}
print(conjunto_vacio)
print(type(conjunto_vacio))
conjunto_colores=set({"Azul", "Rojo", "Verde", "Amarillo"})
conjunto_animales={"Gato", "Perro", "Pollo", "Vaca"}

print(type(conjunto_colores))
print(type(conjunto_animales))
#print(conjunto_colores[0]) NO SE PUEDE - #Los set no ordenan los datos:
print("el primer set tiene los colores:", conjunto_colores)
print("el segundo set tiene los animales", conjunto_animales)