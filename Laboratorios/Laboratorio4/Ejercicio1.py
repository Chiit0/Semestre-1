trabajadores = [
    ["Juan", [700000, 650000, 690000]],
    ["María", [681000, 710000, 590000]],
    ["Pedro", [590000, 635000, 705000]]
]

def promedio(trabajador):
    for trab in trabajador:
        for j in trab:
            if isinstance(j,list):
                promedio = sum(j)/len(j)
                print(promedio)
                
def maximo(trabajador):
    maximo = max(trabajadores[trabajador][1])   # esto lo escribimos al reves en el papel
    return maximo


#def impuesto(sueldo):

for trabajador in trabajadores:
    for i in trabajador:
        if isinstance(i,list):
            promedio = sum(i)/len(i)
            print(promedio)
            print(max(i))

#promedio(trabajadores)

#print(maximo(trabajadores))
