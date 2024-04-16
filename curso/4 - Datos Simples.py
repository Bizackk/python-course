# "del" es eliminar datos que se alojaron en la memoria por ejemplo 
x = 100
print(x)  # Imprime 100
del x # Elimina la variable x
print(x)  # Genera un error, ya que x ya no existe

#tambien podemos utilizar el `del` para borrar cosas de una lista 

my_list = [1, 2, 3, 4, 5]
print(my_list)  # Imprime [1, 2, 3, 4, 5]
del my_list[2]  # Elimina el elemento en el índice 2 (valor 3)
print(my_list)  # Imprime [1, 2, 4, 5]
     
     
# in sirve para verificar si un valor esta en nuestra secuencia ejemplo 
my_set = {1, 2, 3, 4, 5}
print(3 in my_set)  # Imprime True, ya que 3 está en el conjunto
print(6 in my_set)  # Imprime False, ya que 6 no está en el conjunto
 
 #tambien con texto 
my_string = "Hola, ¿cómo estás?"
print("cómo" in my_string)  # Imprime True, ya que "cómo" está en la cadena
print("bien" in my_string)  # Imprime False, ya que "bien" no está en la cadena