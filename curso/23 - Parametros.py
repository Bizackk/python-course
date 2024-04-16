def suma(nombre,*numeros):
    return f"{nombre} esta es la suma de los valores: {sum(numeros)}"

resultado = suma("lucas",4,5,1,4,3,45,)
print(resultado)
