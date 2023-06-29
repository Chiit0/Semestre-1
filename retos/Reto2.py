Estudiante=input("Ingrese nombre del estudiante\n")
Asignatura=input("Ingrese asignatura\n") 
NotaLab1=input("Ingrese la Nota Laboratorio n.° 1\n") #30%
NotaLab2=input("Ingrese la Nota Laboratorio n.° 2\n") #70%
Clase={
    "Estudiante":Estudiante,
    "Asignatura":Asignatura,
    "Nota Laboratorio 1":NotaLab1,
    "Nota Laboratorio 2":NotaLab2
}
NotaFinal=float(NotaLab1)*0.3 + float(NotaLab2)*0.7

Clase["Promedio"] = round(NotaFinal,1)
print(Clase)
