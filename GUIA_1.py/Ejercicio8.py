#Elaborar un algoritmo que permita al usuario ingresar un mes y arroje la estaci´on
#correspondiente a ese mes: verano, oto˜no, invierno o primavera.
mes = input("Ingrese un mes: ")
if mes in ["enero", "febrero", "marzo"]:
    print(f"La estación en {mes} es el verano")
elif mes in ["abril", "mayo", "junio"]:
    print(f"La estación en {mes} es el otoño")
elif mes in ["julio", "agosto", "septiembre"]:
    print(f"La estación en {mes} es el invierno")
elif mes in ["octubre", "noviembre", "diciembre"]:
        print(f"La estación en {mes} es la primavera")
else:
     print(f"{mes} no es un mes valido")


