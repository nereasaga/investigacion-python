# MÉTODOS EN DICCIONARIOS
diccionario = {"nombre": "Ane", "edad": 30}

# keys()	Devuelve las claves
diccionario.keys()
print(diccionario.keys())  # dict_keys(['nombre', 'edad'])

# values()	Devuelve los valores
diccionario.values()
print(diccionario.values())  # dict_values(['Ane', 30])

# items()	Devuelve pares (clave, valor)
diccionario.items()
print(diccionario.items())  # dict_items([('nombre', 'Ane'), ('edad', 30)]) 

# get(x)	Devuelve el valor de x
diccionario.get("nombre")   
print(diccionario.get("nombre"))  # Ane

# update()	Modifica valores del diccionario
diccionario.update({"nombre": "Jon", "edad": 25})
print(diccionario)  # {'nombre': 'Jon', 'edad': 25}

# clear()	Elimina todos los elementos
diccionario.clear()
print(diccionario)  # {}
