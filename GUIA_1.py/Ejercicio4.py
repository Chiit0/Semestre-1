#Elaborar un algoritmo que solicite al usuario su nombre y el nombre de otra
#persona. Luego, mostrar en pantalla un mensaje que indique si ambos nombres
#comienzan con la misma letra o si terminan con la misma letra, o si difieren tanto
#en la letra inicial como en la final. Por ejemplo, si los nombres ingresados son
#Belinda y Beatriz, se mostrar´a un mensaje que indique que ambos nombres comienzan con la misma letra. Si los nombres son Leonardo y Gonzalo, se mostrar´a
#un mensaje que indique que ambos nombres terminan con la misma letra.
nombre1=input("Escriba su nombre: ")
nombre1_list = nombre1.upper()
nombre2=input("Escriba el nombre con el que lo quiere comparar: ")
nombre2_list = nombre2.upper()

nombre1_list=list(nombre1_list)
nombre2_list=list(nombre2_list)
ultima_letra_1=len(nombre1)
ultima_letra_2=len(nombre2)

if nombre1_list[0] == nombre2_list[0] and nombre1_list[ultima_letra_1-1] == nombre2_list[ultima_letra_2-1]:
    print("¡Ambos nombres comienzan y terminan con la misma letra!")
elif nombre1_list[ultima_letra_1-1] == nombre2_list[ultima_letra_2-1]:
    print("!Ambos nombres terminan con la misma letra!")
elif nombre1_list[0] == nombre2_list[0]:
    print("¡Ambos nombres comienzan con la misma letra!")
else:
    print("Los nombres no comienzan ni terminan con la misma letra...")

