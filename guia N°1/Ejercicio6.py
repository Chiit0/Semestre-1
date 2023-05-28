#Simular el comportamiento de un reloj digital, imprimiendo la hora, minutos y segundos
#de un día desde las 00:00:00 horas hasta las 23:59:59 horas.
HH=0
MM=0
SS=0


while HH<24:
    if HH == 24:
        break
    SS += 1
    if SS == 60:
        SS = 0
        MM += 1
    if MM == 60:
        MM = 0
        HH += 1
    print(f"{HH:02}:{MM:02}:{SS:02}")