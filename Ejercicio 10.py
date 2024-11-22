'''Un atleta tiene la costumbre de medir el tiempo(en minutos) y la distancia (en metros)
durante sus tres días de entrenamiento. Al final de la semana quiere saber el total de
tiempo que duro el entrenamiento , la distancia recorrida, y el promedio del tiempo y la
distancia recorrida.'''
tiempo1= int(input("Ingrese el tiempo del primer dia en minutos:"))
tiempo2= int(input("Ingrese el tiempo del segundo dia en minutos:"))
tiempo3= int(input("Ingrese el tiempo del tercer dia en minutos:"))
tiempoTotal= tiempo1+tiempo2+tiempo3
print(f"El tiempo total del entrenamiento es: {tiempoTotal}")
distancia1= int(input("ingrese la distancia del primer dia en metros: "))
distancia2=int(input("ingrese la distancia del segundo dia en metros: "))
distancia3=int(input("ingrese la distancia del tercer dia en metros: "))
distanciaTotal= distancia1+distancia2+distancia3
print(f"La distancia total recorrida durante el entrenamiento es de: {distanciaTotal}")
promedioTiempo= tiempoTotal//3
print(f"El promedio del tiempo en el entrenamiento es: {promedioTiempo}")
promedioDistancia= distanciaTotal//3
print(f"El promedio de la distancia en el entrenamiento es:{promedioDistancia}")