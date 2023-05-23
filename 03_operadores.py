##OPERADORES ARITMETICOS
a = 20
b = 4
c = 69
d = 3
print("suma", a+b)
print("resta",c-a)
print("exponente",b**d)
#faltan

#GRAVEDAD Y VELOCIDAD
t=5.19
g=9.81
v=g*t
print(f"la velocidad de el objeto en caida libre es de: {v} m/s")
print(f"la velocidad de el objeto en caida libre es de: {v:.2f}m/s") #ACORTAR DECIMALES
print("la velocidad de el objeto en caida libre es de: {:.2f}" .format(v), "m/s")

#COMPLEJOS
c2=complex(3, -5)
print("el número complejo es:",c2)

print(c2.real)
print(c2.imag)

#A PROBAR
print("hola"*5) #funciona
#print("hola"*3.5*2) #ya no
print("hola" * 2)

##OPERADORES DE COMPARACIÓN
print("comparando números")
print(a == b) # "==" no es lo mismo que "="
print(b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print("\n")

#Comparar textos
animal_domestico="gato"
animal_salvaje="leopardo"
print(animal_domestico==animal_salvaje)
print(animal_domestico>animal_salvaje)
print(animal_domestico<animal_salvaje)

print(len(animal_domestico)>len(animal_salvaje))


bencina = False
encendido = True
edad = 19

#Utilizando el operador AND
if bencina and encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehichulo no puede arrancar")

#Utilizando el operador OR
if bencina or encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehichulo no puede arrancar")

#Utilizando NOT y OR/AND
if not bencina and encendido:
        print("UTILIZANDO NOT Y AND: El vehiculo puede avanzar")
else:
    print("El vehichulo no puede arrancar")

#OOOO
bencina = True
if not bencina or (encendido and edad>=18):
        print("El vehiculo puede avanzar")
else:
    print("El vehichulo no puede arrancar")

#01-WHILE
#while edad > 18:
#    print("El vehiculo puede avanzar") #BUCLE INFINITO

num = 0
while num <= 200:
     print(num)
     num += 2

while num <= 200:
    print(num)
    num+=2
else:
     print("Mi condición es igual o mayor a 200")

age = 19
print("usted puede votar" if age >= 18 else "no puedes votar aún")

Num = 0
while Num <=50:
    Num+=2
    if Num == 40:
      continue
    print(Num)