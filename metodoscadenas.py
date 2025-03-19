# MÉTODOS EN CADENAS
texto = "hola, mundo!"

# find(x)	Devuelve la posición donde aparece x
texto.find("mundo")    # 6  
print(texto.find("mundo"))    

# capitalize()	Convierte la primera letra en mayúscula
texto.capitalize()
print(texto.capitalize())    # Hola, mundo!

# split(x)	Divide la cadena en una lista según x
texto.split(", ")
print(texto.split(", "))  # ['Hola', 'mundo!']

# join(x)	Une elementos de una lista con x entre ellos
"-".join(["Hola", "mundo"])    
print("-".join(["Hola", "mundo"]))    # Hola-mundo

# replace(a, b)	Reemplaza a por b
texto.replace("mundo", "Python")
print(texto.replace("mundo", "Python"))    # Hola, Python! 

# upper()	Convierte todo a mayúsculas
texto.upper()
print(texto.upper())    # HOLA, MUNDO!

# lower()	Convierte todo a minúsculas
texto.lower()
print(texto.lower())    # hola, mundo!

texto2 = "   Hola, mundo!   "

# strip()	Elimina espacios en los extremos
texto2.strip()
print(texto2.strip())    # Hola, mundo!


