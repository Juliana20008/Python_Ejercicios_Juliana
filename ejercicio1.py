salario= int (input("Digite el salario:"))
retencion= salario*0.18
bonificacion=salario*0.013
salario_neto=(salario-retencion)+bonificacion
print("El salario neto es:", salario_neto)
print("El valor de la retencio es:", retencion)
print("El valor de la bonificacion es:", bonificacion)