#lambda sirve para hacer def´s con mucho menos codigo que con una funcion normal 



numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,12,14]

numeros_pares = filter(lambda numeros: numeros%2 == 0, numeros)#filter es como un bucle que iterable que le ponemos el parametro "," y le ponemos la secuencia osea en donde lo flitramos que en este caso es en la lista 

# Convertir el resultado en una lista
numeros_pares_lista = list(numeros_pares)

print(numeros_pares_lista)
