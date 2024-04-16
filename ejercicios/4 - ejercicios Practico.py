def opciones(suma, resta, multiplicacion, division):
    print("Elige una función")
    opciones = input("Funciones: suma, resta, multiplicacion, division:")
    
    a = float(input("Digite el primer dígito: "))
    b = float(input("Digite el segundo dígito: "))
    
    if opciones == suma:
        return f"El resultado es: {a + b}"
    elif opciones == resta:
        return f"El resultado es: {a - b}"
    elif opciones == multiplicacion:
        return f"El resultado es: {a * b}"
    elif opciones == division:
        if b != 0:
            return f"El resultado es: {a / b}"
        else:
            return "No se puede dividir por cero."
    else:
        return "Por favor, ingresa correctamente la función."

# Llama a la función con las opciones adecuadas
ejecutar = opciones("suma", "resta", "multiplicacion", "division")

# Imprime el resultado
print(ejecutar)