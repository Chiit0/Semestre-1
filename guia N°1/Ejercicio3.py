td=12000*10
tn= 16000*10
tdx=14000*10
tnx= 19000*10
#agrego de inmediato el pago extra del domingo
primer_empleado= {
    "pago del lunes":tn,
    "pago del martes":tn,
    "pago del miercoles":tn,
    "pago del jueves":td,
    "pago del viernes":td,
    "pago semanal":(tn*3)+(td*2)
}
print("el primer empleado recibio")
print (primer_empleado)

segundo_empleado= {
    "pago del martes":tn,
    "pago del miercoles":tn,
    "pago del jueves":tn,
    "pago del domingo":tdx,
    "pago semanal":(tn*3)+(tdx)
}
print ("el segundo empleado recibio")
print (segundo_empleado)

tercer_empleado= {
    "pago del miercoles":td,
    "pago del jueves":td,
    "pago del viernes":td,
    "pago del sabado":tn,
    "pago del domingo":tnx,
    "pago semanal":(td*3)+(tn+tnx)
}
print ("el tercer empleado recibio")
print (tercer_empleado)
