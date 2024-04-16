import pandas as pd 

# usando la funcion read_csv para leer el contenido CSV
df = pd.read_csv("archivo\\datos.csv", names= ["n","a","e"])#podemos cambiarles el nombre a las claves con "name=[]"
df2 = pd.read_csv("archivo\\datos.csv", names= ["n","a","e"])
#obteniendo los datos de la columna nombre 
print(df["n"]) 

#aorendiendo slicing
#podemos hacer rangos con ":"
lista = "0123456789"
#print(lista[5:8])

#ordenando las edades:
df_ordenado = df.sort_values("e",ascending=False)#para ponerlo con orden descendente es con True 
print(df_ordenado)
df_ordenado = df.sort_values("e",ascending=True)#para ponerlo con orden ascendente es con False 
print(df_ordenado)

#concatenando los dos data friends
#df_concatenado = pd.concat([df,df2])
#print(df_concatenado)

#tambien podemos ver las filas que nosotros deseemos en orden de arriba hacia abajo
df_filas = df.head(2)
print(df_filas)

#tambien podemos ver las filas de abajo hacia arriba con el tail
df_filas = df.tail(3)
print(df_filas)

#accediendo a la cantidad de filas y columnas con shape, tambien agregue la forma de desenpaquetado de datos 
filas, columnas = df.shape
print(filas,columnas)

#obteniendo la info del dataframe 
df_info = df.describe()
print(df_info)

#accediendo a un elemento especifico con loc
df_elemento = df.loc[2,"e"]
print(df_elemento)

df_elemento = df.iloc[2,"e"]
print(df_elemento)

#accediendo a todos las filas de una columna 
apellido = df.loc[:,1]