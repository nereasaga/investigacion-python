# Conversiones Diccionarios/JSON y viceversa
import json

# dumps(): Objeto Python → Cadena JSON
# dump(): Objeto Python → Archivo JSON
# Ejemplo con dumps()
datos = {"nombre": "Carlos", "edad": 35, "ciudad": "Valencia"}
cadena_json = json.dumps(datos)# convierte objeto phyton en una cadena json
print(cadena_json)  # Salida: '{"nombre": "Carlos", "edad": 35, "ciudad": "Valencia"}'
 
# Ejemplo con dump()
datos2 = {"nombre": "Laura", "edad": 28, "ciudad": "Sevilla"}
with open("datos2.json", "w") as archivo:
	json.dump(datos2, archivo)
# Se crea el archivo datos2.json, con la información almacenada en formato json.


# loads(): Cadena JSON → Objeto Python
# load(): Archivo JSON → Objeto Python
 # Ejemplo con loads()
cadena_json = '{"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}'
datos3 = json.loads(cadena_json)#convierte una cadena json en un diccionario python
print(datos3)  # Salida: {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}
print(datos3["nombre"]) # Salida: Juan
 
# Ejemplo con load()
# (Primero, creamos un archivo JSON de ejemplo)
with open("datos.json", "w") as archivo:
	json.dump({"nombre": "María", "edad": 25, "ciudad": "Barcelona"}, archivo)
 
# Ahora, cargamos los datos desde el archivo
with open("datos.json", "r") as archivo:
	datos_archivo = json.load(archivo)
print(datos_archivo)  # Salida: {'nombre': 'María', 'edad': 25, 'ciudad': 'Barcelona'}