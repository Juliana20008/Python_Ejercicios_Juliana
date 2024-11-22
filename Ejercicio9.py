'''El propietario de una vivienda necesita renovar parte de esta, para lo cual tiene planeado
enchapar los muros de los baños. La persona responsable de hacer este trabajo mide el
alto y ancho de los muros. Se pide realizar un algoritmo para calcular el área del baño y el
numero de baldosas necesarios para cubrir el baño. Sabiendo que la caja trae 3.5 metros
cuadrados.
'''
altura= float(input("ingrese la altura de los muros: "))
ancho= float(input("ingrese el ancho de los muros: "))
area= altura*ancho
baldosas= area//3.5
print(f"El area del baño es: {area} El numero de baldosas que se requiere para cubrir el baño son: {baldosas}" )
