print (" ")
print("Danna Paola Martinez Jimenez")
print("no. de control: 1195")
print("3ro-W")
print (" ")
#4.- Calcular total de una factura luego del IVA. 
#primero obtener la cantidad sin IVA 
#luego el porcentaje de IVA a aplicar, 
#por ultimo devolver el total de la factura. 
# Solicitar la cantidad sin IVA
cantidad_sin_iva = float(input("Introduce la cantidad sin IVA: "))

# Solicitar el porcentaje de IVA
porcentaje_iva = float(input("Introduce el porcentaje de IVA: "))

# Calcular el total de la factura
iva = cantidad_sin_iva * (porcentaje_iva / 100)
total_factura = cantidad_sin_iva + iva
print (" ")

# Mostrar el total
print("El total de la factura es:", total_factura)

print (" ")