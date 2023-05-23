input_num = int(input("Ingrese el número a probar "))
print(f"{input_num}:")

if input_num%2==0:
    print("Es un número par")
else:
    print("Es un número impar")

if input_num < 50:
    print("Es menor que 50")
elif input_num > 50:
    print("Es mayor que 50")
else:
    print("Obviamente no es ni mayor ni menor que 50")

primo = True
for i in range(2,input_num):
    if input_num%i == 0:
        primo = False
        break

if primo == True:
    print("Y también es un número primo")