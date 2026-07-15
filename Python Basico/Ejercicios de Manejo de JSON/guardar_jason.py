import json # importa el módulo "json" que permite trabajar con datos en formato JSON

# Creamos un diccionario con algunos datos
datos = {
    "nombre": "Jeremy",
    "edad": 17,
    "ciudad": "San José"
}

with open("datos2.json", "w") as archivo: # abre el archivo "datos2.json" en modo escritura ("w") y lo asigna a la variable "archivo"
    json.dump(datos, archivo) # json.dump() convierte el diccionario "datos" en formato JSON y lo escribe en el archivo "archivo"

print(datos) # imprime el diccionario "datos" en la consola, mostrando su contenido