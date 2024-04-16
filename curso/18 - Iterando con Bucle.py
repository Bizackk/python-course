#iterando con lista
#listas
animales = ["gato", "perro", "loro", "cocodrilo"]
numeros = [12,34,12,56]


#iterando con texto:
for animal in animales:
    print(f"ahora la variable animal es: {animal}")
else:
    print ("---------------")
#iterando con numeros
for numero in numeros:
    print (f"los numeros de la lista son {numero}")
else:
    print ("---------------")
#podemos iterar sobre dos lista o mas de dos. con la funcion zip() y las listas tienen que tener el mismo numero de cantidad de elementos 
for animal, numero in zip(animales, numeros):
    print (f"lista numero 1: {animal}")
    print (f"lista numero 2: {numero}")
else:
    print ("---------------")
#tambien podemos iterar con la funcion range(). cuando le ponemos donde empieza y donde termina el numero donde termina es uno menos ejm. pero si no le ponemos un numero inicial termina con el numero que le ponemos ejm for num in range(5): imprime 1 2 3 4
for num in range(5, 10):
    print (f"el rango de los numeros es: {num}") #el dies no cuenta
else:
    print ("---------------")
# forma correcta de recorrer lista por su indice. con la funcion enumerate(). si le pide el [0] te va a mostrar el nuemro de indice si le pides el [1] te va a mostrar el valor 
for num in enumerate (numeros):
    indice = num[0]
    valor = num[1]
    print (f"el numero de indice es {indice} y el valor es {valor}")
else:
    print ("---------------")
    
#todo lo anterior funciona igual con tuplas y conjuntos