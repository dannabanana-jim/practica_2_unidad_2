print (" ")
print("Danna Paola Martinez Jimenez")
print("no. de control: 1195")
print("3ro-W")
print (" ")

#10- Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario
#devuelve False


def es_vocal(caracter):
    return caracter.lower() in 'aeiou'

# Captura de la palabra
palabra = input("Introduce una palabra: ")

# Verificar y mostrar si cada carácter es una vocal
for char in palabra:
    if es_vocal(char):
        print(char, ": es Vocal")
    else:
        print(char, ": No es vocal")
