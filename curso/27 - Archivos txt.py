#no se para que sirve pero les explico como va. con esto podemos imprimir documentos.txt lo metemos en una variable 
archivo = open("ejercicios\\texto.txt", encoding ="UTF-8") #el utf8  es para que pueda leer toda clase de caracteres

#leer archivo completo:
completo = archivo.read()

#Para leer lina por linea. este metodo no deja leer todas las lineas
lineas = archivo.readlines()
archivo.close()

#Para leer una linea especifica. tenemos que poner en el parametro cuantos caracteres va a imprimir 
linea = archivo.readline(50)
archivo.close()
#ahora ya notamos que no podemos imprimir un txt que ya este leido solo una vez por seguridad si queremos volver a mostrar antes tenemos que cerrarlo
#simplemente con variables.close() 


#ahora como podemos leer archivos optimamanete

