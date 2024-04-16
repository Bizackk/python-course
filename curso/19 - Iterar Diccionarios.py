diccionario = {
    "nombre" : "samuel",
    "apellido" : "chavez",
    "peso" : 64.4
}
# asi iteramos un diccionario
for key in diccionario:
    print (f"las claves son {key} ")
    
    

# asi iteramos un diccionario con items para obtener las claves y valores 
for datos in diccionario.items(): 
    key = datos[0]
    value = datos[1]
    print (f"las claves son {key} el valores son {value}")
print("------------")
    
lista = ["banana", "manazana", "pera", "fresa", "guanabana"]
for frutas in lista:
    if frutas == "pera":
        continue #el continue sirve para que cuando este iterando si quieres que no salga algo en la lista pones continue y se quita y los demas sigue   
    print(f"me voy a comer una {frutas}")
    if frutas == "fresa":
        print("no comas mas por que te cayeron mal las fresas")
        break
print("------------")

#iterando en una sola linea 
numeros = [2,3,5,7,9]
numeros_multi = [x*2 for x in numeros]
print(numeros_multi)