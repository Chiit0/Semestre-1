piramide = "1000000000"
piramide
step = 2


piramide_str = [int(x)+2 for x in str(piramide)[:step]]

piramide_str = (str(piramide_str).replace(", ",""))
print(piramide_str)
piramide= str(piramide_str)

step += 1
print(piramide_str)