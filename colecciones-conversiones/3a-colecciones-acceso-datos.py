#ACCESO A DATOS DE ELEMENTOS DE COLECCIONES

### lista
lista1= [90, "Python", 3.87]
print(lista1 [0]) #90
print(lista1 [1]) #Python
print(lista1 [-1]) #3.87
print(lista1 [-2]) #Python
#anidaciones
x = [1, 2, 3, ['p', 'q', [5, 6, 7]]]
print(x[3][0]) #p
print(x[3][2][0]) #5
print(x[3][2][2]) #7


### tupla
mi_tupla = ("manzana", "banana", "cereza")
primer_elemento = mi_tupla[0]
print(primer_elemento) # Output: manzana


### set
#Al no estar ordenados no se puede acceder a sus elementos. 
# Aunque se puede convertir a lista o tupla, acceder a sus datos y luego convertirlo de nuevo en set.
##Ver ejemplo separado

### diccionario
#Usamos la clave para acceder al valor.
persona = {"nombre": "Alicia", "edad": 30}
print(persona["nombre"]) # Salida: Alicia