#Crear una agenda telef´onica que contenga un solo contacto. Est´a agenda se debe
#guardar en un diccionario. Este diccionario debe contar con las siguientes claves:
#Nombre-Direccion-Ciudad-N´umero telef´onico
#A continuaci´on, agrega una nueva clave llamada “Redes Sociales” que contenga al
#menos tres nombres de perfil de diferentes redes sociales (por ejemplo, Facebook,
#Instagram y Twitter). Por ´ultimo, se solicita imprimir solamente el Facebook del
#contacto y luego la agenda completa actualizada.

contacto={
    "Nombre":"Pepe",
    "Dirección":"Juan Mackenna 1020",
    "Ciudad":"Osorno",
    "Número telefonico":"9-988-024-96"
}
contacto["Linkedin"] = "Pepe Martinez"
contacto["Facebook"] = "Pepe Martinez Corral"
contacto["Instagram"] = "@pepito.m"

print(contacto["Facebook"])
print(contacto)