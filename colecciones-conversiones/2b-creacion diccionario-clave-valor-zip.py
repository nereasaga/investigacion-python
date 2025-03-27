## CREACIÖN DE DICCIONARIO A PARTIR DE DDS LISTAS
# Uso de la función zip()

claves = ["mono", "cerdo", "tigre", "mapache","vaca","lobo"] 
valores = ["🐵","🐷","🐯","🦝","🐮","🐺"]

mi_diccionario = dict(zip(claves, valores))  
print(mi_diccionario) # Salida: {'mono': '🐵', 'cerdo': '🐷', 'tigre': '🐯', 'mapache': '🦝', 'vaca': '🐮', 'lobo': '🐺'}

                    
