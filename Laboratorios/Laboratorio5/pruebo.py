dia1 = 3
mes1 = 4
año1 = 2001

dia2 = 2
mes2 = 4
año2 = 2001

dif_dia = dia2 - dia1
dif_mes = mes2 - mes1
dif_año = año2 - año1

print(dif_año)
print(dif_mes)
print(dif_dia)


total_dias = dif_año*365 + dif_mes * 30 + dif_dia
if dif_dia < 0:
    dif_mes -= 1
total_meses = dif_año*12 + dif_mes

print(total_dias)
print(total_meses)