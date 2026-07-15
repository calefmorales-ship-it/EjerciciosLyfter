import json # importa el módulo "json" que permite trabajar con datos en formato JSON

with open("datos.json", "r") as archivo: # abre el archivo "datos.json" en modo lectura ("r") y lo asigna a la variable "archivo"
    datos = json.load(archivo) # json.load() convierte el contenido del archivo JSON en un diccionario de Python

print(datos) # imprime el diccionario "datos" en la consola, mostrando su contenido