''' Calcular el área total de un terreno en metros sabiendo que esta fue reducida en un 10%,
y posteriormente, le fue adicionado un 50% con relación al área después de la reducción.'''
areaInicial= float (input("Ingresar el area inicial del terreno:"))
reduccionTerreno= areaInicial*0.10
reduccionArea= areaInicial-reduccionTerreno
aumentoTerreno= reduccionArea*0.50
areaTotal= reduccionArea+aumentoTerreno
print("El area total del terreno es: ", areaTotal)
