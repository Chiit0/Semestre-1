superficie_los_rios=18429
superficie_magallanes=1382291
habitantes_los_rios=404432
habitantes_magallanes=166533
tabla_regiones = {
    "ID":[14, 12],
    "Nombre":["Los Rios", "Magallanes"],
    "Superficie (Km^2)":[superficie_los_rios, superficie_magallanes],
    "Habitantes (2017)":[habitantes_los_rios, habitantes_magallanes]
}

print(tabla_regiones)

densidad_los_rios = round(habitantes_los_rios/superficie_los_rios,1)
densidad_magallanes = round(habitantes_magallanes/superficie_magallanes,1)
tabla_regiones["Densidad"]=[densidad_los_rios, densidad_magallanes]
tabla_regiones["Capital"]=["Valdivia","Punta Arenas"]
tabla_regiones["Comunas"]=["Río Bueno", "La Unión", "Paillaco"],["Cabo de Hornos", "Puerto Williams","Porvenir"]
tabla_regiones["Provincias"]=("Ranco", "Valdivia"), ("Antártica Chilena", "Magallanes", "Tierra del Fuego", "Última Esperanza")

print(tabla_regiones)
