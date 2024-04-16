#diferencia en porcentaje entre el curso actual:

#duracion de videos
video_rapido = 2.5
video_largo = 7.0
video_promedio = 4.0
video_dalto = 1.5

#diferencia 
diferencia_del_rapido = 100 - video_dalto * 1000 // video_rapido / 10
diferencia_del_largo = 100 - video_dalto * 1000 // video_largo / 10
diferencia_del_promedio = 100 - video_dalto* 1000 // video_promedio/ 10
#prints diferencia
print("-----------")
print("la diferencia es del")
print(diferencia_del_rapido)
print(diferencia_del_largo)
print(diferencia_del_promedio)  
print("-----------")

#hayar el crudo 
crudo_de_otros = 5.0 
crudo_promedio = 100 - video_promedio * 1000 // crudo_de_otros / 10
crudo_dalto = 100 - video_dalto * 1000 // crudo_de_otros / 10
print("-----------")
print("el crudo es del")
print(crudo_promedio)
print(crudo_dalto)
print("-----------")