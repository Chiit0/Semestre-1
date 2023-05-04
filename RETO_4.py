nombre1=str(input("Ingrese el nombre del paciente N°1\n"))
peso1=float(input("Ingrese peso del paciente N°1\n"))
estatura1=float(input("Ingrese la estatura del paciente N°1\n"))
edad1=int(input("Ingrese la edad del pacinte N°1\n"))
while edad1 < 0:
    edad1=int(input("ERROR, porfavor, ingrese una edad valida\n"))

paciente1=(nombre1, peso1, estatura1, edad1)
print(type(paciente1))

nombre2=str(input("Ingrese el nombre del paciente N°2\n"))
peso2=float(input("Ingrese peso del paciente N°2\n"))
estatura2=float(input("Ingrese la estatura del paciente N°2\n"))
edad2=int(input("Ingrese la edad del pacinte N°2\n"))
while edad2 < 0:
    edad2=int(input("ERROR, porfavor, ingrese una edad valida\n"))

paciente2=(nombre2, peso2, estatura2, edad2)

nombre3=str(input("Ingrese el nombre del paciente N°3\n"))
peso3=float(input("Ingrese peso del paciente N°3\n"))
estatura3=float(input("Ingrese la estatura del paciente N°3\n"))
edad3=int(input("Ingrese la edad del pacinte N°3\n"))
while edad3 < 0:
    edad3=int(input("ERROR, porfavor, ingrese una edad valida\n"))

paciente3=(nombre3, peso3, estatura3, edad3)

print(paciente1)
print(paciente2)
print(paciente3)