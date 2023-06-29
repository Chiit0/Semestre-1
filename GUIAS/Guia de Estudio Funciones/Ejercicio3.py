def bisiesto(año):
    return año%4 == 0

year_input = int(input("Ingrese el año: "))

if bisiesto(year_input):
    print(f"{year_input} es un año bisiesto")
else:
    print(f"{year_input} no es un año bisiesto")