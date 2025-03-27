#ACCESO A DATOS DE ELEMENTOS DE COLECCIONES
### set
#Al no estar ordenados no se puede acceder a sus elementos. 
# Aunque se puede convertir a lista o tupla, acceder a sus datos y luego convertirlo de nuevo en set.

##  a- iterar sobre los elementos
# Utlizamos un bucle for para recorrer los elementos del set.
# observese que el orden es arbitrario, pues la colección del set no esta ordenada

mi_set = {10, 20, 30, 40}
for elemento in mi_set:
     print(elemento) # Salida: 10, 20, 30, 40 - el orden será aleatorio

## b- Convertir el set a una lista:
# Los set no estan ordenados, para poder acceder a sus elementos, por indice, hay que convertirlos a lista primero.

#mi_set = {10, 20, 30, 40}
mi_lista = list(mi_set)
# ordenamos la lista con el método sort
mi_lista.sort() 
print(mi_lista[1]) #Salida 20 Accede al segundo elemento

