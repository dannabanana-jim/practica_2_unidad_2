print (" ")
print("Danna Paola Martinez Jimenez")
print("no. de control: 1195")
print("3ro-W")
print (" ")

#7- Función que de un string, regrese la longitud de la última palabra. Las palabras tienen separación por uno o más espacios.

def palabra(texto):
    return len(texto.strip().split()[-1])

# Capturar los datos del usuario
texto = input("Introduce un texto: ")

# Mostrar la longitud de la ultima palabra
print("La longitud de la última palabra es:", palabra(texto))

print (" ")





