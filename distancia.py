print (" ")
print("Danna Paola Martinez Jimenez")
print("no. de control: 1195")
print("3ro-W")
print (" ")

#11-  Que saque la distancia dirigida entre dos puntos

import math

def dist(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Captura de los puntos
x1 = float(input("Introduce x1: "))
y1 = float(input("Introduce y1: "))
x2 = float(input("Introduce x2: "))
y2 = float(input("Introduce y2: "))

# Calcular y mostrar la distancia
distancia = dist(x1, y1, x2, y2)
print("La distancia dirigida entre los puntos es:", distancia)










