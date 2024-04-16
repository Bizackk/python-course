

#AND solo te da verdadero cuando las dos son verdaderas
resultado1 = True & True # Devolver True
resultado2 = False & True # Devolver Falso
resultado3 = True & False # Devolver Falso
resultado4 = False & False# Devolver Falso

#OR solo te va a dar falso cuando ninguna se cumple 
resultado5 = True | True # Devolver True
resultado6 = False | True # Devolver True
resultado7 = True | False # Devolver True
resultado8 = False | False# Devolver Falso

#NOT es lo contrario de cada una. si le damos True no da False, si le damos False nos da True
resultado9 = not True # Devolver False
resultado10 = not False # Devolver True

print(resultado1)