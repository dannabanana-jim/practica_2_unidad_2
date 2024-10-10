print (" ")
print("Danna Paola Martinez Jimenez")
print("no. de control: 1195")
print("3ro-W")
print (" ")
#3- Dar un entero positivo y resuelva su factorial.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Solicitar un entero positivo al usuario
while True:
    try:
        numero = int(input("Introduce un entero positivo: "))
        if numero < 0:
            print("Por favor, introduce un número positivo.")
        else:
            break
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número entero.")

# Calcular el factorial
resultado = factorial(numero)
print("El factorial de", numero, "es", resultado)

print (" ")





