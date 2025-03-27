## CREACIÖN DE DICCIONARIO A PARTIR DE DDS LISTAS
## CONVERSIÓN DE 2 LISTAS EN 1 DICCIONARIO
# Uso de la función zip()

claves = ["mono", "cerdo", "tigre", "mapache","vaca","lobo"] 
valores = ["🐵","🐷","🐯","🦝","🐮","🐺"]

mi_diccionario = dict(zip(claves, valores))  
print(mi_diccionario) # Salida: {'mono': '🐵', 'cerdo': '🐷', 'tigre': '🐯', 'mapache': '🦝', 'vaca': '🐮', 'lobo': '🐺'}

                    
