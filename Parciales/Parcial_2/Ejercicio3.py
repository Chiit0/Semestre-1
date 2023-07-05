temperaturas_minimas = {9, 5, 2, 7, 6, 1}
temperaturas_maximas = {12, 14, 11, 10, 15, 9}

intersect_temp = temperaturas_maximas.intersection(temperaturas_minimas)
if 2 in intersect_temp:
    print("El número 9 se encuentra en ambos set")

if 6 in temperaturas_maximas or 6 in temperaturas_minimas or\
17 in temperaturas_minimas or 17 in temperaturas_maximas:
    print("La temperatura 6°C o 17°C se encuentra en uno de los 2 set")

temperaturas_maximas = {i**4 for i in temperaturas_maximas}
temperaturas_minimas = {i**4 for i in temperaturas_minimas}

temperaturas_unidas = temperaturas_minimas.union(temperaturas_maximas)

print(temperaturas_unidas)

