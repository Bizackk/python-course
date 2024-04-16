

#DIR devuelve la lista de atributos validos del objeto pasado (es una funcion de python )

#print(dir("aña")) # con todo lo que le pidas 

#METODOS




#para que sea considerado un metodo un METODO tiene que ser escrito asi:
#ejm1 = dato.metodo(parametro)
#print (ejm1)




#upper convertir en mayuscula 
ejm1 = "simon es re contra mega gay"
ejm2 = ejm1.upper()
#imprime: SIMON ES RE CONTRA MEGA GAY (mayusulas)

#lower convertir en minuscula 
ejm3 = "simon es re contra mega gay"
ejm4 = ejm3.lower()
#imprime: simon es re contra mega gay (minuscula)

#capitalize convertir la primera en mayuscula 
ejm5 = "simon es re contra mega gay"
ejm6 = ejm5.capitalize()
#imprime: Simon es re contra mega gay (la primera en mayuscula)(si hay otra letra en mayuscula la convierte en minuscula xd)





# find - buscamos una cadena en una cadena

texto = "hola mundo"
busqueda_find = texto.find("hola")
# daria 0
#daria como resultado 0 por que se encuentra en el espacion cero otra cosa importante es que el espacio tambine cuenta

# index - buscamos una cadena en una cadena

text1 = "hola mundo"
busqueda_find = text1.index("mundo")
#daria 2 


#la diferencia de index con con find es que find cuando le pedimos una cadena que no esta nos da -1 pero en index nos tira una exepcion (error)





# isnumeric - si es numerico nos devuelve True sino False

text2 = "487164619"
numeric = text2.isnumeric() 
#daria True

# isalpha - si es alfanumerico nos devuelve True sino False. los alpha solo son los numeros de la A a la Z, si le pones otra cosa no va a dar True ni numeros ni caracteres especiales 

text3 ="holacomoestas"
alpha = text2.isalpha() 
#False 






#count cuenta las coincidencias de una cadena, dentro de otra cadena. devuelve la cantidad de coincidencias 
ejn = "como estas pedrin"
ej1 = ejn.count("o") 
# 2 veces por que hay dos "o" en la cadena

#len es una funcion no un metodo. es escribe asi. y cuenta la cantidad de caracteres que le pedimos 
ejn3 = "como estas pedrin"
ej4 = len(ejn3)
# cantidad: 17}




# startswith confirma si una cadena empieza con otra cadena que le preguntemos (resultado bolean)
sopa = "liquido"
starswith = sopa.startswith("li")
#True

# endswith confirma si una cadena termina con otra cadena que le preguntemos (resultado bolean)
sopa1 = "liquido"
starswith = sopa1.endswith("do")
#True





# replace intercambia una cadena con otra cadena que le demos 

arroz = "tomate sal aceite agua"
arroz1 = arroz.replace("tomate","cebolla")
#cebolla 

# split separar cadenas con las cadenas que le demos. este metodo lo que hace es que hace de la cadena una lista y le decimos como la separe
cadena_separada = arroz.split()
print(cadena_separada)
