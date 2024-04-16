diccionario = {
    "nombre" : "samuel",
    "apellido" : "chavez",
    "plata" : 25000
}

# .keys() no imprime las claves de una diccionario
claves = diccionario.keys()


# get le pedimos un elemento (por que lo hacemos asi y no con el []? por que con el [] no pone un error y por lo tanto el programa se para mientras que con get no tira un none)
valor_de_plata = diccionario.get("plata")

#clear elimina todos los elementos de la lista 
#diccionario.clear()
#print(diccionario) se actualiza. vieron que no tenia que llamar una variable? bueno es por que se actualiza  

#pop borra elementos de una diccionario 
diccionario.pop("plata")

#.items( ) obtener un elemento dict_item iterable
diccionario_iterable = diccionario.items()



print()
