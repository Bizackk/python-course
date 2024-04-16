#esta es una forma optima de leer archivos txt ya que al mismo tiempo que se abre se vuelve a cerrar 
with open("archivo\\texto.txt" , encoding= "UTF-8") as archivo:
    
    #leemos el archivo 
    contenido = archivo.read()
    
    #imprimimos contenido
    print(contenido)

#en todos los sentidos es mejor esta forma de usar archivos txt