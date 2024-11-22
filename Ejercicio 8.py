'''Un cliente de telefonía celular realiza cuatro llamadas: dos a un primer operador, y dos al
segundo operador. El cliente desea conocer el costo de cada llamada, El costo total de las
llamadas a cada operador, y el total de las cuatro llamadas'''

operador1= float (input("ingrese el costo del primer operador por minuto:"))
operador1Llamada1= float (input ("ingrese los minutos que se realizaron en la primera llamada del operador1:"))
valorLlamada1= operador1*operador1Llamada1
print(f"El costo total de la primera llamada al primer operador es: {valorLlamada1}")
operador1Llamada2= float (input ("ingrese los minutos que se realizaron en la segunda llamada del operador1:"))
valorLlamada2= operador1* operador1Llamada2
print(f"El costo total de la segunda llamada al primer operador es: {valorLlamada2}")
operador2= float (input ("ingrese el costo del segundo operador por minuto:"))
operador2Llamada1= float(input("ingrese los minutos que se realizaron en la primera llamada del operador2:"))
valor1Llamada1= operador2*operador2Llamada1
print(f"El costo total de la primera llamada al segundo operador es: {valor1Llamada1}")
operador2Llamada2= float(input("ingrese los minutos que se realizaron en la segunda llamada del operador2:"))
valor2Llamada2= operador2*operador2Llamada2
print(f" El costo total de la segunda llamada al segundo operador es: {valor2Llamada2}")
totalLlamadas1= valorLlamada1+valorLlamada2
print(f"El valor total de las llamadas al primer operador es: {totalLlamadas1}")
totalLlamadas2= valor1Llamada1+valor2Llamada2
print(f"El valor total de las llamadas al segundo operador es: {totalLlamadas2}")
totalLlamadas= totalLlamadas1+totalLlamadas2
print(f" El total de las cuatro llamadas es: {totalLlamadas} ")
