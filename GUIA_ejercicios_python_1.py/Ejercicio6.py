#Se necesita saber si en ambos grupos tienen alg´un estudiante en com´un y, en caso
#de que as´ı sea, imprimir los nombres de esos estudiantes. Todo esto utilizando Sets.

grupo1={"Marcos", "Gabriela", "Benjamin", "Matias"}
grupo2={"Marcos", "Nicolás", "Diego", "Matias"}

print(f"Se repiten los nombres {grupo1.intersection(grupo2)}")