'''El valor del desempleo en Ibagué aumentó en el primer trimestre un 9.5% y en el segundo
trimestre cayó en un 1.5%. Calcular el valor del desempleo actual.
 '''
desempleo=int(input("Ingrese el valor de el desempleo en ibague: "))
primerTrimestre= desempleo*0.095
segundoTrimestre= desempleo*0.015
valorActual=(desempleo-segundoTrimestre)+primerTrimestre
print("El valor del desempleo actual es: ",valorActual )