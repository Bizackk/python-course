#metiendo conjuntos a un conjunto en temas pasado vimos que un set no se puede actualizar pero ahora sabemos como si con el metodo "frozenset"
conjunto1 = frozenset(["dato1", "dato2"])
conjunto2 = {conjunto1, "dato3"}
print(conjunto2)


#teroria de conjuntos
conjunto1 = {1,2,3,10}
conjunto2 = {1,10}

#ahora vamos a verificar qie el conjunto dos se un subjoncunto del conjunto1 (bolean)
resultado1 = conjunto2.issubset(conjunto1)
print(resultado1)#dio true por que los elementos que estan en el set son los mismos elementos que hay en el conjunto 1 osea si es subconjunto 

#verificando si es un super conjunto #issuperset
resultado2 = conjunto1.issuperset(conjunto2)
print(resultado2)

#verificando si hay algun numero en comun 
resultado2 = conjunto1.isdisjoint(conjunto2)
print(resultado2)#va a tirar falso por que todos los numeros son comunes