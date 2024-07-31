def sumar(a, b):
    return a + b

try:
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))
    print(sumar(a, b))
except ValueError:
    print("Por favor, ingresa números válidos.")