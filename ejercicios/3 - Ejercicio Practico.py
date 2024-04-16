#en un salon de clases, el Profesor no fue a dictar clase por lo tanto los estudiantes idearon un plan chimba. uno de los alumnos es profesor otro su asistente
#A) pedir la edad de los compañeros que vinieron hoy a clase y ordenar de menos a mayor 
#B) El mayo de la clase es el profesor y el menor el asistente quien es quien?

def contador_edades():
    N_estudiantes = int(input("ingrese la cantidad de estudiantes: "))
    edades = []
    
    for i in range(N_estudiantes):
        edad = int(input(f"ingrese la edad del estudiante {i+1}: "))
        edades.append(edad)
    
    edades.sort()
    return edades


edades_ordenadas = contador_edades()
print("Edades de los estudiantes ordenadas de menor a mayor:", edades_ordenadas)


primer_elemento = edades_ordenadas[0]
ultimo_elemento = edades_ordenadas[-1]

print(f"El profesor es el estudiante que tiene {ultimo_elemento} años y el asistente es el estudiante que tiene {primer_elemento} años")