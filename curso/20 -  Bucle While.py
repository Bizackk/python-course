# voy a dar este tema con un ejercicio 
#Crea una calculadora simple en Python que realice las siguientes operaciones: suma, resta, multiplicación y división. Debes usar funciones para cada operación y un bucle while para permitir al usuario realizar múltiples cálculos. El programa debe seguir ejecutándose hasta que el usuario decida salir.

#funcion para suma resta multi div
def calculo(suma, resta, multi, divi, a, b, pregunta):
    while pregunta != "chao":
        if pregunta == "suma":
            suma = a + b 
            print("Resultado de la suma:", suma)
        elif pregunta == "resta":
            resta = a - b
            print("Resultado de la resta:", resta)
        elif pregunta == "multi":
            multi = a * b 
            print("Resultado de la multiplicación:", multi)
        elif pregunta == "divi":
            if b == 0:
                print("No se puede dividir por cero.")
            else:
                divi = a / b
                print("Resultado de la división:", divi)
        else:
            print("Ingresaste una operación no válida. Vuelve a intentar.")
        
        pregunta = input("¿Qué operación deseas realizar? (suma, resta, multi, divi) Si terminaste, escribe 'chao': ")
        if pregunta != "chao":
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))

def main():
    suma = 0
    resta = 0
    multi = 0
    divi = 0
    pregunta = ""
    a = 0
    b = 0
    
    calculo(suma, resta, multi, divi, a, b, pregunta)

if __name__ == "__main__":
    main()
