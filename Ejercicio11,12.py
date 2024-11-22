'''Una madre y sus 4 hijos se acercan a recibir información por parte de un abogado
referente al dinero que les corresponde en una herencia dejada por su esposo y padre
respectivamente. El testamento tiene las siguientes condiciones: A la esposa le corresponde el 40% mientras
que a los hijos les corresponde: 30% 20% 40% 10% respectivamente. Se pide un algoritmo
que lea los datos necesarios, y muestre lo que le corresponde a la esposa y a los hijos.'''

herencia= float(input("Ingrese el valor de la herencia: "))
esposa= herencia*0.4
herencia2= herencia - esposa
print(f"La herencia de la esposa equivale a:{esposa}")
hijo1= herencia2*0.3
hijo2=herencia2*0.2
hijo3=herencia2*0.4
hijo4=herencia2*0.1
totalHijos= hijo1+hijo2+hijo3+hijo4
print(f"La herencia de los hijos equivale a:{totalHijos}")

