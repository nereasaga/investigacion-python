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

# setdefault(x)	Devuelve el valor de x o lo crea
diccionario.setdefault("ciudad", "Bilbao")
print(diccionario)  # {'nombre': 'Jon', 'edad': 25, 'ciudad': 'Bilbao'}

# pop(x)	Elimina la clave x y su valor
diccionario.pop("nombre")
print(diccionario)  # {'edad': 30, 'ciudad': 'Bilbao'}

# clear()	Elimina todos los elementos
diccionario.clear()
print(diccionario)  # {}

# reversed()	Invierte el orden de las claves
diccionario = {"nombre": "Ane", "edad": 30} # Restauramos el diccionario
print(dict(reversed(diccionario.items())))  # {'edad': 30, 'nombre': 'Ane'}


