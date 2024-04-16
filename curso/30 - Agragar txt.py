#con el permiso de "a" lo que pasa es que agrega es un append y ya :3
with open("archivo\\texto.txt" , mode= "a" , encoding= "UTF-8") as archivo:
    
    #sobreescribiendo en un archivo
    #archivo.write("jajajaja eso tilin")
    
    #El writelines() es que se agrupa osea se agrega texto
    archivo.writelines(["hola bebe, que fue de usted?" , "eso tilin "])
    archivo.writelines(["\nBien bebe y usted que pues?\n" , "eso tilin "])
    #el \n es el codigo para que lo separe de renglon y que lo haya metido en una lista es por que es un objeto iterable