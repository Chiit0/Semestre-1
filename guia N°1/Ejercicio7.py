
f = int(input("Ingrese el número a clacular el factorial: "))
result = 1

#cuando "f == 0" solo ocurren multiplicaciones neutras (por 1), lo mismo a que no haya ninguna operación,
#esa es la razon de porque 0! es igual a 1.
for i in range(1,f+1):
    result = result * i

print(result)