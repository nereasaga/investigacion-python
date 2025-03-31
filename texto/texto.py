# TXT

with open ('texto.txt', 'r') as f:
    texto = f.read()    
    print(texto)   

with open ('texto.txt', 'a', encoding="utf-8") as f:
    texto = f.write('\nEstoy usando Python')

with open ('texto.txt', 'r') as f:
    texto = f.read()    
    print(texto)   


# CSV

import csv

with open('ejemplo.csv', 'r') as ejemplo:
    csv_reader = csv.reader(ejemplo)
    for linea in csv_reader:
        print(linea)

with open('ejemplo.csv', 'a', newline="") as ejemplo:
    csv_writer = csv.writer(ejemplo)
    csv_writer.writerow(['Nombre', 'Edad', 'Sexo'])
    csv_writer.writerow(['Juan', '25', 'M'])
    csv_writer.writerow(['Ana', '20', 'F'])

with open('ejemplo.csv', 'r') as ejemplo:
    csv_reader = csv.reader(ejemplo)
    for linea in csv_reader:
        print(linea)


# JSON

import json

with open('texto.json', 'r', encoding='utf-8') as f:
    datos = json.load(f)
    print(datos)

with open('texto.json', 'w', encoding='utf-8') as f:
    json.dump({'nombre': 'Juan', 'edad': 25, 'sexo': 'M'}, f)

with open('texto.json', 'r', encoding='utf-8') as f:
    datos = json.load(f)
    print(datos)