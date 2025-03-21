#and
Resultado= True & True #devolver True
Resultado2= False & True #devolver Falso
Resultado3= True & False #devolver Falso
Resultado4= False & False #devolver Falso

#or
Resultado5= True | True #devolver True
Resultado6= False | True #devolver True
Resultado7= True | False #devolver True
Resultado8= False | False #devolver False

#not
Resultado9= not True #devolver False
Resultado10= not False  #devolver True

Resultado11= not 2 > 49 #devolver False

print(Resultado11)

# Ejemplo edad

edad= 20

print (edad > 18 and edad < 30)
print (edad > 18 or edad < 30)
print (not (edad > 17 ))