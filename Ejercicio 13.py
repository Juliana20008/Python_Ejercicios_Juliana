'''El terreno comprado por un influencers tuvo la siguiente destinación: 40% para cultivos,
25% Para construir vivienda, 15% para zonas verdes. Leer el área total del terreno en
metros cuadrados e imprimir el área para cada destino, y el área que queda disponible
para otros proyectos.'''
areaTotal= int(input("Ingrese el area total del terreno en metros cuadrados:"))
cultivos= areaTotal*0.4
print("Los metros cuadrados del terreno destindados para los cultivos es de: ", cultivos)
vivienda= areaTotal*0.25
print("Los metros cuadrados del terreno destindados para construir vivienda es de: ", vivienda)
zonasVerdes= areaTotal*0.15
print("Los metros cuadrados del terreno destindados para las zonas verdes es de: ", zonasVerdes)
areaDisponible= areaTotal-cultivos-vivienda-zonasVerdes
print("Los metros cuadrados disponibles son de: ", areaDisponible)
