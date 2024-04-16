# creando una lista con list. list es una funcion 
lista = list (["samuel", "feo", 1.70, "aña"])


#len devuelve la canitdad de elementos de la lista 
cantidad_de_elementos = len(lista)
#print(cantidad_de_elementos) R/1


# append agrega un elemento a una lista
lista.append("jugador de minecraft")
# esta funcion no es necesaria llamarla. la lista se actualiza automaticamente 

# insert agrega un elemento en un indice especifico 
lista.insert(2, "flaco")

# extend agrega varios elementos a la lista
lista.extend(["bruto", "aweonao"])#tenemos que pasarlo a la lista como una lista (osea con [])




#pop elimina un elemnto de la lista. pide indice y devuleve valor
lista.pop(0) # -1 para eliminar el ultimo, -2 para eliminar anteultimo y asi continuamente

# remove ahora elimina por su valor de una lista 
lista.remove("feo")

# clear elimina la lista completamente 
#lista.clear()



#sort no sirve si tiene cadenas de texto
listo = ([23,False,32,True,95,1004,64,])
listo.sort()# lo reacomoda el False de primero y segundo True (si hay. sino hay pues no xd) tambien lo ordena de menor a mayor(lo numeros|)

#invierte los elementos de una lista
listo.reverse()
#[64, 54, 45, 32, 23, True, False]

