x = 500
y = 456
suma = 0

while x < 800:
    suma = suma + x + y
    x += 10
    y -= 2
    continue
else:
    suma = suma + x
print(f"la suma de todos esos números es igual a: {suma}")