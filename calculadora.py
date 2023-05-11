# Función para la operación de suma (de Joaquin)
def suma():
    num1 = float(input("Ingrese el primer valor: "))
    print()
    num2 = float(input("Ingrese el segundo valor: "))
    print()
    resultado = num1 + num2
    return resultado

# Función para la operación de resta (de Barbara)
def resta():
    num1 = float(input("Ingrese el primer valor: "))
    num2 = float(input("Ingrese el segundo valor: "))
    resultado = num1 - num2
    return resultado

# Función para la operación de multiplicación (de Tobias)
def multiplicacion():
    num1 = float(input("Ingrese el primer valor: "))
    num2 = float(input("Ingrese el segundo valor: "))
    resultado = num1 * num2
    return resultado

# Función para la operación de división (de Diego)
def division():
    num1 = float(input("Ingrese el primer valor: "))
    num2 = float(input("Ingrese el segundo valor: "))
    resultado = num1 / num2
    return resultado

# Mostrar el menú de opciones
print("Claculadora (Grupo 5)")
print()
print("Seleccione la opción correspondiente a la operación que desee realizar:")
print()
print("1. Suma")
print()
print("2. Resta")
print()
print("3. Multiplicación")
print()
print("4. División")
print()

# Solicitar al usuario que seleccione una opción
opcion = int(input("Seleccione una opción (1-4): "))
print()
print()

# Mapeo de las opciones a las funciones correspondientes
operaciones = {
    1: suma,
    2: resta,
    3: multiplicacion,
    4: division
}

if opcion in operaciones:
    # Si la opción seleccionada está dentro en las operaciones,
    # se llama a la función correspondiente y se obtiene el resultado.
    resultado = operaciones[opcion]()
    print()
    print("El resultado es:", resultado)
else:
    # Si la opción no es válida, se muestra un mensaje de error.
    print("Opción inválida. Por favor, seleccione una opción válida (1-4).")
