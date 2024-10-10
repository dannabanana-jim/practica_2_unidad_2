print (" ")
print("Danna Paola Martinez Jimenez")
print("no. de control: 1195")
print("3ro-W")
print (" ")
import math
#5- Calcular el área de un círculo  y el volumen 
#otra que calcule el volumen de un cilindro y utilice  primera función.
# Función para calcular el área de un círculo
def area_circulo(radio):
    return math.pi * (radio ** 2)

# Función para calcular el volumen de un cilindro
def volumen_cilindro(radio, altura):
    return area_circulo(radio) * altura

# Solicitar el radio del círculo y la altura del cilindro
radio = float(input("Introduce el radio del circulo: "))
altura = float(input("Introduce la altura del cilindro: "))

# Calcular y mostrar el área y el volumen
print("El area del circulo es:", area_circulo(radio))
print (" ")
print("El volumen del cilindro es:", volumen_cilindro(radio, altura))
print (" ")
