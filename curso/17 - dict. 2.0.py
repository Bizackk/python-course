#dict normal
diccionario = {
    "nombre" : "samuel",
    "apellido" : "chavez",
    "plata" : 25000
}

#creando un diccionario con dict
diccionario = dict(nombre="lucas",apellido="chavez")
print (diccionario)


# las listas no son claves y podemos meter conjuntos con el frozenset
diccionario = {frozenset(["dalto","rancio"]): "jajaja"}
print(diccionario)

#creando un dict sin valores fromKeys
diccionario = dict.fromkeys(["cuidad", "provincia", "padres"])
print(diccionario)

#tambien podemos hacer que cambie el valor por defecto en vez de que nos tire none podemos decirle que tirar 
diccionario = dict.fromkeys(["cuidad", "provincia", "padres"], "no se xd")
print(diccionario)