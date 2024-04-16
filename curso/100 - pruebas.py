def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    resultado = 0
    for _ in range(abs(int(b))):  # Utilizamos la magnitud de 'b' como contador
        resultado = suma(resultado, a) if b > 0 else resta(resultado, a)
    return resultado 

def division(a, b):
    
    resultado = 0
    a = abs(a)
    b = abs(b)
    
    signo = 1 if (a > 0 and b > 0) or (a < 0 and b < 0) else -1

    while a >= b:
        a = resta(a, b)
        resultado = suma(resultado, 1)
    
    if b == 0:
        return "No se puede dividir por cero."
    return resultado * signo

def calculadora():
    while True:
        print("Operaciones disponibles:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        
        opcion = input("Elige una operación (1/2/3/4/5): ")
        
        if opcion == '5':
            break
        
        if opcion in ('1', '2', '3', '4'):
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            
            if opcion == '1':
                resultado = suma(num1, num2)
                print(f"Resultado de la suma: {resultado}")
            elif opcion == '2':
                resultado = resta(num1, num2)
                print(f"Resultado de la resta: {resultado}")
            elif opcion == '3':
                resultado = multiplicacion(num1, num2)
                print(f"Resultado de la multiplicación: {resultado}")
            elif opcion == '4':
                resultado = division(num1, num2)
                print(f"Resultado de la división: {resultado}")
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    calculadora()
