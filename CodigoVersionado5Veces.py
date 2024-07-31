def sumar(a, b):
    return a + b

while True:
    try:
        a = int(input("Ingresa el primer número: "))
        b = int(input("Ingresa el segundo número: "))
        print(f"La suma de {a} y {b} es {sumar(a, b)}")
        continuar = input("¿Quieres sumar otros números? (sí/no): ")
        if continuar.lower() != 'sí':
            break
    except ValueError:
        print("Por favor, ingresa números válidos.")