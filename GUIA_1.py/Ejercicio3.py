#Desarrollar un programa que al momento de ingresar los lados de un triangulo
#(a, b y c) en consola, indique si es equil´atero, is´osceles o escaleno. Tambi´en se
#solicita calcular el ´area utilizando la formula de Her´on:
Area = 0
while Area <=0:
    print("El triangulo ingresado no puede existir")
    print("Ingrese la longitud de los 3 lados en centimetros")
    a = float(input(""))
    b = float(input(""))
    c = float(input(""))
    sP = (a + b + c)/2
    Area = sP*(sP-a)*(sP-b)*(sP-c)
Area = Area**(1/2)

if a == b == c:
    print("es un triangulo equilátero")
elif a == b or a == c or b == c:
    print("es un triangulo isóceles")
else:
    print("es un triangulo escaleno")

print(f"y su área es de: {Area}cm^2")