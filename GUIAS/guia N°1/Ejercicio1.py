txt = "La Universidad de los Lagos es una institución estatal fundada en 1993 . \
Esta universidad regional entrega una contribución significativa al desarrollo sostenible del territorio . \
Como Universidad sus pilares fundamentales se basan en la inclusión , pluralismo , conciencia ambiental y \
participación democratica ."

universidad_en_txt  = ()


x = (txt.count("Universidad"))
y = (txt.count("universidad"))


txt_split = txt.split()

for i in txt_split:
    if i == "Universidad" or i == "universidad":
        universidad_en_txt = universidad_en_txt + (i,)

print(f"universidad se repite {x+y} veces:")
print(universidad_en_txt)
