# "tupla" esto es una lista que a diferencia de una lista normal no se puede modificar. se acuerdan que en anteriores secciones dije que las variables se podian actualizar?  buneno pues esta NO ejm 

tupla = ("samuel", "chavez", "feo", 170, "fuerte") #recuerden los tuples en vez de "[]"son con "()"
print (tupla[4])

#Que me refiero con que las listas variables se pueden actualizar/modificar

lista = ["samuel", "chavez", "feo", 170, "fuerte"]
lista[2] = "lindo" 
print (lista)

#¿lo vieron? se actualizo de feo a lindo. eso si samuel es feo, era solo por el ejemplo xd

# conjunto (set) es muy parecido a las listas. el set sirve para eliminar duplicados en una lista, tambien no ordenados puede 
conjunto = {"samuel", "chavez", "feo", 170, "fuerte"}
#no se puede acceder por un indice. ejm: print (conjunto[2]) -> no puede acceder al elemento solo se puede mostrar todo 
# Se hace con llaves 
# no se puede repetir datos 

# dict para explicarme mejor: las listan son 0,1,2,3,4,5 en el diccionario tu le pones el nombre u orden 

dict = {
    'nombre' : "samuel",
    'apellido' : "chavez",
    'como es' : "feo",
    'estatura' : 170 
}

